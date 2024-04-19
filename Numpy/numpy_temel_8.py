import numpy as np 

arr1 = np.array([1,2,3,4,5])
print(arr1)
print()
print('sürüm : ',np.__version__)
print()

arr2 = np.array([1,2,3,4,5])
print(arr2)
print(type(arr2))
print()

arr3 = np.array((5,10,15,20))
print(arr3)
print()

arr4 = np.array(43)
print(arr4)
print()

a = np.array(95)
b = np.array([1,3,5,7,9])
c = np.array([[2,4,6,8], [5,10,15,20]])
d = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]])
print(a)
print(a.ndim)
print(b)
print(b.ndim)
print(c)
print(c.ndim)
print(d)
print(d.ndim)
print()

arr5 = np.array([[[[[1,2,3,4]]]]])
print(arr5)
print('boyut sayısı : ', arr5.ndim)
print()

arr6 = np.array([2,5,7,8])
print(arr6[0])
print(arr6[-1])
print()

arr7 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr7)
print(arr7[0,3])
print(arr7[0,-1])
print(arr7[1,2])
print(arr7[1,-4])
print()

arr8 = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]])
print(arr8)
print(arr8[0,1,2])
print(arr8[0,3,1])
print(arr8[0,2,2])
print()

arr9 = np.arange(10,70).reshape(3,5,4)
print(arr9)
print(arr9[0,2,3])
print(arr9[1,3,0])
print(arr9[2,4,1])
print(arr9[2,3,-1])
print()
print('\n\n')

arr10 = np.arange(10,90).reshape(4,5,4)
print(arr10)
print(arr10[0,3,-3])
print(arr10[1,1,-2])
print(arr10[2,3,-1])
print(arr10[3,1,-4])
print()

arr11 = np.array([5,10,15,20,25,30,35,40,45,50])
print(arr11)
print(arr11[2:6])
print(arr11[3:])
print(arr11[:7])
print(arr11[-8:-3])
print(arr11[2:-4])
print('\n\n')

arr12 = np.array([3,6,9,12,15,18,21,24,27,30,33,36,39,42,45])
print(arr12)
print(arr12[3:12:2])
print(arr12[1:13:3])
print(arr12[0:10:1])
print(arr12[::3])
print(arr12[::4])
print(arr12[::-2])
print(arr12[::-5])
print(arr12[::-1])
print(arr12[-1:-11:-3])
print('\n\n')

arr13 = np.array([1,2,3,4])
print(arr13)
print(arr13.dtype)
print()

arr14 = np.array(['elma', 'armut',  'muz'])
print(arr14)
print(arr14.dtype)
print()

arr15 = np.array([1,2,3,4], dtype='str')
print(arr15)
print(arr15.dtype)
print()

arr16 = np.array([1,2,3,4], dtype='complex')
print(arr16)
print(arr16.dtype)
print()

arr17 = np.array([1,3,5,7,8,0,9], dtype='i8')
print(arr17)
print(arr17.dtype)
print()

arr18 = np.array([1.4, 8.2, 5.3, 6.7])
print(arr18)
print(arr18.dtype)
arr19 = arr18.astype('int')
print(arr19)
print(arr19.dtype)
print('\n')

arr20 = np.array([4,5,7,9])
print(arr20)
print(arr20.dtype)
arr21 = arr20.astype('float')
print(arr21)
print(arr21.dtype)
print('\n')

arr22 = np.array([1.4, 8.2, 5.3, 6.7])
print(arr22)
print(arr22.dtype)
arr23 = arr22.astype('complex')
print(arr23)
print(arr23.dtype)
print('\n')

arr24 = np.array([5,2,7,1])
print(arr24)
print(arr24.dtype)
arr25 = arr24.astype('complex')
print(arr25)
print(arr25.dtype)
print('\n')
print(arr25.real)
print(arr25.imag)
print('\n')

arr26 = np.array([1,0,3,7,0,0])
print(arr26)
print(arr26.dtype)
arr27 = arr26.astype(bool)
print(arr27)
print(arr27.dtype)
print('\n')

arr28 = np.array([True,False,False,True,True,True,False,False])
print(arr28)
print(arr28.dtype)
arr29 = arr28.astype(int)
print(arr29)
print(arr29.dtype)
print('\n')

arr30 = np.array([True,False,False,True,True,True,False,False])
print(arr30)
print(arr30.dtype)
arr31 = arr30.astype(float)
print(arr31)
print(arr31.dtype)
print('\n')

arr32 = np.array([True,False,False,True,True,True,False,False])
print(arr32)
print(arr32.dtype)
arr33 = arr32.astype(complex)
print(arr33)
print(arr33.dtype)
print('\n\n')

dizi1 = np.array([1,2,3,4,5])
print(dizi1)
print()
dizi2 = dizi1.copy()
print(dizi2)
print()
dizi1[0] = 333
print(dizi1)
print()
print(dizi2)
print()
dizi2[-1] = 555
print(dizi2)
print()
print(dizi1)
print('\n\n')
print('++++++++++++++++++++++++++++++++++')

dizi3 = np.array([1,2,3,4,5])
print(dizi3)
print()
dizi4 = dizi3.view()
print(dizi4)
print()
dizi3[0] = 66
print(dizi3)
print()
print(dizi4)
print()
dizi4[-1] = 88
print(dizi4)
print()
print(dizi3)
print('\n\n')

dizi5 = np.array([1,2,3,4,5])

x = dizi5.copy()
y = dizi5.view()

print(x.base)
print(y.base)
print('\n\n')

dizi6 = np.array([[1,2,3,4], [5,6,7,8]])
print(dizi6)
print(dizi6.shape)
print()

dizi7 = np.array([[[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]]])
print(dizi7)
print(dizi7.shape)
print(dizi7.ndim)
print(dizi7.nbytes)
print('\n')

dizi8 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
yenidizi = dizi8.reshape(4,3)
print(yenidizi)
print()

dizi9 = np.arange(36).reshape(2,6,3)
print(dizi9)
print('\n')

dizi10 = np.array([10,20,30,40])
tekrarla = np.repeat(dizi10, 2)
print(tekrarla)
print()

dizi11 = np.array([1,2,3,4])
print(dizi11.repeat(3))
print()

dizi12 = np.array([5,8,10,13])
print(dizi12.repeat(dizi12))
print('\n')

dizi13 = np.array([5,10,15,20,25,30,35,40,45,50,
                   55,60,65,70,75,80,85,90,95,100]).reshape(5,4)
print(dizi13)
print()

dizi14 = np.array([5,10,15,20,25,30,35,40,45,50,
                   55,60,65,70,75,80,85,90,95,100]).reshape(2,5,2)
print(dizi14)
print('\n\n')

