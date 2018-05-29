class Fib:
    def __init__(self, max):
        self.a = 0
        self.b = 1
        self.max = max
    def __iter__(self):
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        else:
            self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == '__main__':

    for f in Fib(6):
        print(f)