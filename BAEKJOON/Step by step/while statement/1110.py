first_n = int(input())
new_num = 0
count = 0
n = first_n
while True:
    if int(n) < 10:
        n = "0" + str(int(n))
    else:
        n = str(n)
    n_arr = list(map(int, n))
    a = n_arr[0] + n_arr[1]
    if a < 10:
        new_num = str(n_arr[1]) + str(a)
    else:
        new_num = str(n_arr[1]) + str(a % 10)
    count += 1
    n = new_num
    if int(new_num) == first_n:
        print(count)
        break