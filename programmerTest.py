num1 = range(10)
num2 = range(20)
arr  = [];
i = 0 ;
for (i1, i2) in zip(num1, num2):
  arr.append([i1, i2]);

print(arr)