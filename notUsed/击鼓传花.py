def print_link(h):
    #按照head 和 nxt 构造的顺序， 把valve中的数值显示出来
    #1, 2, 3, 4, 5, 6, 7, 9, 15, 35
    res = []
    p = h
    while p != -1:
        res.append(value[p])
        p = nxt[p]
    return res



#--------------------main----------------------
value = [3, 1, 4, 15, 9, 2, 6, 5, 35, 7]
head = 1 #从小到大排列，第一个数的下标
nxt = [2, 5, 7, 8, 3, 0, 9, 6, -1, 5] #下一个数的下标
print(print_link(head))