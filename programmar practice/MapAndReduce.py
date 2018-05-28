#! encoding=utf-8

lista = [x*x for x in range(10)]
print(lista)

generatorA = (x*x for x in range(10))
# generator object <genexpr>
print(generatorA)
for iter in generatorA:
    print(iter)

# 查看连续,赋值顺序  结论顺序无关，是先计算出右边的值然后在赋值到左边
i, j = 0, 0
i, j = j+10, 20+i

def Filt(max):  # max为费布拉奇数列计算到多少位(j)
    i, j, k = 1, 1, 1
    while k < max:
        j, i = i+j, j
        print('i = ', i, 'j = ', j)
        k += 1;

#print(Filt(10))

def yieldtest(max):
    for i in range(max):
        yield i;

myGene = yieldtest(3);

for item in myGene:
    pass
    #print(item)


