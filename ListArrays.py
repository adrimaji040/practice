
def solution(A,K):
  i = 0
  #print("original list: ",  A)

  while i < K:
    #optain the last item of the arra
    l_lenght = len(A)
    l_lastElement = A[l_lenght - 1]
    #print(l_lastElement)
    
    #Delete the last element of the list
    A.remove(l_lastElement)
    #print(l_list)
    #Put the las item remove in the first place in the list
    A.insert(0,l_lastElement)
    i += 1
    
  return  A



l_list = [3,8,9,7,6]
K = 3
l_result = solution(l_list, K)   
print(l_result)
