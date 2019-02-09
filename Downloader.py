# -------------------------------------------------------------------------------
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright 2019 Payam Maroufi
# -------------------------------------------------------------------------------
import youtube_dl


class YouTubeDLR:

    def __init__(self):
        # # Get information about video
        # Get the name of the video
        # Get available video qualities
        # Check if the video or music is downloadable. Copyright shit
        # Return the downloading process in percent
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3',
                 'preferredquality': '192',
                 },
                {'key': 'FFmpegMetadata'},
            ],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info('https://www.youtube.com/watch?v=PMGV0seQ4sY', download=True)

        print(info_dict)
