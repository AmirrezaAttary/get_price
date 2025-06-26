import requests

# تعریف slug
slug = 'samsung-galaxy-s24-fe-2568gb'
url = f'https://api.kasrapars.ir/api/web/v10/product/slug?slug={slug}&expand=is_wish%2CpriceQuality%2Creview%2Creview.items%2CsurveyScores%2CletMeKnow%2Cimages%2Ccategory%2CcategoryParents%2CgroupedFeatures%2CletMeKnowOnAvailability%2Cvariety.letMeKnowOnAvailability%2Cvarieties%2CcartFeatures%2CcoworkerShortName%2Csrc%2CisInWishList%2Cvarieties.promotionCoworker%2Cvarieties.color%2Cvarieties.canBuyWithBnPlByUser%2CactiveVarietyId%2Cvarieties.guarantee%2Cvarieties.company%2Cvarieties.pack%2Cvarieties.company.surveyStats%2Cvarieties.company.city%2Cvideos%2CsurveyCount%2CsurveyAverageScore%2CquestionCount%2Cvarieties.company.present_sell%2CreserveCeilCount%2Cvarieties.prePayment'

# ارسال درخواست
response = requests.get(url)

# بررسی وضعیت درخواست
if response.status_code == 200:
    data = response.json()
    
    # استخراج داده‌های variety
    varieties = data.get('varieties', [])
    
    for variety in varieties:
        price = variety.get('price_main', 'قیمت مشخص نشده')  # قیمت اصلی
        color = variety.get('color', 'رنگ مشخص نشده')  # رنگ

        # چاپ قیمت و رنگ
        print(f"price: {price} toman, color: {color}")

else:
    print(f"خطا در درخواست: {response.status_code}, پاسخ: {response.text}")