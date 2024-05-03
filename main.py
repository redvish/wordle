import random
import colorama
from colorama import init

init()

keyboard = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
output = ["_", "_", "_", "_", "_"]

with open("russian_nouns.txt", 'r', encoding='utf-8') as text:
    words = [*filter(lambda x: x[:-1] if len(x) == 6 else None, text.readlines())]

word = random.choice(words)
print("""Угадайте слово из 5 букв
У Вас есть 6 попыток
Если буква встречается в загаданном слове один раз, то она подсветится желтым
Если буква встречается в загаданном слове больше одного раза, то она подсветится фиолетовым
Если буквы нет в слове, то она подсветится красным
Удачи!""")
score = 100

for i in range(1, 7):
    guess = input(f'Попытка номер {i}: ')
    for j in range(len(guess)):
        if guess[j] in word:
            if word.count(guess[j]) > 1:
                if guess[j] in keyboard:
                    keyboard[keyboard.index(guess[j])] = colorama.Fore.MAGENTA + keyboard[keyboard.index(guess[j])] + colorama.Fore.RESET
            if word.count(guess[j]) == 1:
                if guess[j] in keyboard:
                    keyboard[keyboard.index(guess[j])] = colorama.Fore.YELLOW + keyboard[keyboard.index(guess[j])] + colorama.Fore.RESET
            if word[j] == guess[j]:
                output[j] = word[j]
        else:
            if guess[j] in keyboard:
                keyboard[keyboard.index(guess[j])] = colorama.Fore.RED + keyboard[keyboard.index(guess[j])] + colorama.Fore.RESET

    print("", *keyboard[:11], '\n', *keyboard[11:22], '\n', *keyboard[22:])
    print("".join(output))
    score -= 20

    if "_" not in output:
        if i == 6:
            score = 10
        print(colorama.Fore.GREEN + "Вы победили!" + colorama.Fore.RESET)
        print(colorama.Fore.GREEN + "Вы набрали " + str(score) + " очков" + colorama.Fore.RESET)
        break

if "_" in output and i == 6:
    print(colorama.Fore.RED + "Вы проиграли!" + colorama.Fore.RESET)
print(f'Было загадано слово {word}')
