# -*- coding: UTF-8 -*-
# 猜拳游戏
import random
while 1:
    s = int(random.uniform(1, 3))
    if s == 1:
        ind = '石头'
    elif s == 2:
        ind = '剪刀'
    elif s == 3:
        ind = '布'
    m = raw_input('输入剪刀、石头，布,输入"end"结束游戏:\n')

    blist = ['剪刀','石头','布']
    if (m not in blist) and (m != 'end'):
        print '输入信息错误，请输入石头，剪刀，布\n'
    elif (m not in blist) and (m == 'end'):
        print '\n游戏结束'
        break
    elif m == ind:
        print "电脑出了:" + ind + "， 平局\n"
    elif (m == '剪刀' and ind == '布') or (m == '石头' and ind == '剪刀') or (m == '布' and ind == '石头'):
        print '电脑出了：' + ind + '， you win\n'
    elif (m == '剪刀' and ind == '石头') or (m == '石头' and ind == '布') or (m == '布' and ind == '剪刀'):
        print '电脑出了：' + ind + '， you lost\n'
