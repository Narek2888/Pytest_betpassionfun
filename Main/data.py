import random


username_list = "abcdefghijklmnopqrstuvwxyz0123456789"
password_list = ["tiko1234567", "harut567890", "vardan321456", "davit5432178", "gegham78901234"]


username = ''
for i in range(0, 5):
    username += random.choice(username_list)
password = random.choice(password_list)
repeat_password = password

username2 = "ar22"
password2 = "po123"

invalid_username = "jeko"
invalid_password = "phantom"