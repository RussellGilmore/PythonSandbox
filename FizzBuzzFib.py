class Fizzy(object):

    def fizz_buzz(self):
        for num in range(0, 100):
            if num % 5 == 0 and num % 3 == 0:
                print("The number " + str(num) + " is a fizz")
            elif num % 5 == 0:
                print("The number " + str(num) + " is a buzz")
            elif num % 3 == 0:
                print("The number " + str(num) + " is a FIZZBUZZ!")
            else:
                print("The number " + str(num) + " is weak!")

    def fibonacci(self):
        a, b = 0, 1
        for i in range(10):
            print(a)
            c = a + b
            a = b
            b = c

    def print_list(self):
        my_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                print(my_list[i][j], end=' ')


def main():
    fizzy = Fizzy()
    # fizzy.fizz_buzz()
    # fizzy.fibonacci()
    fizzy.print_list()


if __name__ == '__main__':
    main()
