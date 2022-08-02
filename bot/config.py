#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = "75"
    API_HASH = "5c9541eefe845"
    BOT_TOKEN = 5534205730:AAGqKRKCrvmG_T37Q-jNUMDHZqmxQc0QYeg"
    DEV = 1322549723
    OWNER = "1164918935"
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i '''{}''' -hide_banner -preset fast -c:v libx265 -vf scale=1280:-2 -x265-params no-info=1 -pix_fmt yuv420p10le -crf 24 -r 23.976 -map 0:v -c:a libopus -b:a 128k -ac 6 -vbr on -map 0:a -c:s copy -map 0:s? '''{}''' -y',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
