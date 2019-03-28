#-------------------------------------------------------------------------------
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (C) 2019 Payam Maroufi
#-------------------------------------------------------------------------------
from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DownloadError
import sys


class YouTubeDLR:
    quality_list = []
    title = ""
    def __init__(self, url):
        # # Get information about video
        # Get the name of the video
        # Get available video qualities
        # Check if the video or music is downloadable. Copyright shit
        # Return the downloading process in percent
        pass
        
    # Getting youtube information
    def get_information(self, url):
        self.quality_list= []
        ydl_opts = {
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            x = ydl.extract_info(url, download=False)
            title = x['title']
            formats = x.get('formats', [x])
            for f in formats:
                z = f['format']
                i = z[z.index("(") + 1:z.index(")")]
                # Check if the first char is a digit. to get rid of all 
                # unwanted qualitys and format
                if i[0].isdigit():
                    self.quality_list.append(i)
                    
        # Removing the doublicated
        quality_list_refined = []
        for q in self.quality_list:
            if q  not in quality_list_refined:
                quality_list_refined.append(q)
                
        quality_list_refined.append(title)

        return quality_list_refined
                
                

    # Get the title 
    def get_title(self):
        return self.title
    

    
    
    def get_audio(self, audio_url):

        pass

    def get_video(self, video_url):
        pass



