# audio-merger

Python script to combine multiple MP3 files into a single MP3 file. It uses the MoviePy library to achieve this functionality. Here's a breakdown of the script:

1. It imports everything (*) from moviepy.editor. This is a common import style to access all the functions and classes provided by the MoviePy library.

2. The script defines a function called combine_mp3_files, which takes the input_folder (path to the folder containing MP3 files) and output_file (path to the merged output MP3 file) as input arguments.

3. It lists all the files in the input_folder that have a ".mp3" extension using a list comprehension.

4. If there are no MP3 files found in the input folder, it prints an error message and returns from the function.

5. It creates a list of AudioFileClip objects, each corresponding to one of the MP3 files in the input_folder.

6. Using concatenate_audioclips, the script combines the audio clips from different MP3 files into a single combined_audio clip.

7. The combined audio clip is then written to the output_file with the codec set to "mp3".

8. The script prints a success message, indicating the number of MP3 files combined and the name of the output file.

9. In the __main__ block, the script takes the input_folder_path from the user and sets the output_file_path to "merged.mp3" inside the same folder as the input folder.

10. The script then calls the combine_mp3_files function with the provided input and output file paths.

11. After the process is completed, the script waits for the user to press the enter key before closing the console.

Overall, the script is a simple and convenient way to merge multiple MP3 files into one. It can be helpful for combining audio tracks or creating a playlist from individual MP3 files.

One suggestion: While it is not mandatory, you might consider adding some error handling to gracefully handle cases where the input folder does not exist or the output file cannot be written due to permission issues or disk space constraints. This can make the script more robust and user-friendly.