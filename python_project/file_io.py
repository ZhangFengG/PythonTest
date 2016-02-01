# import random
# f = open('test.txt', 'w')
# for i in range(1, 20):
#     if i==None:
#         print('last')
#     f.write(str(random.randint(100, 200))+',')
# copy fiel


def _get_file(name):
    with open(name, 'r') as rf:
        while True:
            _line = rf.readline()
            if _line != '':
                yield _line
            else:
                break


def _copy_file(target_name, name):
    with open(target_name, 'w', encoding='utf-8') as wf:
        for line in _get_file(name):
            wf.write(line)
        # wf.seek(1, 2)非二进制数据不能使用seek移位
        wf.seek(0, 0)
        wf.write('什么情况 this is transcript from '+name.split('.')[0]+':')

_copy_file('target.text', 'test.txt')