arr = 100
first,second = 0,1

for x in range(arr+1):
    print first
    first,second = second,first + second
