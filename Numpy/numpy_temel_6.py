import numpy as np 
import time
from functools import reduce

start_time = time.time()
a = np.arange(1000000)
a ** 2
time_1 = time.time() - start_time

start_time_2 = time.time()
k = range(1000000)
[i ** 2 for i in k]
time_2 = time.time() - start_time_2

print(time_1)
print(time_2)
#print(time_2 / time_1)
print('****************************************************')

x = np.array([4,5,6,7])
print(x)

print(type(x))
print(x.shape)
print(x.size)
print(x.ndim)
print(x.nbytes)
print(x.itemsize)
print(x.dtype)
print('***************************************************')

y = np.array([[1,2,3], 
              [4,5,6]])
print(y)

print(type(y))
print(y.shape)
print(y.size)
print(y.ndim)
print(y.nbytes)
print(y.itemsize)
print(y.dtype)
print('***************************************************')

z = np.array([[[1,2], 
              [3,4],
              [5,6],
              [7,8]]])
print(z)

print(type(z))
print(z.shape)
print(z.size)
print(z.ndim)
print(z.nbytes)
print(z.itemsize)
print(z.dtype)

b = np.array([1,'2',3])
print(b)
print(b.dtype)

c = np.array([1,2.8,3])
print(c)
print(c.dtype)

f = np.array([3,4,5], dtype='int')
m = np.array([3,4,5], dtype='float')
s = np.array([3,4,5], dtype='complex')
print(f)
print(m)
print(s)

h = np.array([1.2, 2.6, 3.9], dtype='int')
print(h)
print(h.dtype)

d = np.array([1,2,3,4], dtype='float')
print(d)
print(d.dtype)

r = np.array(h, dtype='complex')
print(r)

p = np.array(d, dtype='complex')
print(p)

t = np.array([1,2,3,4])
print(t)
e = t.astype('complex')
print(e)

dizi1 = np.array([12.7, 16.4, 21.5, 34.8])
print(dizi1)
print(dizi1.dtype)
dizi2 = dizi1.astype('int')
print(dizi2)
print(dizi2.dtype)

dizi3 = np.array([1,2,3], dtype='int')
dizi4 = np.array([5.6, 9.2, 14.8], dtype='float')
dizi5 = np.array([3, 6, 7], dtype='complex')
print(dizi3 + dizi4 + dizi5)
print((dizi3 + dizi4 + dizi5).dtype)

dizi6 = np.sqrt(np.array([-1, 9, 4], dtype='complex'))
print(dizi6)
print(dizi6.dtype)

dizi7 = np.array([2,8,13,17], dtype='complex')
print(dizi7)

print(dizi7.real)
print((dizi7.real).dtype)
print(dizi7.imag)
print((dizi7.imag).dtype)
print('-----------------')

dizi8 = np.array([1+2j, 3+4j, 5+6j])
print(dizi8.real)
dizi8.real = 13
print(dizi8)

dizi9 = np.array([1+2j, 3+4j, 5+6j])
print(dizi9.imag)
dizi9.imag = [8,10,12]
print(dizi9)

sıfırlar = np.zeros(5)
print(sıfırlar)
birler = np.ones(6)
print(birler)

print(sıfırlar.dtype)
print(birler.dtype)

sıfırlar_2 = np.zeros((2,3,4), dtype='int')
print(sıfırlar_2)
print(sıfırlar_2.ndim)
print(sıfırlar_2.shape)
print(sıfırlar_2.size)
print(sıfırlar_2.dtype)

birler_2 = np.ones((3,2), dtype='float')
print(birler_2)

dolu = np.full((4,6,3), 12.9)
print(dolu)
print(dolu.dtype) 

islem = 12.5 * np.ones((2,3))
islem2 = 15.5 + np.zeros((3,4))
print(islem)
print(islem2)

bos = np.empty((4,2))
print(bos)

bos.fill(36)
print(bos)

x2 = np.eye(5,4,k=-1)
print(x2)

y2 = np.identity(8)
print(y2)

z2 = np.diag([4,7,8,13])
print(z2)

bos2 = np.empty(2, dtype='int')
print(bos2)

bos2.fill(9549)
print(bos2)

bos3 = np.empty([3,3], dtype='int')
print(bos3)

bos3.fill(9011)
print(bos3)

bos4 = np.empty([2,3], dtype='int')
print(bos4)

bos4.fill(305)
print(bos4)

x3 = np.arange(10)
print(x3)

x4 = np.arange(4,25,3)
print(x4)

y3 = np.linspace(0,15,10)
print(y3)

y4 = np.linspace(0,98)
print(y4)

y5 = np.linspace(1,20,6, endpoint=False)
print(y5)

y6 = np.arange(30)
print(y6)

x5 = np.reshape(y6, (5,6))
print(x5)

y7 = np.arange(48)
print(y7)

x6 = np.reshape(y7, (4,3,4))
print(x6)

