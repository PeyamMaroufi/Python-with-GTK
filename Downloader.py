#-------------------------------------------------------------------------------
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (C) 2019 Payam Maroufi
#-------------------------------------------------------------------------------
from __future__ import unicode_literals
import youtube_dl

class YouTubeDLR:
    
    def __init__(self, url):
        # # Get information about video
        # Get the name of the video
        # Get available video qualities
        # Check if the video or music is downloadable. Copyright shit
        # Return the downloading process in percent
        self.youtube_url = url
        self.title = self.get_information(self.youtube_url)

    # Getting youtube information
    def get_information(self, url):
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                x = ydl.extract_info(url, download=False)
                y = x['title']
                return y
            except:
                print('Something went wrong')

    # Get the title 
    def get_title(self):
        if self.title is not None:
            return self.title
        else :
            return None
    
    
    def get_audio(self, audio_url):

        pass

    def get_video(self, video_url):
        pass


