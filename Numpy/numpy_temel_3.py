import numpy as np
import time
import math

yaz = np.array([1,3,5,7,9])
print(yaz)

skaler = np.array(90)

vektör = np.array([1,2,3,4,5,6])

matris = np.array([[1,2,3], [4,5,6], [7,8,9]])

tensor = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]]])

print(skaler)
print('----------------------------')
print(vektör)
print('----------------------------')
print(matris)
print('----------------------------')
print(tensor)
print('------------------------------')

z1 = time.time()

liste = []

for a in range(1000000):
    kuvvet = a**2
    liste.append(kuvvet)

z2 = time.time()

print(z2-z1)

print('---------------------------------')


z3 = time.time()

liste2 = np.arange(1000000000)**2

z4 = time.time()

print(z4-z3)

print('----------------------------------------')

vek = np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90])

print(vek[-1])
print(vek[2:6])
print(vek[::-1])
print(vek[::-3])
print(vek[::4])
print(vek[:7])
print(vek[1:14:5])
print(vek[::3])

print('-----------------------------')

vek1 = np.array([10,20,30,40,50,60])

mat1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(vek1)
print(mat1)
print(vek1.size)
print(mat1.size)
print(vek1.shape)
print(mat1.shape)
print(vek1.ndim)
print(mat1.ndim)
print(vek1.dtype)
print(mat1.dtype)
print(type(vek1))
print(type(mat1))

print('--------------------------')

sayilar = np.array([1,3,5,7,9,11,13,15])

print(sayilar.dtype)

sayilar2 = sayilar.astype('int64')
print(sayilar2.dtype)

sayilar3 = np.array([13,23,33,43,53], dtype='int8')
print(sayilar3.dtype)

tarih = np.array(['2022-05-05'])
print(tarih.dtype)

tarih2 = tarih.astype('datetime64[ps]')
print(tarih2.dtype) 

rakam = np.array([12.5,13.8,14.7,15.1,16.9])
print(rakam.dtype)
rakam1 = rakam.astype('int64')
print(rakam1.dtype)

rakam2 = np.array([1,0,3,0,0,1,2,5,546])
print(rakam2.dtype)
rakam3 = rakam2.astype('bool')
print(rakam3.dtype)
print(rakam3)

rakam4 = np.array([10,34,65,455,8798])
print(rakam4.dtype)
rakam5 = rakam4.astype('float')
print(rakam5.dtype)
print(rakam5)

rakam6 = np.array([12,14,16,18])
print(rakam6.dtype)
rakam7 = rakam6.astype('str')
print(rakam7.dtype)
print(rakam7)

rakam8 = np.array(['12', '17', '20'])
print(rakam8.dtype)
rakam9 = rakam8.astype('int')
print(rakam9.dtype)
print(rakam9)

rakam10 = np.array(['12', '17', '20'])
print(rakam10.dtype)
rakam11 = rakam10.astype('float')
print(rakam11.dtype)
print(rakam11)

rakam12 = np.array([90,92,94,96,98])
print(rakam12.dtype)
rakam13 = rakam12.astype('complex')
print(rakam13.dtype)
print(rakam13)

