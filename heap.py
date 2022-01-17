import heapq
#from random import random
import random
random_range=(1,100)
elements=80
heap=[]

dict_exists={}
for i in range(elements):
    
    no=random.randrange(*random_range)
    print(f" no. gen {no}")
    retried= False
    while dict_exists.get(no):
        retried= True
        no=random.randrange(*random_range)
    if retried:
        print(f" no. considered {no}")
    dict_exists[no]=no
    heapq.heappush(heap,no)

print(heap)
for i in range(len(heap)):
    print(heapq.heappop(heap))
    
print(heap)



#2 
heap = [21,31,12,9,5,2,41,36,1]
heapq.heapify(heap)
print(heap)    