y8 = np.linspace(1,88,30)
print(y8)

x7 = np.reshape(y8, (6,5))
print(x7)

y9 = np.linspace(2,97,20).reshape(4,5)
print(y9)

x8 = np.arange(3,51,1).reshape(12,4)
print(x8)

x9 = np.random.random((3,5))
print(x9)

x10 = np.random.randint(1,20, size=(10,5))
print(x10)

dizi10 = np.arange(10)
print(dizi10)
print(dizi10[0])
print(dizi10[2:8])
print(dizi10[::-1])
print(dizi10[::-2])
print(dizi10[:7])
print(dizi10[::2])
print(dizi10[-1])
print(dizi10[-8])
dizi10[5] = 303
print(dizi10)
dizi10[6:10] = [455,456,457,458]
print(dizi10)

dizi11 = np.arange(50,62).reshape(3,4)
print(dizi11)
print(dizi11[0,0])
print(dizi11[2,3])
print(dizi11[1,2])
dizi11[2,2] = 300
print(dizi11)
dizi11[0,3] = 909
print(dizi11)
dizi11[2,0] = 599
print(dizi11)

dizi12 = np.arange(15)
print(dizi12)
print()
dizi13 = np.delete(dizi12, [3,10])
print(dizi13)
print()
print(dizi12)
print()
dizi14 = np.delete(dizi12, [4,5,6,7,8,9])
print(dizi14)
print()
print(dizi12)
print('*******************************************')

dizi15 = np.arange(50)
print(dizi15)
dizi15 = np.delete(dizi15, [5,10,15,20,25,30,35,40,45])
print(dizi15)
print('\n')

dizi16 = np.arange(36).reshape(6,6)
print(dizi16)
print()
dizi16 = np.delete(dizi16, [0,1,2], axis=1)
print(dizi16)
print('************************************************')
dizi17 = np.arange(81).reshape(9,9)
print(dizi17)
print()
dizi17 = np.delete(dizi17, [3,4,5,6,7,8], axis=0)
print(dizi17)
print()
dizi17 = np.delete(dizi17, [1,2,3,4,5,6,7,8], axis=1)
print(dizi17)
print('\n')
dizi18 = np.arange(30).reshape(10,3)
print(dizi18)
print()
dizi18 = np.delete(dizi18, [8,2,13,20,25,28])
print(dizi18)

dizi19 = np.arange(5)
print(dizi19)
dizi19 = np.append(dizi19, 106)
print(dizi19)

dizi20 = np.arange(10)
print(dizi20)
dizi20 = np.append(dizi20, [101,104,106,200])
print(dizi20)
print()

x11 = np.arange(9).reshape(3,3)
print(x11)

x11 = np.append(x11, [[100,200,300]], axis=0)
print(x11)
print()

x11 = np.append(x11, [[550,650,750]], axis=0)
print(x11)

x11 = np.append(x11, [[1000,2000,3000]], axis=0)
print(x11)
print('\n')

x12 = np.arange(12).reshape(4,3)
print(x12)
x12 = np.append(x12, [[99], [199], [299], [399]], axis=1)
print(x12)
print()
x12 = np.append(x12, [[88], [188], [288], [388]], axis=1)
print(x12)

x13 = np.arange(100).reshape(10,10)
print(x13)
print()
x13 = np.append(x13, [[100,101,102,103,104,105,106,107,108,109]], axis=0)
print(x13)
print()
x13 = np.append(x13, [[110,111,112,113,114,115,116,117,118,119]], axis=0)
print(x13)
x13 = np.append(x13, [[300],[301],[302],[303],[304],[305],[306],[307],[308],[309],[310],[311]], axis=1)
print(x13)
x13 = np.append(x13, [[400],[401],[402],[403],[404],[405],[406],[407],[408],[409],[410],[411]], axis=1)
print(x13)
print()

x14 = np.arange(5,11).reshape(3,2)
print(x14)

x14 = np.append(x14, [[50,51]], axis=0)
print(x14)
x14 = np.append(x14, [[60,61]], axis=0)
print(x14)
x14 = np.append(x14, [[770],[771],[772],[773],[774]], axis=1)
print(x14)
x14 = np.append(x14, [[811],[812],[813],[814],[815]], axis=1)
print(x14)
print('****************************************************************************')

x15 = np.arange(10,30).reshape(4,5)
print(x15)
x15 = np.append(x15, [[106],[107],[108],[109]], axis=1)
print(x15)
x15 = np.append(x15, [[282],[283],[284],[285]], axis=1)
print(x15)
x15 = np.append(x15, [[533,534,535,536,537,538,539]], axis=0)
print(x15)
x15 = np.append(x15, [[632,633,634,635,636,637,638]], axis=0)
print(x15)
x15 = np.append(x15, [[903],[904],[905],[906],[907],[908]], axis=1)
print(x15)
print('\n')

