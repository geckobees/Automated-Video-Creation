import os
from tkinter import PROJECTING
import ffmpeg, random, gtts

def create_audio(text, language, slow, output_file):
    if os.path.exists(output_file):
        os.remove(output_file)
    tts = gtts.gTTS(text=text, lang=language, slow=slow)
    output = output_file + ".mp3"

    tts.save(output)

    return output

def create_story(input_story):

    story = input_story

    return story


def trim(in_file, out_file, audio, start, end):
    if os.path.exists(out_file):
        os.remove(out_file)

    in_file_probe_result = ffmpeg.probe(in_file)
    in_file_duration = in_file_probe_result.get(
        "format", {}).get("duration", None)
    print(in_file_duration)

    input = ffmpeg.input(in_file)

    pts = "PTS-STARTPTS"
    video = input.trim(start=start, end=end).setpts(pts)

    audio = ffmpeg.input(audio)
    video_and_audio = ffmpeg.concat(video, audio, v=1, a=1)
    output = ffmpeg.output(video_and_audio, out_file, format="mp4")
    output.run()

    out_file_probe_result = ffmpeg.probe(out_file)
    out_file_duration = out_file_probe_result.get(
        "format", {}).get("duration", None)
    print(out_file_duration)


_story = input("Enter Story: ")


story = create_story(_story)

audio = create_audio(story, "en", False, "blicky")
rand = random.randint(0, 480)
# The example here is using a relative path to movie.mp4
trim("input.mp4", "out.mp4", audio, rand, rand + 80)