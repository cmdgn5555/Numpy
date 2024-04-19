import numpy as np 

arr1 = np.array(55)
print(arr1)
print()

arr2 = np.array([1,2,3,4])
print(arr2)
print()

arr3 = np.array([[1,2,3], [4,5,6]])
print(arr3)
print()
print(arr3[0])
print()
print(arr3[1])
print('\n\n')

arr4 = np.array([[[1,2,3], 
                  [4,5,6], 
                  [7,8,9], 
                  [100,200,300]]])
print(arr4)
print(arr4[0][3])
print(arr4[0,2,2])
print(arr4[0,3,2])
print('\n\n')

arr5 = np.array([[['a','b','c'], ['d','e', 'f']]])
print(arr5)
print(arr5.dtype)
print()

arr6 = np.arange(1,10, step=2)
print(arr6)
print()

arr7 = np.arange(30,100,3)
print(arr7)
print()

arr8 = np.linspace(30,50,6)
print(arr8)
print()

arr9 = np.logspace(1, 3, 7)
print(arr9)
print()

arr10 = np.logspace(2, 5, 8, base=3, dtype='int')
print(arr10)
print()

arr11 = np.zeros(5)
print(arr11)
print()

arr12 = np.zeros((2,3), dtype=int)
print(arr12)
print()

arr13 = np.ones(10)
print(arr13)
print()

arr14 = np.ones((3,5), dtype=int)
print(arr14)
print('-----')

arr15 = np.ones((2,3,5), dtype=int)
print(arr15)
print('********')

arr16 = np.eye(5, k=2)
print(arr16)
print()

arr17 = np.eye(5, k=-2)
print(arr17)
print()

arr18 = np.eye(5)
print(arr18)
print()

arr19 = np.random.rand(3)
print(arr19)
print()

arr20 = np.random.rand(4,5)
print(arr20)
print()

arr21 = np.random.rand(3,4,6)
print(arr21)
print()

arr22 = np.random.rand(8)
print(arr22)
print()
arr23 = arr22 * 1000
print(arr23)
print('****************')

arr24 = np.random.randint(15,50,5)
print(arr24)
print()

arr25 = np.random.randint(0,100, (3,6))
print(arr25)
print('-------')

arr26 = np.array(1000000)
print(arr26)
print(arr26.ndim)
print(arr26.shape)
print()

arr27 = np.array([1,2,3,4,5,6,7,8])
print(arr27)
print(arr27.ndim)
print(arr27.shape)
print()

arr28 = np.array([[10,20,30], [40,50,60]])
print(arr28)
print(arr28.ndim)
print(arr28.shape)
print()

arr29 = np.array([[[150,250,350], [450,550,650], [750,850,950]]])
print(arr29)
print(arr29.ndim)
print(arr29.shape)
print()

arr30 = np.array([100,200,300,400,500,600,700,800,900])
print(arr30[4])
print(arr30[::-1])
print(arr30[2:7])
print(arr30[::-3])
print()

arr31 = np.arange(100,130).reshape(6,5)
print(arr31)
print('************')
print(arr31[3])
print('***************')
print(arr31[5][2])
print('**********')
print(arr31[4,4])
print('***********')
print(arr31[1,1])
print('\n\n')

arr32 = np.arange(200,250).reshape(2,5,5)
print(arr32)
print('----------')
print(arr32[1][3][2])
print(arr32[0][0][4])
print(arr32[1][2][3])
print(arr32[0,4,2])
print(arr32[1,1,3])
print(arr32[1,4,1])
print(arr32[1,0,-1])
print()

arr33 = np.arange(3,10+1)
print(arr33)
print(arr33[-1])
print('---------------------------------------')

arr34 = np.random.randint(1,100,15)
print(arr34)
print(arr34.max())
print(arr34.argmax())
print(arr34.min())
print(arr34.argmin())
print('\n')

