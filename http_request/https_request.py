import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def get_exchange_rates():
    """
    TCMB'nin günlük döviz kurları XML verisini çeker ve parse eder.
    """
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # HTTP hatalarını yakala
    except requests.exceptions.RequestException as e:
        print(f"[HATA] Veri çekilemedi: {e}")
        return None

    try:
        # XML parse işlemi
        tree = ET.ElementTree(ET.fromstring(response.content))
        root = tree.getroot()

        rates = {}
        for currency in root.findall("Currency"):
            code = currency.get("CurrencyCode")
            name = currency.find("Isim").text
            forex_buying = currency.find("ForexBuying").text
            forex_selling = currency.find("ForexSelling").text

            rates[code] = {
                "name": name,
                "buying": float(forex_buying.replace(",", ".")) if forex_buying else None,
                "selling": float(forex_selling.replace(",", ".")) if forex_selling else None
            }
        return rates
    except ET.ParseError as e:
        print(f"[HATA] XML parse edilemedi: {e}")
        return None

if __name__ == "__main__":
    print(f"📅 Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    rates = get_exchange_rates()
    if rates:
        # Örnek: USD ve EUR gösterelim
        for code in ["USD", "EUR"]:
            if code in rates:
                print(f"{code} ({rates[code]['name']}): "
                      f"Alış = {rates[code]['buying']} TL, "
                      f"Satış = {rates[code]['selling']} TL")
    else:
        print("Döviz kurları alınamadı.")