import numpy as np 
import math
import time

dizi1 = np.array([1,2,3,4,5,6,7])

print(dizi1)
print(type(dizi1))
print(dizi1.dtype)
print(dizi1.ndim)

dizi2 = np.array([10,11,12,13,14,15], dtype=str)

print(dizi2)

dizi3 = np.array([16,17,18,19,20,21], dtype=float)

print(dizi3)

dizi4 = np.array([[22,23,24,25,26,27,28]])

print(dizi4)
print(dizi4.ndim)

dizi5 = np.array([[30,31,32,33],[34,35,36,37]])

print(dizi5)
print(dizi5.ndim)

dizi6 = np.array([[[40,41,42,43],[50,51,52,53], [60,61,62,63], [70,71,72,73]]])

print(dizi6)
print(dizi6.ndim)

dizi7 = np.array([[85,86], [87,88], [89,90], [91,92]])

print(dizi7)
print(dizi7.shape)

dizi8 = np.array([100,101,102,103,104,105])

print(dizi8)
print(dizi8.shape)


dizi9 = np.array([112,113,114,115,116,117,118,119,120,121,122,123])
dizi10 = dizi9.reshape(4,3)

print(dizi10)
print(dizi10.ndim)

dizi11 = np.array([130,131,132,133,134])
dizi12 = dizi11.reshape(5,1)

print(dizi12)
print(dizi12.ndim)

dizi13 = np.array([140,141,142,143,144,145,146])
dizi14 = dizi13.reshape(1,7,1,1,1)

print(dizi14)
print(dizi14.ndim)

dizi15 = np.arange(0,15,3)

print(dizi15)
print(dizi15.ndim)
print(dizi15.dtype)

dizi16= np.arange(10)
print(dizi16)

dizi17 = dizi16.copy()
print(dizi17)

dizi18 = np.random.random((4,3,5))
print(dizi18)
print(dizi18.ndim)

dizi19 = np.random.random((3,6))
print(dizi19)
print(dizi19.ndim)

dizi20 = np.random.random((8))
print(dizi20)
print(dizi20.ndim)

dizi21 = np.random.randint(10, size=8)
print(dizi21)

dizi22 = np.arange(1,11)
dizi23 = dizi22.reshape(5,2)

print(dizi23)

dizi24 = np.arange(1,21)
dizi25 = dizi24.reshape(5,4)

print(dizi25)

birinci_satir = dizi25[0] 
print(birinci_satir)

ikinci_satir = dizi25[1] 
print(ikinci_satir)

ücüncü_satir = dizi25[2] 
print(ücüncü_satir)

ilk_üc_satir = dizi25[:3]
print(ilk_üc_satir)

birinci_sutun = dizi25[:,0]
print(birinci_sutun)

ikinci_sutun = dizi25[2:5,1]
print(ikinci_sutun)

ücüncü_sutun = dizi25[1:3,2]
print(ücüncü_sutun)

dizi26 = np.arange(20,50)
dizi27 = dizi26.reshape(6,5)
print(dizi27)

eleman = dizi27[5,3]
print(eleman)

ters = dizi27[::-1]
print(ters)

dizi28 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(dizi28)

liste = dizi28[::2]
print(liste)

liste2 = dizi28[::3]
print(liste2)

liste3 = dizi28[4:17]
print(liste3)

liste4 = dizi28[::-1]
print(liste4)

liste5 = dizi28[::-5]
print(liste5)

liste6 = dizi28[::-4]
print(liste6)

dizi29 = np.zeros((6,3), dtype='int')
print(dizi29)
print(dizi29.ndim)

dizi30 = np.zeros((4,3,2), dtype='int')
print(dizi30)
print(dizi30.ndim)

dizi31 = np.ones((8,4), dtype='int')
print(dizi31)
print(dizi31.ndim)

dizi32 = np.ones((3,5,4), dtype='int')
print(dizi32)
print(dizi32.ndim)

dizi33 = np.eye(9)
print(dizi33)
print(dizi33.ndim)

