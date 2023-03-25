min_score = 100000
my_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score < min_score:
        min_score = score
    my_list.append([name, score])
second_min = 100000
for i in range(0, len(my_list)):
    if my_list[i][1] > min_score and my_list[i][1] < second_min:
        second_min = my_list[i][1]
my_new_list = []
for i in range(0, len(my_list)):
    if my_list[i][1] == second_min:
        my_new_list.append(my_list[i][0])
for i in sorted(my_new_list):
    print(i)