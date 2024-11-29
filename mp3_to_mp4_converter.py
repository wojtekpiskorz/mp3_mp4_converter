import os
import moviepy.config as config
from moviepy.editor import AudioFileClip, VideoFileClip

# Set the path to the FFmpeg executable
config.change_settings({"FFMPEG_BINARY": "/opt/homebrew/bin/ffmpeg"})

def convert_mp3_to_mp4(input_path, output_path):
    # Load the audio file
    audio = AudioFileClip(input_path)
    
    # Create a black video clip with the same duration as the audio
    video = VideoFileClip("black.mp4").subclip(0, audio.duration)
    
    # Set the audio of the video clip
    final_clip = video.set_audio(audio)
    
    # Write the result to a file
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    
    # Close the clips to free up system resources
    audio.close()
    video.close()
    final_clip.close()

# Create a short black video file if it doesn't exist
if not os.path.exists("black.mp4"):
    from moviepy.editor import ColorClip
    ColorClip(size=(640, 480), color=(0,0,0), duration=1).write_videofile("black.mp4", fps=1)

input_dir = "/Users/woji/Dev/python/mp3_mp4_converter/input"
output_dir = "/Users/woji/Dev/python/mp3_mp4_converter/output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith(".mp3"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace(".mp3", ".mp4"))
        print(f"Converting {filename}...")
        convert_mp3_to_mp4(input_path, output_path)

print("Conversion complete!")