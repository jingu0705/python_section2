import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as dw

imgUrl ="https://ssl.pstatic.net/tveta/libs/1218/1218517/49d61f269ebf8f78dfe3_20190305182448600.jpg"
htmlURL ="http://google.com"

savePath1 ="c:/test1.jpg"
savePath2 ="c:/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb') # w : write, r: read , a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    savePath2.write(f2)

print("다운로드 완료!")
