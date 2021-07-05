import hashlib

string_bank = set()
my_string = input('Введите строку: ')

for i in range(len(my_string)):
    for j in range(i + 1, len(my_string) + 1):
        if len(my_string[i:j]) != len(my_string):
            print(my_string[i:j])
            # т.к. нам необходимо высчитывать хэш для подстрок в текущем запуске, используем ф-ию hash()
            string_bank.add(hash(my_string[i:j]))

print(string_bank)
print(len(string_bank))
