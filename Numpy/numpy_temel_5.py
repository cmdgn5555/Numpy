import numpy as np 

liste1 = [1,2,3,4,5,6]
print(liste1)

arr1 = np.array([1,2,3,4,5,6])
print(arr1)
print(type(arr1))
print(arr1.dtype)

arr2 = np.array([1,2,3,4,5,6], dtype=float)
print(arr2)
print(type(arr2))
print(arr2.dtype)

arr3 = np.array([1,2,3,4,5,6], dtype=complex)
print(arr3)
print(type(arr3))
print(arr3.dtype)

arr4 = np.array([[1,2,3], 
                 [4,5,6], 
                 [7,8,9]])

print(arr4.ndim)

arr5 = np.array([[[1,2,3], 
                 [4,5,6], 
                 [7,8,9]]])

print(arr5.ndim)

arr6 = np.array([[1,2], 
                 [3,4], 
                 [5,6],
                 [7,8]])

print(arr6.shape)

arr7 = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
print(arr7.shape)
print(arr7)
print(arr7.size)
print('\n')

arr8 = np.array([1,2,3], dtype=np.int8)
arr9 = np.array([1,2,3], dtype=np.int16)
arr10 = np.array([1,2,3], dtype=np.int32)
arr11 = np.array([1,2,3], dtype=np.int64)

print(arr8.itemsize)
print(arr9.itemsize)
print(arr10.itemsize)
print(arr11.itemsize)
print('---------------------------------------------------------')

arr12 = np.array([1,2,3], dtype=np.float16)
arr13 = np.array([1,2,3], dtype=np.float32)
arr14 = np.array([1,2,3], dtype=np.float64)

print(arr12.itemsize)
print(arr13.itemsize)
print(arr14.itemsize)
print('---------------------------------------------------------')

arr15 = np.array([1,2,3], dtype=np.complex_)
arr16 = np.array([1,2,3], dtype=np.complex64)
arr17 = np.array([1,2,3], dtype=np.complex128)

print(arr15.itemsize)
print(arr16.itemsize)
print(arr17.itemsize)
print('---------------------------------------------------------')

arr18 = np.arange(0,20,4)
print(arr18)

arr19 = arr18.copy()
print(arr19)

arr20 = np.random.random((4,4,4))
print(arr20)
print(arr20.ndim)

arr21 = np.random.randint(7,12, size=10)
print(arr21)
print('******************************************************')

arr22 = np.arange(1,11).reshape(5,2)
print(arr22)

birinci_satir = arr22[0]
ikinci_satir = arr22[1]
ilk_iki_satir = arr22[0:2]
birinci_sütun = arr22[:,0]
ikinci_sütun = arr22[:,1]
ilk_iki_sütun = arr22[:,0:2]
eleman = arr22[4,1]
print(birinci_satir)
print(ikinci_satir)
print(ilk_iki_satir)
print(birinci_sütun)
print(ikinci_sütun)
print(ilk_iki_sütun)
print(eleman)
print('\n')

arr23 = [10,20,30,40,50,60,70]
print(arr23)

tersi1 = arr23[::-1]
print(tersi1)

tersi2 = arr23[::-2]
print(tersi2)

tersi3 = arr23[::-3]
print(tersi3)

tersi4 = arr23[::-4]
print(tersi4)

tersi5 = arr23[::-5]
print(tersi5)

tersi6 = arr23[::-6]
print(tersi6)
print('\n')

arr24 = np.zeros((6,3,2))
print(arr24)

arr25 = np.ones((4,5,3))
print(arr25)

arr26 = np.eye(8, k=1)
print(arr26)

dizi1 = np.array([[1,2,3],
                  [4,5,6]])
print(dizi1)

dizi2 = np.array([[7,8,9],
                  [10,11,12]])
print(dizi2)

birlesme = np.concatenate([dizi1, dizi2], axis=1)
print(birlesme)

birlesme2 = np.concatenate([dizi1, dizi2], axis=0)
print(birlesme2)

dizi3 = np.array([[30,15,40],
                  [55,5,20]])

dizi4 = np.array([[75,50,35],
                  [90,10,60]])

a = dizi3.min()
print(a)

b = dizi4.min()
print(b)

c = dizi3.max()
print(c)

d = dizi4.max()
print(d)

dizi5 = np.array([[2,6,9],
                  [13,15,23]])

dizi6 = np.array([[3,4,7],
                  [11,20,26]])

topla = dizi5.sum(axis=1)
print(topla)

topla2 = dizi5.sum(axis=0)
print(topla2)

topla3 = dizi6.sum(axis=1)
print(topla3)

topla4 = dizi6.sum(axis=0)
print(topla4)

