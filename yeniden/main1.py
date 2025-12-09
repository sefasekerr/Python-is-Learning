import os
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip
from openai import OpenAI
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# -------- 1) Trend konusunu çek (HTML scraping) --------
def get_tr_trends():
    url = "https://trends.google.com/trends/trendingsearches/daily?geo=TR"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    # Google arayüzü değişirse selector kırılabilir; fallback için kontrol ekledik.
    titles = [t.get_text(strip=True) for t in soup.select("div.feed-item div.title")]
    if not titles:
        # Alternatif selector dene (UI değişikliklerine dayanıklı olmak için)
        titles = [t.get_text(strip=True) for t in soup.select("div.feed-item h2.title")]
    return titles

def get_trending_topic():
    try:
        topics = get_tr_trends()
        return topics[0] if topics else "Yapay zekâ"
    except Exception as e:
        print("Trend alınamadı, fallback kullanılacak:", e)
        return "Yapay zekâ"

# -------- 2) Script üret --------
def generate_script(topic: str) -> str:
    # Kısa Shorts tarzı metin (yaklaşık 20–40 saniye)
    return (
        f"{topic} bugün gündemde. Kısaca özetleyelim: {topic} hakkında yeni gelişmeler hızla yaşanıyor. "
        f"Bu başlık etrafında farklı bakış açıları oluşuyor ve dikkatle takip edilmesi gerekiyor. "
        f"Sence {topic} önümüzdeki günlerde nasıl şekillenir?"
    )

# -------- 3) TTS (gTTS) --------
def text_to_speech(text: str, filename: str = "audio.mp3") -> str:
    tts = gTTS(text=text, lang="tr")
    tts.save(filename)
    return filename

# -------- 4) AI görsel üretimi (OpenAI) --------
def generate_ai_image(prompt: str, filename: str = "ai_image.png") -> str:
    api_key = os.getenv("sk-proj-")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY ortam değişkeni bulunamadı. PowerShell: setx OPENAI_API_KEY \"sk-proj-...\"")

    client = OpenAI(api_key=api_key)
    # 1280x720 (Shorts dikey değil ama basit görsel için yeterli; istersen 1080x1920 kullan)
    # Dikey Shorts için: size="1080x1920" ve MoviePy'de portrait canvas ayarlayabilirsin.
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1280x720"
    )

    image_url = result.data[0].url
    img_data = requests.get(image_url, timeout=30).content
    with open(filename, "wb") as f:
        f.write(img_data)
    return filename

# -------- 5) Video üretimi (Shorts basit sürüm) --------
def create_video(image_path: str, audio_path: str, output: str = "shorts.mp4") -> str:
    audio = AudioFileClip(audio_path)
    # Görseli ses süresine göre oynat
    clip = ImageClip(image_path).set_duration(audio.duration)
    # Düşük bitrate düşmesin diye codec ve bitrate ayarı
    clip = clip.set_audio(audio)
    clip.write_videofile(
        output,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        bitrate="3000k",
        threads=4
    )
    return output

# -------- 6) YouTube’a yükleme --------
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_to_youtube(video_file: str, title: str, description: str):
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # client_secret.json aynı klasörde olmalı
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    youtube = build("youtube", "v3", credentials=creds)
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["trend", "gündem", "otomatik video", "shorts"],
                "categoryId": "22"  # People & Blogs (isteğe göre güncelle)
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_file)
    )
    response = request.execute()
    print("Video yüklendi, ID:", response.get("id"))

# -------- Main --------
if __name__ == "__main__":
    # 1) Konu
    topic = get_trending_topic()
    print("Seçilen konu:", topic)

    # 2) Script
    script = generate_script(topic)

    # 3) Ses
    audio_file = text_to_speech(script)

    # 4) AI görsel (Shorts'a uygun minimalist arka plan)
    prompt = (
        f"{topic} hakkında modern, minimalist bir arka plan. "
        f"Temiz tipografi hissi, yumuşak kontrast, profesyonel video arka plan estetiği. "
        f"YouTube Shorts için uygun arka plan, dikkat dağıtmayan ama ilgi çekici kompozisyon."
    )
    image_file = generate_ai_image(prompt)

    # 5) Video
    video_file = create_video(image_file, audio_file)

    # 6) YouTube
    upload_to_youtube(video_file, f"Gündem: {topic}", script)
