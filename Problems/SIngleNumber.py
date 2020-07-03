class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number_map = dict()
        for num in nums:
            if num not in number_map:
                number_map[num] = 1
            else:
                number_map[num] = number_map[num] + 1
        single = None
        for key, value in number_map.items():
            if value == 1:
                single = key
        return single

def main():
    sol = Solution()
    list_one = [2, 2, 1]
    list_two = [4, 1, 2, 1, 2]
    print(sol.singleNumber(list_one))
    print(sol.singleNumber(list_two))


if __name__ == '__main__':
    main()
