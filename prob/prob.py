row = input().split()
s = ''.join(row)
my_list, temp_list = [[]], []
for elem in range(len(row)):
    temp_list.append(row[elem])
    my_list.append(temp_list)
    temp_list = []
print(s)
