from uuid import uuid4
import hashlib

salt = uuid4().hex


class WebPage:
    def __init__(self):
        self.elems = {}

    def __str__(self):
        return str(self.elems)

    def check_page(self, new_page):
        if self.elems.get(new_page):
            print(f'Страница {new_page} находится в кэше')
        else:
            res = hashlib.sha256(salt.encode() + new_page.encode()).hexdigest()
            self.elems[new_page] = res
            print(self.elems)


def check_url(my_url):
    new_web = input('Input URL, please. For exit print "exit": ')
    if new_web == 'exit':
        print(my_url)
        print("Checking stop")
        return
    else:
        my_url.check_page(new_web)
    return check_url(my_url)


new_url = WebPage()
check_url(new_url)
