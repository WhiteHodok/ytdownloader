import pytube

'''
For personal using only, need to install pytube.
'''

link = 'link oy Yt video'
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()