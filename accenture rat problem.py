def calculate (r, unit,arr,n):
    sum=0
    res=[]
    if len(arr)==0:
        return -1
    totalfood=(r*unit)
    for i in range(n):
        sum+=arr[i]
        res.append(i)
        if sum>=totalfood:
            break
    return len(res)
r = int (input ())
unit = int (input ())
n = int (input ())
  
arr = list (map (int, input ().split ()))
print (calculate (r, unit, arr, n))