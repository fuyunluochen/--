def print_file_info(file_name):
    text = None
    try:
        text = open(file_name, 'r', encoding='UTF-8')
        for line in text:
            print(line)
    except Exception as e:
        print(f'文件打开异常,原因是：{e}')
    finally:
        if text != None:
            text.close()


def append_to_file(file_name, data):
    with open(file_name, 'a', encoding='utf-8') as text:
        text.write(data)