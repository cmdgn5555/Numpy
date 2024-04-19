import numpy as np 
from io import StringIO

liste = np.array([1,2,3])
liste *= 10
print(liste)

liste2 = np.array([8,11,14,17,22,25])
liste3 = liste2**2
print(liste3)

liste4 = np.array([33,35,43,47,51,59])
liste4 += 50
print(liste4)

liste5 = np.array([110,120,130,140,150,160])
liste5 -= 20
print(liste5)

liste6 = np.array([12,21,39,45,48,54,60])
liste6 //= 3
print(liste6)

liste7 = np.array([2,3,4,5])
liste8 = np.array([11,12,13,14])
print(liste7*liste8)

print(liste8[3])
print(liste8[1:])

liste9 = [13,23,33,43,53,63,73,83]
liste10 = np.array(liste9)
print(liste10)
print(liste10.shape)
print(liste10.size)
print(liste10.ndim)
print(liste10.dtype)
print(type(liste10))
print(type(liste9))

liste11 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(liste11[5:])

liste12 = [1,2,3,'4','seyfi']
print(type(liste12))

liste13 = np.array([5,10,'25', 'salih', 5.7])
print(liste13.dtype)

liste14 = np.array([5,10,12.7])
print(liste14.dtype)

liste15 = [2.4, 6.8, 9.5]
print(type(liste15))

liste16 = np.array(liste15)
print(liste16.dtype)
print(type(liste16))
print(liste16.shape)

liste17 = ([1,2], [3,4])
liste18 = np.array(liste17)
print(liste17)
print(liste18)
print(liste18.ndim)
print(liste18.size)
print(liste18.shape)
print(liste18.dtype)

liste19 = ([[[5,6], [7,8]]])
liste20 = np.array(liste19)
print(liste19)
print(liste20)
print(liste20.ndim)
print(liste20.size)
print(liste20.shape)
print(liste20.dtype)

dizi1 = np.array([10,20,30,40,50,60,70])
print(dizi1)
dizi1.fill(99)
print(dizi1)

matris2 = np.full((4, 3, 3), 25)
print(matris2)
print('*********************************')

matris3 = np.full((5, 6, 4, 3), 18)
print(matris3)

matris4 = np.array([[1,2,3], 
                    [4,5,6], 
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]])
print(matris4)
print(matris4[3,2])
print(matris4[2:])
print(matris4[0:1])
print(matris4[1:4])
print(matris4[:,2])
print(matris4[1:5,1])
print(matris4[:3,0])
matris4[4,2] = 200
print(matris4)
matris4[3] = [303,304,305]
print(matris4)
matris4[:,0] = [550,551,552,553,554]
print(matris4)

matris5 = np.array([[11,12,13],[14,15,16],[17,18,19]])
print(matris5)

matris6 = matris5
print(matris6)

matris5[1,1] = 30
print(matris5)
print(matris6)
matris6[2,2] = 45
print(matris6)
print(matris5)
print('***********************************')

matris7 = np.array([[8,10,12],
                   [14,16,18],
                   [20,22,24]])

matris8 = matris7.copy()
print(matris7)
print(matris8)

matris7[:,2] = [30,40,50]
print(matris7)
print(matris8)

matris8[:,0] = [100,200,300]
print(matris8)
print(matris7)
print('---------------------------------')

matris9 = np.array([[19,29,39],
                    [49,59,69],
                    [79,89,99]])

matris10 = matris9.view()
print(matris9)
print(matris10)

matris9[0] = [18,28,38]
print(matris9)
print(matris10)

matris10[:,2] = [16,26,36]
print(matris10)
print(matris9)

matris11 = np.random.randint(1,20,6)
print(matris11)

matris12 = np.random.random(4)
print(matris12)

dizi2 = np.array([1,2,3,4])
print(dizi2.nbytes)

dizi3 = np.array([1,2,3,4], dtype=np.float64)
print(dizi3.nbytes)

dizi4 = np.zeros((3,5,2))
print(dizi4)
print(dizi4[0].nbytes)

dizi5 = np.array([[1,2,3], 
                 [4,5,6],
                 [7,8,9]])