dizi15 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4)
print(dizi15)
print()
x1 = dizi15.copy()
y1 = dizi15.view()
print(x1)
print()
print(y1)
print()
print(x1.base)
print()
print(y1.base)
print('\n\n')

dizi16 = np.arange(48).reshape(-1,4,3)
print(dizi16)
print('\n\n')

dizi17 = np.arange(60).reshape(5,-1,4)
print(dizi17)
print('\n\n')

dizi17 = np.arange(80).reshape(8,2,-1)
print(dizi17)
print('\n\n')

dizi18 = np.arange(30).reshape(-1,6)
print(dizi18)
print('\n\n')

dizi19 = np.arange(48).reshape(12,-1)
print(dizi19)
print('\n\n')

dizi20 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(dizi20)
dizi21 = dizi20.reshape(-1)
print(dizi21)
print('\n\n')

dizi22 = np.arange(18).reshape(2,3,3)
print(dizi22)
print()
dizi23 = dizi22.reshape(-1)
print(dizi23)
print('\n\n')

dizi24 = np.arange(200).reshape(5,2,4,5)
print(dizi24)
print()
dizi25 = dizi24.reshape(-1)
print(dizi25)
print()

dizi26 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(dizi26)
print()
print(np.rot90(dizi26, 1))
print()
print(np.rot90(dizi26, 2))
print()
print(np.rot90(dizi26, 3))
print()
print(np.rot90(dizi26, 4))
print()
print('\n\n')
print('+++++++++++++++++++')

dizi27 = np.array([[5,10,15], [20,25,30], [35,40,45], [50,55,60]])
print(dizi27)
print()
print(np.rot90(dizi27, -1))
print()
print(np.rot90(dizi27, -2))
print()
print(np.rot90(dizi27, -3))
print()
print(np.rot90(dizi27, -4))
print('\n\n')
print('++++++++++++++++++++++++')

dizi28 = np.arange(24).reshape(2,4,3)
print(dizi28)
print('--')
print(np.flip(dizi28, axis=0))
print('------')
print(np.flip(dizi28, axis=1))
print('--------------')
print(np.flip(dizi28))
print('\n\n\n')

dizi29 = np.array([-3,-5,-7,9,1,2])
print(np.absolute(dizi29))
print()

dizi30 = np.array([-3,-5,-7,9,1,-2])
print(np.abs(dizi30))
print('\n\n')

dizi31 = np.diag([1,2,3,4,5])
print(dizi31)
print()
print(np.fliplr(dizi31))
print('\n\n')

dizi32 = np.eye(6)
print(dizi32)
print()
print(np.fliplr(dizi32))
print('\n\n')

dizi33 = np.identity(4)
print(dizi33)
print()
print(np.fliplr(dizi33))
print('\n\n')

dizi34 = np.identity(7)
print(dizi34)
print()
print(np.flipud(dizi34))
print('\n\n')

dizi35 = np.diag([5,10,15,20])
print(dizi35)
print()
print(np.flipud(dizi35))
print('\n\n')

dizi36 = np.array([[1,3,5], [2,4,6], [5,15,25], [10,20,30]])
print(dizi36)
print()
print(np.flipud(dizi36))
print('\n\n')

dizi37 = np.array([[1,3,5], [2,4,6], [5,15,25], [10,20,30]])
print(dizi37)
print()
print(np.fliplr(dizi37))
print('\n\n')

dizi38 = np.array([[5,10,15],
                    [20,25,30],
                    [35,40,45],
                    [50,55,60]])
print(dizi38)
print()
print(np.fliplr(dizi38))
print('\n\n')

dizi39 = np.array([[2,4,6,8,10,12,14],
                    [16,18,20,22,24,26,28],
                    [30,32,34,36,38,40,42],
                    [44,46,48,50,52,54,56]])
print(dizi39)
print()
print(np.fliplr(dizi39))
print('\n\n')

dizi40 = np.array([[1,3,5,7,9],
                   [11,13,15,17,19],
                   [21,23,25,27,29],
                   [31,33,35,37,39],
                   [41,43,45,47,49]])
print(dizi40)
print()
print(np.flipud(dizi40))
print('\n\n')
print('-----------------------------------------')

dizi41 = np.arange(40).reshape(2,5,4)
print(dizi41)
print('+++++++++++++')
print(np.flip(dizi41, axis=0))
print('\n\n')

dizi42 = np.arange(60).reshape(3,4,5)
print(dizi42)
print('+++++++++++++')
print(np.flip(dizi42, axis=0))
print('\n\n') 

dizi43 = np.arange(120).reshape(4,6,5)
print(dizi43)
print('+++++++++++++')
print(np.flip(dizi43, axis=0))
print('\n\n')
print('\n\n\n\n\n\n')
print('-----------------------------------------------------------------')

dizi44 = np.arange(30).reshape(2,5,3)
print(dizi44)
print('+++++++++++++')
print(np.flip(dizi44, axis=1))
print('\n\n')

dizi45 = np.arange(20).reshape(4,5)
print(dizi45)
print('+++++++++++++')
print(np.flip(dizi45, axis=1))
print('\n\n') 

dizi46 = np.arange(15).reshape(5,3)
print(dizi46)
print('+++++++++++++')
print(np.flip(dizi46))
print('\n\n') 

dizi47 = np.arange(40).reshape(2,4,5)
print(dizi47)
print('+++++++++++++')
print(np.flip(dizi47))
print('\n\n') 

dizi48 = np.arange(120).reshape(3,2,4,5)
print(dizi48)
print('+++++++++++++')
print(np.flip(dizi48))
print('\n\n')

dizi49 = np.array([1,2,3,4,5])
for a in dizi49:
    print(a)
print('\n\n')

dizi50 = np.array([[5,10,15,20], [25,30,35,40]])
for a in dizi50:
    print(a)
    for h in a:
        print(h)
print('\n\n')

dizi51 = np.arange(10).reshape(2,5)
print(dizi51)
print()
for a in dizi51:
    print(a)
    print()
    for b in a:
        print(b**2)
print('\n\n')

dizi52 = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]])
print(dizi52)
print()
for a in dizi52:
    print(a)
    print()
    for b in a:
        print(b)
        print()
        for c in b:
            print(c)
            print()
print('\n\n\n')
print('+++++++++++++++++++++++++++++++++++++++++++')

dizi53 = np.array([[[1,2], [3,4], [5,6], [7,8]]])
print(dizi53)
for a in np.nditer(dizi53):
    print(a)
print('\n\n')

dizi54 = np.array([1,2,3,4,5,6,7])
print(dizi54)
for a in np.nditer(dizi54):
    print(a)
print('\n\n')

