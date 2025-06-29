import requests
import re

def get_kasrapars_product_prices(url):
    # استخراج slug از URL
    match = re.search(r'/product/([^/?#]+)', url)
    if not match:
        print("❌ آدرس نامعتبر است یا slug پیدا نشد.")
        return

    slug = match.group(1)

    # ساخت URL API
    api_url = (
        f'https://api.kasrapars.ir/api/web/v10/product/slug?slug={slug}&expand='
        'is_wish,priceQuality,review,review.items,surveyScores,letMeKnow,images,category,'
        'categoryParents,groupedFeatures,letMeKnowOnAvailability,variety.letMeKnowOnAvailability,'
        'varieties,cartFeatures,coworkerShortName,src,isInWishList,varieties.promotionCoworker,'
        'varieties.color,varieties.canBuyWithBnPlByUser,activeVarietyId,varieties.guarantee,'
        'varieties.company,varieties.pack,varieties.company.surveyStats,varieties.company.city,'
        'videos,surveyCount,surveyAverageScore,questionCount,varieties.company.present_sell,'
        'reserveCeilCount,varieties.prePayment'
    )

    # ارسال درخواست GET
    response = requests.get(api_url)

    # بررسی پاسخ
    if response.status_code == 200:
        data = response.json()
        varieties = data.get('varieties', [])

        for variety in varieties:
            price = variety.get('price_main', 'قیمت مشخص نشده')
            color = variety.get('color', 'رنگ مشخص نشده')
            print(f"💰 Price: {price} تومان - 🎨 Color: {color}")
    else:
        print(f"❌ خطا در درخواست: {response.status_code}, پاسخ: {response.text}")


get_kasrapars_product_prices("https://plus.kasrapars.ir/product/xiaomi-redmi-pb200lzm-power-bank-20000-mah-with-microusb-conversion-cable")
