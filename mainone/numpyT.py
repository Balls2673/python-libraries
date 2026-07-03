import numpy as np

array = np.array([[[['A','d',''],['A','c','f'],['A','','']],
                  [['A','',''],['A','',''],['A','','']],
                  [['A','',''],['A','',''],['A','','']]],
                  [[['A','',''],['A','',''],['A','','']],
                  [['A','',''],['A','',''],['A','','']],
                  [['A','',''],['A','',''],['A','','']]]])

word = array[0,0,0,1]+  array[1,0,2,0]
print(word)


numarray = np.array([[1,3,2,43],[14,30,72,45],[16,35,29,48],[17,34,23,41],[16,35,29,48],[17,34,23,41]])

# array[start:end:step]

print(numarray[0:2,2:4])




#scalar arithmetic

scalararray = np.array([1,3,2,4])
print(scalararray + 1)
print(scalararray - 3)
print(scalararray * 5)

#vectorized math func

vecarray = np.array([1.3,3.2,4.24,5,2])
print(np.sqrt(vecarray))
print(np.round(vecarray))
print(np.floor(vecarray))
print(np.ceil(vecarray))

#exercies
arrayround = np.round(vecarray)
A = np.pi * arrayround ** 2
print(A)


#elemet wise arithmetic

array1 = np.array([1,3,2,4])
array2 = np.array([5,7,6,8])

print(array1 + array2)

#comparsion opraters

scores = np.array([23,55,75,36,46,97,86,100])
scores[scores < 50] = 0
print(scores)

#broadcasting

arrayb1 = np.array([[1,2,3,4]])
arrayb2=np.array([[1],[2],[3],[4]])
print(arrayb1.shape)
print(arrayb2.shape)
print(arrayb1*arrayb2) 
print("dog")