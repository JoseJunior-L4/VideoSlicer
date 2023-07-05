import subprocess
import re
import os
import argparse

# Default output folder path
output_folder = "output"

def cut_video(start_time, end_time, title, output_file, main_video_file):
    command = [
        "ffmpeg",
        "-i",
        main_video_file,
        "-ss",
        start_time,
        "-to",
        end_time,
        "-c:v",
        "copy",
        "-c:a",
        "copy",
        output_file
    ]
    subprocess.run(command)

def read_timestamps_file(timestamps_file_path):
    timestamps = []
    if not os.path.isfile(timestamps_file_path):
        raise FileNotFoundError(f"Timestamps file not found: {timestamps_file_path}")

    with open(timestamps_file_path, "r") as file:
        for line in file:
            parts = line.strip().split(" ")
            if len(parts) >= 2:
                timestamp = parts[0]
                title = " ".join(parts[1:])
                timestamps.append((timestamp, title))
    return timestamps

def get_video_length(main_video_file):
    command = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        main_video_file
    ]
    output = subprocess.check_output(command).decode().strip()
    return float(output)

def sanitize_filename(filename):
    # Remove invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def create_output_folder(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def main(main_video_file):
    create_output_folder(output_folder)

    timestamps_file = "timestamps.txt"
    try:
        timestamps = read_timestamps_file(timestamps_file)
    except FileNotFoundError as e:
        print(e)
        return

    video_length = get_video_length(main_video_file)

    for i, (timestamp, title) in enumerate(timestamps):
        start_time = timestamp
        if i < len(timestamps) - 1:
            end_time = timestamps[i+1][0]
        else:
            end_time = str(video_length)

        # Sanitize the title to ensure it's a valid filename
        sanitized_title = sanitize_filename(title)
        output_file = os.path.join(output_folder, f"{i+1}_{sanitized_title}.mp4")

        print(f"Cutting video: {start_time} - {end_time}")
        cut_video(start_time, end_time, title, output_file, main_video_file)

        print(f"Video {i+1} cut successfully: {output_file}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Path to the main video file", required=True)
    args = parser.parse_args()
    main(args.input)
