from bs4 import BeautifulSoup
import mmh3
import math
from urllib.request import urlopen

false_positive_probability = 0.0001


class CountableBloomFilter:

    def __init__(self, text_len):
        print("n: {}".format(text_len))
        self.size = self.get_size(n=text_len)
        self.hash_count = self.get_hash_count(n=text_len, m=self.size)
        self.cbf_array = [0] * self.size

    def get_size(self, n):
        size = int(-(n * math.log(false_positive_probability)) / (math.log(2) ** 2))
        print("m: {}".format(size))
        return size

    def get_hash_count(self, n, m):
        hash_count = math.ceil((m / n) * math.log(2))
        print("hash_count: {}".format(hash_count))
        return hash_count

    def add(self, word):
        for i in range(self.hash_count):
            index = mmh3.hash(key=word, seed=i) % self.size
            self.cbf_array[index] = self.cbf_array[index] + 1

    def check(self, word):
        for i in range(self.hash_count):
            index = mmh3.hash(key=word, seed=i) % self.size
            if self.cbf_array[index] == 0:
                return False
        return True


def start():
    words = []
    stringUrl = "https://ru.wikipedia.org/wiki/Instagram"
    page = urlopen(stringUrl).read()
    text = BeautifulSoup(page, features="html.parser").find_all('p')

    for word in text:
        words.extend(word.getText().split(' '))

    cbf = CountableBloomFilter(text_len=len(words))

    for word in words:
        cbf.add(word=word)

    words_for_check = ["Instagram", "фото", "видео", "filter", "Facebook", "миллион", "Вконтакте", "ИТИС", "itis"]
    print()
    for word in words_for_check:
        if cbf.check(word=word):
            print("\"{}\" is contained on the page".format(word))
        else:
            print("\"{}\" is not contained on the page".format(word))


if __name__ == '__main__':
    start()
