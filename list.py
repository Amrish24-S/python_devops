ls = ["am", "ar", "s3", "route53"]
ls2 = ["eks", "vpc"]
ln = [1, 5, 4, 9, 2, 7]
print(ls)
print(ls[0:3])
print(len(ls))
print(type(ls))
ls.remove("am")
print(ls)
ls.append("rds")
print(ls)
ls = ls + ls2
ls.sort()
print(ls)
ls.extend(ls2)
ln.sort()
print(ln)
if "eks" in ls:
    print("true")
for i in ls:
    print(i)
for i in range (10):
    print(i)
