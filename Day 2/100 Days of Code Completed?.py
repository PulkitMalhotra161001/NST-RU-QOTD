https://my.newtonschool.co/playground/code/zb320x1xkda0


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
assert(len(list1) == len(list2) and len(list2) == 100)
for i in range(100):
    if(list1[i] + list2[i] == 0):
        print("False")
        exit()
print("True")
