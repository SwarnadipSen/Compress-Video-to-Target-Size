from moviepy.editor import VideoFileClip
import os

def reduce_video_size(clip,target_size_mb):
    target_size_bytes = target_size_mb * 1024 * 1024
    duration = clip.duration
    target_bitrate = (target_size_bytes * 8) / duration
    return target_bitrate

def render_video(input_path, target_size_mb, output_path):
    clip = VideoFileClip(input_path)
    target_bitrate = reduce_video_size(clip,target_size_mb)
    width,height = clip.size
    clip.write_videofile(
        output_path,
        bitrate=f"{int(target_bitrate)}",
        codec='libx264',
        audio_codec='aac',
        threads=4,  
        preset='medium',  
        ffmpeg_params=[
            '-vf', f'scale={width}:{height}',  
            '-aspect', f'{width}/{height}'  
        ]
    )
    clip.close()

if __name__ == "__main__":
    videos = (os.listdir("./input_videos"))

    print("\n")
    for i in range(len(videos)):
        print(f"{i+1}  {videos[i]}")
    print("\n")
    
    video = int(input("Select Video: "))
    input_video_path = "./input_videos/"+ videos[video+1]

    output_video_path = "./output_videos/" + videos[video+1]
    target_size_mb = float(input("Target Video Size: "))

    render_video(input_video_path, target_size_mb, output_video_path)

    output_size_mb = os.path.getsize(output_video_path) / (1024 * 1024)
    print(f"Output video size: {output_size_mb:.2f} MB")
