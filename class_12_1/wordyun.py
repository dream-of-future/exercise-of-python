import jieba
import wordcloud
import numpy as np
from hm_3__threekingdoms import wdcd_list
from PIL import Image
print(wdcd_list)

img = Image.open(r'C:\Users\90903\Desktop\图片1.png') #打开图片
img_array = np.array(img)

txt=" ".join(wdcd_list)     #使用空格拼接获得字符串

wd = wordcloud.WordCloud(background_color='white',
    width=1000,
    height=800,
    mask=img_array, #设置背景图片
    font_path=r'C:\Windows\Fonts\FZSTK.TTF'
    )


wd.generate(txt)  # 由txt文本生成词云
wd.to_file("sample.png")  # 将词云图保存为名为sample的文件