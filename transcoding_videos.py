

import subprocess
import ffmpeg
import os

def get_codecs():
    cmd = "ffmpeg -codecs"
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'\n')
    for e in x:
        print(e)


def get_formats():
    cmd = "ffmpeg -formats"
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'\n')
    for e in x:
        print(e)


def convert_any_to_mxf(input_folder):
    
    input_folder =  r"C:/Users/dell/Downloads/transcode_video"
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            print('hhh',file)
            input_path = input_folder + '/' +str(file)
            print(input_path)


    output =r'C:/Users/dell/Downloads/out' + '/' + str()

    cmd = f'ffmpeg -i "{input}" "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)

convert_any_to_mxf(r"C:/Users/dell/Downloads/out/out.mp4")
# def convert_mov_to_seq():
#     input = r"C:\Users\HP\Desktop\FFMPEG\playblast.mov"
#     output = r"C:\Users\HP\Desktop\FFMPEG\v001\car_scene_v001.%03d.png"
#
#     cmd = f'ffmpeg  -i "{input}" "{output}"'
#     print(cmd)
#     subprocess.check_output(cmd, shell=True)
#
#
# def get_thumbnail():
#     input = r"C:\Users\HP\Desktop\FFMPEG\comp.mov"
#     output = r"C:\Users\HP\Desktop\FFMPEG\thumb.png"
#     cmd = f'ffmpeg -i "{input}" -ss 00:00:01.000 -vframes 1  -s 640x360  "{output}"'
#     print(cmd)
#     subprocess.check_output(cmd, shell=True)