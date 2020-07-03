import typing
from typing import List, Tuple


class Calculator(object):

    def __init__(self):
        pass

    # Tips
    # Use the min and max functions
    def range(self, range_list: List[int]) -> Tuple:
        low = range_list[0]
        high = range_list[0]
        for num in range_list:
            if num > high:
                high = num
            if num < low:
                low = num
        return (low, high)

    # Tips
    # Use the sum function
    def mean(self, mean_list: List[int]) -> int:
        sum = 0
        for num in mean_list:
            sum += num
        return sum / len(mean_list)

    # Tips
    # Use the sort function
    def median(self, median_list: List[int]) -> int:
        middle_pos = round(len(median_list) / 2)
        return median_list[middle_pos]

    # Sort the list, or use a dict
    def mode(self, mode_list: List[int]) -> int:
        number_map = dict()
        mode = None
        for num in mode_list:
            if mode_list[num] not in number_map:
                number_map[mode_list[num]] = 1
                if mode is None:
                    mode = mode_list[num]
            else:
                number_map[mode_list[num]] = number_map[mode_list[num]] + 1
                if number_map[num] > number_map[mode]:
                    mode = num
        return mode


def main():
    my_list = [1, 3, 3, 2, 5, 8, 9, 4, 4, 7, 4, 8]
    calc = Calculator()
    
    print(calc.range(my_list))
    print(calc.mean(my_list))
    print(calc.median(my_list))
    print(calc.mode(my_list))


if __name__ == '__main__':
    main()
