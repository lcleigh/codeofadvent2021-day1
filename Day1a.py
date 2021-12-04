def n_increases(string):
    #making the string a list
    list1 = string.split("\n")
    print(list1)
    int_list = list(map(int, list1))
    print(int_list)
    count = 0
    for i in range(len(int_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(int_list) - 1):
            if int_list[j+1] > int_list[j]:
                count += 1
        return count


example1 = """199
200
208
210
200
207
240
269
260
263"""

print(n_increases(open('input.txt').read()))

