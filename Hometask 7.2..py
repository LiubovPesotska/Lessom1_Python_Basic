def correct_sentence(sentence1: str, sentence2: str) -> str:
    # Функция для исправления одного предложения
    def fix_sentence(sentence):
        # Начинаем с заглавной буквы
        if not sentence[0].isupper():
            sentence = sentence[0].upper() + sentence[1:]
        # Заканчиваем точкой
        if not sentence.endswith('.'):
            sentence += '.'
        return sentence

    # Исправляем оба предложения
    sentence1 = fix_sentence(sentence1)
    sentence2 = fix_sentence(sentence2)

    # Возвращаем исправленные предложения
    return sentence1 + " " + sentence2


# Пример использования функции
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

corrected_sentences = correct_sentence(sentence1, sentence2)
print(corrected_sentences)