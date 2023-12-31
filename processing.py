import os
import subprocess
import glob

def read_srt_file(srt_file):
    with open(srt_file, 'r', encoding='utf8') as f:
        srt_content = f.read()
    return srt_content

def split_audio_by_srt(audio_file, srt_file, output_dir, index):
    srt_content = read_srt_file(srt_file)
    srt_lines = srt_content.strip().split('\n\n')
    
    basename = os.path.basename(srt_file).split("_")
    character_name = basename[0]
    lang = basename[1]

    for i, srt_line in enumerate(srt_lines):
        parts = srt_line.split('\n')
        start_time, end_time = parts[1].split(' --> ')
        start_time = convert_time_format(start_time)
        end_time = convert_time_format(end_time)

        output_file = os.path.join(output_dir, f"{index}_{i}.wav")
        global txtLabel
        txtLabel = txtLabel + f"{index}_{i}.wav|{character_name}|{lang}|{parts[2]}\n"
        
        subprocess.call(['ffmpeg', '-i', audio_file, '-ss', start_time, '-to', end_time, '-ac', '1', output_file])

def convert_time_format(time_str):
    h, m, s = time_str.split(':')
    s, ms = s.split(',')
    return f"{int(h)*3600 + int(m)*60 + int(s)}.{ms}"

# 使用相對路徑取得腳本所在的資料夾
script_dir = os.path.dirname(os.path.abspath(__file__))
audio_dir = os.path.join(script_dir, "audio")
srt_dir = os.path.join(script_dir, "srt")
output_dir = os.path.join(script_dir, "raw")
txtLabel = ""

# 使用 glob.glob 來取得符合條件的檔案清單
audios = glob.glob(os.path.join(audio_dir, "*.wav"))
srts = glob.glob(os.path.join(srt_dir, "*.srt"))

for i in audios:
    print(i)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(0, len(audios)):
    split_audio_by_srt(audios[i], srts[i], output_dir, i+1)

with open(".\\esd.list", 'w', encoding="utf8") as fr:
    fr.writelines(txtLabel)