print(dizi5)
print(np.sum(dizi5))
print(np.sum(dizi5, axis=0))
print(np.sum(dizi5, axis=1))
print(np.sum(dizi5, axis=1, initial=10))
print(np.sum(dizi5, axis=0, initial=20))
print('******************************')

print(np.prod(dizi5))
print(np.prod(dizi5, axis=0))
print(np.prod(dizi5, axis=1))
print(np.prod(dizi5, axis=1, initial=2))
print(np.prod(dizi5, axis=0, initial=3))
print('*******************************')

print(np.mean(dizi5, dtype=int))
print(np.mean(dizi5, axis=0, dtype=int))
print(np.mean(dizi5, axis=1, dtype=int))
print('*******************************')

print(np.transpose(dizi5))

dizi6 = np.array([[9,8,7],
                  [4,5,6],
                  [3,2,1]])

print(dizi6.max())
print(dizi6.max(axis=1))
print(dizi6.max(axis=0))

print(dizi6.min())
print(dizi6.min(axis=1))
print(dizi6.min(axis=0))
print('******************************')

print(dizi6.argmin())
print(dizi6.argmin(axis=1))
print(dizi6.argmin(axis=0))
print('----------------------------')
print(dizi6.argmax())
print(dizi6.argmax(axis=1))
print(dizi6.argmax(axis=0))
print('******************************')

dizi7 = np.array([[5,10,15],
                  [20,25,30],
                  [35,40,45]])

print(dizi7.std(axis=0))
print(dizi7.std(axis=1))

print(dizi7.var(axis=0))
print(dizi7.var(axis=1))

print('**************************************')

dizi8 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(dizi8.clip(3,8))
print(dizi8.clip(10,15))

dizi9 = np.array([3.499999999, 5.89, 6.9999, 6.50, 9.51])
print(dizi9.round())

dizi10 = np.array([13.66666666, 22.13456789, 35.88885555])
print(dizi10.round(decimals=5))

dizi11 = np.array([[3,6,1,13,22,18,16,9],
                   [4.6, 2.3, 11.24, 7.5, 32.4, 10.2, 15.44, 26.1]])
print(np.sort(dizi11, axis=0))
print(np.sort(dizi11, axis=1))

dizi12 = np.array([2,3,4,5,26,37,44,67])
num = 45
print(np.searchsorted(dizi12, num))

dizi13 = np.array([12,15,20,23,27,32,40])
num2 = [33,34,35,36]
print(np.searchsorted(dizi13, num2))

dizi14 = np.arange(6)
print(dizi14)
print(dizi14.shape)
dizi14.shape = 2,3
print(dizi14)
dizi14.shape = 3,2
print(dizi14)

dizi15 = np.arange(8)
print(dizi15.shape)

dizi16 = dizi15[np.newaxis, :]
print(dizi16)
print(dizi16.shape)

dizi17 = dizi15[:, np.newaxis]
print(dizi17)
print(dizi17.shape)

dizi18 = np.array([[[2,4,6], 
                    [3,5,7], 
                    [10,20,30]]])
print(dizi18)
print(dizi18.shape)
out_arr = np.squeeze(dizi18)
print(out_arr)
print(out_arr.shape)

matris13 = np.array([[1,2,3], 
                     [4,5,6],
                     [7,8,9],
                     [10,11,12],
                     [13,14,15]])
print(matris13)
print(matris13.T)

matris14 = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
print(matris14)

matris15 = np.array([[10,20,30],
                     [40,50,60],
                     [70,80,90]])
print(matris15)

matris16 = np.concatenate((matris14, matris15), axis=1)
print(matris16)

matris17 = np.concatenate((matris14, matris15), axis=0)
print(matris17)

matris18 = np.vstack((matris14, matris15))
print(matris18)

matris19 = np.hstack((matris14, matris15))
print(matris19)

sırala_1 = np.array([[5,10],
                   [15,20],
                   [25,30]])

sırala_2 = np.array([[3,6],
                     [12,15],
                     [21,24]])

sırala_3 = np.array([[100,101],
                     [103,104],
                     [106,107]])

