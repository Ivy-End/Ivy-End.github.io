import os

img = os.listdir('./')  # 列出文件夹下所有的目录与文件
for i in range(0, len(img)):
    print ('![' + img[i][ : -4] + ']({{site.paths.image}}2015/' + img[i][ : -4] + '.png "' + img[i][ : -4] + '")')
