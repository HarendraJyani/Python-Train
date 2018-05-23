#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    min_sum = max_sum = 0
    for i in range(len(arr)):
        if(i == len(arr)-1):
            break
        min_sum += arr[i]
    for i in range(len(arr)-1):
        max_sum += arr[i+1]
    print(min_sum,max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
