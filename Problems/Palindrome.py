class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        value = str(x)
        start = 0
        end = len(str(x)) - 1
        if len(value) == 2:
            if value[0] == value [1]:
                return True
            else:
                return False
        elif len(value) == 1:
            return True
        else:
            while start != end:
                if value[start] == value[end]:
                    start += 1
                    end -= 1
                else:
                    return False

            return True


def main():
    input_one = 121
    input_two = -121

    sol = Solution()
    sol.isPalindrome(input_one)
    sol.isPalindrome(input_two)


if __name__ == '__main__':
    main()
