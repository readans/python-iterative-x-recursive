import sys
class Iterative:
    @staticmethod
    def is_prime(num):
        if (num < 1):
            return False
        for i in range(2, num):
            if (num % i == 0):
                return False
        return True

    @staticmethod
    def fibonacci(n):
        a, b = 0, 1
        for i in range(n - 1):
            yield a
            a, b = b, b + a

class Recursive:
    @staticmethod
    def is_prime(num, n = 2):
        if (n == num):
            return True
        return False if (num % n == 0) else Recursive.is_prime(num, n + 1)

    @staticmethod
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return Recursive.fibonacci(n - 1) + Recursive.fibonacci(n - 2)


if __name__ == "__main__":
    for i in Iterative.fibonacci(int(sys.argv[1])):
        print(i)
