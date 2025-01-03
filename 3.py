# regex in python
import re


# consider only those that are in the form of mul(a,b) as valid instructions in the memory
def day3Part1(data):
    data = str(data)
    # filter only the valid
    goodMatch = re.findall(r"mul\([0-9]+,[0-9]+\)", data)

    # find the resulting value for each mul(a,b) instruction and add them up 
    total = 0
    for match in goodMatch:
        numbers = re.findall(r"[0-9]+", match)
        total += int(numbers[0]) * int(numbers[1])
    
    return total


# additionally, consider 'do' and 'dont' conditional statements
def day3Part2(data):
    data = str(data)
    # filter only the valid
    goodMatch = re.findall(r"(?:mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))", data)
    # find the resulting value for each mul(a,b) instruction and add them up 
    total = 0
    
    isEnabled = True
    for match in goodMatch:
        if isEnabled and match != "do()" and match != "don't()":
            numbers = re.findall(r"[0-9]+", match)
            total += int(numbers[0]) * int(numbers[1])
        elif match == "do()":
            isEnabled = True
        elif match == "don't()":
            isEnabled = False
    
    return total






data = []
for line in open("3.txt"):
    data.append(line)


print(day3Part1(data))   # 153469856
print(day3Part2(data))   # 153469856