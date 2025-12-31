import random
import math

def random_seq(q: float):
    length = 10**5
    if not (0.0 < q < 1.0):
        raise ValueError("q Out of Range")
    else:
        seq = [1 if random.random() < q else 0 for _ in range(length)]
    str_seq = ''.join(map(str, seq))
    return str_seq

def enc_lz78(code):
    dictionary = []
    rst = []
    word = ""
    num = 0
    chk = 0
    for i in code:
        word = word + i
        if word in dictionary:
            num = dictionary.index(word)
            chk = 1 
        else:
            dictionary.append(word)
            if chk == 0:
                rst.append((num,i))
            else:
                rst.append((num + 1,i))
            word = ""
            num = 0
            chk = 0
    if word != "":
        rst.append((dictionary.index(word) + 1, ''))
    c = len(rst)
    R_c = c * (math.log2(c) + 1) / len(code)
    return (rst, R_c)

def dec_lz78(lst):
    rst = ""
    dictionary = []
    for i in range(len(lst)):
        if lst[i][0] == 0:
            rst = rst + lst[i][1]
            dictionary.append(lst[i][1])
        else:
            word = dictionary[lst[i][0] - 1] + lst[i][1]
            rst = rst + word
            dictionary.append(word)
    return rst

random_code = random_seq(0.5)
enc_lst = enc_lz78(random_code)
print(random_code)
print(enc_lst)
print(dec_lz78(enc_lst[0]))