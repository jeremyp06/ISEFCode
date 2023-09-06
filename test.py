a = input()
out = []

while (a != "done"):
    if a.startswith('6'):
        out.append (int(a.split(' + ')[1])+6)
    a = input()

for i in out:
    print (i)