arr35 = np.arange(50,65)
print(arr35)
print()
arr36 = arr35[5:10]
print(arr36)
arr37 = arr35[-5:]
print(arr37)
arr38 = arr35[-11:-3]
print(arr38)
arr39 = arr35[-13:-1]
print(arr39)
arr40 = arr35[4:]
print(arr40)
arr41 = arr35[3:13:2]
print(arr41)
arr42 = arr35[2:12:4]
print(arr42)
arr43 = arr35[5:14:3]
print(arr43)
arr44 = arr35[3:11][2]
print(arr44)
arr45 = arr35[0:]
print(arr45)
arr45[5:10] = 989
print(arr45)
print('**************')

arr46 = np.arange(-30,11)
print(arr46)
arr47 = arr46[5:19]
print(arr47)
print('\n\n')

arr48 = np.array([1.3, 4.7, 11.8, 13.5])
print(arr48)
print(arr48.dtype)
print()
arr49 = arr48.astype('int')
print(arr49)
print(arr49.dtype)
print('**************')

arr50 = np.array([1.3, 4.7, 11.8, 13.5])
print(arr50)
print(arr50.dtype)
print()
arr51 = arr50.astype('complex')
print(arr51)
print(arr51.dtype)
print(arr51.real)
print(arr51.imag)
print('************')

arr52 = np.array([16,21,23,27,30,34])
print(arr52)
print(arr52.dtype)
print()
arr53 = arr52.astype('float')
print(arr53)
print(arr53.dtype)
print(arr53.real)
print(arr53.imag)
print('******************')

arr54 = np.array(['5','7','10','12','15','18'])
print(arr54)
print(arr54.dtype)
arr55 = arr54.astype('int')
print(arr55)
print(arr55.dtype)
print()

arr56 = np.array(['55', '66', '77'])
print(arr56)
print(arr56.dtype)
print()
arr56 = arr56.astype('int')
print(arr56)
print(arr56.dtype)
print()
arr56 = arr56.astype('float')
print(arr56)
print(arr56.dtype)
print()
arr56 = arr56.astype('complex')
print(arr56)
print(arr56.dtype)
print('\n\n')

arr57 = np.identity(8)
print(arr57)
print()

arr58 = np.diag([1,2,3,4,5], k=2)
print(arr58)
print()

arr59 = np.diag([5,10,15,20,25,30], k=-1)
print(arr59)
print()

arr60 = np.arange(120).reshape(3,-1,5)
print(arr60)
print('\n\n')

arr61 = np.arange(180).reshape(-1,5,9)
print(arr61)
print('\n\n')

arr62 = np.arange(150).reshape(5,3,-1)
print(arr62)
print('*************************************************')

arr63 = np.arange(40).reshape(8,5)
print(arr63)
print(arr63.shape)
print()

arr64 = arr63.reshape(-1)
print(arr64)
print(arr64.shape)
print('\n\n')

arr65 = np.arange(30).reshape(10,3)
print(arr65)
print(arr65.shape)
print()

arr66 = arr65.reshape(-1)
print(arr66)
print(arr66.shape)
print('\n\n')

arr67 = np.arange(60).reshape(3,4,5)
print(arr67)
print(arr67.shape)
print()

arr68 = arr67.reshape(-1)
print(arr68)
print(arr68.shape)
print('\n\n\n')

arr69 = np.arange(30).reshape(2,5,-1)
print(arr69)
print(arr69.shape)
print()

arr70 = arr69.reshape(-1)
print(arr70)
print(arr70.shape)
print('\n\n\n\n')

arr71 = np.arange(80).reshape(-1,4,5)
print(arr71)
print(arr71.shape)
print()

arr72 = arr71.reshape(-1)
print(arr72)
print(arr72.shape)
print('\n\n\n')

arr73 = np.random.randint(1,50, size=90).reshape(3,-1,6)
print(arr73)
print(arr73.shape)
print()

arr74 = arr73.reshape(-1)
print(arr74)
print(arr74.shape)
print('\n\n\n\n')

arr75 = np.random.randint(1,10,size=5)
print(arr75)
np.random.shuffle(arr75)
print(arr75)
print('\n\n')
print('++++++++++++++++++++++++++++++++++++++++')

arr76 = np.arange(10)
print(arr76)
print()

for x in arr76:
    print(x)