dizi34 = np.array([[1,2,3], [4,5,6]])
print(dizi34)
print(dizi34.ndim)

dizi35 = np.array([[7,8,9], [10,11,12]])
print(dizi35)
print(dizi35.ndim)

dizi36 = np.array([[13,14,15], [16,17,18]])
print(dizi36)
print(dizi36.ndim)

birlesme = np.concatenate([dizi34, dizi35, dizi36], axis=0)
print(birlesme)
print(birlesme.ndim)

birlesme2 = np.concatenate([dizi34, dizi35, dizi36], axis=1)
print(birlesme2)
print(birlesme2.ndim)

a = dizi36.max()
print(a)

b = dizi35.min()
print(b)

c = dizi34.sum()
print(c)

satirlarin_toplami = dizi36.sum(axis=1)
print(satirlarin_toplami)

sutunlarin_toplami = dizi35.sum(axis=0)
print(sutunlarin_toplami)

ortalama = dizi34.mean()
print(ortalama)

ortalama2 = dizi35.mean(axis=1, dtype=int)
print(ortalama2)

dizi37 = np.array([[1,2,3], [4,5,9]])

varyans = dizi37.var()
print(varyans)

dizi38 = np.array([[1,2,3], [4,5,9], [10,11,18]])

varyans = dizi38.var()
print(varyans)

dizi39 = np.array([[10,20,30], [40,50,60], [70,80,90], [100,110,120]])

varyans = dizi39.var()
print(varyans)

dizi40 = np.array([[4,9,14], [18,24,30], [1,2,3], [4,5,6]])

varyans = dizi40.var(dtype=int)
print(varyans)

dizi41 = np.array([1,2,3,4,5,6,7,12])

varyans = dizi41.var()
print(varyans)

dizi42 = np.array([8,12,15,20,25])

varyans = dizi42.var()
print(varyans)

dizi43 = np.array([3,6,9,12,15])

standart_sapma = dizi43.std()
print(standart_sapma)

dizi44 = np.array([[5,10,15], [20,30,40]])

standart_sapma = dizi44.std()
print(standart_sapma)

dizi45 = np.array([[2,4,6], [8,10,12], [18,30,45]])

standart_sapma = dizi45.std()
print(standart_sapma)

dizi46 = np.array([[[4,8,12], [16,20,24], [28,32,36], [40,60,80]]])

standart_sapma = dizi46.std()
print(standart_sapma)
print(dizi46.ndim)
print(dizi46.size)
print(dizi46.shape)

dizi47 = np.array([[6,12,18,24], [10,20,30,40]])

varyans = dizi47.var()
print(varyans)
standart_sapma = dizi47.std()
print(standart_sapma)
print(dizi47.ndim)
print(dizi47.size)
print(dizi47.shape)
print(dizi47)

dizi48 = np.array([[1,2,3], [4,5,6]])
dizi49 = np.array([[17,28,39], [10,41,52]])

islem = dizi48 - dizi49

print(islem)

dizi48 = np.array([[1,2,3], [4,5,6]])
dizi49 = np.array([[17,28,39], [10,41,52]])

islem = dizi48 + dizi49

print(islem)

dizi48 = np.array([[1,2,3], [4,5,6]])
dizi49 = np.array([[17,28,39], [10,41,52]])

islem = dizi48 * dizi49

print(islem)

dizi48 = np.array([[1,2,3], [4,5,6]])
dizi49 = np.array([[17,28,39], [10,41,52]])

islem = dizi49 / dizi48

print(islem)

dizi48 = np.array([[1,2,3], [4,5,6]])
dizi49 = np.array([[17,28,39], [10,41,52]])

islem = dizi49  % dizi48

print(islem)

dizi50 = np.array([[30,50,70], [10,12,14]])
islem = dizi50 * 3
print(islem)

dizi50 = np.array([[30,50,70], [10,12,14]])
islem = dizi50 / 2
print(islem)

dizi50 = np.array([[30,50,70], [10,12,14]])
islem = dizi50 - 10
print(islem)

dizi50 = np.array([[30,50,70], [10,12,14]])
islem = dizi50 + 20
print(islem)

