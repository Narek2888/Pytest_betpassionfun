username_list = "abcdefghijklmnopqrstuvwxyz0123456789"
password_list = ["tiko1234567", "harut567890", "vardan321456", "davit5432178", "gegham78901234"]

import random

username = ''
for i in range(0, 5):
    username += random.choice(username_list)
password = random.choice(password_list)
repeat_password = password

username2 = "arthur2"
password2 = "poker123"