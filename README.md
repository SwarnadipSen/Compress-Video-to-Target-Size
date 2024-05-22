# Video Size Reducer

This script reduces the size of a video to a given size using the `moviepy` library.

## Prerequisites

Make sure you have `moviepy` installed. You can install it using pip:

```sh
pip install moviepy
```

## How to use

1. Place your videos in the `input_videos` folder.

2. Execute the `main.py` script.

3. **Select Video and Set Target Size:**
   - You will be prompted with a list of videos along with corresponding numbers.
   - Enter the number corresponding to the video you want to resize.
   - Enter your target size in MB when prompted.

4. The script will process the selected video, compress it to the target size, and save the output in the `output_videos` folder.
