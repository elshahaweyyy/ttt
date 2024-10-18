import requests
import time

# تعريف عناوين URL (يرجى التأكد من وضع العناوين الصحيحة هنا)
url_reward = 'https://dogs.triplecloudmining.com/get/advertisement/reward'
url_claim = 'https://dogs.triplecloudmining.com/claim/points/by/watching/ad'

# إعداد الرؤوس
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "referer": "https://dogs.triplecloudmining.com/",
    "x-requested-with": "XMLHttpRequest",
}

# قراءة ملفات تعريف الارتباط من ملف
def read_cookies(file_path):
    with open(file_path, 'r') as f:
        cookies = {}
        for line in f:
            key, value = line.strip().split('=')
            cookies[key] = value
    return cookies

# قائمة حسابات المستخدمين
accounts = [
    'path_to_cookies_file1.txt',  # استبدل بمسار ملف الكوكيز الأول
    'path_to_cookies_file2.txt',  # استبدل بمسار ملف الكوكيز الثاني
    'path_to_cookies_file3.txt',
    # يمكنك إضافة المزيد من الحسابات هنا
]

while True:
    for account in accounts:
        try:
            cookies = read_cookies(account)

            # طلب المكافأة
            response_reward = requests.get(url_reward, headers=headers, cookies=cookies)
            
            if response_reward.status_code == 200:
                print(f"Account {account}: 1 dogs added")
                
                # مطالبة النقاط
                response_claim = requests.get(url_claim, headers=headers, cookies=cookies)
                
                if response_claim.status_code == 200:
                    print(f"Account {account}: 0.25 dogs added")
            else:
                print(f"Account {account}: Failed to get reward: {response_reward.status_code}")

        except requests.exceptions.RequestException as e:
            print(f'Account {account}: Error: {e}. Retrying in 2 seconds...')
        
        time.sleep(2)  # الانتظار لمدة ثانيتين بين الطلبات للحسابات المختلفة
    
    time.sleep(5)  # الانتظار لمدة دقيقة بين مجموعات الحسابات
