from DataStructures.Stack.Stack import Stack


def main(number):
    s = Stack()

    while number > 0:
        remainder = number % 2
        s.push(remainder)
        number = number // 2

    bin_num = ""
    while s.is_empty() is not True:
        bin_num += str(s.pop())
    return bin_num


if __name__ == '__main__':
    print(main(242))