print('\n\n')

arr77 = np.arange(20).reshape(4,5)
print(arr77)
print()

for y in arr77:
    print(y)
print()

for a in arr77:
    for b in a:
     print(b)
print('\n')

arr78 = np.arange(30).reshape(-1,2,5)
print(arr78)

for j in arr78:
   for k in j:
      for m in k:
         print(m)
print('\n\n')

arr79 = np.arange(30).reshape(-1,3,5)
print(arr79)
print(np.nditer(arr79))
for i in np.nditer(arr79):
   print(i)
print('\n\n')

arr79 = np.arange(30).reshape(-1,3,5)
print(arr79)
print(np.nditer(arr79))
for i in np.nditer(arr79):
   print(i)
print('\n\n')

arr80 = np.arange(120).reshape(3,10,-1)
print(arr80)
print(np.nditer(arr80))
for s in np.nditer(arr80):
   print(s)
print('\n\n')

arr81 = np.random.randint(10,20, size=(2,5,4))
print(arr81)
print(np.nditer(arr81))
for f in np.nditer(arr81):
   print(f)
print('\n\n')

arr82 = np.array([10,20,30,40,50,60,70,80,90])
print(arr82)
print(np.nditer(arr82))
for v in np.nditer(arr82):
   print(v)
print('\n\n\n')

array1 = np.array([10,20,150,100])
array2 = np.array([5,4,75,-25])
print(array1)
print(array2)
print(array1 + array2)
print(np.add(array1, array2))
print(array1 - array2)
print(np.subtract(array1, array2))
print(array1 * array2)
print(np.multiply(array1, array2))
print(array1 / array2)
print(np.divide(array1, array2))

array3 = np.arange(1,5)
array4 = np.array([2,3,4,5])
print(array3)
print(array4)
print(array3 ** array4)
print(np.power(array3, array4))
print()

array5 = np.array([5,6,7,8])
array6 = np.exp(array5)
print(array6)
print('************************')

array7 = np.random.randint(0,10,10)
print(array7)
print(array7.sum())
print(array7.mean())
print('\n')

array8 = np.array([1,3,5,8,12,19])
print(array8.var())
print(array8.std())
print()

array9 = np.array([4,7,10,15,14])
print(array9.var())
print(array9.std())
print()

array10 = np.array([5,15,20,25,35,40,70])
print(array10.var())
print(array10.std())
print('\n\n')

array11 = np.array([16,25,36,49,81,100,121,144])
print(array11)
print(array11 ** 0.5)
print(array11 ** 2)
print('\n\n')

array12 = np.logspace(1,4,8, base=3)
print(array12)
print('\n\n')

array13 = np.array([4,9,16,25,36,49])
print(array13)
print(np.sqrt(array13))
print('\n')

array14 = np.random.randint(15,100, size=10)
print(array14)
print(array14.max())
print(array14.argmax())
print(array14.min())
print(array14.argmin())
print('\n\n')

dizi1 = np.array([10,20,30,70])
dizi2 = np.array([100,200,600,900])
print(dizi1)
print(dizi2)
birlestir1 = np.concatenate([dizi1, dizi2], axis=0)
print(birlestir1)
print('\n\n')

dizi3 = np.array([[2,4,5,7],
                  [10,13,15,19]])
dizi4 = np.array([[30,50,80,90],
                  [150,250,350,450]])
print(dizi3)
print(dizi4)
birlestir2 = np.concatenate([dizi3, dizi4], axis=1)
print(birlestir2)
print('\n\n\n')

dizi5 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

dizi6 = np.array([[10,11,12],
                  [13,14,15],
                  [16,17,18]])

dizi7 = np.array([[19,20,21],
                  [22,23,24],
                  [25,26,27]])

print(dizi5)
print(dizi6)
print(dizi7)
print()
birlestir3 = np.concatenate([dizi5, dizi6, dizi7], axis=0)
print(birlestir3)
print('\n\n\n')

dizi8 = np.array([[30,31,32,33],
                  [34,35,36,37],
                  [38,39,40,41],
                  [42,43,44,45]])

