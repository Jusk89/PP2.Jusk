class EvenNumbers():
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= self.n:
            x=self.num
            self.num+=12
            return x
        else:
            raise StopIteration

n=int(input())
even= EvenNumbers(n)
print(",".join(str(i) for i in even))

import sys

class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.n:
            x = self.num
            self.num += 12
            return x
        raise StopIteration

n = int(sys.stdin.readline())
it = EvenNumbers(n)

out = sys.stdout.write
first = True

for x in it:
    if first:
        out(str(x))
        first = False
    else:
        out(" " + str(x))