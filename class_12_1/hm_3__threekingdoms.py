import info
import jieba   # 中文分词库
import copy
index1 = 10  # 词频数
index2 = 5  # 人名数

def sort1(x):
    if len(x[0]) == 1 or len(x[0]) >= 4:
        return 0
    else:
        return x[1]


def sort2(x):
    from test import family_name_list
    if len(x[0]) == 1 or len(x[0]) >= 4:
        return 0
    elif x[0][0] not in family_name_list:
        return 0
    else:
        return x[1]

sort_key = sort1  # 排序方式

txt = open(r"C:\Users\90903\Desktop\red_dream.txt", "r", encoding="utf-8").read()  # 得到所有文本组成的字符串
words = jieba.lcut(txt)

new_words = set(words)
# print(new_words)
remove_list = ['，', '．', '：', ' ', '“', '。', '”', ':', ';', '：', '；', '！', '？', '\n', '"', '-', '`', '、']
for i in remove_list:
    new_words.discard(i)

word_list = list(new_words)
lenth1 = len(words)
lenth2 = len(word_list)

zero = [0 for i in range(lenth2)]
dic = dict(zip(new_words,zero))
for i in words:
    try:
        dic[i] += 1
    except KeyError:
        pass

new_arr = sorted(dic.items(),key=sort_key, reverse=True)
ret_list = list(new_arr[0:100])

wdcd_list = copy.deepcopy(ret_list)  # 为wordyun.py做铺垫
for i in range(len(wdcd_list)):
    wdcd_list[i] = wdcd_list[i][0]

# print(wdcd_list)

def print_top10_words(idx = index2, list1 = ret_list):
    '''
    :param idx: 控制输出词语个数
    :param list1: 输出词来源（list）
    :return: None
    '''
    for i in range(0, idx):
        for j in [0, 1]:
            print(list1[i][j], end=' ')
        print('\n', end='')


if __name__ == '__main__':
    print_top10_words()
