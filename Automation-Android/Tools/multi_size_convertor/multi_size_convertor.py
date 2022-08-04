import subprocess
import os

input_file = '/Users/xin.xu/Downloads/output-av1.mkv'

target_sizes = [   
    [128, 96, 'sqcif'],
    [160, 120, 'qqvga'],
    [176, 144, 'qcif'],
    [240, 160, 'hqvga'],
    [320, 200, 'cga'],
    [320, 240, 'qvga'],
    [352, 240, 'qntsc'],
    [400, 240, 'wqvga'],
    [432, 240, 'fwqvga'],
    [352, 288, 'qpal'],
    [480, 320, 'hvga'],
    [640, 350, 'ega'],
    [640, 360, 'nhd'],
    [640, 480, 'sntsc'],
    [720, 480, 'ntsc'],
    [852, 480, 'wvga'],
    [960, 540, 'qhd'],
    [704, 576, '4cif'],
    [720, 576, 'pal'],
    [768, 576, 'spal'],
    [800, 600, 'svga'],
    [1280, 720, 'hd720'],
    [1024, 768, 'xga'],
    [1366, 768, 'wxga'],
    [2048, 858, '2kscope'],
    [1280, 1024, 'sxga'],
    [1600, 1024, 'wsxga'],
    [1920, 1080, 'hd1080'],
    [1998, 1080, '2kflat'],
    [2048, 1080, '2k'],
    [1408, 1152, '16cif'],
    [1600, 1200, 'uxga'],
    [1920, 1200, 'wuxga'],
    [2048, 1536, 'qxga'],
    [2560, 1600, 'woxga'],
    [2560, 2048, 'qsxga'],
    [3200, 2048, 'wqsxga'],
    [3840, 2160, 'uhd2160'],
    [3996, 2160, '4kscope'],
    [4096, 2160, '4k'],
    [3840, 2400, 'wquxga'],
    [5120, 4096, 'hsxga'],
    [6400, 4096, 'whsxga'],
    [7680, 4320, 'uhd4320'],
    [7680, 4800, 'whuxga']
]

for size in target_sizes:
    lenth = size[0]
    height = size[1]
    format_name = size[2]
    # cmd = 'ffmpeg -i {0} -s {1}x{2} -color_range pc yuv444p-pc-{1}x{2}-{3}.mkv'.format(input_file, lenth, height, format_name)
    cmd = 'ffmpeg -i {0} -s {1}x{2} -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental av1-{1}x{2}-{3}.mkv'.format(input_file, lenth, height, format_name)
    os.system(cmd)
    