arr1 = np.arange(100,120)
print(arr1)
arr1 = np.insert(arr1, 18, 33333)
print(arr1)

arr2 = np.arange(21,41)
print(arr2)
arr2 = np.insert(arr2, 11, 404040)
print(arr2)

arr3 = np.arange(5,15)
print(arr3)
arr3 = np.insert(arr3, 0, 7887)
print(arr3)

arr4 = np.arange(25,40)
print(arr4)
arr4 = np.insert(arr4, 12, [1,2,3,4,5])
print(arr4)

arr5 = np.arange(50,60)
print(arr5)
arr5 = np.insert(arr5, 9, [45,46,47,48,49])
print(arr5)

arr6 = np.arange(16).reshape(4,4)
print(arr6)
arr6 = np.insert(arr6, 2, [34,44,54,64], axis=0)
print(arr6)

arr7 = np.arange(9).reshape(3,3)
print(arr7)
arr7 = np.insert(arr7, 1, [50,500,5000], axis=0)
print(arr7)

arr8 = np.arange(25).reshape(5,5)
print(arr8)
arr8 = np.insert(arr8, 3, [44,45,46,47,48], axis=1)
print(arr8)

arr9 = np.arange(36).reshape(9,4)
print(arr9)
arr9 = np.insert(arr9, 3, [90,91,92,93,94,95,96,97,98], axis=1)
print(arr9)

arr9 = np.insert(arr9, 5, [75,76,77,78,79], axis=0)
print(arr9)

arr9 = np.insert(arr9, 1, [201,202,203,204,205,206,207,208,209,210], axis=1)
print(arr9)

arr9 = np.insert(arr9, 7, [506,507,508,509,510,511], axis=0)
print(arr9)

arr9 = np.insert(arr9, 4, [3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], axis=1)
print(arr9)

arr10 = np.arange(3)
print(arr10)
print()

arr11 = np.arange(9).reshape(3,3)
print(arr11)
print()

arr12 = np.vstack((arr11,arr10))
print(arr12)
print()

arr13 = np.hstack((arr10,arr11.reshape(9,)))
print(arr13)
print('**************************************')

dizi21 = np.arange(6)
print(dizi21)
print()

dizi22 = np.arange(6,42).reshape(6,6)
print(dizi22)
print()

dikey1 = np.vstack((dizi21, dizi22))
print(dikey1)
print('----------------------------------------------------')

dizi23 = np.arange(12)
print(dizi23)
print()

dizi24 = np.arange(20,50).reshape(10,3)
print(dizi24)
print()

dikey2 = np.vstack((dizi23.reshape(4,3), dizi24))
print(dikey2)
print('----------------------------------------------------')

dizi25 = np.arange(5,15)
print(dizi25)
print()

dizi26 = np.arange(30,80)
print(dizi26)
print()

dikey3 = np.vstack((dizi25, dizi26.reshape(5,10)))
print(dikey3)
print('----------------------------------------------------')

dizi27 = np.arange(5,15)
print(dizi27)
print()

dizi28 = np.arange(50,70).reshape(2,10)
print(dizi28)
print()

dikey4 = np.vstack((dizi27, dizi28))
print(dikey4)
print('----------------------------------------------------')
print()

dizi29 = np.arange(15)
print(dizi29)
print()

dizi30 = np.arange(60)
print(dizi30)
print()

dikey5 = np.vstack((dizi29.reshape(5,3), dizi30.reshape(20,3)))
print(dikey5)
print('----------------------------------------------------')

arr14 = np.arange(18)
print(arr14)
print()
arr15 = np.arange(18,30)
print(arr15)
print()

yatay1 = np.hstack((arr14,arr15))
print(yatay1)
print('\n')

arr16 = np.arange(20)
print(arr16)
print()
arr17 = np.arange(100).reshape(10,10)
print(arr17)
print()

yatay2 = np.hstack((arr16.reshape(10,2),arr17))
print(yatay2)
print('\n')

arr18 = np.arange(10).reshape(5,2)
print(arr18)
print()
arr19 = np.arange(50)
print(arr19)
print()

yatay3 = np.hstack((arr18,arr19.reshape(5,10)))
print(yatay3)
print('\n')

arr20 = np.arange(30).reshape(10,3)
print(arr20)
print()
arr21 = np.arange(60)
print(arr21)
print()

yatay4 = np.hstack((arr20,arr21.reshape(10,6)))
print(yatay4)

a1 = np.arange(10)
print(a1)
print()
print(a1[2:6])
print()
print(a1[4:])
print()
print(a1[:7])
print(a1[:-1])
print(a1[:-2])
print(a1[-4:-2])
print(a1[-6:-3])
print('\n')

a2 = np.arange(25).reshape(5,5)
print(a2)
print()

a3 = a2[0:3, 1:4]
print(a3)
print('\n')

a4 = a2[2:]
print(a4)
print()

