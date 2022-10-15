import youtube_dl
import wget
class Downloader():
    def __init__(self, link):

        with youtube_dl.YoutubeDL() as ydl:
           self.info = ydl.extract_info(link, download = False)
           self.vid_title = self.info['title'].title()
           self.uploader = self.info['uploader'].title()
           self.views = self.info['view_count']
           self.thumbnail = self.info['thumbnail']
           self.thumbs_dict = [elements for elements in self.info['thumbnails']]
           self.thumbs = []
           self.res = []
           for th in self.thumbs_dict:
               for key, value in th.items():
                   if key == 'url':
                       self.thumbs.append(wget.download(value,'./assets', bar=None))

            for r in slef.thumbs_dict:
                for key,value in r.items():
                    if key == 'resolution':
                        self.res.append(value)
    

    
