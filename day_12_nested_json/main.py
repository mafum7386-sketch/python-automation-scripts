# =========================================================
# اليوم 12: قراءة وتفكيك JSON Response المتداخل
# =========================================================

import requests

def main():
    # --- الجزء الأول: تفكيك الـ JSON المتداخل ---
    weather_url = "https://api.open-meteo.com/v1/forecast?latitude=36.75&longitude=3.05&current_weather=true"
    w_data = requests.get(weather_url).json()

    print("--- 1. تفكيك بيانات متداخلة ---")
    print("الارتفاع:", w_data["elevation"])
    print("درجة الحرارة:", w_data["current_weather"]["temperature"], "°C")
    print("اتجاه الرياح:", w_data["current_weather"]["winddirection"], "درجة")

    # --- الجزء الثاني: سكريبت المقارنة بين مصدرين ---
    print("\n--- 2. مقارنة سعر الدولار/اليورو بين مصدرين ---")
    api1_url = "https://open.er-api.com/v6/latest/USD"
    api2_url = "https://api.frankfurter.app/latest?from=USD"

    val1 = requests.get(api1_url).json()["rates"]["EUR"]
    val2 = requests.get(api2_url).json()["rates"]["EUR"]

    print(f"المصدر 1: {val1} | المصدر 2: {val2}")
    
    if val1 >= val2:
        print("النتيجة: المصدر الأول أعلى أو يساويه.")
    else:
        print("النتيجة: المصدر الثاني أعلى.")

main()