matris20 = np.vstack((sırala_1, sırala_2, sırala_3))
print(matris20)

matris21 = np.hstack((sırala_1, sırala_2, sırala_3))
print(matris21)

birlestir_1 = np.array([[1,11,21,31],
                        [2,12,22,32],
                        [3,13,23,33]])

birlestir_2 = np.array([[111,222,333,444],
                        [555,666,777,888],
                        [888,999,2000,1000]])

matris22 = np.concatenate((birlestir_1, birlestir_2), axis=0)
print(matris22)

matris23 = np.concatenate((birlestir_1, birlestir_2), axis=1)
print(matris23)

arr = np.array([[[2,3,4],[6,5,9]]])
print(arr)
print(arr.shape)

arr2 = np.squeeze(arr)
print(arr2)
print(arr2.shape) 

arr3 = np.arange(0,10,2, dtype=np.float64)
print(arr3)

arr4 = np.linspace(0,12,6)
print(arr4)

arr5 = np.linspace(0,12,6)
print(arr5)

print('**********************************')

x,y = np.meshgrid(arr4, arr5)
print(x)

print('-------------------------------')
print(y)

print('*************************************')

a = [1,2,3,4,5]
b = [1,2,3,4,5,6,7,8,9,10]
c = [1,2,3,4,5,6,7,8]

aa,bb,cc = np.meshgrid(a,b,c)
print(aa)
print('--------------------------', end='\n\n')
print(bb)
print('--------------------------', end='\n\n')
print(cc)
print(end='\n\n\n')

xxx = np.arange(0,7)
yyy = np.arange(0,7)
x1,y1 = np.meshgrid(xxx,yyy)
print(x1)
print()
print(y1)

array1 = np.linspace(0,10,5)
array2 = np.linspace(0,10,6)
print(array1)
print(array2)
print('komo*--------------*-------------*---------*')

x5,y5 = np.meshgrid(array1, array2)
print(x5)
print()
print(y5)

array3 = np.r_[0:8:2]
print(array3)

array4 = np.c_[0:12:3]
print(array4)

array5 = np.r_[2:15:3]
print(array5)

array6 = np.c_[4:24:5]
print(array6)

array7 = np.zeros(6)
print(array7)

array8 = np.zeros((8,4))
print(array8)

array9 = np.ones(7)
print(array9)

array10 = np.ones((4,6))
print(array10)

array11 = np.zeros(5) - 9
print(array11)

array12 = np.zeros((4,3)) + 15
print(array12)

array13 = np.ones(10) * 35
print(array13)

array14 = np.ones((7,6)) / 2
print(array14)

array15 = np.array([[2,4,6],
                    [3,5,7],
                    [10,15,20]])

array16 = np.zeros_like(array15)
print(array16)

array17 = np.ones_like(array15)
print(array17)

array18 = np.identity(5)
print(array18)

array19 = np.array([0,1,4,5,8,9,2,6,3,7,10])
array20 = np.array([2,3,4,9,6,5,7,1,0,8,10])
print(array19 == array20)
print(array19 != array20)
print(array19 >= array20)
print(array19 <= array20)
print(array19 > array20)
print(array19 < array20)

rastgele1 = np.random.rand(2,3,4)
print(rastgele1)
print(rastgele1.round())

print('*************------------------------***************')

rastgele2 = np.random.rand(5,4) * 10
print(rastgele2)
print(rastgele2.round())

rastgele3 = np.random.randint(10,20, size=(5,3))
print(rastgele3)

rastgele4 = np.random.randint(0,10,8)
print(rastgele4)

print('*-*-*-*-**-*-*-*-*-*-*-*-*-*--**-*-*-')

dizi19 = np.array([1,2,3,4,5])
print(dizi19)

np.random.shuffle(dizi19)
print(dizi19)

print('****************************-------------------------')

dizi20 = np.array([[5,10,15],
                   [20,25,30],
                   [35,40,45]])
print(dizi20)

np.random.shuffle(dizi20)
print(dizi20)

print('------------------------------------------')

arr6 = np.arange(10)
print(arr6)

np.random.shuffle(arr6)
print(arr6)

