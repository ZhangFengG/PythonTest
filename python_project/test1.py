#   题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

def fun(d):
    datas = d
    for n in datas:
        b = False
        for x in datas:
            if n == x:
                continue
            else:
                for z in datas:
                    if z == x or z == n:
                        continue
                    else:
                        print(n, x, z)

fun([1, 2, 3, 4])