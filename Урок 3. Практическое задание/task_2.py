from uuid import uuid4
import hashlib

salt = uuid4().hex
pass_bank = {}


def enter_pass():
    new_name = input('Введите имя нового пользователя: ')
    new_pass = input('Введите пароль пользователя: ')
    hash_pass = hashlib.sha256(salt.encode() + new_pass.encode()).hexdigest()
    pass_bank[new_name] = hash_pass


def check_pass():
    ch_name = input('Введите имя пользователя: ')
    ch_pass = input('Введите пароль пользователя: ')
    hash_check_pass = hashlib.sha256(salt.encode() + ch_pass.encode()).hexdigest()
    if pass_bank[ch_name] == hash_check_pass:
        print(f'User {ch_name} successfully registered')
    else:
        print('Try one more time!')
        return check_pass()


enter_pass()
enter_pass()
print(pass_bank)

check_pass()