print('***********************************************')

mylist = ['A','C','B','B','B','A','A','C','B','A','C','B']

uniquelist, counts = np.unique(mylist, return_counts=True)

print(uniquelist, counts)

mylist2 = ['a','a','c','c','c','c','b','b','a','b','a','a']

uniquelist2, counts2 = np.unique(mylist2, return_index=True)

print(uniquelist2, counts2)

mylist3 = ['A','B','C','D','E','F','F','F','C','D','d','d']

uniquelist3, counts3 = np.unique(mylist3, return_inverse=True)

print(uniquelist3, counts3)

mylist4 = ['S','M','T','S','T','M','T','S','M','T','T','M']

uniquelist4, counts4, index4 = np.unique(mylist4, return_counts=True, return_index=True)

print(uniquelist4, counts4, index4)

dizi21 = np.array([1,2,3,4,5,6,7,8])
np.savetxt('array_dizi.txt', dizi21,  fmt='%d')

dosyaYük = np.loadtxt('array_dizi.txt')
print(dosyaYük)

dizi22 = np.array([10,20,30,40,50,60])
np.savetxt('array_dizi_2.txt', dizi22,  fmt='%d')

dosyaYük2 = np.loadtxt('array_dizi_2.txt')
print(dosyaYük2)

dizi23 = np.arange(0,10,1)
np.savetxt('array_dizi_3.txt', dizi23, delimiter=',')

dizi24 = np.arange(0,10,1)
dizi25 = np.arange(10,20,1)
dizi26 = np.arange(20,30,1)

np.savetxt('array_dizi_4.txt', (dizi24,dizi25,dizi26))

dosyaYük3 = np.loadtxt('array_dizi_4.txt')
print(dosyaYük3)

dizi27 = np.arange(0,50,5)
dizi28 = np.arange(50,100,5)
dizi29 = np.arange(100,150,5)

np.savetxt('array_dizi_5.txt', (dizi27,dizi28,dizi29), fmt='%d')

dosyaYük4 = np.loadtxt('array_dizi_5.txt')
print(dosyaYük4)

dosyaYük5 = np.loadtxt('array_dizi_6.txt', skiprows=1)
print(dosyaYük5)

mamo = np.arange(1,100,7)
np.save('deneme1', mamo)

dosyaYük6 = np.load('deneme1.npy')
print(dosyaYük6)

mamo2 = np.linspace(1,21,5)
np.save('deneme2', mamo2)

dosyaYük7 = np.load('deneme2.npy')
print(dosyaYük7)

mamo3 = StringIO('0 1 2 \n3 4 5')
dosyaYük8 = np.loadtxt(mamo3)
print(dosyaYük8)

dosyaYük9 = np.loadtxt('yaslar.txt', dtype=int, 
                       delimiter=',', comments='#',
                       usecols=(0,4), skiprows=5,
                       max_rows=4)
print(dosyaYük9)

dosyaYük10 = np.loadtxt('sayılar.txt', dtype=float,
                       delimiter=',', comments='#',
                       usecols=(0,1,2), skiprows=2,
                       max_rows=5)
print(dosyaYük10)

g = np.genfromtxt('tarihler.csv', dtype=int,
                  delimiter=',', comments='#', skip_header=2,
                  usecols=(0,1,2),max_rows=7, filling_values=2075,
                  )
print(g)

num3 = np.arange(0,502,2)
print(num3)

np.savetxt('numbers.csv', num3, delimiter=',', fmt='%d', newline='\n\n')

num4 = np.arange(0,1005,5)
print(num4)

np.savetxt('numbers_2.txt', num4, delimiter=',', 
           fmt='%d', newline='\n\n')

num5 = np.arange(1000,2010,10)
print(num5)

num5.tofile('nums1.csv', sep=':', format='%d')

num6 = np.random.randint(50,100,15)
print(num6)

num6.tofile('nums2.txt', sep=';', format='%d')

num7 = np.arange(10000,101000,1000)
print(num7)

num7.tofile('nums3.txt', sep=',', format='%d')

num8 = np.random.randint(1,1001,200)
print(num8, end='\n')