topla5 = dizi5.sum()
print(topla5)

topla6 = dizi6.sum()
print(topla6)

ortalama1 = dizi5.mean()
ortalama2 = dizi6.mean()
print(ortalama1)
print(ortalama2)

ortalama3 = dizi5.mean(axis=0)
ortalama4 = dizi5.mean(axis=1)
print(ortalama3)
print(ortalama4)

ortalama5 = dizi6.mean(axis=0)
ortalama6 = dizi6.mean(axis=1)
print(ortalama5)
print(ortalama6)

dizi7 = np.array([[5,10,15,50], 
                  [20,30,40,70]])
varyans = dizi7.var()
print(varyans)
standart_sapma = dizi7.std()
print(standart_sapma)
varyans2 = dizi7.var(axis=1)
print(varyans2)
varyans3 = dizi7.var(axis=0)
print(varyans3)

dizi8 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

varyans4 = dizi8.var(axis=0)
print(varyans4)
varyans5 = dizi8.var(axis=1)
print(varyans5)

dizi9 = np.array([[2,4,6],
                  [3,5,7],
                  [7,12,14]])

standart_sapma2 = dizi9.std(axis=0)
print(standart_sapma2)

standart_sapma3 = dizi9.std(axis=1)
print(standart_sapma3)

dizi10 = np.array([5,6,7])
e = np.exp(dizi10)
print(e)

dizi11 = np.array([[12,14,16],
                   [18,20,22]])
dizi12 = np.array([[1,2,3],
                   [4,5,6]])

islem = dizi11 + dizi12
print(islem)
islem2 = dizi11 - dizi12
print(islem2)
islem3 = dizi11 * dizi12
print(islem3)
islem4 = dizi11 / dizi12
print(islem4)
islem5 = dizi11 // dizi12
print(islem5)
islem6 = dizi11 % dizi12
print(islem6)

dizi13 = np.array([[3,5,7],
                   [2,4,6]])

islem7 = dizi13 + 10
print(islem7)
islem8 = dizi13 - 20
print(islem8)
islem9 = dizi13 * 15
print(islem9)
islem10 = dizi13 / 2
print(islem10)

dizi14 = np.array([2,3,4,5])
print(np.exp2(dizi14))
dizi15 = np.array([2,3,4,5])
print(np.exp(dizi15))

dizi16 = np.array([[4,9,16],
                   [25,36,49],
                   [64,81,100]])
print(np.sqrt(dizi16))

dizi17 = np.array([[4,9,16],
                   [25,36,49],
                   [64,81,100]])
print(np.log(dizi17))

dizi18 = np.array([[1,2,3],
                    [4,5,6]])

dizi19 = np.array([[7,8],
                   [9,10],
                   [11,12]])

print(np.dot(dizi18, dizi19))

dizi20 = np.array([[1,2,3,4],
                   [1,2,3,4],
                   [1,2,3,4]])

dizi21 = np.array([[5,5,5],
                   [10,10,10],
                   [20,20,20],
                   [30,30,30]])

print(np.dot(dizi20, dizi21))


dizi22 = np.array([[1,2,3,10,20],
                   [4,5,6,30,40]])

dizi23 = np.array([[100,200],
                   [300,400],
                   [500,600],
                   [700,800],
                   [900,1000]])

print(np.dot(dizi22, dizi23))

dizi24 = np.array([[1,2,3,4,5,6,7,8],
                   [9,10,11,12,13,14,15,16],
                   [17,18,19,20,21,22,23,24],
                   [25,26,27,28,29,30,31,32]])

print(dizi24.T)

dizi25 = np.array([[5,7,9],
                   [12,16,18],
                   [25,30,35]])

print(dizi25)

dogruluk = dizi25 > 15
print(dogruluk)

dogruluk2 = dizi25[dizi25 > 10]
print(dogruluk2)

dogruluk3 = dizi25 <= 12
print(dogruluk3)

dogruluk4 = dizi25[dizi25 < 20]
print(dogruluk4)

dogruluk5 = dizi25 == 18
print(dogruluk5)

dogruluk6 = dizi25[dizi25 == 25]
print(dogruluk6)

dogruluk7 = dizi25 != 9
print(dogruluk7)

dogruluk8 = dizi25[dizi25 != 16]
print(dogruluk8)

dogruluk9 = dizi25[dizi25 %2 == 0]
print(dogruluk9)

dogruluk10 = dizi25[dizi25 %2 == 1]
print(dogruluk10)

dogruluk11 = dizi25[dizi25 %3 == 0]
print(dogruluk11)

dogruluk12 = dizi25[dizi25 %5 == 0]
print(dogruluk12)

