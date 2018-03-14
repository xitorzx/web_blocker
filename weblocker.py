import time
from datetime import datetime as dt
import os,sys




class blocker:
    def __init__(self):
        self.osname = os.name
        self.platform = sys.platform
        self.list = []
    def setpath(self):
        if self.osname == 'posix' and self.platform == 'linux':
            self.host_path = r'/etc/hosts'
        elif self.osname == 'nt' and self.platform == 'win32':
            self.host_path = r'C:\Windows\System32\drivers\etc\hosts'

    def redrict(self):
        self.redirect = '127.0.0.1'
    def block_list(self):        
        self.num = input("Please input the number of website you wanna block:\n")
        for i in range (int(self.num)):
            self.list.append()