a5 = a2[::]
print(a5)
print()

a6 = a2[:,3:]
print(a6)
print('*******************************')

b1 = np.arange(9).reshape(3,3)
print(b1)
print()

b2 = b1[1:2, 0:2]
print(b2)
print()

b2[0,1] = 333
print(b2)
print()

print(b1)
print()

print(np.shares_memory(b1,b2))
print('*****************************************')

b3 = np.arange(16).reshape(4,4)
print(b3)
print()
b4 = np.copy(b3[0:3, 1:3])
print(b4)
print()

print(np.shares_memory(b3,b4))
print()

b4[0,0] = 150
print(b4)
print(b3)
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

c1 = b3[1:2, 1:2].copy()
print(c1)
print(np.shares_memory(c1,b3))
print('********************************************')

deneme1 = np.arange(63).reshape(9,7)
print(deneme1)
print()

deneme2 = deneme1[2:5,1:5]
print(deneme2)
print()
deneme3 = deneme2[:,3] = 500,600,700
print(deneme3)
print()
print(deneme2)
print()
print(np.shares_memory(deneme2,deneme3))

xx = np.arange(21).reshape(7,3)
print(xx)
print()

yy = xx[6:7,:]
print(yy)
print()

yy[0,2] = 35000
print(yy)
print()
print(xx)
print()
print(np.shares_memory(xx,yy))
print('*****-------*********---------********---------**********------******')

xxx = np.arange(32).reshape(8,4)
print(xxx)
print()

yyy = np.copy(xxx[0:2,2:4])
print(yyy)
print()
print(np.shares_memory(xxx,yyy))
print()

yyy[1,1] = 4040
print(yyy)
print()
print(xxx)
print()

zzz = xxx[1:2, 1:2].copy()
print(zzz)
print()
print(np.shares_memory(xxx,zzz))
print()

mmm = xxx[3:4, 2:3]
print(mmm)
print()
print(np.shares_memory(xxx,mmm))
print()
mmm[0,0] = 3909
print(mmm)
print()
print(xxx)
print()

fff = xxx[0:4, 0:1].copy()
print(fff)
print()
fff[:,:] = 101
print(fff)
print()
print(xxx)
print()
print(np.shares_memory(xxx,fff))

print('--------------------------------------------------------------------')

örn1 = np.linspace(1,21,11)
print(örn1)
print()

örn2 = np.array([2,4,7])
print(örn2)
print()

print(örn1[örn2])
print('\n')

örn3 = np.arange(5,100,5)
print(örn3)
print()

örn4 = np.array([1,5,8,10,12,18])
print(örn4)
print()
print(örn3[örn4])

print('***********************************************************')

örn5 = np.arange(25).reshape(5,5)
print(örn5)
print()
örn6 = np.array([1,2])
print(örn6)
print()
print(örn5[örn6,:])
print()
print(örn5[:,örn6])
print('\n')

örn7 = np.arange(36).reshape(6,6)
print(örn7)
print()
örn8 = np.array([1,2])
print(örn8)
print()

örn9 = örn7[örn8]
print(örn9)
print()
örn9[1,0] = 9449
print(örn9)
print()
print(örn7)
print()
print(np.shares_memory(örn7,örn9))
print('**************------------------------------------------------')

xxxx = np.arange(10)
print(xxxx)
print()
print(xxxx[xxxx % 2 == 0])
print()
zzzz = xxxx[(xxxx % 2 == 0)]
print(zzzz)
print()
zzzz[0] = 1001
print(zzzz)
print()
print(xxxx)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

xxxxx = np.random.randint(10, size=10)
yyyyy = np.random.randint(10, size=10)
print(xxxxx)
print(yyyyy)
print(xxxxx > yyyyy)
print(type(xxxxx > yyyyy))
print((xxxxx > yyyyy).dtype)
print('\n\n')

xxxxxx = np.random.randint(25, size=15)
yyyyyy = np.random.randint(25, size=15)
print(xxxxxx)
print(yyyyyy)
zzzzzz = xxxxxx < yyyyyy
print(zzzzzz)
print(type(zzzzzz))
print((zzzzzz).dtype)
print('\n\n')

aa = np.random.randint(15, size=5)
bb = np.random.randint(3, size=5)
print(aa)
print(bb)

print(aa > bb)
print(type(aa > bb))
print((aa > bb).dtype)
print(np.all(aa > bb))
print('\n\n')

aaa = np.random.randint(5, size=5)
bbb = np.random.randint(50, size=5)
print(aaa)
print(bbb)

print(aaa > bbb)
print(type(aaa > bbb))
print((aaa > bbb).dtype)
print(np.any(aaa > bbb))

s = np.linspace(1,21,11)
print(s)

ş = (s % 3 == 0)
print(ş)
print(type(ş))
print(s[ş])
s[ş] = 690
print(s)
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")

