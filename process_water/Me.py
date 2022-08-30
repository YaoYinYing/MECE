import pandas as pd
import numpy as np

with open(r'E:\壳聚糖酶\gradcam\c1754.pro.align') as file:
    line = file.readlines()
id = [i.strip('\n').split()[0][1:].split('.')[0] for i in line[::2]][1:]
seq = [i.strip('\n') for i in line[1::2]][1:]
# print(id)
# print(seq)
id_xin = []
seq_xin = []

dict_id_seq = dict(zip(id, seq))
# dict_id_seq = dict(zip(id_xin, seq_xin))
# print(dict_id_seq)

with open(r"E:\壳聚糖酶\gradcam\1754blastdb90-xin.txt") as file2:
    line2 = file2.readlines()
id2 = [i.strip('\n').split()[0][1:].split('.')[0] for i in line2[::2]][1:]
seq2 = [i.strip('\n') for i in line2[1::2]][1:]
# print(id2)
# print(seq2)
dict_id_seq2 = dict(zip(id2, seq2))
print(dict_id_seq2)

# url = r'E:\壳聚糖酶\gradcam\csv-18\\'
# url_xin = r'E:\壳聚糖酶\gradcam\\'
a = '46'
p_xin = []
for key, value in dict_id_seq.items():
    # print(key)
    # print(value)

    url2 = r"E:\壳聚糖酶\deeplift\1754-blast\align\align.%s.1.water" % key
    url3 = r"E:\壳聚糖酶\gradcam\csv-%s\%s_vactor_mean.csv" % (a, key)
    with open(url3) as file3:
        line3 = file3.readlines()[1:-1]
    p = []
    for i in range(len(line3)):
        p.append((dict_id_seq2.get(key)[i], line3[i].strip('\n').split(',')[1:]))
    # print(p)

    with open(url2) as file:
        line = file.readlines()
    xiangxixinxi = []
    for aaa in line:
        if aaa == '\n':
            pass
        elif aaa[0] == '#':
            pass
        else:
            xiangxixinxi.append(aaa)
    number = int(xiangxixinxi[2].split()[1]) - 1 - 1
    temp = []
    # print(p)
    # print('p:%s' % len(p))
    for j in value.strip('\n'):
        tiaojian = True
        while tiaojian:
            # try:
            if j == '-':
                temp.append([np.nan] * 20)
                tiaojian = False
            else:
                number += 1
                # print('id:%s' % key)
                # print('number:%s' % number)
                # # print('i:%s' % i)
                # print(len(p))
                # print('j:%s' % j)
                # print('temp:%s' % len(temp))
                if number < 734:
                    try:
                        h = p[number]
                        if j == h[0]:
                            # print(h[0])

                            hhhh = []
                            for i in h[1]:
                                if i == '0':
                                    hhhh.append(i)
                                else:
                                    hhhh.append('1')
                            print(hhhh)
                            temp.append(hhhh)
                            # temp.append(h[1])
                            # print(h[1])
                            tiaojian = False
                    except IndexError:
                        print('id:%s' % key)
                        print(p)
                        print(len(p))
                        print(number)

                else:
                    temp.append([np.nan] * 20)
                    tiaojian = False
    if len(temp) != 278:
        print('temp')
    # print(len(temp))
    p_xin.append(temp)
# print(p_xin)
p_arr = np.array(p_xin, dtype=float)
print(p_arr.shape)
p_arr = np.nanmean(np.array(p_arr), 0)
df = pd.DataFrame(p_arr)
csv_name = r"E:\壳聚糖酶\gradcam\csv-xin\1754-vactor_mean-duizhao%s.csv" % a
df.to_csv(csv_name)
