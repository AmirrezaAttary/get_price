import requests

# آدرس API
url = "https://services.developzseh.ir/client/Product/Preview"

# داده‌هایی که می‌خواهید ارسال کنید
payload = {
    "slug": "samsung-galaxy-a56-128gb-ram-8gb-mobile-phone",
    "commentCount": 10
}

# هدرها
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer undefined",  # اگر توکن واقعی دارید آن را وارد کنید
    "Domain": "mobile140.com",  # اضافه کردن دامنه به هدرها
    "Origin": "https://mobile140.com",
    "Referer": "https://mobile140.com/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
}

# ارسال درخواست POST
response = requests.post(url, json=payload, headers=headers)

# بررسی وضعیت درخواست
if response.status_code == 200:
    # داده‌های دریافت شده
    variants = response.json()['data']['variants']
    
    # استخراج قیمت و رنگ
    for variant in variants:
        price = variant['options'][0]['amount']  # قیمت
        color_attribute = next((attr for attr in variant['attributes'] if attr['title'] == 'رنگ'), None)
        color = color_attribute['display'] if color_attribute else 'رنگ مشخص نشده'
        
        print(f"price: {price} toman, color: {color}")

else:
    print(f"خطا در درخواست: {response.status_code}, پاسخ: {response.text}")