import os
from PIL import Image
from moviepy import VideoFileClip

# Paths (inside static/assets)
BASE_DIR = os.path.join("static", "assets")
IMG_DIR = os.path.join(BASE_DIR, "img")
VIDEO_DIR = os.path.join(BASE_DIR, "videos")
OUTPUT_IMG_DIR = os.path.join(IMG_DIR, "compressed")
OUTPUT_VIDEO_DIR = os.path.join(VIDEO_DIR, "compressed")

# Create output folders if they don't exist
os.makedirs(OUTPUT_IMG_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEO_DIR, exist_ok=True)

# ---------- IMAGE COMPRESSION ----------
def compress_image(input_path, output_path, quality=75, max_width=1600):
    """Resize & compress image while keeping clarity."""
    img = Image.open(input_path)

    # Resize if too wide
    if img.width > max_width:
        ratio = max_width / img.width
        new_size = (max_width, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    # Convert PNGs with transparency to RGB
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.save(output_path, "JPEG", optimize=True, quality=quality)
    print(f"✅ Compressed image: {os.path.basename(input_path)} → {output_path}")


# ---------- VIDEO COMPRESSION ----------
def compress_video(input_path, output_path, bitrate="1200k"):
    """Compress video file using moviepy."""
    try:
        clip = VideoFileClip(input_path)
        clip.write_videofile(
            output_path,
            codec="libx264",
            bitrate=bitrate,
            audio_codec="aac",
            audio_bitrate="128k",
            preset="medium"
        )
        clip.close()
        print(f"✅ Compressed video: {os.path.basename(input_path)} → {output_path}")
    except Exception as e:
        print(f"⚠️ Error compressing video {input_path}: {e}")


# ---------- MAIN EXECUTION ----------
if __name__ == "__main__":
    print("🔧 Starting media compression...")

    # Compress images
    for filename in os.listdir(IMG_DIR):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            input_path = os.path.join(IMG_DIR, filename)
            output_path = os.path.join(OUTPUT_IMG_DIR, filename.replace(".png", ".jpg"))
            compress_image(input_path, output_path)

    # Compress videos
    for filename in os.listdir(VIDEO_DIR):
        if filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
            input_path = os.path.join(VIDEO_DIR, filename)
            output_path = os.path.join(OUTPUT_VIDEO_DIR, f"compressed_{filename}")
            compress_video(input_path, output_path)

    print("\n🎉 Compression complete! All images and videos inside static/assets are optimized.")