dizi9 = np.array([[46,47,48,49],
                  [50,51,52,53],
                  [54,55,56,57],
                  [58,59,60,61]])

dizi10 = np.array([[62,63,64,65],
                  [66,67,68,69],
                  [70,71,72,73],
                  [74,75,76,77]])

print(dizi8)
print(dizi9)
print(dizi10)
print()
birlestir4 = np.concatenate([dizi8, dizi9, dizi10], axis=1)
print(birlestir4)

dizi11 = np.array([[1,2,3,4],
                  [5,6,7,8]])

dizi12 = np.array([[10,11,12,13],
                  [14,15,16,17]])

dizi13 = np.array([[20,21,22,23],
                  [24,25,26,27]])

print(dizi11)
print(dizi12)
print(dizi13)
print()
yıgın1 = np.stack([dizi11, dizi12, dizi13], axis=0)
print(yıgın1)
print('\n\n')

dizi14 = np.array([[28,29,30],
                  [31,32,33]])

dizi15 = np.array([[34,35,36],
                  [37,38,39]])

dizi16 = np.array([[40,41,42],
                  [43,44,45]])

dizi17 = np.array([[46,47,48],
                  [49,50,51]])


print(dizi14)
print(dizi15)
print(dizi16)
print(dizi17)
print()
yıgın2 = np.stack([dizi14, dizi15, dizi16, dizi17], axis=1)
print(yıgın2)
print('\n\n')

dizi18 = np.array([[3,6,9], [2,4,7]])
dizi19 = np.array([[5,10,15], [20,25,30]])
dizi20 = np.array([[40,50,60], [70,80,90]])
print(dizi18)
print(dizi19)
print(dizi20)
yatay_yıgınla = np.hstack([dizi18, dizi19, dizi20])
print(yatay_yıgınla)
print('\n\n\n')

dizi21 = np.array([[3,6,9], [2,4,7]])
dizi22 = np.array([[5,10,15], [20,25,30]])
dizi23 = np.array([[40,50,60], [70,80,90]])
print(dizi21)
print(dizi22)
print(dizi23)
dikey_yıgınla = np.vstack([dizi21, dizi22, dizi23])
print(dikey_yıgınla)
print('\n\n\n')

örnek1 = np.array([1,2,5,6,7,7,9,2,9,1,5,6])
print(örnek1)
print(np.where(örnek1 == 2))
print(np.where(örnek1 == 5))
print(np.where(örnek1 == 6))
print(np.where(örnek1 != 9))
print(np.where(örnek1 > 6))
print(np.where(örnek1 < 5))
print(np.where(örnek1 >= 7))
print(np.where(örnek1 <= 6))
print(np.where(örnek1 != 7))
print(np.where(örnek1 > 8))
print(np.where(örnek1 % 2 == 0))
print(np.where(örnek1 % 2 == 1))
print(np.where(örnek1 % 3 == 0))
print(np.where(örnek1 % 5 == 0))
print('\n')

örnek2 = np.arange(10,20)
print(örnek2)
print(np.where(örnek2 < 15, örnek2, örnek2 * 10))
print(np.where(örnek2 > 15, örnek2, örnek2 / 2))
print(np.where(örnek2 == 15, örnek2, örnek2 + 5))
print(np.where(örnek2 != 15, örnek2, örnek2 - 3))  
print('\n\n\n')

örnek3 = np.array([-3,-5,-8,10,14,17])
print(np.random.choice(örnek3, size=(5,4)))
print(np.random.choice(örnek3))
print('\n\n')

örnek4 = np.arange(1000,1125)
print(np.random.choice(örnek4, size=(3,2)))
print(np.random.choice(örnek4))
print('\n\n\n')
print('***************************************************')

diziler1 = np.array([1,2,3,4,5,6,7,8])
diziler2 = [1,2,3,4,5,6,7,8]
print(type(diziler1))
print(type(diziler2))
print()

diziler3 = [[1,2,3], [4,5,6], [7,8,9]]
diziler4 = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
print(diziler3)
print(diziler4)
print(type(diziler3))
print(type(diziler4))
print(diziler4.ndim)
print(diziler4.shape)
print(diziler4.size)
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('\n')

