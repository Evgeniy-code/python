def pascal(raw):
    my_list = []
    for i in range(raw):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        my_list.append(temp_list)
    return my_list


n = int(input())
my_pascal_list = pascal(n)
for i in my_pascal_list:
    print(*i)