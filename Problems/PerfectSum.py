# Input: arr[] = {5, 10, 12, 13, 15, 18}, K = 30
# Output: {12, 18}, {5, 12, 13}, {5, 10, 15}
# Explanation:
# Subsets with sum 30 are:
# 12 + 18 = 30
# 5 + 12 + 13 = 30
# 5 + 10 + 15 = 30
#
# Input: arr[] = {1, 2, 3, 4}, K = 5
# Output: {2, 3}, {1, 4}


class Problem(object):

    def perfect_sum(self, nums, target):
        list_of_sets = list()
        nums.sort()
        solution_sets = list()
        solution_set = list()
        temp_set = list()
        pos = 0
        while pos != len(nums):

            for i in range(pos, (len(nums))):
                temp_set.append(nums[i])

            # print(temp_set)
            solution_set.append(self.add_set(temp_set, target))
            if solution_set is not None:
                solution_sets.append(solution_set)
            pos += 1
            solution_set.clear()
            temp_set.clear()

        return solution_sets

    def add_set(self, nums, target):
        current_sum = 0
        target_found = list()
        for num in nums:
            if current_sum < target:
                current_sum += num
                target_found.append(num)
        if current_sum == target:
            print(target_found)
            return target_found
        else:
            return None


def main():
    sol = Problem()
    my_list = [5, 4, 3, 2, 1]
    target = 5

    print(sol.perfect_sum(my_list, target))


if __name__ == '__main__':
    main()