num8.tofile('nums4.csv', sep='-', format='%d')

num9 = np.random.randint(1,101,99)
print(num9)

np.savetxt('numbers_4.csv', num9, delimiter=',', 
           fmt='%d', newline='\n')

num10 = np.arange(10,105,5)
print(num10)

np.savetxt('numbers_5.txt', num10, delimiter=',', 
           fmt='%d', newline='\n')


dosyaYük11 = np.loadtxt('yaslar.txt', dtype=int,
                       delimiter=',', comments='#',
                       usecols=(2,3,4), skiprows=2,
                       max_rows=8, unpack=False)
print(dosyaYük11)

dizi30 = np.array([1,2,3,4,5,6,7])

np.savetxt('numbers_6.txt', dizi30, fmt='%.2f')
np.save('nums5.npy', dizi30)
dosyaYük12 = np.load('nums5.npy')
print(dosyaYük12)

dizi31 = np.array([10,20,30,40,50])
dizi32 = np.arange(10)

np.savez('nums6.npz', aaa = dizi31, bbb = dizi32)

xx = np.load('nums6.npz')
print(xx.keys())
print(xx['aaa'])
print(xx['bbb'])

dizi33 = np.arange(1,100,6)
dizi34 = np.linspace(1,29,15)
dizi35 = np.array([[1000,1001,1002],
                   [1002,1003,1004],
                   [1005,1006,1007]])

np.savez('nums7.npz', abc = dizi33, xyz = dizi34, www = dizi35)

yy = np.load('nums7.npz')
print(yy.keys())
print(yy['abc'])
print(yy['xyz'])
print(yy['www'])

matris24 = np.arange(9).reshape(3,3)
print(matris24)

matris24[[1,0]] = matris24[[0,1]]
print(matris24)

matris25 = np.arange(25).reshape(5,5)
print(matris25)

matris25[[3,4]] = matris25[[0,1]]
print(matris25)

matris26 = np.array([[5,10,15],
                     [20,25,30],
                     [35,40,45],
                     [50,55,60]])
print(matris26)

matris26[[3,2,1,0]] = matris26[[2,3,0,1]]
print(matris26)

matris27 = np.arange(40).reshape(8,5)
print(matris27)
print()

matris27[[7,0,6,1,5,2,4,3]] = matris27[[0,7,1,6,2,5,3,4]]
print(matris27)

matris28 = np.arange(10).reshape(10,1)
print(matris28)
print()

matris28[[9,0,8,1,7,2,6,3,5,4]] = matris28[[0,9,1,8,2,7,3,6,4,5]]
print(matris28)
print('******----------***********-------**************')

dizi36 = np.arange(30)
print(dizi36)

np.random.shuffle(dizi36)
print(dizi36)

print('-*-*--**--*-*---***--***--*******--**----')

dizi37 = np.arange(20).reshape(5,4)
print(dizi37)
print('---------------------------------------')

n = 3
print(dizi37[np.argpartition(-dizi37,n,axis=1)[:n]])

in_arr = np.array([[2,0,1], [5,4,9]])
print(in_arr)
print('*******')
out_arr = np.argpartition(in_arr, 1, axis=1)
print(out_arr)
print('********************')

abo1 = np.array([1,9,5,8,7,13,4,22,26,30])
print(abo1)
argp = np.argpartition(-abo1,-1)[:5]
print(argp)
print(np.sort(abo1[argp]))
print()

barb1 = [1,3,5,4,2]
print(barb1)
print(np.argpartition(barb1,3))

barb2 = [10,23,50,41,28]
print(barb2)
print(np.argpartition(barb2,3))


data = [10,11,15,64]

data_average = np.average(data)
print(data_average)

data2 = [10,20,30,12,13,70,80,90]

data_median = np.median(data2)
print(data_median)
print(end='\n')


dizi38 = np.array([[1,6,13,15,20],
                   [4,10,23,26,28],
                   [5,7,11,19,30]])

print(np.median(dizi38, axis=0))
print(np.median(dizi38, axis=1))
print('\n')

