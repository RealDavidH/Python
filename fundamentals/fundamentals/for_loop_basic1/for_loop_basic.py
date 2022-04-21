from genericpath import exists


for i in range(0,151):
    print(i)

for k in range (5, 101):
    k *= 5
    print(k)

for j in range(1, 100):
    if(j % 10 == 0):
        print("Coding Dojo")
        continue
    elif(j % 5 == 0):
        print("Coding")
    else:
        print(j)

sum = 0
for odd in range(0, 500000):
    if(odd % 2 == 1):
        sum += odd

print(sum)

for down in range(2018, 0, -4):
    print(down)

highnum = 9
lownum = 2
mult = 3
for i in range(lownum,highnum+1):
    if i%mult == 0:
        print(i)

