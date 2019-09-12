import os, requests
import time
import pygame
from bs4 import BeautifulSoup
import tkinter
import urllib.parse

def play_song(filepath, m, root):
    # names = os.listdir()
    names = filepath.split("/")
    item = names[-1]
    if (item[-3:]) == 'mp3':
        songname = item
    print(songname)
    songname.replace("&","")

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(songname)

    pygame.mixer.music.play(0)
    start = time.time()
    print(songname)
    base = "https://www.rentanadviser.com/en/subtitles/subtitles4songs.aspx?src=" + urllib.parse.quote(songname)

    print(base)
    # print(base)
    def make_soup(url):
        try:
            html = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
        except:
            return None
        return BeautifulSoup(html, "html.parser")

    soup = make_soup(base)
    table = (soup.find("div", {"id": "tablecontainer"}))
    links = table.find_all('a')

    storelinks = []
    for item in links:
        storelinks.append(item.get('href'))  # item.text.strip())

    print(storelinks[0])
    # To choose -
    linktochoose = storelinks[0]
    srcbase = "https://www.rentanadviser.com/en/subtitles/"
    srcbase += linktochoose
    print(srcbase)

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

        return float((mins * 60) + spl[1])

    for item in divide:
        spl = item.split("]")
        tup = (timetosec(spl[0]), spl[1])
        finaltimestamps.append(tup)

    end = time.time()
    taken = end - start
    print(taken)
    while finaltimestamps[0][0] < taken:
        del finaltimestamps[0]
    print(finaltimestamps[0][0])
    print((finaltimestamps[0][0]) - taken)
    syncfactor = 6
    time.sleep((finaltimestamps[0][0]) - taken)
    print(finaltimestamps[0][1])

    print("I am here 2")

    for i in range(1, len(finaltimestamps)):
        time.sleep(finaltimestamps[i][0] - finaltimestamps[i - 1][0])
        print(finaltimestamps[i][0], finaltimestamps[i][1])
        m.config(text = finaltimestamps[i][1])
        root.update()








    