dizi39 = np.array([[32,35,37,41,46,48],
                   [56,53,57,59,54,51],
                   [60,69,67,63,62,66]])

print(np.median(dizi39, axis=0))
print(np.median(dizi39, axis=1))
print(end='\n')

data3 = [6,94,88,5,33,65,8,12,17,30,2]

data_median2 = np.median(data3)
print(data_median2)
print(end='\n')

dizi40 = np.array([[30,35,37,41,46,55],
                   [12,15,50,42,19,51],
                   [60,69,67,63,62,66],
                   [18,11,13,15,97,98]])

print(np.median(dizi40, axis=0))
print(np.median(dizi40, axis=1))
print(end='\n')

dizi41 = np.arange(1,21)
print(dizi41)

k = 3

print(dizi41[np.argpartition(-dizi41, k)[:10]])

matris29 = np.identity(5)
print(matris29)
print(matris29.nbytes)

boyut = matris29.size
print(boyut)

deger = matris29.itemsize
print(deger)

bitdegeri = boyut*deger
print(bitdegeri)

print('%d byte yer kaplar.' %bitdegeri)
print('******--------------------------***********')

matris30 = np.eye(7)
print(matris30)
print(matris30.nbytes)

boyut = matris30.size
print(boyut)

deger = matris30.itemsize
print(deger)

bitdegeri = boyut*deger
print(bitdegeri)

print('%d byte yer kaplar.' %bitdegeri)

print('******--------------------------***********')

matris31 = np.diag([[5,10,15,20,25,30],
                    [35,40,45,50,55,60],
                    [65,70,75,80,85,90],
                    [95,100,105,110,115,120],
                    [125,130,135,140,145,150],
                    [155,160,165,170,175,180]])
print(matris31)
print(matris31.nbytes)

boyut = matris31.size
print(boyut)

deger = matris31.itemsize
print(deger)

bitdegeri = boyut*deger
print(bitdegeri)

print('%d byte yer kaplar.' %bitdegeri)

print('******--------------------------***********')

matris32 = np.diag([3,6,9,12,15,18])
print(matris32)
print(matris32.nbytes)

boyut = matris32.size
print(boyut)

deger = matris32.itemsize
print(deger)

bitdegeri = boyut*deger
print(bitdegeri)

print('%d byte yer kaplar.' %bitdegeri)

print('***********************************-------------------------------------')

matris33 = np.zeros((4,4))
print(matris33)

matris33 = np.pad(matris33, pad_width=1, mode='constant', constant_values=15)
print(matris33)

print(end='\n\n')

matris34 = [1,3,5,7,9]

pad_arr = np.pad(matris34, (3,3), mode='constant', constant_values=(0,0))
print(pad_arr)

matris35 = [6,8,5,7,3]
pad_arr2 = np.pad(matris35, (3,5), mode='linear_ramp', end_values=(11,11))
print(pad_arr2)

matris36 = [2,4,6,7,8]
pad_arr3 = np.pad(matris36, (4,3), mode='maximum')
print(pad_arr3)

matris37 = [1,4,3,9,5]
pad_arr4 = np.pad(matris37, (5,3), mode='minimum')
print(pad_arr4)

matris38 = [[7,2],[3,6]]
pad_arr4 = np.pad(matris38, (3,), mode='maximum')
print(pad_arr4)

matris39 = [1,2,3,4,5]
pad_arr5 = np.pad(matris39, (2,3), mode='constant', constant_values=(4,6))
print(pad_arr5)

matris40 = [9,2,3,4,7]
pad_arr6 = np.pad(matris40, (6,5), mode='edge')
print(pad_arr6)

matris41 = [9,2,3,4,6]
pad_arr7 = np.pad(matris41, (3,5), mode='linear_ramp', end_values=(5,-4))
print(pad_arr7)

matris42 = [5,8,2,9,1]
pad_arr8 = np.pad(matris42, (3,5), mode='maximum')
print(pad_arr8)

matris43 = [5,8,7,9,1]
pad_arr9 = np.pad(matris43, (4,8), mode='mean')
print(pad_arr9)

matris44 = [5,8,9,6,3]
pad_arr10 = np.pad(matris44, (5,3), mode='median')
print(pad_arr10)

