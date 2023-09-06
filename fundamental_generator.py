n = 17
fin = open("ASL1_new.txt", "r")
fout = open("quandle.txt", "w")
lines = fin.readlines()

fq = []

#Generates all the crossings in the tangles directed from top to bottom
for i in range (2, 20):
    line = lines[i].split()
    for j in range(3):
        line[j] = int(line[j])
    for j in range (n):
        fq.append ([40*j + line[0], 40*j + line[1], 40*j + line[2]])

#Generates all the crossings in the tangles directed from bottom to top
for i in range (22, 40):
    line = lines[i].split()
    for j in range(3):
        line[j] = int(line[j])
    for j in range (n):
        fq.append ([40*j + line[0], 40*j + line[1], 40*j + line[2]])

left = []

for i in reversed (range (2*n-1)):
    left.append ((4*n-i)*10)

for i in range (5):
    left.append (40*n+i+1)

#Generates all the crossings in the top row
for i in range (n):
    fq.append ([left[1+2*i], 21+40*(n-1)-40*i , left[0+2*i]])
    fq.append ([21+40*(n-1)-40*i, left[1+2*i], 31+40*(n-1)-40*i])
    fq.append ([1+40*(n-1)-40*i, left[1+2*i], 11+40*(n-1)-40*i])
    fq.append ([left[1+2*i], 1+40*(n-1)-40*i, left[2+2*i]])

#Crossing at the very top
fq.append ([left[-4], left[0], left[-3]])

#Link crossings
fq.append ([left[0]-10, left[-2], 10])
fq.append ([left[-3], left[-2], left[0]])
fq.append ([left[-2], 10 , left[-1]])
fq.append ([left[-1], left[0], left[-2]])

(print (len(fq)))
print (fq)

for [i, j, k] in fq:
    fout.write(str(i) + ' ' + str(j) + ' ' + str(k) + '\n')