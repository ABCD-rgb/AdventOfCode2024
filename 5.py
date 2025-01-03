def day5part1(rules, pageUpdates):
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
    
    # get the middle page number on each valid pageUpdate and sum them
    sum = 0
    for row in valid:
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


print(day5part1(rules, pageUpdates))    # 4609