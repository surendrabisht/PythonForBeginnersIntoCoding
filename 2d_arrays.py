array=[]
m = 3
n = 3

for i in range(m):
    array.append([])
    for j in range(n):
        array[i].append(f" {i} {j}")
  
      
for one_d_array in array:
    for item in one_d_array:
        print(item,end=" ")
    print("")


