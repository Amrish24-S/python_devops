import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
add = a+b
sub = a-b
mul = a*b
dev = a/b
floor_div= a//b
mod = a%b
exp = a**b
print(f"{add}, {sub}, {mul}, {dev}, {floor_div}, {mod}, {exp} ")
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a//=b
print(a)
a**=b
print(a)
a%=b
print(a)
print(a is b)
print((a < b) and (b == a))

