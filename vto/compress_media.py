import os
from PIL import Image
from moviepy import VideoFileClip


# Define your static path
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

def compress_images():
    print("🔧 Compressing images...")
    for root, _, files in os.walk(STATIC_DIR):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                path = os.path.join(root, file)
                try:
                    img = Image.open(path)
                    img.save(path, optimize=True, quality=82)  # increased from 75 → 82 for better clarity
                    print(f"✅ Compressed: {file}")
                except Exception as e:
                    print(f"⚠️ Error compressing {file}: {e}")

def compress_videos():
    print("🎬 Compressing videos...")
    for root, _, files in os.walk(STATIC_DIR):
        for file in files:
            if file.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
                path = os.path.join(root, file)
                output_path = os.path.join(root, f"compressed_{file}")
                try:
                    clip = VideoFileClip(path)
                    clip.write_videofile(
                        output_path,
                        codec="libx264",
                        bitrate="1200k",   # slightly higher (1000k → 1200k) for sharper playback
                        audio_codec="aac",
                        audio_bitrate="128k",  # richer audio quality
                        preset="medium"        # better visual quality, still optimized
                    )
                    print(f"✅ Compressed video: {file}")
                except Exception as e:
                    print(f"⚠️ Error compressing {file}: {e}")

if __name__ == "__main__":
    compress_images()
    compress_videos()
    print("\n🎉 Compression complete! Your static files are now optimized.")
