from sympy import symbols
import math

#quandle.txt is any funadmental quandle
fin = open("quandle.txt", "r")
lines = fin.readlines()
num_vars = len(lines)
vars = ""

#Define a variable for each of the strands in which we will define a coloring
for i in range (num_vars-1):
    vars += ("S_" + str(i) + ", ")
vars += "S_" + str(i+1)
s = symbols(vars)
symbolslist = []
for i in s:
    symbolslist.append(i)
    i = 1

#u will be used to calculate the cocycle invariant, a and b will be used to define the coloring of the link
u, a, b = symbols('u, a, b')

visited = []
queue = []
for i in range (num_vars):
    visited.append (False)
    temp = lines[i].split()
    queue.append ( (int(temp[0])-1, int(temp[1])-1, int(temp[2])-1) )

#Pick the t for the cocyle calculation
t = 2
n = num_vars

#x, y, z represent any starting point on the link
x, y, z = queue.pop(0)
symbolslist[x] = a
symbolslist[y] = b
symbolslist[z] = t*symbolslist[x] + (1-t)*symbolslist[y]

visited[x] = True
visited[y] = True
visited[z] = True

#algorithm for finding the coloring of the link
while False in visited:
    cont = False
    for i in range(len(queue)):
        x, y, z = queue[i]

        if (visited[x] and visited[y] and not visited[z]):
            queue.pop(i)
            symbolslist[z] = t*symbolslist[x] + (1-t)*symbolslist[y]
            visited[z] = True
            cont = True
            break
        if (visited[y] and visited[z] and not visited[x]):
            queue.pop(i)
            symbolslist[x] = (symbolslist[z] - (1-t)*symbolslist[y]) * pow(t, -1, n)
            visited[x] = True
            cont = True
            break
        if (visited[x] and visited[z] and not visited[y]):
            queue.pop(i)
            symbolslist[y] = (symbolslist[z] - t*symbolslist[x] * pow(1-t, -1, n))
            visited[y] = True
            cont = True
            break

    if not cont:
        break

def phi(a, b):
    if (a, b) in [(0, 1), (1, 0), (1+t, 0), (0, 1+t), (1, 1+t), (1+t, 1)]:
        return u
    else:
        return 1

cocycle = 0

#algorithm for calculating the cocycle of the link
for i in range(num_vars):
    for j in range(num_vars):

        if i == j:
            cocycle += 1
        else:
        #(i, j) refers to an element in R_num_vars x R_num_vars
            cocycle += (phi(i, j) * phi(b, t*a+(1-t)*b) * phi (t*a + (1-t)*b, a) * phi (b, b))**2

print (cocycle)