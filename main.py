import os
from ftplib import FTP
from download_ftp_tree import download_ftp_tree


# def getDirList(dirs):
#     result = []
#     for i in dirs:
#         if i[1]['type'] == 'dir':
#             result.append(i[0])
#     return result
#


ftp = FTP("192.168.1.53", 'esp', 'esp')
ftp.set_debuglevel(1)

download_ftp_tree(ftp, 'DATA', 'backup/')
