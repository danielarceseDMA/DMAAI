import sys
import math

def findhypotenuse(a, b):
    a_squared=math.pow(a,2)
    b_squared=math.pow(b,2)
    return math.sqrt(a_squared+b_squared)


def main():
    command=sys.argv[1]



    if command=="add":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x+y)
    if command=="subtract" or command=="minus":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x-y)
    if command=="countto":
        x = int(sys.argv[2])
        k = 1
        while k <= x:
            print(k)
            k=k+1
    if command=="findhypotenuse":
        x=int(sys.argv[2])
        y= int(sys.argv[3])
        print(findhypotenuse(x,y))


    for i in ['dog','cat','fish']:
        print(i)

    k = 1
    while k < 4:
        print(k)
        k = k + 1
if __name__ == "__main__":
    main()
