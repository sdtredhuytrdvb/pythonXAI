# 21.if
#    功能:假設第一種情境
# 22.elif
#    功能:同時需要多個else(定義)但要多種結果時,用elif就可設定多種結果
# 23.else
#    功能:其他所有的情境
# 24.for i in range(?):
#        print("?")
#    for i in range(?,?):
#        print("?")
#    for i in range(?,?,?):
#        print("?")
# 25..copy
# 功能:複製
# 26.n = [1,2,3,"a","b","c"]
# for i in range(0,len(n)):
#     print(n[i])
# for i in n:
#     print(i)

# 列表篇(list):
# 1. []（不是函數的[] 功能不一樣
#   功能：處理複雜資料（列表裡的括號
#        （備註：字串的第一個數字是第0位-1是倒數第一位[?：?]
#          問號一是從哪位開始取
#          問號二是一路取到第幾位
#          但不包含填的那一位
#          問號一也可以不填
#          代表從問號二開始取
#          一直取到字串開頭
#          Belike：[：?]
#          問號二也可以不填
#          代表從問號一的數開始取
#          一直取到字串結束
#          Belike：[？：]
#          (情況三:
#          [?1:?2:?3])
#          ?1,?2上面已說明
#          ?3是兩個連續的數差(特殊用法[::?])
# 2..append()
#   功能:在列表後面加入
# 3..remove()
#   功能:從列表中刪除
# 4..pop()
#   功能:從列表中刪除後取出
# 5.sort()
#   功能:列表排序

# 補充知識:
# # callby value
# # a = 1
# # b = a
# # b = 2

# # call by reference
# # a = [1,2,3]
# # b = a
# # b[0] = 2
# =
# # a = [1,2,3]
# # b = a.copy()
# # b[0] = 2 #(代替方案)

# f = open("pages\class1-1.py", "n", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()
# with open("pages\class1-1.py", "n", encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# filename = "class1.md"
# print(filename.endswith(".md"))
# filename2 = "notes.txt"
# print(filename2.endswith(".md"))
