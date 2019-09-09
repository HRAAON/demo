s1 = set([1,2,3,4,5,6])
for i in s1:
    print(i)
    # set是没有索引的，所以无法通过索引取参数
    # set不能有重复的数据，用来做过滤
    # print(s1[2])

s2 = set([1,2,3])
s3 = set([2,3,4])

# set去重演示
c = [1,2,3,4,4,3,5,6,7,8]
d = set(c)
e = list(d)
print(e)


# 交集
a1 = s2 & s3
print(a1)

# 并集  |
a2 = s2 | s3


# set --> list
a ={1,2,3,4}
b = list(a)
print(b)