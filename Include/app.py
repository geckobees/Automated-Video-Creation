import os
from tkinter import PROJECTING
import ffmpeg, random, gtts, pysrt
from pydub import AudioSegment
import speech_recognition as sr
from google.cloud import speech
import assemblyai as aai
import subprocess


aai.settings.api_key = "e3a5f4dce2e945de8510fde3e428d141"
audio_length = 0



def create_audio(text, language, slow, output_file, speed):
    if os.path.exists(output_file):
        os.remove(output_file)
    
    # Create TTS audio in MP3 format
    tts = gtts.gTTS(text=text, lang=language, slow=slow)
    mp3_output = output_file + ".mp3"
    tts.save(mp3_output)

    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(mp3_output)
    fast_audio = audio.speedup(playback_speed = speed)
    wav_output = output_file + ".wav"
    fast_audio.export(wav_output, format="wav")

    return wav_output  # Return WAV file path


def create_story(input_story):

    story = input_story

    return story


def trim(in_file, out_file, audio_file, start, end):
    if os.path.exists(out_file):
        os.remove(out_file)


    video_input = ffmpeg.input(in_file)
    audio_input = ffmpeg.input(audio_file)


    pts = "PTS-STARTPTS"
    video = video_input.trim(start=start, end=end).setpts(pts)

    video_and_audio = ffmpeg.concat(video, audio_input, v=1, a=1).node


    video_stream = video_and_audio[0]  # Video stream
    audio_stream = video_and_audio[1]  # Audio stream

    output = ffmpeg.output(video_stream, audio_stream, out_file, format="mp4")
    output.run()


    out_file_probe_result = ffmpeg.probe(out_file)
    out_file_duration = out_file_probe_result.get("format", {}).get("duration", None)
    print(out_file_duration)
    
    return output

def resize_video(input_file, output_file, width, height, x, y):
    command = [
        'ffmpeg',
        '-i', input_file,  # Input video file
        '-vf', f"crop={width}:{height}:{x}:{y}",
        output_file         
    ]

    try:
        subprocess.run(command, check=True)
        print(f'Subtitles added successfully to {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred: {e}')


def add_styled_subtitles(input_file, subtitle_file, output_file):
    # Construct the FFmpeg command with subtitles
    command = [
        'ffmpeg',
        '-i', input_file,  # Input video file
        '-vf', f"subtitles={subtitle_file}:force_style='Allignment=0,MarginV=90,MarginL=0,FontSize=16,PrimaryColour=&HFFFFFF&'", 
        '-c:a', 'copy',
        output_file         
    ]

    try:
        subprocess.run(command, check=True)
        print(f'Subtitles added successfully to {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred: {e}')



def transcribe_audio(audio_file, srt_file):

    transcript = aai.Transcriber().transcribe(audio_file)

    subs = transcript.export_subtitles_srt()

    with open('out.srt', 'w') as file:
        file.write(subs)

    return srt_file



def main():
    _story = input("Enter Story: ")

    story = create_story(_story)

    audio = create_audio(story, "en", False, "blicky", 1.2) # .wav
    transcript = transcribe_audio(audio, "out.srt")


    if transcript:

        _audio = AudioSegment.from_file(audio)
        audio_length = len(_audio) / 1000

        rand = random.randint(0, 480)
        out = trim("input.mp4", "out.mp4", audio, rand, rand + audio_length)

        resize_video("out.mp4", "scaled.mp4", 540, 1080, 730, 1080 // 2)

        add_styled_subtitles("scaled.mp4", "out.srt", "output.mp4")

        # Clean up intermediate files
        os.remove(audio)  
        os.remove("blicky.mp3")
        os.remove("out.mp4")
        os.remove("scaled.mp4")
    else:
        print("Transcription failed.")


main()


