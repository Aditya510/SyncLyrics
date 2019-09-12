# SyncLyrics

We use a python crawler to fetch the lyrics from https://www.rentanadviser.com/en/subtitles/subtitles4songs.aspx  
This site has a collection of 17346 songs lyrics  
Some songs are repeated like for a song you can get a youtube video lyrics and some specific mp3 lyrics

## Starting

```bash
pip3 install BeautifulSoup4
pip3 install pygame
pip3 install tkinter

python tkinter_sample.py
```

Then select the mp3 file preferable downloaded from a youtube video

## 
- We use **Pygame** to play songs
- We use **tkinter** for UI (is independent of OS)
- **BeautifulSoup** is used to crawl https://rentanadviser.com

## Current Limitations
- **Pygame:** Only able to play mp3 downloaded from youtube videos, fails to play most of the mp3s
- **Rentanadviser search is not good:** Results are not well ordered like more relevant results are not the first one, but we are choosing first one
- **No Lyrics for songs not on Rentanadviser:** Rentanadviser songs library is very limited