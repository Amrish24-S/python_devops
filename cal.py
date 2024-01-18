import sys
def adder (x=0, y=0, z=0):
    res = x+y+z
    return res
def add (x=0, y=0):
    res = x+y
    return res
def sub (x=0, y=0):
    res = x-y
    return res
def mul (x=0, y=0):
    res = x*y
    return res
a = float(sys.argv[1])
opp = sys.argv[2]
b = float(sys.argv[3])

if opp == "add":
    out = add(a, b)
    print(out)
elif opp == "sub":
    out = sub(a, b)
    print(out)
else:
    out = mul(a, b)
    print(out)

