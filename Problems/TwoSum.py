import typing
from typing import List


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#

class Solution(object):
    def __init__(self):
        pass

    def two_sum(self, nums: typing.List[int], target: int) -> List[int]:
        try:
              for x in range(len(nums)):
                for y in range(len(nums)):
                    if (nums[x] + nums[y]) == target and x != y:
                        return [x, y]
            # raise Exception("No combination found")
        except ValueError as err:
            print(err)
        finally:
            print("Executed")

    def read_names(self):
        blarg_file = open("blarg.txt", "r")
        for name in blarg_file.readable():
            print(name)
        blarg_file.close()


def main():
    sol = Solution()
    nums = [9, 7, 11, 15]
    target = 9
    print(sol.two_sum(nums, target))


def hello_world():
    print("Blarg")


if __name__ == '__main__':
    # main()
    hello_world()
