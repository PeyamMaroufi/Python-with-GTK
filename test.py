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
    quality_list=[]
    ydl_opts = {
                    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        x = ydl.extract_info("https://www.youtube.com/watch?v=y7ThbUlPdrg", download=False)
        title = x['title']
        formats = x.get('formats', [x])
        for f in formats:
            z = f['format']
            i = z[z.index("(") + 1:z.index(")")]
            # Check if the first char is a digit. to get rid of all 
            # unwanted qualitys and format
            if i[0].isdigit():
                quality_list.append(i)
        # Removing the doublicated
    quality_list_refined = []
    for q in quality_list:
        if q  not in quality_list_refined:
            quality_list_refined.append(q)
                
    quality_list_refined.append(title)
    print(quality_list_refined)
                    
            
                

    # Get the title 
def get_title(title):
        print(title)
    
def get_qualities(quality):
    quality_list_refined = []
    for q in quality:
        if q  not in quality_list_refined:
            quality_list_refined.append(q)
    return quality_list_refined
        
def get_audio(self, audio_url):

        pass

def get_video(self, video_url):
        pass
    
if __name__ == "__main__":
    main()



