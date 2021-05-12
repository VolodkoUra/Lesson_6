my_string = "dfsfsdgsgsg"
my_list = list(my_string)
result = " ".join(my_list)
print(result)
res = ""
for i in my_list:
    res += (i + " ")
print(res)



exit()
email = 'zdfzvzvdv@vmskgm.jhk'

if "@" in email and "." in email:
    print(True)
    result = email.split("@")
if "." in result[1]:
    # print(result[1])
    if len(result[-1].split(".")[-1]) > 1:
        result[-1].split(".")[-1]
        print(True)
    else:
        print(False)


exit()
cc = "123456789012"
ccc = "#"*len(cc[0:-4]) + cc[-4:]
print(ccc)

fib_list = [0,1,]
for i in range(100):
    fib_list.append(fib_list[i-1]+fib_list[i-2])
print(fib_list)

lst = []
for i in range(4):
    lst.append([])

print(lst)
for i in lst:
    for j in range(4):
        i.append(0)

for i in lst:
    print(i)

t = 0
for i, ii in enumerate(lst):
    for j, jj in enumerate(lst[i]):
        if i == j:
            lst[i][j] = 1
for i in lst:
    print(i)

my_list = [1,2,3,4,5]