matris45 = [1,2,3,4,5,6,7,8,9]
pad_arr11 = np.pad(matris45, (5,5), mode='reflect')
print(pad_arr11)

matris46 = [1,2,3,4,5,6,7,8,9]
pad_arr12 = np.pad(matris46, (10,10), mode='reflect', reflect_type='odd')
print(pad_arr12)

matris47 = [1,2,3,4,5,6,7,8,9]
pad_arr13 = np.pad(matris47, (6,7), mode='symmetric')
print(pad_arr13)

matris48 = [1,2,3,4,5,6,7,8,9]
pad_arr14 = np.pad(matris48, (5,4), mode='symmetric',reflect_type='odd')
print(pad_arr14)

matris49 = [1,2,3,4,5,6,7,8,9]
pad_arr15 = np.pad(matris49, (3,3), mode='wrap')
print(pad_arr15)

matris50 = np.ones((4,4))
print(matris50)

matris50 = np.pad(matris50, pad_width=2, mode='constant', constant_values=33)
print(matris50)

import calendar

print(calendar.month(2001,9))

tarih = np.arange('2015-03', '2015-04', dtype='datetime64[D]')
print(tarih)

tarih2 = np.array(np.datetime64('2005-04-30'))
print(tarih2)

tarih3 = np.array(np.datetime64('2005-09', 'D'))
print(tarih3)

tarih4 = np.datetime64(1,'Y')
print(tarih4)

tarih5 = np.datetime64('2014-02')
print(tarih5)

tarih6 = np.datetime64('2014-02')
print(tarih6)

tarih7 = np.datetime64('2008-08', 'D')
print(tarih7)

tarih8 = np.datetime64('2002-01-04T08:30')
print(tarih8)

tarih9 = np.datetime64('nat')
print(tarih9)

tarih10 = np.arange('2024-02', '2024-03', dtype='datetime64[D]')
print(tarih10)

print(np.datetime64('1999') == np.datetime64('1999-01-01'))

print(np.datetime64('1998-04-15T23') == np.datetime64('1998-04-15T23:00:00.00'))

tarih11 = np.datetime64('2024-01-28') - np.datetime64('2012-04-22')
print(tarih11)

tarih12 = np.datetime64('1998-06-28') - np.datetime64('1994-06-01')
print(np.timedelta64(tarih12))

tarih13 = np.datetime64('2024-01-28') + np.timedelta64(20, 'D')
print(tarih13)

tarih14 = np.datetime64('2024-01-28T00:44') + np.timedelta64(13, 'h')
print(tarih14)

tarih15 = np.timedelta64(20,'W') / np.timedelta64(14, 'D')
print(tarih15)

tarih15 = np.timedelta64(8,'W') + np.timedelta64(44, 'D')
print(tarih15)

tarih16 = np.timedelta64(4,'W') // np.timedelta64(10, 'D')
print(tarih16)

tarih16 = np.timedelta64(6,'W') % np.timedelta64(11, 'D')
print(tarih16)

tarih17 = np.timedelta64(15,'W') - np.timedelta64(100, 'D')
print(tarih17)

tarih18 = np.timedelta64(30,'Y') - np.timedelta64(350, 'M')
print(tarih18)

tarih19 = np.timedelta64(15,'Y') / np.timedelta64(36, 'M')
print(tarih19)

tarih20 = np.timedelta64(7,'Y') + np.timedelta64(26, 'M')
print(tarih20)

tarih21 = np.busday_offset('2024-01-31', -15)
print(tarih21)

tarih22 = np.busday_offset('2023-12-05', 18)
print(tarih22) 

tarih23 = np.busday_offset('2023-11-06', 13, roll='forward')
print(tarih23) 

tarih24 = np.is_busday(np.datetime64('2024-01-05'))
print(tarih24) 

tarih25 = np.is_busday(np.datetime64('2024-01-06'))
print(tarih25) 

tarih26 = np.is_busday(np.datetime64('2024-01-07'))
print(tarih26) 