mylist = [['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 43, 55, 'hasan']]

uniqueList, counts = np.unique(mylist, return_counts=True)

print(uniqueList, counts)


mylist2 = [['V', 'L', 'M', 'V', 'V', 'M', 'S', 'D', 22, 10, 22, 10]]

uniqueList, index = np.unique(mylist2, return_index=True)

print(uniqueList, index)


mylist3 = np.array([2,4,6,5,6,3,5,2,4,3,2,5,3,6,5,4])

benzersiz = np.unique(mylist3)

print(benzersiz)


mylist4 = np.array([[10,25,20], [25,10,20], [20,25,10]])

benzersiz2 = np.unique(mylist4)

print(benzersiz2)

print('----------------------------------------')

mat2 = np.array([[1,2,3,4,50,60,70], [5,6,7,8,100,110,120], 
                 [9,10,11,12,130,140,150], [13,14,15,16,160,170,180], 
                 [17,18,19,20,190,200,210], [21,22,23,24,220,230,240], 
                 [25,26,27,28,250,260,270]])
print(mat2)
print('----------------------------------------')
print(mat2[3])
print('----------------------------------------')
print(mat2[1:5])
print('----------------------------------------')
print(mat2[3:6,0:3])
print('----------------------------------------')
print(mat2[6:7,0:7])
print('----------------------------------------')
print(mat2[5][6])
print('----------------------------------------')
print(mat2[2:6,1:2])
print('----------------------------------------')
print(mat2[2:5,4:5])
print('----------------------------------------')

rastgele = np.random.randint(0,10, (4,3))
print(rastgele)

rastgele2 = np.random.randint(0,20, (6,6)) - 10 
print(rastgele2)

rastgele3 = np.random.randint(20,30, (5,4)) * 2
print(rastgele3)

sayilar4 = np.arange(5,1000000)
print(sayilar4)

sayilar5 = np.arange(2,50,4)
print(sayilar5)

sayilar6 = np.linspace(3,24,8)
print(sayilar6)

sayilar7 = np.linspace(12,45, 10)
print(sayilar7)

print(sayilar7[5] - sayilar7[4])

print('----------------------------')

m1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(m1)
print(m1.shape)

print('----------------------------')

m2 = m1.reshape(4,3)
print(m2)
print(m2.shape)

print('----------------------------')

m3 = m1.reshape(2,6)
print(m3)
print(m3.shape)

print('----------------------------')

m4 = m1.reshape(6,2)
print(m4)
print(m4.shape)

print('----------------------------')

m5 = m1.reshape(12,1)
print(m5)
print(m5.shape)

print('----------------------------')

m6 = m1.reshape(1,12)
print(m6)
print(m6.shape)

print('----------------------------')

m7 = np.random.randint(0,2,(8,6)).reshape(12,4)
print(m7)

print('----------------------------')

m8 = np.linspace(52,80,15).reshape(5,3)
print(m8)

print('----------------------------')

m9 = np.random.randint(0,5,(4,4))
print(m9)

print('----------------------------')

m10 = m9.view()
print(m10)

print(m9[0][0])
print(m10[0][0])
print(m9[1])
print(m10[1])

m10[0]=[50,51,52,53]
print(m10)

m10[1]=[60,61,62,63]
print(m10)

m10[2]=[70,71,72,73]
print(m10)

m10[3]=[80,81,82,83]
print(m10)

print('----------------------------')
print('----------------------------')

m11 = np.random.randint(1,11, (3,5))
print(m11)

m12 = m11.view()
print(m12)

m12[:,4] = [123,133,143]
print(m12)

m12[:,3] = [250,260,270]
print(m12)

m12[:,2] = [301,302,303]
print(m12)

m12[:,1] = [1000,2000,3000]
print(m12)

m12[:,0] = [55,65,75]
print(m12)

m12[0,:] = [1010,2020,3030,4040,5050]
print(m12)

m12[1,:] = [101,201,301,401,501]
print(m12)

m12[2,:] = [55,66,77,88,99]
print(m12)

print('----------------------------------------------')
print('----------------------------------------------')
print('----------------------------------------------')

m13 = np.random.randint(5,15,(6,6))
print(m13)

m14 = m13.view()
print(m14)

m14[5] = [1000,2000,3000,4000,5000,6000]
print(m14)

print(m13)

print('----------------------------------------------')
print('----------------------------------------------')
print('----------------------------------------------')
print('----------------------------------------------')
print('----------------------------------------------')
print('----------------------------------------------')

m15 = np.random.randint(0,10,(5,5))
print(m15)

m16 = m15.copy()
print(m16)

print(m15[0])
print(m16[0])

m16[0] = [123,123,123,123,123]
print(m16)

print(m15)

m17 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(m17)

m18 = m17.copy()
print(m18)

m18[2] = [150,250,350]
print(m18)
print(m17)

m19 = np.array([[5,15,25,35], [6,16,26,36], [7,17,27,37], [8,18,28,38]])
print(m19)

m20 = m19.view()
print(m20)

m20[3] = [202,302,402,502]
print(m20)
print(m19)

sıfırlar = np.zeros(10)
print(sıfırlar)

sıfırlar2 = np.zeros((4,5))
print(sıfırlar2)

birler = np.ones(12)
print(birler)

birler2 = np.ones((6,2))
print(birler2)

doldur = np.full((3,7), 1023)
print(doldur)

doldur2 = np.full((8,4), 90900)
print(doldur2)

doldur3 = np.full((4,9), 'ali')
print(doldur3)

iden = np.identity(4)
print(iden)

e = np.eye(5,k=-1)
print(e) 

dia = np.diag([1,1,1,1,1], k=2)
print(dia)

e2 = np.eye(3)
print(e2)

e3 = np.eye(3,8)
print(e3)

dia2 = np.diag([12,23,34,45,56,67,78,89], k=-1)
print(dia2)

e4 = np.eye(7,7, k=-1)
print(e4)

e5 = np.eye(5, dtype=int)
print(e5)

iden2 = np.identity(4, dtype=int)
print(iden2)

rast = np.random.random(7)
print(rast)

uni = np.random.uniform(1,5, size=6)
print(uni)

e6 = np.eye(5,6)
print(e6)

A = np.array([[1,2,3,40,50], [4,5,6,70,80], [7,8,9,110,120], 
              [10,11,12,160,170], [13,14,15,180,190]])
print(A.ndim)
print(A)

dia3 = np.diag(A)
print(dia3)

B = np.array([12,13,14,15,16])

dia4 = np.diag(B)
print(dia4)

C = np.array([[10,20,30,40], [50,60,70,80], [90,100,110,120], [130,140,150,160]])

dia5 = np.diag(C)
print(dia5)

D = ([[7,17,27,150], [37,47,57,250], [67,77,87,350], [97,107,117,450]])
print(D)

dia6 = np.diag(D, k=-1)
print(dia6)

E = np.array([10,20,30,40,50])

dia7 = np.diag(E, k=-1)
print(dia7)

dia8 = np.diag([1,1,1,1,1])
print(dia8)

dia9 = np.diag([1,2,3,2,1])
print(dia9)
print('****************************************')

ran = np.random.randint(0,10,(5,5))
print(ran)

diag10 = np.diag(ran)
print(diag10)

diag11 = np.diag(np.diag(ran))
print(diag11)

print('****************************************')

ran2 = np.random.randint(15,20,(6,6))
print(ran2)

diag12 = np.diag(ran2)
print(diag12)

diag13 = np.diag(np.diag(ran2))
print(diag13)

cs =  np.count_nonzero([2,4,0,0,5,9,0,0,0])
print(cs) 

matris1 = np.ones((5,5))
matris2 = np.full((5,5),23)

print(matris1)
print(matris2)

matris3 = matris1.astype('int16')

print(matris3)
print(matris3.dtype)

print(matris3*4)
print(matris2+3)
print(matris3+matris2)
print(matris3-matris2)
print(matris2/3)
print(matris2//4)
print(matris2%7)

matris4 = np.full((5,6),12)
print(matris4)

print(matris4.shape)
print(matris2.shape)


matris4 = matris4.reshape(30)[:25].reshape(5,5)
print(matris4)
print(matris4.shape)
print(matris4*matris2)

matris1[0] = matris1[0]*10
print(matris1)

matris5 = np.arange(2,27).reshape((5,5))
print(matris5)

print(matris1*matris5)
print(matris1/matris5)
print(matris1+matris5)

matris6 = matris1 + matris5
print(matris6)

print(matris6*np.diag(matris6))
print(matris6+np.identity(5))
print(matris6-np.eye(5,5))

matris7 = np.random.randint(0,10,(5,5))
print(matris7)

print(matris7 > 4)
print(matris7 < 6)
print(matris7 == 3)
print(matris7 != 8)

print(matris7)
print(matris7[matris7 > 6]) 
print(matris7[matris7 < 3])
print(matris7[matris7 == 2].size)
print(matris7[matris7 != 5].size)
print(matris7)
print(matris7 % 2==0)
print(matris7 % 2==1)
print(matris7)
print(matris7[matris7 % 2==0])
print(matris7[matris7 % 2==1])
print(matris7[matris7 % 5==0])
print(matris7[matris7 % 3==0])

print(matris7)
sifir = matris7 == 0
bir = matris7 == 1
sifira_esit_olmayan = matris7 != 0
cift = matris7 % 2 == 0
tek = matris7 % 2 == 1
ücten_büyük = matris7 > 3
print(matris7[sifir])
print(matris7[cift])
print(matris7[sifira_esit_olmayan & tek])
print(matris7[tek & bir])
print(matris7[cift & sifira_esit_olmayan | bir])
print(matris7[tek & ücten_büyük])

matris8 = np.full((5,5), 90)
print(matris8)

print(matris8[cift & sifira_esit_olmayan | bir])






















