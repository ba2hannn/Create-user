import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sayi = int(input('Lütfen kaç isim oluşturmak istediğinizi giriniz: '))
class Names:
    def __init__(self,sayi):
        self.sayi= sayi
    

    def open_filles(self):
        '''Lütfen aşşağıdaki "onad" ve "soyisimler" isimlerini değiştirmeyi unutmayınız.'''
        takes_names = open('onad','r',encoding='utf-8')
        taked_names = takes_names.readlines()
        self.written_names =[x[:-1] for x in taked_names]
        last1_names = open('soyisimler','r',encoding='utf-8')
        lasted_names = last1_names.readlines()
        self.written_lastnames =[x[:-1] for x in lasted_names]
        print(self.written_lastnames[1])

    def write_names(self):
        self.open_filles()
        a = 0
        while True:
            a += 1
            if a == sayi:
                break
            else:
                first_name = str(random.choice(self.written_names))
                last_name = str(random.choice(self.written_lastnames))
                randomPassword = str(random.randrange(1000,9999))
                randomMail = password = (f'{last_name}{first_name}{randomPassword}@yandex.com')
                kullaniciadi = (f'{last_name}{first_name}{randomPassword}')
                password = (f'{first_name}{last_name}{randomPassword}')
                '''Lütfen alttaki .txt dosyanın başını kendi dosya isimleriniz ile değiştirmeyi unutmayınız.'''
                file = open('isimler.txt','a', encoding='utf-8')
                file1 = open('sifreler.txt','a', encoding='utf-8')
                file2 = open('hesaplar.txt','a', encoding='utf-8')
                file3 = open('mailler.txt','a', encoding='utf-8')
                file4 = open('kullaniciadi.txt','a', encoding='utf-8')
                file4.write(f'kullanıcıadı:{kullaniciadi}\n')
                file4.close
                file3.write(f'mail:{randomMail}\n')
                file3.close
                file2.write(f'username:{first_name} {last_name} / password:{password} / mail:{randomMail} / kullanıcı adı:{kullaniciadi}\n')
                file2.close()
                file1.write(f'password:{password}\n')
                file1.close()
                file.write(f'username:{first_name} {last_name}\n')
                file.close()
name = Names(sayi)
name.write_names()