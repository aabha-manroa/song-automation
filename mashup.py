from moviepy.editor import AudioFileClip, concatenate_audioclips
import os
import logging

# Set up logging
logging.basicConfig(filename='mashup_log.txt', level=logging.INFO, encoding='utf-8')

folder_path = r'C:\Users\DELL\OneDrive\Documents\songs automation\songdwl'
output_file = r'C:\Users\DELL\OneDrive\Documents\songs automation\mashup.webm'  # Output file

# List to hold audio clips
audio_clips = []

# Scan the folder for webm files
for filename in os.listdir(folder_path):
    if filename.lower().endswith('.webm'):
        full_path = os.path.join(folder_path, filename)
        logging.info(f"Found: {full_path}")  # Log the found file path
        try:
            audio_clip = AudioFileClip(full_path)
            audio_clips.append(audio_clip)  # Add audio clip
        except Exception as e:
            logging.error(f"Error adding file {full_path}: {e}")

# Check if we found any audio clips
if not audio_clips:
    logging.info("No audio files found in the specified folder.")
else:
    # Concatenate the audio clips
    mashup = concatenate_audioclips(audio_clips)
    # Save the output as a different format if .webm continues to cause issues
    output_format = 'mp3'  # Change the output format to mp3
    output_file_mp3 = output_file.replace('.webm', f'.{output_format}')
    mashup.write_audiofile(output_file_mp3)  # Output as mp3 audio
    logging.info("Mashup created successfully!")

print("Log written to mashup_log.txt. Check it for details.")