ana1 = np.arange(5,30)
print(ana1)

baba1 = (ana1 % 5 == 0)
print(baba1)
print(type(baba1))
print(ana1[baba1])
ana1[baba1] = 1298
print(ana1)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

aaaa = np.linspace(5,62,20)
print(aaaa)
bbbb = np.array([4,6,12,16])
print(bbbb)
print(aaaa[bbbb])
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

n = np.arange(49).reshape(7,7)
print(n)
v = np.array([5,6])
print(v)
print(n[v,:])
print('-------------------------------------')

n = np.arange(49).reshape(7,7)
print(n)
v2 = np.array([0,1,2])
print(v2)
print(n[:,v2])
print('-------------------------------------')

w = n[v2,:]
print(w)
w[2,6] = 94329423
print(w)
print(n)
print(np.shares_memory(w,n))
print('*****************************************')

ww = np.arange(25).reshape(5,5)
print(ww)

dd = ww[0:2,2:4]
print(dd)

dd[1,1] = 40434

print(dd)

print(ww)
print(np.shares_memory(ww,dd))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

j = np.arange(10)
print(j)
print(j[(j % 2 == 0)])

jj = j[(j % 2 == 0)]
print(jj)
jj[4] = 2393
print(jj)
print(j)
print(np.shares_memory(j,jj))

gg = np.linspace(10,100,19)
print(gg)

mask = (gg % 3 == 0)
print(mask)
print(type(mask))
print(mask.dtype)
print(gg[mask])
gg[mask] = 3404
print(gg)
print('***************************************************************')

kes1 = np.array([2,4,6,8,9,1])
kes2 = np.array([9,2,4,14,16,17,19])
kes3 = np.intersect1d(kes1,kes2)
print(kes3)
print('\n')

kes4 = np.array([53,56,60,62,100,106,111,156,195,202,265,278])
kes5 = np.array([50,75,81,56,111,195,278,304,315])
kes6 = np.intersect1d(kes4, kes5, return_indices=True)
print(kes6)

red = reduce(np.intersect1d, ([1,3,5,9], [5,6,10,13], [8,12,13,5]))
print(red)

red2 = reduce(np.intersect1d, ([10,30,20,40], [30,40,15,25], 
                               [35,45,30,40], [40, 88, 99, 30]))
print(red2)

red3 = reduce(np.intersect1d, ([1,2,3,4,5,6,7,8,9], 
                               [8,3,6,1,12,14,16,20], 
                               [35,8,3,40,45,1,50,6,66], 
                               [69,3,71,74,78,8,100,110,6,113,117,1,124,126], 
                               [91,8,92,93,94,6,95,96,97,1,98,99,3]))
print(red3)
print('*************************************************************')
kes7 = np.arange(20)
kes8 = np.linspace(1,28,10)
print(kes7)
print(kes8)

kes9 = np.intersect1d(kes7,kes8,return_indices=True)
print(kes9)

kes10 = np.array([5,10,15,20,25,30,35,40,45,50])
kes11 = np.array([10,20,30,40,50])
print(kes10)
print(kes11)

kes12 = np.intersect1d(kes10,kes11,return_indices=True)
print(kes12)

kes13 = np.array([[3,6,9], [2,4,6]])
kes14 = np.array([[3,2,6], [1,7,9]])
print(kes13)
print(kes14)

kes15 = np.intersect1d(kes13,kes14,return_indices=True)
print(kes15)

kes16 = np.array([[2,6,9], [7,11,10], [12,13,15], [20,22,23]])
kes17 = np.array([[3,2,6], [1,7,9], [23,25,29], [15,18,12]])
print(kes16)
print(kes17)

kes18 = np.intersect1d(kes16,kes17,return_indices=True)
print(kes18)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

fark1 = np.array([3,5,8,12,16,20,24,26,29,35,37])
fark2 = np.array([2,10,16,20,24,29,30,33,38])
fark3 = np.setdiff1d(fark1,fark2)
print(fark3)
print()

fark4 = np.array([3,5,8,12,16,20,24,26,29,35,37])
fark5 = np.array([2,10,16,20,24,29,30,33,38])
fark6 = np.setdiff1d(fark5,fark4)
print(fark6)
print()

fark7 = np.array([101,102,106,110,118,121,123,127,130,132,134,137,140])
fark8 = np.array([100,103,106,110,119,120,123,127,131,135,137,140])
fark9 = np.setdiff1d(fark7,fark8)
print(fark9)
print()

fark10 = np.array([101,102,106,110,118,121,123,127,130,132,134,137,140])
fark11 = np.array([100,103,106,110,119,120,123,127,131,135,137,140])
fark12 = np.setdiff1d(fark11,fark10)
print(fark12)
print('****************************************************************')

birlesim1 = np.array([8,11,12,14,16,17,19,20,22,23,25])
birlesim2 = np.array([6,13,14,16,17,20,24,29,30,32,33,35])
birlesim3 = np.union1d(birlesim1,birlesim2)
print(birlesim3)

