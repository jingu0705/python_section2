import pytube
import os
import subprocess


#다운 받을 동영상 URL 지정
yt = pytube.YouTube("https://www.youtube.com/watch?v=9HSU6iEJYqM")
videos = yt.streams.all()

#print('videos',videos)

for i in range(len(videos)): #range(1,6) 1,2,3,4,5, range(6) 0,1,2,3,4,5
    print(i, ',', videos[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

down_dir = "C:\youtube"

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, newFileName),
])

print("동영상 다운로드 및 mp3 변환 완료!")
