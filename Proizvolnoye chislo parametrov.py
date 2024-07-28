# Создаем функцию с параметрами

def single_root_words(root_word, *other_words):
    same_words = [] # Пустой список
    root_word = root_word.lower() # По умолчанию делаем низкий регистр

    for word in other_words: # Прописываем цикл
        word = word.lower() # По умолчанию делаем низкий регистр
# Проверяем условие: если root_word(суффикс) попадается в каждом word или word в каждом root_word(суффикс). Добавляем в список.
        if root_word in word or word in root_word:
            same_words.append(word)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)