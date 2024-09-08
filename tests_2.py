import re
import unittest


class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.cleaned_text = None

    def clean_text(self):
        # Удаляет все небуквенные символы и приводит текст к нижнему регистру
        self.cleaned_text = re.sub(r'[^a-zA-Z\s]', '', self.text).lower()

    def remove_stop_words(self, stop_words):
        # Удаляет стоп-слова из текста
        if self.cleaned_text is None:
            self.clean_text()
        words = self.cleaned_text.split()
        filtered_words = [word for word in words if word not in stop_words]
        self.cleaned_text = ' '.join(filtered_words)


class TestTextProcessor(unittest.TestCase):
    def test_clean_text(self):
        # Проверить, что метод правильно удаляет небуквенные символы.
        processor = TextProcessor('Hello, World!')
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, 'hello world')

        # Проверить, что текст приводится к нижнему регистру.
        processor = TextProcessor('123 ABC!!!')
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, ' abc')

        # Проверить, что метод работает на пустой строке.
        processor = TextProcessor('')
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, '')

    def test_remove_stop_words(self):
        # Проверить, что стоп-слова удаляются из текста.
        processor = TextProcessor('this is a test')
        processor.remove_stop_words(['this', 'is'])
        self.assertEqual(processor.cleaned_text, 'a test')

        # Проверить, что метод корректно работает, если стоп-слова отсутствуют в тексте.
        processor = TextProcessor('hello world')
        processor.remove_stop_words([])
        self.assertEqual(processor.cleaned_text, 'hello world')


if __name__ == '__main__':
    unittest.main()