dizi50 = np.array([[30,50,70], [10,12,14]])
islem = dizi50 % 4
print(islem)

dizi51 = np.array([[4,16,25], [36,49,64]])
islem = np.sqrt(dizi51)
print(islem)

dizi51 = np.array([[3,4,5], [6,7,8]])
islem = np.exp(dizi51)
print(islem)

sayı = math.pow(2.71828182845904523536,8)
print(sayı)

dizi52 = np.array([[1,2,3], [4,5,6]])
dizi53 = np.array([[10,20], [30,40], [50,60]])

islem2 = np.dot(dizi52, dizi53)
print(islem2)

# 1*10 + 2*30 + 3*50 = 220
# 1*20 + 2*40 + 3*60 = 280
# 4*10 + 5*30 + 6*50 = 490
# 4*20 + 5*40 + 6*60 = 640

dizi54 = np.array([[7,8], [9,10]])
dizi55 = np.array([[50,100], [150,200]])

islem3 = np.dot(dizi54, dizi55)
print(islem3)

# 7*50 + 8*150 = 1550
# 7*100 + 8*200 = 2300
# 9*50 + 10*150 = 1950
# 9*100 + 10*200 = 2900

dizi56 = np.array([[5,10,15,20], [25,30,35,40]])
dizi57 = np.array([[1000,2000], [3000,4000], [5000,6000], [7000,8000]])

islem3 = np.dot(dizi56, dizi57)
print(islem3)

# 5*1000 + 10*3000 + 15*5000 + 20*7000 = 250000
# 5*2000 + 10*4000 + 15*6000 + 20*8000 = 300000
# 25*1000 + 30*3000 + 35*5000 + 40*7000 = 570000
# 25*2000 + 30*4000 + 35*6000 + 40*8000 = 700000

dizi58 = np.array([[2,4,6,8]])
dizi59 = np.array([[100,200], [300,400], [500,600], [700,800]])

islem4 = np.dot(dizi58, dizi59)
print(islem4)

# 2*100 + 4*300 + 6*500 + 8*700 = 10000
# 2*200 + 4*400 + 6*600 + 8*800 = 12000

dizi60 = np.array([[20,30,40]])
dizi61 = np.array([[1,2], [3,4], [5,6]])

islem5 = np.dot(dizi60, dizi61)
print(islem5)

# 20*1 + 30*3 + 40*5 = 310
# 20*2 + 30*4 + 40*6 = 400


dizi62 = np.array([[10,12,14,16], [18,20,22,24]])
print(dizi62)
ters_cevir = dizi62.T
print(ters_cevir)
print('-------------------------')

dizi63 = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(dizi63)
ters_cevir = dizi63.T
print(ters_cevir)
print('-------------------------')

dizi64 = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],[16,17,18,19,20]])
print(dizi64)
ters_cevir = dizi64.T
print(ters_cevir)

dizi65 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]])

dogruluk = dizi65 >= 10
print(dogruluk)

dogruluk2 = dizi65[dizi65 < 8]
print(dogruluk2)

dizi66 = np.array([[3,5,7,9], [2,4,6,8], [5,10,15,20]])
np.save('kaydedilenDosya', dizi66)

dosyaYükle = np.load('kaydedilenDosya.npy')
print(dosyaYükle)

dosyaAc = np.genfromtxt('tarihler.csv', delimiter=',', 
                        names='', skip_header=3, 
                        usecols=(3), dtype=int, unpack=True, max_rows=10)
print(dosyaAc)

g = np.genfromtxt('yaslar.txt', delimiter=',', skip_header=2,
                  max_rows=7, usecols=(0, -1), dtype=int, 
                  unpack=True)
print(g)

g1 = np.fromfile('tarihler.csv', count=3, sep=',')
print(g1)

g2 = np.arange(1,1001,10)
print(g2)
np.savetxt('sayılar.txt', g2, delimiter=',', fmt='%d')

g3 = np.arange(0,100,2)
print(g3)
g3.tofile('sayılar2.txt', sep=',', format='%d')





















































