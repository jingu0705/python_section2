import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as dw

imgUrl ="http://post.phinf.naver.net/MjAxNzExMTZfODQg/MDAxNTEwODI5MTI1NzQ4.flgQJ8ApZ6ceM47egkwYt4dFynPw1cSsl-teMLlgwUkg.NZIBFNwgIYvaX7H37lhPfMCjjiUf4bPIu1KGfaeJBCkg.PNG/Im9H6oSo4BMEOGymm_qUxE6cofrA.jpg"
htmlURL ="http://google.com"

savePath1 ="c:/test1.jpg"
savePath2 ="c:/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
