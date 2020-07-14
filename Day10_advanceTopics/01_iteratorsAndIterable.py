class Fib:
    def __init__(self):
         self.prev = 0
         self.curr = 1   
    def __iter__(self):
        return self
    def __next__(self):
        value = self.curr
        if value<100:
            self.curr += self.prev
            self.prev = value
            return value
        else:
            raise StopIteration

myFib=Fib()
for i in myFib:
    print(i,end=" ")
print("\nnext example")
number=[5,6,7,8]
iteratorOfNumber=iter(number)
print(iteratorOfNumber.__next__(),end=" ")
print(next(iteratorOfNumber),end=" ")
print(next(iteratorOfNumber),end=" ")


li =[2,3,4,5,6]
comprehension = [x*2  for x in li ]
comprehension2 = [str(x)+" is even" if x%2==0 else str(x)+" is odd"  for x in li ]
comprehension3 = [ x  for x in li  if x%2==0]
comprehension4 ={ x ,x*(i+1) for x in comprehension3 for i in range(10) }
print(comprehension)
print(comprehension2)
print(comprehension3)
print(comprehension4)
