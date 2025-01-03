def day1Part1(left_list, right_list):
    # sort left and right list
    left_list.sort()
    right_list.sort()

    # pair up numbers (left[0] with right[0], left[1] with right[1], etc.)
    # get total distance of all pairs
    distance = 0
    for i in range(len(left_list)):
        distance += abs(left_list[i] - right_list[i])
    return distance


def day1Part2(left_list, right_list):
    left_list.sort()
    right_list.sort()

    # calculate total similarity score
    # add up each number to the left list after multiplying it by the number of times it appears to the right list
    similarity = 0
    for i in range(len(left_list)):
        similarity += left_list[i] * right_list.count(left_list[i])
    return similarity





# ===== main =====

# open file; get left and right list
left_list = []
right_list = []
for line in open("1.txt"):
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))
    

print(day1Part1(left_list, right_list)) # 1889772 
print(day1Part2(left_list, right_list)) # 23228917