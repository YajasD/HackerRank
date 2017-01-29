## A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5] , then the array would become [3,4,5,1,2] .

## Given an array of n integers and a number, k , perform k left rotations on the array. Then print the updated array as a single line of space-separated integers.

n, k = raw_input().split(" ") 
n = int(n)
k = int(k)

a = raw_input().split(" ")
a = map(int, a)


a1 = a[:n+1] #Slices the array to select n elements
answer = a1[k:] + a1[:k] #Left rotation happens here
print  ' '.join(map(str, answer))





