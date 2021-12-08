#pip install moviepy | pip install ffmpeg | Converte Video em Audio

import moviepy.editor as mp 

video = mp.VideoFileClip("nomeDoVideo.mp4")
video.audio.write_audiofile("nomeDoVideoConvertidoEmAudio.mp3")