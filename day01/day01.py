# Read the input file in python
def read_input():
    input_file = open("day01/input.txt", "r")
    input = input_file.read()
    input_file.close()
    return input

# Parse the input file
def parse_input(input, l, r):
    

    input = input.split("\n")
    for i in range(len(input)):
        input[i] = input[i].split(" ")
        # add to l and r list
        l.append(input[i][0])
        r.append(input[i][3])
    
    print(sum)

# Part 1
def part1(l, r):
    # sort the list
    l.sort()
    r.sort()
    sum = 0
    for i in range(len(l)):
        sum += abs(int(l[i]) - int(r[i]))
    return sum

def part2(l, r):
    # build a frequence table for r
    freq, sum = {}, 0
    for i in r:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for i in l:
        if i in freq:
            sum += int(i) * (freq[i])

    return sum


l, r = [], []
parse_input(read_input(), l, r)
print(part1(l, r))
print(part2(l, r))