dizi54 = np.array([[[[5,10,15], [20,25,30], [35,40,45], [50,55,60]]]])
print(dizi54)
for a in np.nditer(dizi54):
    print(a)
print('\n\n')

dizi55 = np.arange(30).reshape(5,6)
print(dizi55)
for a in np.nditer(dizi55):
    print(a)
print('\n\n')

dizi56 = np.array([1,2,3])
print(dizi56)
print()
for a in np.nditer(dizi56, flags=['buffered'], op_dtypes=['float']):
    print(a)

dizi57 = np.array([2.4, 8.5, 16.7])
print(dizi57)
print()
for a in np.nditer(dizi57, flags=['buffered'], op_dtypes=['S']):
    print(a)
print('\n\n')

dizi58 = np.array([23, 34, 40])
print(dizi58)
print()
for a in np.nditer(dizi58, flags=['buffered'], op_dtypes=['S']):
    print(a)
print('\n\n')

dizi59 = np.array([1,6,8,9])
print(dizi59)
print()
for a in np.nditer(dizi59, flags=['buffered'], op_dtypes=['complex']):
    print(a)
print('\n\n')

dizi60 = np.array([23.4, 35.1, 40.8, 47.9])
print(dizi60)
print()
for a in np.nditer(dizi60, flags=['buffered'], op_dtypes=['complex']):
    print(a)
print('\n\n\n')
print('************************************************')

dizi61 = np.array([[1,2,3,4,5], [10,20,30,40,50], [15,25,35,45,55]])
print(dizi61)
print()
for a in np.nditer(dizi61[:,1:4]):
    print(a)
print('\n\n')

dizi62 = np.arange(40).reshape(8,5)
print(dizi62)
print()
for a in np.nditer(dizi62[0:3,1:4]):
    print(a)
print('\n\n')

dizi63 = np.arange(30).reshape(5,6)
print(dizi63)
print()
for a in np.nditer(dizi63[2:4,3:5]):
    print(a)
print('\n\n')

dizi64 = np.arange(20).reshape(4,5)
print(dizi64)
print()
for a in np.nditer(dizi64[:,-3:-1]):
    print(a)
print('\n\n')

dizi65 = np.arange(100).reshape(10,10)
print(dizi65)
print()
for a in np.nditer(dizi65[-7:-2, -8:-4]):
    print(a)
print('\n\n')

dizi66 = np.array([1,2,3,4,5])
print(dizi66)
print()
for a, b in np.ndenumerate(dizi66):
    print(a, b)
print()

dizi67 = np.array(['ali', 'veli', 'seyfi'])
print(dizi67)
print()
for a, b in np.ndenumerate(dizi67):
    print(a, b)
print()

dizi68 = np.array([[5,10,15], [20,25,30], [35,40,45], [50,55,60]])
print(dizi68)
print()
for a, b in np.ndenumerate(dizi68):
    print(a, b)
print()

dizi69 = np.array([[[10,20,30],[40,50,60],[70,80,90]]])
print(dizi69)
print()
for a, b in np.ndenumerate(dizi69):
    print(a, b)
print('\n\n')

dizi70 = np.array([[5,10,15], [20,25,30], [35,40,45], [50,55,60]])
print(dizi70)
print()
for a, b in np.ndenumerate(dizi68):
    print(a, b)
print('\n\n')

dizi71 = np.array([['ali','veli','seyfi','canberk','orhan'], 
                   ['salih', 'zeynel', 'ümit','kenan','sabri'], 
                   ['ahmet','mehmet','taner','ömer','soner']])
print(dizi71)
print()
for a, b in np.ndenumerate(dizi71):
    print(a, b)
print('\n\n')

dizi72 = np.array([[['erkan','ertan','serkan','sertan'],
                    ['nuri','hasan','emrah','emre'],
                    ['fahri','yasin','taha','beklan']]])
print(dizi72)
print()
for a, b in np.ndenumerate(dizi72):
    print(a, b)
print('\n\n')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')

dizi73 = np.array([1,2,3])
dizi74 = np.array([4,5,6])
print(dizi73)
print(dizi74)
print()
birlestir1 = np.concatenate((dizi73, dizi74), axis=0)
print(birlestir1)
print('\n\n')

dizi75 = np.array([[1,2,3],[4,5,6]])
dizi76 = np.array([[7,8,9],[10,11,12]])
print(dizi75)
print(dizi76)
print()
birlestir2 = np.concatenate((dizi75, dizi76), axis=0)
print(birlestir2)
print()
birlestir3 = np.concatenate((dizi75, dizi76), axis=1)
print(birlestir3)
print('\n\n')

dizi77 = np.array([[['a','b','c'],['d','e','f'],['g','h','j']]])
dizi78 = np.array([[['k','l','m'],['n','o','ö'],['p','r','s']]])
print(dizi77)
print(dizi78)
print()
birlestir4 = np.concatenate((dizi77, dizi78), axis=0)
print(birlestir4)
print()
birlestir5 = np.concatenate((dizi77, dizi78), axis=1)
print(birlestir5)
print('\n\n\n')

dizi79 = np.array([[1,2,3],[4,5,6]])
dizi80 = np.array([[7,8,9],[10,11,12]])
dizi81 = np.array([[13,14,15],[16,17,18]])
print(dizi79)
print(dizi80)
print(dizi81)
print()
birlestir6 = np.concatenate((dizi79, dizi80, dizi81), axis=0)
print(birlestir6)
print()
birlestir7 = np.concatenate((dizi79, dizi80, dizi81), axis=1)
print(birlestir7)
print('\n\n\n\n')
print('****************************************')

dizi82 = np.array([1,2,3])
dizi83 = np.array([4,5,6])
print(dizi82)
print(dizi83)
print()
yıgınla1 = np.stack((dizi82, dizi83), axis=0)
print(yıgınla1)
print()
yıgınla2 = np.stack((dizi82, dizi83), axis=1)
print(yıgınla2)
print('\n\n')

dizi84 = np.array([1,2,3])
dizi85 = np.array([4,5,6])
print(dizi84)
print(dizi85)
print()
print(np.hstack((dizi84, dizi85)))
print()

dizi86 = np.array([[5,7,9,11], [13,15,17,19], [21,23,25,27]])
dizi87 = np.array([[2,4,6,8], [10,12,14,16], [18,20,22,24]])
print(dizi86)
print(dizi87)
print()
print(np.hstack((dizi86, dizi87)))
print('\n\n')

dizi88 = np.array([[5,7,9,11], [13,15,17,19], [21,23,25,27]])
dizi89 = np.array([[2,4,6,8], [10,12,14,16], [18,20,22,24]])
dizi90 = np.array([[30,31,32,33], [34,35,36,37], [38,39,40,41]])
print(dizi88)
print(dizi89)
print(dizi90)
print()
print(np.hstack((dizi88, dizi89, dizi90)))
print('\n\n\n\n')

