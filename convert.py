import ffmpeg
import os

def convert_to_circle(input_path, output_path):
    stream = ffmpeg.input(input_path)
    stream = ffmpeg.output(
        stream, output_path,
        vf='scale=240:240:force_original_aspect_ratio=decrease,pad=240:240:(ow-iw)/2:(oh-ih)/2:color=black',
        vcodec='libx264',
        pix_fmt='yuv420p',
        f='mp4'
    )
    ffmpeg.run(stream)

