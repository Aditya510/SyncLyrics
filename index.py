import os, requests
import time
import pygame
from bs4 import BeautifulSoup
names = os.listdir()
for item in names:
    if (item[-3:]) == 'mp3':
        songname = item
print(songname)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(songname)

pygame.mixer.music.play(0)
start = time.time()
base = "https://www.rentanadviser.com/en/subtitles/subtitles4songs.aspx?src="
for char in songname.split():
    base+= char + '%20'
#print(base)
def make_soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html, "html.parser")

soup = make_soup(base)
table = (soup.find("div", {"id": "tablecontainer"}))
links = table.find_all('a')

storelinks = []
for item in links:
    storelinks.append(item.get('href'))#item.text.strip())


#To choose -
linktochoose = storelinks[1]
srcbase = "https://www.rentanadviser.com/en/subtitles/"
srcbase += storelinks[0]

newsoup = make_soup(srcbase)
newsoup.prettify()
lyrics = newsoup.find("span", {"id": "ctl00_ContentPlaceHolder1_lbllyrics_simple"})
lyricstext = lyrics.text

divide = lyricstext.split("[")
while divide[0][0].isnumeric() == False:
    del divide[0]

finaltimestamps = []


def timetosec(currentstr):
    spl = currentstr.split(":")
    mins = spl[0]
    
    return float((mins*60) + spl[1])


for item in divide:
    spl = item.split("]")
    tup = (timetosec(spl[0]),spl[1])
    finaltimestamps.append(tup)





end = time.time()
taken = end - start
while finaltimestamps[0][0] < taken:
    del finaltimestamps[0]
time.sleep((finaltimestamps[0][0]) - taken)
print(finaltimestamps[0][1])

    
for i in range(1,len(finaltimestamps)):
    
    time.sleep(finaltimestamps[i][0] - finaltimestamps[i-1][0])
    print(finaltimestamps[i][1])

    
    




    