dizi91 = np.array([1,2,3,4,5])
dizi92 = np.array([6,7,8,9,10])
dizi93 = np.array([11,12,13,14,15])
print(dizi91)
print(dizi92)
print(dizi93)
print()
print(np.vstack((dizi91, dizi92, dizi93)))
print('\n\n')

dizi94 = np.array([[1,2,3,4,5], [50,51,52,53,54]])
dizi95 = np.array([[6,7,8,9,10], [62,63,64,65,66]])
dizi96 = np.array([[11,12,13,14,15], [74,75,76,77,78]])
print(dizi94)
print(dizi95)
print(dizi96)
print()
print(np.vstack((dizi94, dizi95, dizi96)))
print('\n\n')

dizi97 = np.array([['elm','arm','er'], ['muz','nar','ayv']])
dizi98 = np.array([['pat','fas','bro'], ['lim','tur','eng']])
dizi99 = np.array([['bak','kaz','kad'], ['süt','lok','gof']])
print(dizi97)
print()
print(dizi98)
print()
print(dizi99)
print()
print(np.vstack((dizi97, dizi98, dizi99)))
print()
print(np.hstack((dizi97, dizi98, dizi99)))
print('\n\n')

array1 = np.array([1,2,3,4,5,6])
array2 = np.array([10,11,12,13,14,15])
array3 = np.array([22,23,24,25,26,27])
print(array1)
print()
print(array2)
print()
print(array3)
print()
print(np.dstack((array1, array2, array3)))
print('\n\n')

array4 = np.array([[100,101,102,103], [104,105,106,107]])
array5 = np.array([[200,201,202,203], [204,205,206,207]])
array6 = np.array([[300,301,302,303], [304,305,306,307]])
print(array4)
print()
print(array5)
print()
print(array6)
print()
print(np.dstack((array4, array5, array6)))
print('\n\n')

array7 = np.array(['ali','veli','nuri','seyfi','halil'])
array8 = np.array(['can','osman','hakan','tarkan','korcan'])
array9 = np.array(['metin','feyyaz','berkan','erkan','serkan'])
print(array7)
print()
print(array8)
print()
print(array9)
print()
print(np.dstack((array7, array8, array9)))
print('\n\n')

array10 = np.array(['g','a','l','a','t','a','s','a','r','a','y'])
array11 = np.array(['g','e','o','r','g','h','e','h','a','g','i'])
array12 = np.array(['b','e','r','k','a','n','k','u','t','l','u'])
print(array10)
print()
print(array11)
print()
print(array12)
print()
print(np.dstack((array10, array11, array12)))
print('\n\n')

array13 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(array13)
print()
böl1 = np.array_split(array13, 3)
print(böl1)
print()
böl2 = np.array_split(array13, 4)
print(böl2)
print()
böl3 = np.array_split(array13, 2)
print(böl3)
print()
böl4 = np.array_split(array13, 12)
print(böl4)
print()
print('\n\n')

array14 = np.array(['ali','veli','hasan','hakan','ayhan','ahmet','saffet','nuri'])
print(array14)
print()
böl5 = np.array_split(array14, 3)
print(böl5)
print('\n\n')

array15 = np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95])
print(array15)
print()
böl6 = np.array_split(array15, 7)
print(böl6)
print('\n\n')

array16 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
print(array16)
print()
böl7 = np.array_split(array16, 4)
print(böl7)
print('\n\n')

array17 = np.array([10,20,30,40,50,60,70,80,90,100])
print(array17)
print()
böl8 = np.array_split(array17, 6)
print(böl8)
print('\n\n')

array18 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(array18)
print()
böl9 = np.array_split(array18, 3, axis=1)
print(böl9)
print('\n\n')

array19 = np.array([[1,2,3], 
                    [4,5,6], 
                    [7,8,9], 
                    [10,11,12], 
                    [13,14,15], 
                    [16,17,18]])
print(array19)
print()
böl10 = np.hsplit(array19, 3)
print(böl10)
print()
böl11 = np.vsplit(array19, 2)
print(böl11)
print()
print('\n\n')

array20 = np.array([[[1,2,3], 
                    [4,5,6], 
                    [7,8,9], 
                    [10,11,12], 
                    [13,14,15], 
                    [16,17,18]]])
print(array20)
print()
böl11 = np.dsplit(array20, 3)
print(böl11)
print('\n\n\n\n\n')

diziler1 = np.array([1,2,3,4,5,6,7,8,4])
ara1 = np.where(diziler1 == 4)
print(ara1)
print()
ara2 = np.where(diziler1 % 2 == 0)
print(ara2)
print()
ara3 = np.where(diziler1 % 2 == 1)
print(ara3)
print()
ara4 = np.where(diziler1 % 5 == 0)
print(ara4)
print()
ara5 = np.where(diziler1 % 3 == 0)
print(ara5)
print()
ara6 = np.where(diziler1 != 4)
print(ara6)
print('+++++')
print()

diziler2 = np.array([1,2,3,4,5,7,8,9,10])
ara7 = np.searchsorted(diziler2, 6)
print(ara7)
print()

diziler3 = np.array([10,11,14,15,17,20])
ara8 = np.searchsorted(diziler3, 13)
print(ara8)
print()

diziler4 = np.array([22,23,26,27,30,33,34,36,37])
ara9 = np.searchsorted(diziler4, 35)
print(ara9)
print()

diziler5 = np.array([80,81,82,83,84,85,86,87])
ara10 = np.searchsorted(diziler5, 86)
print(ara10)
print()

diziler6 = np.array([1,2,3,4,5,6,7,9,10,11])
ara11 = np.searchsorted(diziler6, 12)
print(ara11)
print()

diziler7 = np.array([5,6,7,8,9,10,11,12])
ara12 = np.searchsorted(diziler7, [4,13])
print(ara12)
print()

diziler8 = np.array([1,3,5,6,1,7,9])
ara13 = np.searchsorted(diziler8, 4)
print(ara13)
print()

diziler9 = np.array([1,3,5,2,1,7,9])
ara14 = np.searchsorted(diziler9, 4)
print(ara14)
print()

diziler10 = np.array([22,11,10,9,3,7,5])
ara15 = np.searchsorted(diziler10, 12, side='right')
print(ara15)
print()

diziler11 = np.array([3,5,7,10,14,17,21,25,28,30])
ara16 = np.searchsorted(diziler11, [6,13,18,29])
print(ara16)
print('\n\n\n\n')

diziler12 = np.array([9,13,15,7,2,10,14,20])
print(np.sort(diziler12))
print()

