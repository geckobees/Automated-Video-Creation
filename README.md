# Automated Video Creation

This project is a Python script that automatically generates short videos with AI-narrated stories, using a background video of your choice. It leverages several libraries to generate a story, convert it to audio, transcribe the audio, and combine it with a background video.

## How it Works

1.  **Story Generation:** The script uses OpenAI's GPT-3.5-turbo model to generate a short, suspenseful story about fantasy and magic.
2.  **Text-to-Speech:** The generated story is converted to audio using Google Text-to-Speech (gTTS).
3.  **Audio Transcription:** The audio is transcribed into text using AssemblyAI, generating an SRT file for subtitles.
4.  **Video Processing:**
    *   A background video is trimmed to match the length of the generated audio.
    *   The trimmed video is resized to a vertical format (540x1080).
    *   The generated subtitles are added to the video.
5.  **GUI:** The `gui.py` script is used to launch the graphical user interface.
6.  **Output:** The final video is saved as an MP4 file.

## Dependencies

*   `assemblyai`: For audio transcription.
*   `openai`: For generating the story.
*   `pydub`: For audio manipulation.
*   `ffmpeg`: For video processing.
*   `gtts`: For text-to-speech conversion.

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install assemblyai openai pydub ffmpeg-python gtts
    ```
2.  **Set API Keys:**
    *   Replace `"your assemblyai key here"` in `reddit_stories.py` with your AssemblyAI API key.
    *   Replace `"your openai api key here"` in `reddit_stories.py` with your OpenAI API key.
3.  **Background Video:** Place a background video named `background.mp4` in the same directory as the script.

## Notes

*   The script generates a random start point for the background video.
*   The output videos are in a vertical format suitable for platforms like TikTok or Instagram Reels.
*   This project is intended for fun and may be updated in the future.
*   The GUI is not fully working
*   Feel free to replace the gTTS voice with an elevenlabs voice
