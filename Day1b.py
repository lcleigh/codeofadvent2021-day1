def sum_increased(string):
    list1 = string.split("\n")
    print(list1)
    int_list = list(map(int, list1))
    print(int_list)
    sum_list = []
    for i in range(len(int_list)-2):
        sum_list.append(sum(int_list[i:i+3]))
    return sum_list

def sum_increased2(sum_list):
    count = 0
    for i in range(len(sum_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(sum_list) - 1):
            if sum_list[j+1] > sum_list[j]:
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

print(sum_increased(open('input.txt').read()))
print(sum_increased2(sum_increased(open('input.txt').read())))