birlesim4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
birlesim5 = np.array([1,2,3,4,5,6,30,31,32,33,34,35,36,37,38,39,40,41,42])
birlesim6 = np.union1d(birlesim4,birlesim5)
print(birlesim6)

birlesim7 = np.array([[5,10,15],[20,25,30],[35,40,45],[50,55,60]])
birlesim8 = np.array([[2,4,6],[8,12,14],[1,3,7],[9,11,13]])
birlesim9 = np.union1d(birlesim7,birlesim8)
print(birlesim9)

tek = np.array([2,4,5,7,8,2,5,7,1,8,1,4,2,8,1,7,5,4,2,7,8,1])
result = np.unique(tek)
print(result)
print('\n')

icinde1 = np.array([3,4,5,10,11,12,25,26,27,30,31,32])
icinde2 = np.array([8,9,10,12,23,24,28,30,32,33,40,41])
icinde3 = np.in1d(icinde1,icinde2)
print(icinde3)
print()

icinde4 = np.array([0,5,8,17,33,45,46,53,58,64,66])
icinde5 = np.array([0,5,10,33,45,52,57,64,66,70,71])
icinde6 = np.in1d(icinde5,icinde4)
print(icinde6)

icinde7 = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
icinde8 = np.array([[8,11,1,3],[2,5,4,7],[34,38,40,43]])
icinde9 = np.in1d(icinde8,icinde7)
print(icinde9)
print('\n')

sırala1 = np.random.randint(1,10, size=10)
print(sırala1)
print(np.sort(sırala1))
print(sırala1)
print()

sırala2 = np.random.randint(50,200,size=10)
print(sırala2)
sırala2.sort()
print(sırala2)
print('\n\n')
print('*****************************************')

sırala3 = np.random.randint(100,200,size=(3,3)) 
print(sırala3)
print()
print(np.sort(sırala3, axis=0))
print()
print(np.sort(sırala3, axis=1))
print()

test = np.array([0,1,2,5,0])
states = [0,2]
mask2 = np.in1d(test, states)
print(mask2)
print(test[mask2])
print()
mask3 = np.in1d(test, states, invert=True)
print(mask3)
print(test[mask3])
print('\n\n')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

sırala4 = np.array([[4,2],[3,1],[8,7],[9,6]])
sırala5 = np.sort(sırala4, axis=1)
print(sırala5)
print()

sırala6 = np.array([[12,10],[15,11],[19,14],[17,16]])
sırala7 = np.sort(sırala6, axis=None)
print(sırala7)
print()

sırala8 = np.array([[12,10],[15,11],[19,14],[17,16]])
sırala9 = np.sort(sırala8, axis=0)
print(sırala9)
print()

sırala10 = np.array([[29,26,24,23,21,20],[39,35,37,32,34,30],[45,43,48,46,44,40]])
sırala11 = np.sort(sırala10, axis=1)
print(sırala11)
print()

sırala12 = np.array([[3,214,91,65,110,87],[193,162,151,14,52,23],[185,132,106,78,206,5]])
sırala13 = np.sort(sırala12, axis=None)
print(sırala13)
print()

sırala14 = np.array([[72,15,98,22,35,80],
                     [70,14,91,19,17,23],
                     [79,11,88,59,78,50],
                     [75,18,99,43,61,10]])
sırala15 = np.sort(sırala14, axis=0)
print(sırala15)
print('\n\n')

sırala16 = np.random.randint(0,100,size=(4,4))
print(sırala16)
print()
sırala17 = np.sort(sırala16, axis=0)
print(sırala17)
print()
sırala18 = np.sort(sırala16, axis=1)
print(sırala18)
print('**********************************************************************')

sırala19 = np.random.randint(1,50, size=5)
print(sırala19)
print(np.sort(sırala19))
print(sırala19)
print('\n\n')

sırala20 = np.random.randint(1,100, size=(3,3))
print(sırala20)
sırala20.sort()
print(sırala20)
print()

sırala21 = np.random.randint(1,100, size=(3,3))
print(sırala21)
sırala22 = np.sort(sırala21, axis=None)
print(sırala22)
print('\n\n')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

islemler1 = np.random.randint(1,10, size=5)
print(islemler1)
islemler2 = np.random.randint(1,10, size=5)
print(islemler2)
print()

print(islemler1 + islemler2)
print(np.add(islemler1, islemler2))
print(type(islemler1 + islemler2))
print(type(np.add(islemler1, islemler2)))
print()

print(islemler1 - islemler2)
print(np.subtract(islemler1, islemler2))
print(type(islemler1 - islemler2))
print(type(np.subtract(islemler1, islemler2)))
print()

print(islemler1 * islemler2)
print(np.multiply(islemler1, islemler2))
print(type(islemler1 * islemler2))
print(type(np.multiply(islemler1, islemler2)))
print()

