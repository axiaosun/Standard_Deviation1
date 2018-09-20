#!/usr/bin/env python3

#Find the standard deviation given n, the number of elements in an array, and x, the elements in an array

n = int(input())
x = list(map(int, input().split()))

mean = sum(x)/n

list_ = []
for i in range(n):
    sq_dist = (x[i]-mean) ** 2
    list_.append(sq_dist)

st_dev = (sum(list_)/n)**0.5

print("{0:0.1f}".format(st_dev))
