#!/usr/bin/python

import ftplib

from mylib import *

server = "192.168.1.53"
user = "esp"
password = "esp"
source = "DATA"
destination = "backup"
debug_level = 0

ftp = ftplib.FTP(server)
ftp.set_debuglevel(debug_level)
ftp.login(user, password)

# print(_get_list_of_folder(ftp, 'DATA'))

print_list(get_ls(ftp, 'ARCHIVE/20201005'))
