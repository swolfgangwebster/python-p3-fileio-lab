def write_file(file_name, file_content):

    l = open(str(file_name) + '.txt', mode='w', encoding='utf-8')
    l.write(file_content)
    l.close()

def append_file(file_name, append_content):
    l = open(str(file_name) + '.txt', mode='a', encoding='utf-8')
    l.write(append_content)
    l.close()

def read_file(file_name):
    l = open(str(file_name) + '.txt', mode='r', encoding='utf-8')
    return l.read()