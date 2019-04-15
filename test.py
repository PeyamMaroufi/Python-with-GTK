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
#         get_information()
        get_information()
        get_audio()
    # Getting youtube information
def get_information():
    quality_list = []
    quality_list.append([])
    quality_list.append([])
    
    ydl_opts = {
                    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        x = ydl.extract_info("https://www.youtube.com/watch?v=y7ThbUlPdrg", download=False)
        title = x['title']
        formats = x.get('formats', [x])
        formatss = x.get('ext', [x])
        print(formatss)
        for f in formats:
            z = f['format']
            print(f)
            i = z[z.index("(") + 1:z.index(")")]
            d = z[0:z.index("-") - 1]
            # Check if the first char is a digit. to get rid of all 
            # unwanted qualitys and format
            if i[0].isdigit():
                quality_list[0].append(d)
                quality_list[1].append(i)
    # Removing the doublicated
    quality_list_refined = []
    quality_list_refined.append([])
    quality_list_refined.append([])
    
    for q in quality_list[1]:
        if q  not in quality_list_refined[1]:
            quality_list_refined[1].append(q)
            # Finding the corresponding format code
            quality_list_refined[0].append(quality_list[0][quality_list[1].index(q)]) 
                
    quality_list_refined.append(title)
    print(quality_list_refined[0])
    print(quality_list_refined[1])
    print(quality_list_refined[2])
                    
            
                

    # Get the title 
def get_title(title):
        print(title)
    
def get_qualities(quality):
    quality_list_refined = []
    for q in quality:
        if q  not in quality_list_refined:
            quality_list_refined.append(q)
    return quality_list_refined
        
def get_audio():
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(format)s'
                }
            print(ydl_opts)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?v=668nUCeBHyY'])

def get_video():
    pass
#     format_code = ['144', '240p']
#     for q in format_code:
#         ydl_opts = {
#                     'format': q + '/bestaudio/best',
#                     'outtmpl': '%(id)s-' + q,  # name the file the ID of the video 
#                     
#                     
#                         }
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download(['https://www.youtube.com/watch?v=668nUCeBHyY'])
#         
    
if __name__ == "__main__":
    main()



