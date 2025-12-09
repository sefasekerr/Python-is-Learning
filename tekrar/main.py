# main.py
import os, random, textwrap, datetime, sys, io, base64, json
from pathlib import Path
import requests
from pytrends.request import TrendReq
from gtts import gTTS
from moviepy.editor import ImageClip, VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# -------- Yapılandırma --------
BASE_DIR = Path(__file__).parent
OUT_DIR = BASE_DIR / "out"
OUTPUT_SIZE = (1080, 1920)       # Shorts dikey
VIDEO_DURATION_SEC = 40          # 30–45 sn ideal
LANG = "tr"
FONT_PATH = "C:/Windows/Fonts/arial.ttf"  # Windows varsayılan
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CATEGORY_ID = "27"
PRIVACY_STATUS = "public"

# -------- Yardımcılar --------
def ensure_dirs():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

def save_tmp_image(img: Image.Image, path: Path):
    img.save(path, format="PNG")

# -------- 1) Konu seçimi (trend + AI rafine) --------
def fetch_trending_topic():
    try:
        pytrends = TrendReq(hl="tr-TR", tz=180)
        df = pytrends.trending_searches(pn='turkey')
        topics = [t for t in df[0].tolist() if isinstance(t, str)]
        if topics:
            seed = random.choice(topics[:10])
        else:
            seed = random.choice(["Bilimsel gerçek", "Tarihsel olay", "Teknoloji gelişmesi", "Popüler kültür"])
    except Exception:
        seed = random.choice(["Bilimsel gerçek", "Tarihsel olay", "Teknoloji gelişmesi", "Popüler kültür"])

    # Basit rafine: kısa ve net başlık üretimi
    refined = f"{seed} hakkında 40 saniyelik ilginç bilgi"
    return seed, refined

# -------- 2) Script üretimi (kurallı şablon) --------
def build_script(topic):
    hook = f"{topic} hakkında bunu biliyor muydunuz?"
    fact = f"Kısa ama çarpıcı bir bilgi: çoğu kişinin gözünden kaçan bu ayrıntı, olaya farklı bir açı katıyor."
    detail = f"Konuya bakışımızı gözden geçirince, küçük bir farkın büyük sonuçlar doğurabildiğini görüyoruz."
    close = "Devamını merak ediyorsanız yorumlarda söyleyin; en ilginç noktayı birlikte açalım."
    # Ekran yazısı (segmentlere bölünecek)
    screen_text = f"{hook}\n\n{fact}\n\n{detail}\n\n{close}"
    # Seslendirme metni
    narration = f"{hook}. {fact}. {detail}. {close}."
    title = f"{topic} • 40 saniyede ilginç bilgi"
    description = f"{topic} hakkında kısa bir bilgi. Günlük içerikler için takipte kalın. #shorts #bilgi #trend"
    tags = [topic, "shorts", "ilginç bilgi", "trend", "günlük içerik"]
    return screen_text, narration, title, description, tags

# -------- 3) TTS (gTTS) --------
def generate_tts(narration_text, out_mp3):
    tts = gTTS(text=narration_text, lang=LANG, slow=False)
    tts.save(out_mp3)

