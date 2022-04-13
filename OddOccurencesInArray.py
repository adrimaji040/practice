A = [9,3,3,7,3,9,2]


#Solution 1
def solution(A):
    if (len(set(A)) == len(A)):
        print(f"All elements are unique, {set(A)}")
    else:
        print("The elemets are not unique")


#Solution 2 count()
B = []
def solution2(A):
    for elem in A:
        if A.count(elem) > 1: #There are duplicates in the list
            B.append(elem)
            print("B duplicates:",B)
            return True
        else:
             print("B not duplicates:",B) # These are the element not duplicates  
        return False


# Solution 3 final solution 
# To find the unique number in the list, the soution set to codility


def solution3(A):
    dupli = {}
    for elem in A:
        l_count = 0
        for i in A:
            if elem == i:
                l_count += 1
                dupli[elem] = l_count
        result = dupli
    print("result")
    x= result.values()
    print ("Values of final dictionary: ", x)

    fn = []
    for key, value in result.items():
       if value == 1: #just print key with value = 1, they are the unique element
          fn.append(key)
    
    for i in fn:
       return i 
           
            
NumberUnique = solution3(A)
print(NumberUnique)


# The same solution but JavaScript




        

    
        

    


          
    

