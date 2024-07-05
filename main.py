# import pandas as pd
# from gtts import gTTS
# from moviepy.editor import concatenate_audioclips, AudioFileClip, AudioClip
# import os
#
# # Load the Excel file
# df = pd.read_excel('C:\\Users\\vsuva\\Desktop\\cyber_definitions.xlsx')
#
# # Create the output directory if it doesn't exist
# output_dir = "cyber_audio"
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
#
# # Function to convert text to speech and save as an audio file
# def text_to_speech(text, filename):
#     tts = gTTS(text=text, lang='en')
#     tts.save(filename)
#
#
# # Process each row and generate audio files
# for index, row in df.iterrows():
#     topic = row['TOPIC']
#     definition = row['Definition']
#
#     # Generate topic audio
#     topic_filename = os.path.join(output_dir, f"{topic}_topic.mp3")
#     text_to_speech(topic, topic_filename)
#
#     # Generate definition audio
#     definition_filename = os.path.join(output_dir, f"{topic}_definition.mp3")
#     text_to_speech(definition, definition_filename)
#
#     # Load the audio files using moviepy
#     topic_audio = AudioFileClip(topic_filename)
#     definition_audio = AudioFileClip(definition_filename)
#
#     # Concatenate topic and definition without a pause
#     final_audio = concatenate_audioclips([topic_audio, definition_audio])
#
#     # Export the final audio file
#     final_audio_filename = os.path.join(output_dir, f"{topic}.mp3")
#     final_audio.write_audiofile(final_audio_filename, codec='mp3')
#
#     # Clean up intermediate files
#     topic_audio.close()
#     definition_audio.close()
#     os.remove(topic_filename)
#     os.remove(definition_filename)
#
# print("Audio files generated successfully in the 'cyber_audio' folder!")
import pandas as pd
from gtts import gTTS
from moviepy.editor import concatenate_audioclips, AudioFileClip
import os
import math

# Load the Excel file
df = pd.read_excel('C:\\Users\\vsuva\\Desktop\\tech_first_50.xlsx')

# Create the output directory if it doesn't exist
output_dir = "tech_first_50_audio"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Function to convert text to speech and save as an audio file
def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)


# Function to calculate duration in seconds
def get_audio_duration(audio_clip):
    return round(audio_clip.duration)


# Initialize counters for different durations
duration_counts = {}

# Process each row and generate audio files
for index, row in df.iterrows():
    topic = row['Topic']
    definition = row['Definition']

    # Generate topic audio
    topic_filename = os.path.join(output_dir, f"{topic}_topic.mp3")
    text_to_speech(topic, topic_filename)

    # Generate definition audio
    definition_filename = os.path.join(output_dir, f"{topic}_definition.mp3")
    text_to_speech(definition, definition_filename)

    # Load the audio files using moviepy
    topic_audio = AudioFileClip(topic_filename)
    definition_audio = AudioFileClip(definition_filename)

    # Concatenate topic, definition, and subscription message
    subscribe_message = "Subscribe for more"
    subscribe_audio = gTTS(text=subscribe_message, lang='en')
    subscribe_audio_filename = os.path.join(output_dir, f"{topic}_subscribe.mp3")
    subscribe_audio.save(subscribe_audio_filename)
    subscribe_audio_clip = AudioFileClip(subscribe_audio_filename)

    final_audio = concatenate_audioclips([topic_audio, definition_audio, subscribe_audio_clip])

    # Export the final audio file
    final_audio_filename = os.path.join(output_dir, f"{topic}.mp3")
    final_audio.write_audiofile(final_audio_filename, codec='mp3')

    # Calculate duration
    audio_duration = get_audio_duration(final_audio)
    duration_label = f"{audio_duration}s"

    # Update duration counts
    if duration_label in duration_counts:
        duration_counts[duration_label] += 1
    else:
        duration_counts[duration_label] = 1

    # Clean up intermediate files
    topic_audio.close()
    definition_audio.close()
    subscribe_audio_clip.close()
    os.remove(topic_filename)
    os.remove(definition_filename)
    os.remove(subscribe_audio_filename)

print("Audio files generated successfully in the 'cyber_audio' folder!")

# Calculate and print average audio length
total_duration = sum(int(label[:-1]) * count for label, count in duration_counts.items())
total_count = sum(duration_counts.values())
average_length = total_duration / total_count if total_count > 0 else 0

print(f"Average audio length: {average_length:.1f} seconds")

# Print duration counts
print("Duration counts:")
for label, count in duration_counts.items():
    print(f"{label}: {count}")
