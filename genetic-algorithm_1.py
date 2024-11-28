import random
def Generate_point():
    lst=[]
    for i in range(8):
        lst.append(random.randint(15,110))
    return lst
def Alpha_Beta(point,a,b):
    if not point:
        return 0
    Val_Max=float('-inf')
    for i in point:
        Val_Max = max(Val_Max,-Alpha_Beta(point[1:],-a,-b)+i)
        a = max(a,Val_Max)
        if a>=b:
            break
    return Val_Max
Rand_Point=Generate_point()
ID=int(input("Enter ID: "))
win_points=int(input("Enter the total point to win: "))

print(f"Generated 8 random point between the minimum and maximum point limits:{Rand_Point}")
gain=Alpha_Beta(Rand_Point,float('-inf'),float('inf'))
print(f"Total points to win: {win_points}")
if gain>= win_points:
    result="Optimus Prime"
else:
    result="Megatron"
print(f"achieved points= {gain}")
print(f"The winner is {result}")
