def get_ls(ftp_handle, name):
    result = {}
    if (name != ''):
        ftp_handle.cwd(name);
    for i in ftp_handle.mlsd():
        if (i[1]['type'] == 'dir'):
            result[i[0]] = True
        else:
            result[i[0]] = False
    return result


def print_list(list):
    for i in list:
        print(i)