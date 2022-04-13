 # Function to convert integer to binary

def NumberToBinary(number):
    l_binary = bin(number)[2:]
    l_binaryList = [int(d)  for d in str(l_binary)]
    return l_binary, l_binaryList


# Found a binary gap
def solution(binarynumber):
    l_count = 0
    l_max   = 0
    for i in binarynumber:
        if int(i) == 0:
            l_count += 1
        elif l_max < l_count:
             l_max = l_count    
             l_count = 0    
    return l_max
          
  
def primary():
    l_value = int(input("type a number to become in binary: "))
    l_binaryResult = NumberToBinary(l_value)
    #print(f"The Binary equivalent of the number {l_value} is:  {l_binaryResult[0]}")
    s = solution(l_binaryResult[1])
    if s == 0:
        print(f" The number {l_value} has a binary representation {l_binaryResult[0]}  and has NOT a binary gap")
    elif s > 0:
        print(f" The number {l_value} has a binary representation {l_binaryResult[0]}  and has a binary gap, {s}")
primary()    
