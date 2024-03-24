print("Owned By Emin INC.")
print("Robux Redeem Code Generator and Chacker 1.0")
import random
import string
import requests

def generate_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choices(characters, k=length))
    return code

def check_code(code):
    url = f"https://www.roblox.com/redeem/code/?code={code}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    return False

def main():
    num_codes = int(input("Kaç kod üretmek istiyorsunuz? "))
    code_length = int(input("Kodların kaç haneli olmasını istiyorsunuz? "))

    for _ in range(num_codes):
        generated_code = generate_code(code_length)
        print("Üretilen Kod:", generated_code)
        if check_code(generated_code):
            print("Kod geçerli.")
        else:
            print("Kod geçerli değil.")

if __name__ == "__main__":
    main()
