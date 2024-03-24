import random
import string
import requests
import time

def generate_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    formatted_code = '-'.join([code[i:i+4] for i in range(0, len(code), 4)])
    return formatted_code

def check_code(code):
    url = f"https://play.google.com/redeem?code={code}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def generate_and_check_codes(num_of_codes, mode='normal'):
    for _ in range(num_of_codes):
        code = generate_code()
        print(f"Kod üretildi: {code}")
        time.sleep(1 if mode == 'normal' else 0.5)  # Bekleme süresi

        if check_code(code):
            print(f"{code} geçerli.")
        else:
            print(f"{code} geçersiz.")

# Kullanıcı girişi
num_of_codes = int(input("Kaç adet kod üretmek istiyorsunuz? "))
mode = input("Hangi modda çalışmasını istiyorsunuz? (normal/orta hız): ").lower()

generate_and_check_codes(num_of_codes, mode)
