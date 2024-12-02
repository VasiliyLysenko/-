class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                file_str = file.read().lower()
                for k in punc:
                    if k in file_str:
                        file_str = file_str.replace(k, ' ')
                words = file_str.split()
                all_words[i] = words
        return all_words

    def find(self, word):
        res = {}
        word = word.lower()
        all_words = self.get_all_words()
        for key in all_words:
            for i in all_words[key]:
                if word == i:
                    res[key] = all_words[key].index(i) + 1
                    break
        return res

    def count(self, word):
        res = {}
        count = 0
        word = word.lower()
        all_words = self.get_all_words()
        for key in all_words:
            for i in all_words[key]:
                if word == i:
                    count += 1
            if count > 0:
                res[key] = count
            count = 0
        return res


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))