from moviepy.editor import *

def combine_mp3_files(input_folder, output_file):
    mp3_files = [f for f in os.listdir(input_folder) if f.endswith('.mp3')]

    if not mp3_files:
        print("Error: No MP3 files found in the input folder.")
        return

    audio_clips = [AudioFileClip(os.path.join(input_folder, mp3_file)) for mp3_file in mp3_files]
    combined_audio = concatenate_audioclips(audio_clips)

    combined_audio.write_audiofile(output_file, codec="mp3")

    print(f"Successfully combined {len(mp3_files)} MP3 files into '{output_file}'.")

if __name__ == "__main__":
    input_folder_path = input("Enter the path to your mp3's folder: ")
    output_file_path = input_folder_path + "\merged.mp3"
    print("Proccesing. . .")
    combine_mp3_files(input_folder_path, output_file_path)
    #print("Done. The merge mp3 file was saved in: " + output_file_path)
    print("Press enter key to close the console")
    input()
    
