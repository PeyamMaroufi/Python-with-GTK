#-------------------------------------------------------------------------------
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (C) 2019 Payam Maroufi
#-------------------------------------------------------------------------------
from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DownloadError, MaxDownloadsReached
import sys
import getpass


class YouTubeDLR:
    def __init__(self, url):
        # # Get information about video
        # Get the name of the video
        # Get available video qualities
        # Check if the video or music is downloadable. Copyright shit
        # Return the downloading process in percent
        self.isitOkToDownload = True
    # Getting youtube information
    def get_information(self, url):
        self.quality_list = []
        self.quality_list.append([])
        self.quality_list.append([])
        ydl_opts = {
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                x = ydl.extract_info(url, download=False)
                self.title = x['title']
                formats = x.get('formats', [x])
                for f in formats:
                    print(f)
                    z = f['format']
                    i = z[z.index("(") + 1:z.index(")")]
                    d = z[0:z.index("-") - 1]
                    # Check if the first char is a digit. to get rid of all
                    # unwanted qualitys and format
                    if i[0].isdigit():
                        self.quality_list[0].append(d)
                        self.quality_list[1].append(i)
                    y = True
                    # Removing the doublicated
                quality_list_refined = []
                quality_list_refined.append([])
                quality_list_refined.append([])

                for q in self.quality_list[1]:
                    if q  not in quality_list_refined[1]:
                        quality_list_refined[1].append(q)
                        # Finding the corresponding format code
                        quality_list_refined[0].append(self.quality_list[0][self.quality_list[1].index(q)])

                quality_list_refined.append(self.title)
                self.isitOkToDownload = True
                return quality_list_refined, y
            except DownloadError:
                y = False
                x = "NOT A VALID LINK"
                self.isitOkToDownload = False
                return x, y


    def get_audio(self, audio_url):
        x = getpass.getuser()
        if self.isitOkToDownload:
            print(audio_url)
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '/home/'+x+'/Downloads/%(title)s.%(format)s'
                }
            print(ydl_opts)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([audio_url])




    def get_video(self, video_url, format_codes, quality_list):
        x = getpass.getuser()
        if self.isitOkToDownload:
            i = 0
            for q in format_codes:
                print(q)
                print(video_url)
                ydl_opts = {
                        'format': q + '+bestaudio/best',
                        'outtmpl':'/home/'+x+'/Downloads/%(id)s-' + quality_list[i],
                            }
                print(ydl_opts)
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
                i = i + 1


