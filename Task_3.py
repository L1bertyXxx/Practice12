eng_ru = {}

with open("en-ru.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "-" in line:
            eng_word, ru_words = line.split("-", 1)
            eng_ru[eng_word.strip()] = ru_words.strip()

ru_eng = {}
for eng, ru in eng_ru.items():
    if "," in ru:
        ru_list = ru.split(", ")
        for word in ru_list:
            ru_eng[word] = eng
    else:
        ru_eng[ru] = eng

ru_eng = dict(sorted(ru_eng.items()))
with open("ru-en.txt", "w", encoding="utf-8") as result:
    for ru_word, eng_word in ru_eng.items():
        result.write(f"{ru_word} - {eng_word}\n")