diziler13 =np.array(['ali','salih','kadir','cemil','murat'])
print(np.sort(diziler13))
print()

diziler14 = np.array([True,False,False,True,True,False,False])
print(np.sort(diziler14))
print()

diziler15 = np.array([[3,1,7,2,8,5], [14,12,10,15,13,19]])
print(np.sort(diziler15))
print('\n\n\n')

filtre1 = np.array([51,52,53,54,55,56,57,58])
filtre2 = [True,False,False,False,True,False,False,True]
filtre3 = filtre1[filtre2]
print(filtre3)
print()

filtre4 = np.array(['can','ali','onur','ibo','hasan','kaan'])
filtre5 = [False,True,False,True,True,False]
filtre6 = filtre4[filtre5]
print(filtre6)
print()

filtre7 = np.array([[2,3],[4,5],[6,7],[8,9],[10,11],[12,13]])
filtre8 = [True,True,False,True,True,False]
filtre9 = filtre7[filtre8]
print(filtre9)
print('------------')

dizimiz1 = np.array([40,41,42,43,44,45,46,47,48,49,50])
print(dizimiz1)

bos_liste = []

for a in dizimiz1:
    if a >= 44:
       bos_liste.append(True)
    else:
       bos_liste.append(False)

yenidizimiz1 = dizimiz1[bos_liste]

print(bos_liste)
print(yenidizimiz1)
print('\n\n\n')

dizimiz2 = np.array([10,11,12,13,14,15,16,17,18])
print(dizimiz2)

bos_liste2 = []

for a in dizimiz2:
    if a < 13:
       bos_liste2.append(True)
    else:
       bos_liste2.append(False)

yenidizimiz2 = dizimiz2[bos_liste2]

print(bos_liste2)
print(yenidizimiz2)
print('\n\n\n')

dizimiz3 = np.array([15,16,17,18,19,20,21,22,23,24,25])
print(dizimiz3)

bos_liste3 = []

for a in dizimiz3:
    if a % 2 == 0:
       bos_liste3.append(True)
    else:
       bos_liste3.append(False)

yenidizimiz3 = dizimiz3[bos_liste3]

print(bos_liste3)
print(yenidizimiz3)
print('\n\n\n')

dizimiz4 = np.array([12,14,16,18,20,23,25])
print(dizimiz4)

bos_liste4 = []

for a in dizimiz4:
    if a % 2 == 1:
       bos_liste4.append(True)
    else:
       bos_liste4.append(False)

yenidizimiz4 = dizimiz4[bos_liste4]

print(bos_liste4)
print(yenidizimiz4)
print('\n\n')

dizimiz5 = np.array(['xyz','x','y','z','xyz'])
print(dizimiz5)

bos_liste5 = []

for a in dizimiz5:
    if a == 'xyz':
       bos_liste5.append(True)
    else:
       bos_liste5.append(False)

yenidizimiz5 = dizimiz5[bos_liste5]

print(bos_liste5)
print(yenidizimiz5)
print('\n\n')

dizimiz6 = np.array([5,3,8,10,12,5,21,5,24])
print(dizimiz6)

bos_liste6 = []

for a in dizimiz6:
    if a == 5:
       bos_liste6.append(True)
    else:
       bos_liste6.append(False)

yenidizimiz6 = dizimiz6[bos_liste6]

print(bos_liste6)
print(yenidizimiz6)
print('\n\n\n')

dizimiz7 = np.array([3,4,5,6,7,8])
print(dizimiz7)

filter_arr = dizimiz7 > 5
new_arr = dizimiz7[filter_arr]

print(filter_arr)
print(new_arr)
print('\n\n')

dizimiz8 = np.array(['ana','a','n','ana','ana'])
print(dizimiz8)

filter_arr2 = dizimiz8 == 'ana'
new_arr2 = dizimiz8[filter_arr2]

print(filter_arr2)
print(new_arr2)
print('\n\n')

dizimiz8 = np.array(['ana','a','n','ana','ana'])
print(dizimiz8)

filter_arr2 = dizimiz8 == 'ana'
new_arr2 = dizimiz8[filter_arr2]

print(filter_arr2)
print(new_arr2)
print('\n\n')

dizimiz9 = np.array([10,12,13,15,17])
print(dizimiz9)

filter_arr3 = dizimiz9 % 2 == 0
new_arr3 = dizimiz9[filter_arr3]

print(filter_arr3)
print(new_arr3)
print('\n\n')

dizimiz10 = np.array([50,50,33,50,50,50,45])
print(dizimiz10)

filter_arr4 = dizimiz10 != 50
new_arr4 = dizimiz10[filter_arr4]

print(filter_arr4)
print(new_arr4)
print('\n\n')

dizimiz11 = np.array([100,150,200,250,300,350])
print(dizimiz11)

filter_arr5 = dizimiz11 > 3**5
new_arr5 = dizimiz11[filter_arr5]

print(filter_arr5)
print(new_arr5)
print('\n\n')

dizimiz12 = np.array([125,493,939])
print(dizimiz12)

filter_arr6 = dizimiz12 == 5**3
new_arr6 = dizimiz12[filter_arr6]

print(filter_arr6)
print(new_arr6)
print('\n\n\n\n\n')

from numpy import random

rasgele1 = random.randint(100)
print(rasgele1)
print()

rasgele2 = random.rand()
print(rasgele2)
print()

rasgele3 = random.randint(10, size=5)
print(rasgele3)
print()

rasgele4 = random.randint(30,50, size=(3,4))
print(rasgele4)
print()

rasgele5 = random.rand(10)
print(rasgele5)
print()

rasgele6 = random.rand(2,3)
print(rasgele6)
print()

rasgele7 = random.choice([4,1,6,9,7,8,])
print(rasgele7)
print()

rasgele8 = random.choice([10,20,30,40,50], size=(3,3))
print(rasgele8)
print('\n')

örnek1 = [4,5,6,7]
örnek2 = [1,2,3,8]
örnek3 = []

for i, j in zip(örnek1, örnek2):
    örnek3.append(i + j)
    print(örnek3)
print('\n\n')

örnek4 = [4,5,6,7]
örnek5 = [1,2,3,8]

örnek6 = np.add(örnek4, örnek5)
print(örnek6)
print()
örnek7 = np.subtract(örnek4, örnek5)
print(örnek7)
print()

def myadd(a, b):
    return a + b
hesap = np.frompyfunc(myadd, 2, 1)
print(hesap([1,2,3,4], [5,6,7,8]))
print('\n\n')

dizilerimiz1 = np.array([10,11,12,13,14,15])
dizilerimiz2 = np.array([20,21,22,23,24,25])

