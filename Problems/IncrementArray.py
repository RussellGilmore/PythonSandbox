list_one = [1, 4, 9]
list_two = [9, 9, 9]


# Add one
def plus_one(number_list):
    number_list[-1] += 1
    for i in reversed(range(1, len(number_list))):
        if number_list[i] != 10:
            break
        number_list[i] = 0
        number_list[i-1] += 1

    if number_list[0] == 10:
        number_list[0] = 1
        number_list.append(0)
    return number_list

print(plus_one(list_one))
print(plus_one(list_two))


