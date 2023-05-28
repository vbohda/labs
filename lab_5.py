def number_to_word(num):
   
    words = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

   
    return words.get(num, '---')


print('Вітаю')


num = int(input('Введіть число: '))


print(number_to_word(num))