yeniarray1 = np.add(dizilerimiz1, dizilerimiz2)
print(yeniarray1)
print('\n')

dizilerimiz3 = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(2,5)
print(dizilerimiz3)
print()
dizilerimiz4 = np.array([11,12,13,14,15,16,17,18,19,20]).reshape(2,5)
print(dizilerimiz4)
print()

yeniarray2 = np.add(dizilerimiz3, dizilerimiz4)
print(yeniarray2)
print('\n')

dizilerimiz5 = np.array([5,15,25,35,45,55]).reshape(3,2)
print(dizilerimiz5)
print()
dizilerimiz6 = np.array([3,6,9,12,15,18]).reshape(3,2)
print(dizilerimiz6)
print()

yeniarray3 = np.subtract(dizilerimiz5, dizilerimiz6)
print(yeniarray3)
print('\n')

dizilerimiz7 = np.array([2,4,6,8,10,12,14,16,18]).reshape(3,3)
print(dizilerimiz7)
print()
dizilerimiz8 = np.array([3,5,7,9,11,13,15,17,19]).reshape(3,3)
print(dizilerimiz8)
print()

yeniarray4 = np.multiply(dizilerimiz7, dizilerimiz8)
print(yeniarray4)
print('\n')

dizilerimiz9 = np.array([50,60,80,100,120,140,200,270,300,330,360,520]).reshape(4,3)
print(dizilerimiz9)
print()
dizilerimiz10 = np.array([2,3,4,5,6,7,8,9,10,11,12,13]).reshape(4,3)
print(dizilerimiz10)
print()

yeniarray5 = np.divide(dizilerimiz9, dizilerimiz10)
print(yeniarray5)
print('\n')

dizilerimiz11 = np.array([2,3,4,5]).reshape(2,2)
print(dizilerimiz11)
print()
dizilerimiz12 = np.array([5,6,7,8]).reshape(2,2)
print(dizilerimiz12)
print()

yeniarray6 = np.power(dizilerimiz11, dizilerimiz12)
print(yeniarray6)
print('\n')

dizilerimiz13 = np.array([50,60,70,80,90,100]).reshape(2,3)
print(dizilerimiz13)
print()
dizilerimiz14 = np.array([12,13,15,16,17,18]).reshape(2,3)
print(dizilerimiz14)
print()

yeniarray7 = np.mod(dizilerimiz13, dizilerimiz14)
print(yeniarray7)
print('\n')

dizilerimiz15 = np.array([50,55,60,65,70,75,80,85]).reshape(4,2)
print(dizilerimiz15)
print()
dizilerimiz16 = np.array([3,4,7,8,9,10,11,12]).reshape(4,2)
print(dizilerimiz16)
print()

yeniarray8 = np.remainder(dizilerimiz15, dizilerimiz16)
print(yeniarray8)
print('\n')

dizilerimiz17 = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(2,5)
print(dizilerimiz17)
print()
dizilerimiz18 = np.array([11,12,13,14,15,16,17,18,19,20]).reshape(2,5)
print(dizilerimiz18)
print()

yeniarray9 = np.add(dizilerimiz17, dizilerimiz18)
print(yeniarray9)
print('\n')

dizilerimiz19 = np.array([20,30,40,50,60,70]).reshape(3,2)
print(dizilerimiz19)
print()
dizilerimiz20 = np.array([3,4,6,7,8,9]).reshape(3,2)
print(dizilerimiz20)
print()

yeniarray10 = np.divmod(dizilerimiz19, dizilerimiz20)
print(yeniarray10)
print('\n\n')

dizilerimiz21 = np.array([50,51,52,53,54,55,56,57,58]).reshape(3,3)
print(dizilerimiz21)
print()
dizilerimiz22 = np.array([3,4,5,6,7,8,9,10,11]).reshape(3,3)
print(dizilerimiz22)
print()

yeniarray11 = np.divmod(dizilerimiz21, dizilerimiz22)
print(yeniarray11)
print('\n\n')

dizilerimiz23 = np.array([100,150,200,250,300])
print(dizilerimiz23)
print()
dizilerimiz24 = np.array([12,13,14,15,16])
print(dizilerimiz24)
print()

yeniarray12 = np.divmod(dizilerimiz23, dizilerimiz24)
print(yeniarray12)
print('\n\n')

dizilerimiz25 = np.array([30,31,32,33,34])
print(dizilerimiz25)
print()
dizilerimiz26 = np.array([7,8,9,10,11])
print(dizilerimiz26)
print()

yeniarray13 = np.divmod(dizilerimiz25, dizilerimiz26)
print(yeniarray13)
print('\n\n\n\n\n')

dizilerimiz27 = np.array([-3,-9,-6,-2,-1,-5,10,11,12])
print(dizilerimiz27)
print()

yeniarray14 = np.absolute(dizilerimiz27)
print(yeniarray14)
print()
yeniarray15 = np.abs(dizilerimiz27)
print(yeniarray15)
print('\n\n')

dizilerimiz28 = np.trunc([3.89645654, -2.56643, 93.949, -66.493943])
print(dizilerimiz28)
print()

dizilerimiz29 = np.fix([32.94943, 49.59394, -55.94384, -12.394993])
print(dizilerimiz29)
print()

dizilerimiz30 = np.floor([22.999, 30.9584, 35.12949])
print(dizilerimiz30)
print()

dizilerimiz31 = np.floor([-8.00001, -13.99999, -21.0, -25.0])
print(dizilerimiz31)
print()

dizilerimiz32 = np.ceil([12.00001, 14.4392, 18.99999])
print(dizilerimiz32)
print()

dizilerimiz33 = np.ceil([-14.00001, -17.99999, -45.4923])
print(dizilerimiz33)
print()

dizilerimiz34 = np.around(3.4645643646, 7)
print(dizilerimiz34)
print()

dizilerimiz35 = np.around(3.49999999)
print(dizilerimiz35)
print()

dizilerimiz36 = np.around([33.49, 32.5, 11.5, 14.5])
print(dizilerimiz36)
print()

dizilerimiz37 = np.around([24.4999999999999999, 27.4999999999999999])
print(dizilerimiz37)
print()

dizilerimiz38 = np.around([-5.4999999999999999, -8.4999999999999999])
print(dizilerimiz38)
print()

dizilerimiz36 = np.around([55.1932452232496], 8)
print(dizilerimiz36)
print()

dizilerimiz40 = np.array([5,10,15,20])
print(dizilerimiz40)
dizilerimiz41 = np.array([2,3,5,8])
print(dizilerimiz41)

topla1 = np.sum([dizilerimiz40, dizilerimiz41])
print(topla1)
topla2 = np.add(dizilerimiz40, dizilerimiz41)
print(topla2)
print('\n\n')

