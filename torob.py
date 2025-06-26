import requests

# آدرس API
url = 'https://api.torob.com/v4/base-product/similar-base-product/?page=0&prk=9a7ac136-05ed-4fee-b459-6b048dde0f01&limit=24&_http_referrer=https%3A%2F%2Fwww.google.com%2F&source=next_mobile'

# ارسال درخواست به API
response = requests.get(url)

# بررسی وضعیت پاسخ
if response.status_code == 200:
    data = response.json()
    
    # استخراج قیمت 5 محصول اول
    prices = []
    for product in data.get('results', [])[:5]:  # فقط 5 محصول اول
        price = product.get('price', 'قیمت مشخص نشده')  # فرض بر این است که قیمت در کلید 'price' است
        prices.append(price)

    # چاپ قیمت‌ها
    for idx, price in enumerate(prices, start=1):
        print(f"قیمت محصول {idx}: {price} تومان")
else:
    print(f"خطا در درخواست: {response.status_code}, پاسخ: {response.text}")