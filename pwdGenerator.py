import random
import string

def pwdGen(num_of_letters, num_of_digits, num_of_special_characters):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(num_of_letters)))
    digits = ''.join((random.choice(string.digits) for i in range (num_of_digits)))
    characters = ''.join((random.choice(string.punctuation) for i in range (num_of_special_characters)))

    pwd_list = list(letters + digits + characters)
    random.shuffle(pwd_list)

    pwd = ''.join(pwd_list)
    print("Random Password: ", pwd)

# enter number of letters, numbers, special characters to generate password of desired length
# (number of letters, total numbers, total special characters)
pwdGen(20, 3, 4)