tarih27 = np.arange(np.datetime64('2024-01-15'), np.datetime64('2024-01-22'))
print(np.is_busday(tarih27)) 


tarih28 = np.arange(np.datetime64('2023-12-09'), np.datetime64('2023-12-30'))
print(np.is_busday(tarih28))


tarih29 = np.busday_count(np.datetime64('2023-10-08'), np.datetime64('2023-10-31'))
print(tarih29)

tarih30 = np.arange(np.datetime64('2023-09-02'), np.datetime64('2023-09-28'))
print(np.count_nonzero(np.is_busday(tarih30))) 

tarih31 = np.arange('2023-09-07','2023-11-02', dtype='datetime64[W]')
print(tarih31)
print()

tarih32 = np.arange('2020-05-31','2023-03-30', dtype='datetime64[M]')
print(tarih32)
print()

tarih33 = np.arange('2023-06-05','2023-07-20', dtype='datetime64[D]')
print(tarih33)
print()

tarih34 = np.arange('2024-01-08','2024-01-10', dtype='datetime64[h]')
print(tarih34)
print()

tarih35 = np.arange('2016-01-08','2024-01-10', dtype='datetime64[Y]')
print(tarih35)
print('\n')

result = np.datetime64('now')
print('güncel tarih ve saat:')
print(result)
print()

date_today = np.datetime64('today', 'D')
print('bugünün tarihi:')
print(date_today)
print()

year = np.datetime64('2024', 'Y')
month = np.datetime64('2024-04', 'M')
day = np.datetime64('2024-04-15', 'D')
hour = np.datetime64('2024-04-15T12', 'h')
minute = np.datetime64('2024-04-15T12:30', 'm')
second = np.datetime64('2024-04-15T12:30:23', 's')

print('yıl :', year)
print('ay :', month)
print('gün :', day)
print('saat :', hour)
print('dakika :', minute)
print('saniye :', second)
print()

from datetime import datetime

dt64 = np.datetime64('2024-03-12T20:36:45')
print(dt64)

dt = dt64.astype(datetime)
print(dt)
print()

dt2 = datetime(2016, 7, 16, 5, 45, 52)
print(dt2)

dt64_2 = np.datetime64(dt2)
print(dt64_2)
print()

dates = np.arange('2022-05-01', '2022-05-19', dtype='datetime64[D]')
print(dates)
print()

today = np.datetime64('today')
tomorrow = today + np.timedelta64(1, 'D')

print('bugünün tarihi : ', today)
print('yarının tarihi : ', tomorrow)
print()

date1 = np.datetime64('2024-05-02')
date2 = np.datetime64('2024-05-29')

num_days = date2 - date1

print(date2, 'ile', date1, 'arasındaki gün sayısı', num_days, 'gündür!!')

date3 = np.datetime64('2024-02-01')
date4 = np.datetime64('2024-02-28')

num_business_days = np.busday_count(date3, date4)

print(date4, 'ile', date3, 'tarihleri arasındaki iş günü sayısı', num_business_days, 'gün olarak hesaplanmıştır!!')
print('\n\n')

dizi42 = np.random.rand(5) * 10
print(dizi42)

zemin = np.floor(dizi42)
print(zemin)

dizi43 = np.array([1.342532, 2.8, 5.775, 9.2])
zemin2 = np.floor(dizi43)
print(zemin2)

dizi44 = np.zeros(5)
print(dizi44)

dizi44[4] = 686
print(dizi44)

dizi44[0] = 9349
print(dizi44)

dizi45 = np.ones(7)
print(dizi45)

#dizi45.flags.writeable = False

dizi45[0] = 354
print(dizi45)

dizi46 = np.arange(12)
print(dizi46)

dizi46.flags.writeable = True

dizi46_view = dizi46[5:]
print(dizi46_view)

print(dizi46_view.flags.writeable)

dizi46_view[6] = 4444
print(dizi46_view)
print('*-------*******-*******************-******---------------*****')
dizi47 = np.arange(33)
print(dizi47)

dizi47[10:15] = [101,102,103,104,105]
print(dizi47)

dizi47.flags.writeable = False

dizi47[0] = [313]
print(dizi47)





