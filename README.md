# Video Cutter

Video Cutter is a Python script that allows you to cut a long video into smaller segments based on specified timestamps. It's a useful tool for splitting videos into separate clips based on different sections or topics.

## Prerequisites

Before using the Video Cutter script, make sure you have the following dependencies installed:

- [Python](https://www.python.org/downloads/) (version 3 or above)
- [FFmpeg](https://ffmpeg.org/) (a command-line tool for video manipulation)

## Usage

1. Clone the repository to your local machine:
`git clone https://github.com/yourusername/video-cutter.git`

2. Navigate to the project directory:
`cd video-cutter`

3. Prepare your video file: Place the long video file (e.g., input.mp4) that you want to cut into the same directory as the script.

4. Create a timestamps.txt file: In the same directory, create a file named timestamps.txt and list the timestamps and corresponding titles for each desired cut. Each line should follow the format HH:MM:SS Title. :

## Example

Let's take a look at an example timestamps.txt file:

00:00:00 Intro
00:05:30 Main Section 1
00:12:45 Main Section 2
00:20:10 Conclusion

With the above timestamps, the script will create the following video clips:

- video_1_Intro.mp4 (from 00:00:00 to 00:05:30)
- video_2_Main_Section_1.mp4 (from 00:05:30 to 00:12:45)
- video_3_Main_Section_2.mp4 (from 00:12:45 to 00:20:10)
- video_4_Conclusion.mp4 (from 00:20:10 to the end of the video)

# License

- Feel free to modify the README file according to your preferences and add any additional sections or information you deem necessary.


