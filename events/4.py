string = ""
string += "Беркман"
string += "Гребеников"
string += "Карпинский"
string += "Кирсанова"
string += "Майданец"
string += "Пугачев"
string += "Савон"
string += "Смакотина"
string += "Терентьева"
string += "Трофимов"
string += "удалова"
string += "Мирошниченко"
string += "Тягунова"
string += "Киреев"

sum_gl = 0
for i in string:
    if i in ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
        sum_gl += 1

print("Кол-во гласных:{}, кол-во букв {}, вероятность, {}".format(sum_gl, len(string), sum_gl / len(string))