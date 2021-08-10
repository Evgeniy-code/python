def pascal(raw):
    for i in range(raw + 1):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        my_list.append(temp_list)
    return print(my_list[raw])


n = int(input())
my_list = []
pascal(n)