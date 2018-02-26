import time
from datetime import datetime as dt
#import requests as r

host_tmp = 'hosts'
host_path ='/etc/hosts'
redirect = '127.0.0.1'

website_list = ['www.facebook.com','facebook.com']




while True:
    if 0 < dt.now().hour < 7:
        print('Rest hour...')
        with open(host_path,'r+') as file:
            content = file.read()
            print (content)
            time.sleep(1)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+'\n')
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print('Free time!!!')
    time.sleep(300)