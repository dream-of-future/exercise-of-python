import ybc_face as face
import ybc_box as box

print(box.__version__)
pic = box.fileopenbox('选择一张你的照片')
res = face.info(pic)
box.msgbox('这张照片的识别结果是：'+ res,pic)