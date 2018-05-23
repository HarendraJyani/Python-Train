Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    two = arr[len(arr)-1]
    for i in range(len(arr)):
        if(arr[len(arr)-i-1]< two):
            two = arr[len(arr)-i-1]
            break
    print(two)
   