print(islemler1 / islemler2)
print(np.divide(islemler1, islemler2))
print(type(islemler1 / islemler2))
print(type(np.divide(islemler1, islemler2)))
print('\n\n')

islemler3 = np.random.randint(10,15,size=5)
print(islemler3)
print()
print(islemler3 + 2)
print(islemler3 - 2)
print(islemler3 * 2)
print(islemler3 / 2)
print('\n\n')

islemler4 = np.random.randint(20,25,size=10)
print(islemler4)
islemler5 = np.random.randint(20,25,size=10)
print(islemler5)
print(islemler4 == islemler5)
print((islemler4 == islemler5).dtype)
print('\n\n')
print('*****************************************************************')

islemler6 = np.random.randint(1,10, size=(3,3))
print(islemler6)
print()
islemler7 = np.random.randint(1,10, size=(3,3))
print(islemler7)
print()

print(np.add(islemler6, islemler7))
print()

print(np.subtract(islemler6, islemler7))
print()

print(np.multiply(islemler6, islemler7))
print()

print(np.divide(islemler6, islemler7))
print('\n\n')

islemler8 = np.random.randint(1,5, size=5)
print(islemler8)
islemler9 = np.random.randint(1,5, size=5)
print(islemler9)
print(np.array_equal(islemler8, islemler9))
print('\n\n')

islemler10 = np.array([1,6,8,13,15,17,21,23,26])
print(islemler10)
islemler11 = np.array([1,6,8,13,15,17,21,23,26])
print(islemler11)
print(np.array_equal(islemler10, islemler11))
print()

islemler12 = np.random.randint(1,10, size=(2,2))
print(islemler12)
print(np.sqrt(islemler12))
print()

islemler13 = np.array([16,25,36,49,64,81,100,121,144])
print(islemler13)
print(np.sqrt(islemler13))
print()

islemler14 = np.array([2,3,4,5,6,7,8])
print(islemler14)
print(np.power(islemler14, 5))
print()

islemler15 = np.random.randint(5,10, size=(3,3))
print(islemler15)
print(np.power(islemler15, 3))
print()

islemler16 = np.arange(2,8)
print(islemler16)
print(np.power(islemler16, 4))
print('\n')

islemler17 = np.arange(1,6)
print(islemler17)
print(np.exp(islemler17))
print()

islemler18 = np.random.randint(3,8, size=5)
print(islemler18)
print(np.exp(islemler18))
print('\n\n')

islemler19 = np.random.randint(1,10, size=9).reshape(3,3)
print(islemler19)
print(np.sum(islemler19))
print()

islemler20 = np.random.randint(1,10, size=9).reshape(3,3)
print(islemler20)
print('--------')
print(np.sum(islemler20))
print('--------')
print(islemler20.sum(axis=0))
print('--------')
print(islemler20.sum(axis=1))
print('--------')
print(islemler20.min())
print('--------')
print(islemler20.max())
print('--------')
print(islemler20.argmin())
print('--------')
print(islemler20.argmax())
print()

islemler21 = np.random.randint(1,200, size=25).reshape(5,5)
print(islemler21)
print()
print(islemler21.min(axis=0))
print(islemler21.min(axis=1))
print('\n')

islemler22 = np.random.randint(1,300, size=25).reshape(5,5)
print(islemler22)
print()
print(islemler22.max(axis=0))
print(islemler22.max(axis=1))
print()
print('*************************************************************')

islemler23 = np.random.randint(1,200, size=25).reshape(5,5)
print(islemler23)
print()
print(islemler23.argmin(axis=0))
print(islemler23.argmin(axis=1))
print('\n')

islemler24 = np.random.randint(1,300, size=25).reshape(5,5)
print(islemler24)
print()
print(islemler24.argmax(axis=0))
print(islemler24.argmax(axis=1))
print()

islemler25 = np.random.randint(1,20, size=16).reshape(4,4)
print(islemler25)
print(islemler25.sum(axis=0))
print(islemler25.sum(axis=1))
print('**************************************************')

islemler26 = np.random.randint(1,10, size=8)
print(islemler26)
print()
print(islemler26.mean())
print()
print(np.median(islemler26))
print()
print(islemler26.std())
print()
print(islemler26.var())
print('\n\n')

islemler27 = np.array([[10,5,75], 
                       [20,15,85], 
                       [30,25,95], 
                       [40,35,105]])
print(islemler27.mean(axis=0))
print(islemler27.mean(axis=1))
print('\n\n')

islemler28 = np.array([2,4,6,8,10,12,14,17,20,23,27])
print(np.median(islemler28))
print()
islemler28 = np.array([2,4,6,8,10,12,14,17,20,23,27,55])
print(np.median(islemler28))
print()
islemler29 = np.array([[2,5,7,8],
                       [4,9,13,15],
                       [18,21,23,26],
                       [33,35,36,39]])
