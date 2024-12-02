import requests

def read_input():
    url = "https://adventofcode.com/2024/day/2/input"
    headers = {
        "cookie": "session=53616c7465645f5f63a856ba19e95367fa21132c7b88d7080837ed80307fc185733755862375aad5db6b377b1e6d65d5063eceaf76b33ac4a571295f8969ee78"
    }
    response = requests.get(url, headers=headers)
    return response.text

def part1(input):
    input = input.split("\n")
    count = 0
    for i in range(len(input)):
        seq = input[i].split(" ")
        previous = None
        unsafe = False
        #print(seq," ",str(len(seq)))
        if len(seq) <= 1:
            continue
   
        for j in range(len(seq)-1):
            increasing = True if int(seq[j]) >= int(seq[j+1]) else False
            gap = abs(int(seq[j])-int(seq[j+1]))
            #print(f'{int(seq[j])} {int(seq[j+1])} {increasing} {gap}')
            if (previous != None and previous != increasing) or gap > 3 or gap < 1:
                unsafe = True
                break
            previous = increasing

        if unsafe == False:
            count=count + 1
        
    print(count)

def isSequenceSafe(sequence):
    previous = None
    for j in range(len(sequence)-1):
        increasing = True if int(sequence[j]) >= int(sequence[j+1]) else False
        gap = abs(int(sequence[j])-int(sequence[j+1]))
        if (previous != None and previous != increasing) or gap > 3 or gap < 1:
            return False
        previous = increasing
    return True

def part2(input):
    input = input.split("\n")
    count = 0
    for i in range(len(input)):
        seq = input[i].split(" ")
        if len(seq) <= 1:
            continue
        
        for i in range(len(seq)):
            permutatedSeq = seq[:i] + seq[i+1:]
            if(isSequenceSafe(permutatedSeq)):
                #print(permutatedSeq)
                count+=1
                break

    print(count)

input = read_input()
part1(input)
part2(input)

