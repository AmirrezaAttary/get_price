import requests
import re

def get_product_prices(url):
    # استخراج slug از آدرس محصول
    match = re.search(r'/product-single/([^/]+)', url)
    if not match:
        print("❌ آدرس نامعتبر است یا slug پیدا نشد.")
        return

    slug = match.group(1)

    # داده‌هایی که به API ارسال می‌شود
    payload = {
        "slug": slug,
        "commentCount": 10
    }

    # هدرها
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer undefined",  # در صورت داشتن توکن، مقدار واقعی قرار دهید
        "Domain": "mobile140.com",
        "Origin": "https://mobile140.com",
        "Referer": "https://mobile140.com/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    # ارسال درخواست
    response = requests.post(
        "https://services.developzseh.ir/client/Product/Preview",
        json=payload,
        headers=headers
    )

    # بررسی پاسخ
    if response.status_code == 200:
        try:
            variants = response.json()['data']['variants']
            for variant in variants:
                price = variant['options'][0]['amount']
                color_attr = next((a for a in variant['attributes'] if a['title'] == 'رنگ'), None)
                color = color_attr['display'] if color_attr else 'نامشخص'
                print(f"💰 Price: {price} تومان - 🎨 Color: {color}")
        except Exception as e:
            print(f"❌ خطا در پردازش داده‌ها: {e}")
    else:
        print(f"❌ خطا در درخواست: {response.status_code}, پاسخ: {response.text}")


get_product_prices("https://mobile140.com/product-single/xiaomi-poco-x7-512gb-ram-12gb-5g-mobile-phone")