dizilerimiz42 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(dizilerimiz42)
print()
dizilerimiz43 = np.array([[25,26,27,28], [33,34,35,36], [46,47,48,49]])
print(dizilerimiz43)
print()

topla3 = np.sum([dizilerimiz42, dizilerimiz43], axis=0)
print(topla3)
print('\n\n')

dizilerimiz44 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizilerimiz44)
print()
dizilerimiz45 = np.array([[12,15,18],[24,25,27],[31,36,38]])
print(dizilerimiz45)
print()

topla4 = np.sum([dizilerimiz44, dizilerimiz45], axis=0)
print(topla4)
print('\n\n')

dizilerimiz46 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(dizilerimiz46)
print()
dizilerimiz47 = np.array([[25,26,27,28], [33,34,35,36], [46,47,48,49]])
print(dizilerimiz47)
print()

topla4 = np.sum([dizilerimiz46, dizilerimiz47], axis=1)
print(topla4)
print('\n\n')

dizilerimiz48 = np.array([1,5,7,8,10,12])
print(dizilerimiz48)
print()
dizilerimiz49 = np.array([21,23,24,26,28,29])
print(dizilerimiz49)
print()

topla5 = np.sum([dizilerimiz48, dizilerimiz49])
print(topla5)
print('\n\n')

dizilerimiz50 = np.array([12,14,15,20,25])
print(dizilerimiz50)
print()
dizilerimiz51 = np.array([3,4,6,7,8])
print(dizilerimiz51)
print()

topla6 = np.sum([dizilerimiz50, dizilerimiz51], axis=0)
print(topla6)
print('\n\n')

dizilerimiz52 = np.array([4,5,6,7,8])
print(dizilerimiz52)
print()
dizilerimiz53 = np.array([13,14,15,16,17])
print(dizilerimiz53)
print()

topla7 = np.sum([dizilerimiz52, dizilerimiz53], axis=1)
print(topla7)
print('\n\n')

dizilerimiz54 = np.array([2,4,6,8])
print(dizilerimiz54)
print()
dizilerimiz55 = np.array([3,5,7,9])
print(dizilerimiz55)
print()
dizilerimiz56 = np.array([10,20,30,40])
print(dizilerimiz56)
print()

topla8 = np.sum([dizilerimiz54, dizilerimiz55, dizilerimiz56], axis=1)
print(topla8)
print()
topla9 = np.sum([dizilerimiz54, dizilerimiz55, dizilerimiz56], axis=0)
print(topla9)
print('\n\n\n')

dizilerimiz57 = np.array([1,2,3,4,5,6,7,8])
kümülatif_toplam1 = np.cumsum(dizilerimiz57)
print(kümülatif_toplam1) 
print('\n\n')

dizilerimiz58 = np.array([5,10,15,20,25,30,35,40])
kümülatif_toplam2 = np.cumsum(dizilerimiz58)
print(kümülatif_toplam2)
print('\n\n')

dizilerimiz59 = np.array([2,4,6,8,10,12])
kümülatif_toplam3 = np.cumsum(dizilerimiz59)
print(kümülatif_toplam3)
print('\n\n')

dizilerimiz60 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(dizilerimiz60)
print()
kümülatif_toplam4 = np.cumsum(dizilerimiz60, axis=0)
print(kümülatif_toplam4)
print('\n\n\n')

dizilerimiz61 = np.array([[10,20,30,40,50],[1,2,3,4,5],[13,14,15,16,17],[21,22,23,24,25]])
print(dizilerimiz61)
print()
kümülatif_toplam5 = np.cumsum(dizilerimiz61, axis=0)
print(kümülatif_toplam5)
print('\n\n')

dizilerimiz62 = np.array([[10,20,30,40,50],[1,2,3,4,5],[13,14,15,16,17],[21,22,23,24,25]])
print(dizilerimiz62)
print()
kümülatif_toplam6 = np.cumsum(dizilerimiz62, axis=1)
print(kümülatif_toplam6)
print('\n\n')

dizilerimiz63 = np.array([10,15,20,5])
fark1 = np.diff(dizilerimiz63)
print(fark1)
print()

dizilerimiz63 = np.array([3,7,11,18,5,6,10,12,9,14])
fark2 = np.diff(dizilerimiz63)
print(fark2)
print()

dizilerimiz64 = np.array([85,70,45,40,30,10,1])
fark3 = np.diff(dizilerimiz64)
print(fark3)
print()

dizilerimiz65 = np.array([3,10,2,13,5,18])
fark4 = np.diff(dizilerimiz65, n=2)
print(fark4)
print()

dizilerimiz66 = np.array([5,10,25,20,45,35])
fark5 = np.diff(dizilerimiz66, n=3)
print(fark5)
print()

dizilerimiz67 = np.array([50,10,30,20,70,60])
fark6 = np.diff(dizilerimiz67, n=4)
print(fark6)
print()

dizilerimiz68 = np.array([90,80,100,60,30,70])
fark7 = np.diff(dizilerimiz68, n=5)
print(fark7)
print()

dizilerimiz69 = np.array([[3,7,2],[1,6,5],[8,4,9],[14,12,13],[19,17,16]])
print(dizilerimiz69)
print()
fark8 = np.diff(dizilerimiz69, axis=0)
print(fark8)
print()

dizilerimiz70 = np.array([[2,9,4,8,5,6], [11,13,12,16,15,18], [25,22,26,21,28,27], [36,32,35,34,39,38]])
print(dizilerimiz70)
print()
fark9 = np.diff(dizilerimiz70, axis=1)
print(fark9)
print()

dizilerimiz71 = np.array([[10,5,20,25],[40,35,30,50],[80,70,75,60],[100,85,95,90],[130,120,125,140]])
print(dizilerimiz71)
print()
fark10 = np.diff(dizilerimiz71, axis=0)
print(fark10)
print()
print('***********************************************************')

num1 = np.array([3,5,10,12])
num2 = np.array([4,11,7,15])
num3 = np.lcm(num1,num2) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num3)
print()

num4 = np.array([[3,4,5],[6,7,8]])
num5 = np.array([[7,9,12],[14,15,18]])
num6 = np.lcm(num4,num5) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num6)
print()

num7 = np.array([[21,22,23,24],[25,26,27,28]])
num8 = np.array([[7,8,9,10],[3,4,5,6]])
num9 = np.lcm(num7,num8) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num9)
print()

num10 = np.array([4,7,10])

num11 = np.lcm.reduce(num10) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num11)
print()

num12 = np.array([5,6,8,15])

num13 = np.lcm.reduce(num12) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num13) 
print()

num14 = np.array([10,6,16,30])

num15 = np.lcm.reduce(num14) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num15)
print()

