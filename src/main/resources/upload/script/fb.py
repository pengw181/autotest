from fa import A
import sys


class B(A):

    def __init__(self, a, b):
        super(B, self).__init__(a, b)

    def funb(self):
        return self.a + self.b


def main(argv):
    t = B(argv[1], argv[2])
    m = t.funb()
    print(m)


if __name__ == "__main__":
    main(sys.argv)