print(np.median(islemler29, axis=0))
print(np.median(islemler29, axis=1))
print()

islemler29 = np.array([[1,2,3,4],
                      [5,6,7,8],
                      [9,10,11,12],
                      [13,14,15,16]])
print(islemler29)
print()
print(np.median(islemler29, axis=0))
print(np.median(islemler29, axis=1))
print()

islemler30 = np.array([[50,52,55,57,58],
                      [61,62,64,66,69],
                      [73,74,77,78,79],
                      [82,85,86,87,88]])
print(islemler30)
print()
print(np.median(islemler30, axis=0))
print(np.median(islemler30, axis=1))
print()


islemler30 = np.array([[10,20,30,40,50,60],
                      [70,80,90,100,110,120],
                      [130,140,150,160,170,180],
                      [190,200,210,220,230,240],
                      [250,260,270,280,290,300],
                      [310,320,330,340,350,360]])
print(islemler30)
print()
print(np.median(islemler30, axis=0))
print(np.median(islemler30, axis=1))
print()

islemler31 = np.array([3,7,5,10,15,8,9,19,17,16,20,24,22,26])
print(islemler31)
print()
print(np.median(islemler31))
print()

islemler32 = np.array([5,10,15,20,25,30,35,40,45,50,55])
print(islemler32)
print()
print(np.median(islemler32))
print('***********************************************************')
print('\n')

islemler33 = np.random.randint(3,10, size=10)
print(islemler33)
print(islemler33.var())
print(islemler33.std())
print()

islemler34 = np.array([8,10,12,15,18,22,25,30,35,25])
print(islemler34)
print(islemler34.var())
print(islemler34.std())
print()

islemler35 = np.random.randint(5,30, size=(5,5))
print(islemler35)
print(np.median(islemler35, axis=1))
print(np.median(islemler35, axis=0))
print()

islemler36 = np.random.randint(5,20, size=(3,3))
print(islemler36)
print(np.median(islemler36, axis=1))
print(np.median(islemler36, axis=0))
print('\n\n')
print('--------------------------------------------------------------------')

array1 = np.random.randint(1,10, size=(4,2))
print(array1)
print()

array2 = np.random.randint(1,10, size=(1,2))
print(array2)
print()

print(array1 + array2)
print()

array3 = np.arange(10).reshape(10,)
print(array3)
print()

array4 = np.arange(5,6).reshape(1,)
print(array4)
print()

print(array3 + array4)
print('\n\n')

array5 = np.ones((3,3))
print(array5)
print()

array6 = np.arange(9).reshape(3,3)
print(array6)
print()

print(array5 + array6)
print()

array7 = np.arange(5).reshape(5,1)
print(array7)
print()

array8 = np.arange(25).reshape(5,5)
print(array8)
print()

print(array7 + array8)
print()

array9 = np.array([5,10,20,30]).reshape(4,1)
print(array9)
array10 = np.array([2,4,6,8,10])
print(array10)
print(array9 + array10)
print('\n\n')

örnek1 = np.arange(7,43,2)
print(örnek1)
print()

örnek2 = np.random.randint(1,10, size=(4,4))
print(örnek2)
print()

örnek3 = np.linspace(0.1, 1, 10)
print(örnek3)
print()

örnek4 = np.arange(25).reshape(5,5)
print(örnek4)
print()
örnek5 = örnek4[1:3,2:4]
print(örnek5)
print()

örnek6 = np.arange(1,17,).reshape(4,4)
print(örnek6)
print()
örnek7 = örnek6[örnek6 % 2 == 0].reshape(2,4)
print(örnek7)
print()

örnek8 = np.arange(1,101,).reshape(10,10)
print(örnek8)
print()
örnek9 = örnek8[örnek8 % 5 == 0].reshape(10,2)
print(örnek9)
print()

örnek10 = np.arange(3,30).reshape(3,9)
print(örnek10)
print()
örnek11 = örnek10[örnek10 % 2 == 1].reshape(2,7)
print(örnek11)
print()

örnek12 = np.random.randint(1,5,8)
print(örnek12)
örnek13 = np.random.randint(1,5,8)
print(örnek13)
print(np.dot(örnek12, örnek13))
print()

örnek14 = np.random.randint(1,5, size=(3,3))
print(örnek14)
print()
örnek15 = np.random.randint(1,5, size=(3,3))
print(örnek15)
print()
print(np.dot(örnek14, örnek15))
print()

örnek16 = np.array([[2,4],
                   [3,5]])
print(örnek16)
print()
örnek17 = np.array([[5,10],
                   [15,20]])
print(örnek17)
print()
print(np.dot(örnek16, örnek17))
print()

A = np.array([[1,1], [50,75]])
print(A)

B = np.array([150, 8750])
print(B)

sonuc = np.linalg.solve(A,B)
print(sonuc)




























