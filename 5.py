def getValidPageUpdates(rules, pageUpdates):
    valid = []
    for pageUpdate in pageUpdates:
        isValid = True
        for left,right in rules:
            if left in pageUpdate and right in pageUpdate:
                if pageUpdate.index(left) > pageUpdate.index(right):
                    isValid = False
                    break
            # when the values in the rule are not in the pageUpdate
            else:
                continue
        
        valid.append(pageUpdate) if isValid else None
    return valid


def day5part1(rules, pageUpdates):
    valid = getValidPageUpdates(rules, pageUpdates)
    # get the middle page number on each valid pageUpdate and sum them
    sum = 0
    for row in valid:
        midIndex = len(row) // 2
        sum += row[midIndex]
    
    return sum


def day5part2(rules, pageUpdates):
    # get incorrect pageUpdates and correct them (then sum the middle page number)
    valid = getValidPageUpdates(rules, pageUpdates)
    invalid = [update for update in pageUpdates if update not in valid]
    corrected = []

    
    while invalid != []:    # keep correcting the invalid pageUpdates until all are valid
        for pageUpdate in invalid:
            for left, right in rules:
                if left in pageUpdate and right in pageUpdate:
                    if pageUpdate.index(left) > pageUpdate.index(right):
                        leftIndex = pageUpdate.index(left)
                        rightIndex = pageUpdate.index(right)
                        pageUpdate[leftIndex], pageUpdate[rightIndex] = pageUpdate[rightIndex], pageUpdate[leftIndex]
            # make sure that the corrected pageUpdate is actually valid (iterate over and over since the correction may lead to another incorrect pageUpdate)
            if getValidPageUpdates(rules, [pageUpdate]) != []:
                corrected.append(pageUpdate)
        invalid = [update for update in invalid if update not in corrected]

    
    sum = 0
    for row in corrected:
        midIndex = len(row) // 2
        sum += row[midIndex]

    return sum

rules = []
pageUpdates = []
# section 1
for line in open("5.txt", "r"):
    if line == "\n":
        break
    row = (line.strip().split("|"))
    rules.append([int(i) for i in row])

# section 2: continue reading the file from the last line
start = False
for line in open("5.txt", "r"):
    if line == "\n":
        start = True
        continue
    if start:
        row = (line.strip().split(","))
        pageUpdates.append([int(i) for i in row])


# print(day5part1(rules, pageUpdates))    # 4609
print(day5part2(rules, pageUpdates))