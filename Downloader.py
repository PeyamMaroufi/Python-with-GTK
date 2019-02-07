#-------------------------------------------------------------------------------
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright 2019 Payam Maroufi
#-------------------------------------------------------------------------------
from pytube import YouTube
import os

path_adress=[]
class YouTubeDL:
    
    def __init__(self):
        pass
    
    def set_path(self, path):
        path_adress = path
        
    def videoYoutube(self, videoUrl):
        video_downloader = YouTube(videoUrl)
        video_downloader = video_downloader.streams.filter(progressive=True, file_extension='mp4')
        
        if not os.path.exists(path_adress):
            os.makedirs(path_adress)
        video_downloader.download(path_adress)
        
