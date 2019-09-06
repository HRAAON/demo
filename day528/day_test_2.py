word ="""
[00:32.13]那个她取代我在你身边
[00:37.85]那个故事已经换了主角
[00:42.80]那个你曾经说要给我永远
[00:47.17]那个我竟然相信这份诺言
[00:52.81]那个她出现得我毫无防备
[00:57.80]那个爱离开得不知不觉
[01:02.73][01:04.73]那一个分手的夜无言的诀别
[01:07.60][01:09.60]那一条寒冷的街不再有你陪
[01:11.48][01:12.10][01:13.60]我以为我能坚强地面对
"""
# 字典
dirr = {}
wordList = word.splitlines()
for words in wordList:
    lrvList = words.split("]")
    # 遍历列表lrvList的前两个数据
    for i in range(len(lrvList)-1):
        # [1:]输出第二位到最后一位的内容
        # i 表示每一个【xx】内容
        result = lrvList[i][1:]

        print(result)

        timeList = result.split(":")
        timee = float(timeList[0])*60+float(timeList[1])
        dirr[timee]=lrvList[-1]
        print(timee)

allTime = []
# 从dirr里取出来的是key
for ii in dirr:
    allTime.append(ii)
    allTime.sort()
print(allTime)

while 1:
    getTime = float(input("请输入时间"))
    for n in range(len(allTime)):
        tempTime = allTime[n]
        if getTime < tempTime:
            break
    if n == 0:
        print("时间太小")
    else:
        print(dirr[allTime[n-1]])




