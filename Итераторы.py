class EvenNumbers():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            while self.current % 2 != 0:
                self.current += 1
            result = self.current
            self.current += 2
            return result


en = EvenNumbers(10, 25)
for i in en:
    print(i)