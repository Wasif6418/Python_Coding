def reverse(A,start,end):
    while(start<end):
        A[start],A[end]= A[end], A[start]
        start=start+1
        end=end-1

A=[1,2,3,4,5]
print(A)
reverse(A,0,4)
print(A)