num16 = np.array([5,9,15,20,40])

num17 = np.lcm.reduce(num16) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num17)
print()

num16 = np.array([5,9,15,20,40])

num17 = np.lcm.reduce(num16) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num17)
print()

num18 = np.array([2,3,4,5,6])

num19 = np.lcm.reduce(num18) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num19)
print()

num20 = np.array([10,20,30,40,50])

num21 = np.lcm.reduce(num20) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num21)
print()

num22 = np.arange(2,10,2)
print(num22)

num23 = np.lcm.reduce(num22) # lcm -> least common multiple -> en küçük ortak kat (EKOK)
print(num23)
print('\n\n\n\n')

numara1 = 200
numara2 = 250

numara3 = np.gcd(numara1, numara2) # gcd -> greatest common divisor -> en büyük ortak bölen (EBOB)
print(numara3)
print()

numara1 = np.array([130,150,180,200,250,300])
numara2 = np.array([15,20,25,30,40,70])

numara3 = np.gcd(numara1, numara2) # gcd -> greatest common divisor -> en büyük ortak bölen (EBOB)
print(numara3)
print()

numara4 = np.array([24,36,48,60,72,84,96])

numara5 = np.gcd.reduce(numara4) # gcd -> greatest common divisor -> en büyük ortak bölen (EBOB)
print(numara5)
print()

numara6 = np.array([12,16,20,24,32])

numara7 = np.gcd.reduce(numara6) # gcd -> greatest common divisor -> en büyük ortak bölen (EBOB)
print(numara7)
print()

numara8 = np.array([35,40,45,50,55,60])

numara9 = np.gcd.reduce(numara8) # gcd -> greatest common divisor -> en büyük ortak bölen (EBOB)
print(numara9)
print()

numara10 = np.array([55,66,77,88,99,110,121,132,143,154])

numara11 = np.gcd.reduce(numara10) # gcd -> greatest common divisor -> en büyük ortak bölen (EBOB)
print(numara11)
print('\n\n\n\n')

sayı1 = np.array([3,5,7,8])
print(sayı1)
sayı2 = np.array([4,12,24,15])
print(sayı2)

hipotenüs1 = np.hypot(sayı1, sayı2)
print(hipotenüs1)
print('\n\n')

sayı3 = np.array([6,10,14,16])
print(sayı3)
sayı4 = np.array([8,24,48,30])
print(sayı4)

hipotenüs2 = np.hypot(sayı3, sayı4)
print(hipotenüs2)
print('\n\n')

sayı5 = np.array([5,6,7,8,9])
print(sayı5)
sayı6 = np.array([10,11,12,13,14])
print(sayı6)

hipotenüs3 = np.hypot(sayı5, sayı6)
print(hipotenüs3)
print('\n\n')

sayı7 = 3
sayı8 = 5

hipotenüs4 = np.hypot(sayı7,sayı8)
print(hipotenüs4)
print('\n\n')

array21 = np.array([1,3,1,1,2,4,4,2,3,3,4,3,3,1,1,2,2,2,4,4])
print(array21)
print()
essiz1 = np.unique(array21, return_counts=True)
print(essiz1)
print('\n')

array22 = np.array([1,3,1,1,2,4,4,2,3,3,4,3,3,1,1,2,2,2,4,4])
print(array22)
print()
essiz2 = np.unique(array22, return_index=True)
print(essiz2)

array23 = np.array([1,3,1,1,2,4,4,2,3,3,4,3,3,1,1,2,2,2,4,4])
print(array23)
print()
essiz3 = np.unique(array23, return_inverse=True)
print(essiz3)
print('\n\n\n')

array24 = np.array([10,10,10,20,20,20,30,30,30,40,40,40])
print(array24)
print()
essiz4 = np.unique(array24)
print(essiz4)
print()
essiz5 = np.unique(array24, return_counts=True)
print(essiz5)
print()
essiz6 = np.unique(array24, return_index=True)
print(essiz6)
print()
essiz7 = np.unique(array24, return_inverse=True)
print(essiz7)
print('\n\n\n\n')

dizis1 = np.array([1,2,3,4,5,6,7,8,9])
dizis2 = np.array([5,6,7,8,9,10]) 

yeniarr1 = np.union1d(dizis1, dizis2)
print(yeniarr1)
print('\n\n')

dizis3 = np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90])
dizis4 = np.array([5,10,15,20,100,200,300,400,500,60,65,70,75,80,85,90,95,150,250]) 

yeniarr2 = np.union1d(dizis3, dizis4)
print(yeniarr2)
print('\n\n')

dizis5 = np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90])
dizis6 = np.array([5,10,15,20,100,200,300,400,500,60,65,70,75,80,85,90,95,150,250]) 

yeniarr3 = np.union1d(dizis5, dizis6)
print(yeniarr3)
print()

dizis7 = np.array([2,4,6,8,10,12,14,16,18,20,22,24])
dizis8 = np.array([1,3,5,7,9,10,12,14,16,17,19,21,23,25,27,29]) 

yeniarr4 = np.union1d(dizis7, dizis8)
print(yeniarr4)
print('\n\n\n')

dizis9 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
dizis10 = np.array([3,6,9,12,15,18,21,24]) 

yeniarr5 = np.intersect1d(dizis9, dizis10)
print(yeniarr5)
print()

dizis11 = np.array([6,13,20,24,29,32,38,41,45,53])
dizis12 = np.array([4,7,13,22,26,29,34,38,40,42,45,50]) 

yeniarr6 = np.intersect1d(dizis11, dizis12, return_indices=True)
print(yeniarr6)
print()

dizis13 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
dizis14 = np.array([3,6,9,12,15,18,21,24]) 

yeniarr7 = np.intersect1d(dizis13, dizis14)
print(yeniarr7)
print('\n\n\n\n')

küme1 = np.array([1,2,3,4,5,6,7,8,9,10])
küme2 = np.array([3,5,6,7,9])

sonuc1 = np.setdiff1d(küme1, küme2)
print(sonuc1)
print('\n')

küme3 = np.array([5,10,15,20,25,30,35,40,45,50])
küme4 = np.array([1,4,5,9,10,14,15,19,20,23,25])

sonuc2 = np.setdiff1d(küme4, küme3)
print(sonuc2)
print('\n\n\n\n')

küme5 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
küme6 = np.array([3,4,5,6,7,8,9,10,20,25,30])

sonuc3 = np.setxor1d(küme5, küme6)
print(sonuc3)
print('\n')

küme7 = np.array([100,200,300,400,500,600,700,800,900,1000])
küme8 = np.array([50,100,150,200,250,300,350,400,450,500])

sonuc4 = np.setxor1d(küme8, küme7) 
print(sonuc4)


















           
           


    