result = np.array([1,3,5,7,9])
print(result)
print()

result2 = np.arange(1,30)
print(result2)
print()

result3 = np.arange(50,100,3)
print(result3)
print()

result4 = np.zeros(10)
print(result4)
print()

result5 = np.ones(10)
print(result5)
print()

result6 = np.linspace(1,36,8)
print(result6)
print()

result7 = np.logspace(1,3,10, base=3)
print(result7)
print()

result8 = np.random.randint(0,10)
print(result8)
print()

result9 = np.random.randint(4)
print(result9)
print()

result10 = np.random.randint(2,7, size=3)
print(result10)
print()

result11 = np.random.rand(5)
print(result11)
print()

result12 = np.random.rand(5)
print(result12)
result13 = result12 * 100
print(result13)
print()

result14 = np.random.randn(12)
print(result14)
print()

result15 = np.arange(50).reshape(5,10)
print(result15)
print(result15.sum(axis=1))
print(result15.sum(axis=0))
print()

result16 = np.random.randint(1,100,10)
print(result16)
print(result16.max())
print(result16.min())
print(result16.argmax())
print(result16.argmin())
print(result16.mean())
print(np.median(result16))
print()

result17 = np.random.randint(1,30,6)
print(result17)
print(np.median(result17))
print()

result18 = np.array([0,5,10,15,20,25,50,75])
print(result18)
print(result18[7])
print(result18[-1])
print(result18[0:3])
print(result18[::-3])
print(result18[::-1])
print()

result19 = np.array([[1,3,5], [2,4,6], [50,100,150]])
print(result19)
print(result19[0])
print(result19[-1])
print(result19[0,2])
print(result19[2,1])
print(result19[:,2])
print(result19[:,1])
print(result19[:,0])
print(result19[0,:])
print(result19[1,:])
print(result19[2,:][0])
print('\n\n')

result20 = np.arange(0,10)
print(result20)
result21 = result20
print(result21)
print()

result21[0] = 333 * 3
print(result20)
print(result21)
print('\n\n')

result22 = np.arange(100,110)
result23 = result22.copy()
print(result22)
print(result23)

result23[0] = 22
print(result23)
print(result22)
print('\n\n')

result24 = np.arange(200,210)
result25 = result24.view()
print(result24)
print(result25)

result25[-1] = 950
print(result25)
print(result24)
print('\n\n')

numbers1 = np.random.randint(10,15,3)
numbers2 = np.random.randint(10,15,3)
print(numbers1)
print(numbers2)
print()
print(numbers1 + numbers2)
print(numbers1 + 10)
print(numbers2 * 2)
print(numbers1 - numbers2)
print(numbers1 - 3)
print(numbers2 - 7)
print(numbers1 * numbers2)
print(numbers1 / numbers2)
print(numbers1 / 2)
print(numbers2 / 3)
print(np.sqrt(numbers1))
print(np.sqrt(numbers2))
print(np.power(numbers1, 2))
print(np.power(numbers2, 2))
print('**********************************************')

numbers3 = np.random.randint(3,10,size=(2,3))
numbers4 = np.random.randint(3,10,size=(2,3))
print(numbers3)
print()
print(numbers4)
print()
print(np.vstack((numbers3, numbers4)))
print()
print(np.hstack((numbers3, numbers4)))
print('-----------------------------------------')

numbers5 = np.random.randint(20,50, size=(2,3))
print(numbers5)
print()
print(numbers5 >= 30)
print()
print(numbers5 % 2 == 0)
print()
print(numbers5 % 2 == 1)
print()
print(numbers5[numbers5 % 5 == 0])
print()
print(numbers5[numbers5 % 5 != 0])
print()
print(numbers5[numbers5 < 25])
print()
print(numbers5[numbers5 == [22,26,28]])
print()
print(numbers5 == 47)
print()
print(numbers5 != [36,41,46])
print()
print(numbers5 > [33,36,39])
print('\n\n')
print('*************************************************')


















 







