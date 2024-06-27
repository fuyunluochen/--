import random

lives = 3
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
secret_word = random.choice(words)
# print(secret_word)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1


while lives > 0:
    print(clue)
    print('剩余生命次数' + heart_symbol * lives)
    guess = input("猜测字母或者整个单词:")
    if guess == secret_word:
        guessed_word_correctly = True
        break
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print("错误，您丢了一条命")
        lives -= 1
if guessed_word_correctly:
    print("您赢了!秘密单词是：" + secret_word)
else:
    print("您输了!秘密单词是：" + secret_word)
