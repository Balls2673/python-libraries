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

#agreegate function
agreearray = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.mean(agreearray))
print(np.sum(agreearray))
print(np.std(agreearray))
print(np.sum(agreearray, axis=1))

#filtering
ages = np.array([[23,43,65,23,15,13],[23,43,56,45,43,12]])
adults = np.where(ages >= 18, ages, -1)
print(adults)

#random number
rng = np.random.default_rng()
print(rng.integers(1,7,(3,2)))
print(np.random.uniform(-1,1))
Rarray = np.array([1,2,3,4,5])
rng.shuffle(Rarray)
print(Rarray)
fruits = np.array(["apple","green apple","tommato","beans"])
fruit = rng.choice(fruits)
print(fruit)


#just exerciecing 
Earray=np.array([1,2,3,4,5,6,7,8,9,10])
print(Earray[4])
onlyfiveoropove = np.where(Earray < 5, Earray, 0)
rng = np.random.default_rng()
print(rng.integers(1,100,10))
print(np.min(Earray))
print(np.max(Earray))
print(np.std(Earray))
print(np.mean(Earray))
print(np.sum(Earray))

Aarray = np.array([[ 1,  2,  3],[ 4 , 5 , 6],[ 7 , 8,  9]])

print(Aarray[1])
print(Aarray[:,2])
print(np.where(Aarray > 5, Aarray,999))