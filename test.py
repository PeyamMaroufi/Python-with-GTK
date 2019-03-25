#-------------------------------------------------------------------------------
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (C) 2019 Payam Maroufi
#-------------------------------------------------------------------------------
from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DownloadError


    
def main():
        # # Get information about video
        # Get the name of the video
        # Get available video qualities
        # Check if the video or music is downloadable. Copyright shit
        # Return the downloading process in percent
        get_information()
    # Getting youtube information
def get_information():
        ydl_opts = {
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                x = ydl.extract_info("https://www.youtube.com/watch?v=y7ThbUlPdrg", download=False)
                print(x)
                y = x['title']
                print(y)
                y = x['resolution']
                print(y)

            
                

    # Get the title 
def get_title():
    pass
    
    
def get_audio(self, audio_url):

        pass

def get_video(self, video_url):
        pass
    
if __name__ == "__main__":
    main()



