import math

def fun1(x):
    return x - x**2

def fun2(a, b, c):
    D = b**2-4*a*c
    if D < 0:
        print("Вещественных корней нет")
        return
    if D>0:
        x1 = ((-b)+D**0.5)/(2*a)
        x2 = ((-b)-D**0.5)/(2*a)
        return x1, x2
    return  (-b)/(2*a)

def fun3(x ,y):
    return x*(math.e**3) + math.tan(abs(x-y)**0.5)

def distance(x1, y1, x2, y2):
    return((x1-x2)**2+(y1-y2)**2)**0.5
def find_max_distance(arr):
    maxdist = 0
    ndist = 0
    points = []
    for i, el in enumerate(arr):
        for j in range(i+1,len(arr)):
            ndist = distance(el[0],el[1], arr[j][0], arr[j][1])
            if maxdist < ndist:
                maxdist = ndist
                points = [[el[0],el[1]], [arr[j][0], arr[j][1]]]
    return maxdist, points
if __name__ == '__main__':
    inp=input()
    arr=[]
    while inp!='':
        arr+=[list(map(int,inp.split()))]
        inp=input()

    print(find_max_distance(arr), distance(1,1,7,1))

