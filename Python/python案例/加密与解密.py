from tkinter import messagebox, simpledialog, Tk


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    return [
        message[counter]
        for counter in range(len(message))
        if is_even(counter)
    ]


def get_odd_letters(message):
    odd_letters = []
    for counter in range(len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
        return odd_letters


def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = f"{message}x"
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(len(message) // 2):
        letter_list.extend((odd_letters[counter], even_letters[counter]))
    return ''.join(letter_list)


def get_task():
    return simpledialog.askstring('任务', '您是否想要解密或解密信息？')


def get_message():
    return simpledialog.askstring('信息', '输入相关信息:')


root = Tk()
while True:
    task = get_task()
    if task == "加密":
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('密文的内容为:', encrypted)
    elif task == '解密':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('密文的内容为:', decrypted)
    else:
        break
root.mainloop()