# -------- 4) AI arka plan (görsel -> loop video) --------
def generate_ai_background_image(topic) -> Image.Image:
    # Yerel, basit AI-stil görsel: tipografi + gradient (harici servise ihtiyaç duymadan)
    w, h = OUTPUT_SIZE
    img = Image.new("RGB", (w, h), color=(20, 24, 32))
    draw = ImageDraw.Draw(img)

    # Gradient bant
    for y in range(h):
        r = 30 + int(40 * (y / h))
        g = 40 + int(50 * (y / h))
        b = 80 + int(60 * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Metin stilizasyonu
    try:
        font_title = ImageFont.truetype(FONT_PATH, 96)
    except Exception:
        font_title = ImageFont.load_default()

    title = topic[:40]
    bbox = draw.textbbox((0,0), title, font=font_title)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.rectangle([(w//2 - tw//2 - 20, h//2 - th//2 - 20), (w//2 + tw//2 + 20, h//2 + th//2 + 20)], fill=(0,0,0,128))
    draw.text((w//2 - tw//2, h//2 - th//2), title, fill=(255, 255, 255), font=font_title)

    # Hafif doku noktaları
    for _ in range(800):
        x = random.randint(0, w-1)
        y = random.randint(0, h-1)
        draw.point((x, y), fill=(random.randint(100,200), random.randint(100,200), random.randint(100,200)))

    return img

def build_loop_video_from_image(image_path, duration, out_video_path):
    # Görseli 40 sn'lik hafif zoom ve parallax ile loop videoya çevir
    clip = ImageClip(str(image_path)).set_duration(duration).resize(height=OUTPUT_SIZE[1]).crop(x_center=OUTPUT_SIZE[0]//2, width=OUTPUT_SIZE[0])
    # Yavaş zoom
    clip = clip.resize(lambda t: 1.0 + 0.03 * (t / duration))
    final = clip
    final.write_videofile(out_video_path, fps=30, codec="libx264", audio_codec="aac")

# -------- 5) Dikey Shorts montaj --------
def build_shorts_video(screen_text, audio_path, bg_video_path, video_path):
    bg_clip = VideoFileClip(bg_video_path).without_audio()
    # Süre senkronu
    bg_clip = bg_clip.subclip(0, min(bg_clip.duration, VIDEO_DURATION_SEC))
    if bg_clip.duration < VIDEO_DURATION_SEC:
        from moviepy.editor import concatenate_videoclips
        loops = int(VIDEO_DURATION_SEC // bg_clip.duration) + 1
        bg_clip = concatenate_videoclips([bg_clip] * loops).subclip(0, VIDEO_DURATION_SEC)

    narration = AudioFileClip(audio_path).volumex(1.0)

    lines = [l.strip() for l in screen_text.split("\n") if l.strip()]
    seg_duration = max(7, int(VIDEO_DURATION_SEC / max(1, len(lines))))
    text_clips = []
    for line in lines:
        wrapped = textwrap.fill(line, width=25)
        txt = TextClip(
            wrapped,
            fontsize=92,
            font="Arial",
            color="white",
            stroke_color="black",
            stroke_width=3,
            method="caption",
            size=(OUTPUT_SIZE[0] - 120, None),
            align="center"
        )
        txt = txt.set_position(("center", "center")).set_duration(seg_duration).fadein(0.35).fadeout(0.35)
        text_clips.append(txt)

    final = CompositeVideoClip([bg_clip] + text_clips, size=OUTPUT_SIZE).set_audio(narration)
    final.write_videofile(video_path, fps=30, codec="libx264", audio_codec="aac", threads=4)

# -------- 6) Thumbnail --------
def generate_thumbnail(topic, thumbnail_path):
    img = generate_ai_background_image(topic)
    try:
        font_sub = ImageFont.truetype(FONT_PATH, 48)
    except Exception:
        font_sub = ImageFont.load_default()
    draw = ImageDraw.Draw(img)
    sub = "Kısa • İlginç Bilgi"
    bbox = draw.textbbox((0,0), sub, font=font_sub)
    sw, sh = bbox[2]-bbox[0], bbox[3]-bbox[1]
    w, h = OUTPUT_SIZE
    draw.text((w//2 - sw//2, h//2 + 140), sub, fill=(200, 230, 255), font=font_sub)
    img.save(thumbnail_path, quality=90)

# -------- 7) YouTube upload --------
def youtube_auth():
    flow = InstalledAppFlow.from_client_secrets_file(str(BASE_DIR / "credentials.json"), SCOPES)
    creds = flow.run_local_server(port=0)
    service = build("youtube", "v3", credentials=creds)
    return service

def youtube_upload(service, video_path, title, description, tags, category_id=CATEGORY_ID, privacy_status=PRIVACY_STATUS, thumbnail_path=None):
    body = {
        "snippet": {"title": title, "description": description, "tags": tags, "categoryId": category_id},
        "status": {"privacyStatus": privacy_status, "madeForKids": False}
    }
    media = MediaFileUpload(video_path, chunksize=-1, resumable=True, mimetype="video/*")
    response = service.videos().insert(part="snippet,status", body=body, media_body=media).execute()
    video_id = response["id"]
    if thumbnail_path and os.path.exists(thumbnail_path):
        service.thumbnails().set(videoId=video_id, media_body=MediaFileUpload(thumbnail_path)).execute()
    return video_id

# -------- 8) Çalıştır --------
def run_once():
    ensure_dirs()

    seed_topic, refined_title = fetch_trending_topic()
    screen_text, narration_text, title, description, tags = build_script(seed_topic)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    base = OUT_DIR / f"short_{timestamp}"
    audio_path = f"{base}.mp3"
    video_path = f"{base}.mp4"
    thumb_path = f"{base}.jpg"
    bg_image_path = f"{base}_bg.png"
    bg_video_path = f"{base}_bg.mp4"

    # TTS
    generate_tts(narration_text, audio_path)

    # AI background (görsel → loop video)
    img = generate_ai_background_image(refined_title)
    save_tmp_image(img, Path(bg_image_path))
    build_loop_video_from_image(bg_image_path, VIDEO_DURATION_SEC, bg_video_path)

    # Thumbnail
    generate_thumbnail(refined_title, thumb_path)

    # Montaj
    build_shorts_video(screen_text, audio_path, bg_video_path, video_path)

    # YouTube upload
    service = youtube_auth()
    video_id = youtube_upload(service, video_path, title, description, tags, thumbnail_path=thumb_path)
    print("Yüklendi:", video_id)

if __name__ == "__main__":
    run_once()
