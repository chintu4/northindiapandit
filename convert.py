import os
from pathlib import Path
from PIL import Image

def convert_images_to_webp(directory=".", quality=80):
    """
    Convert all .jpg and .png files in a directory to .webp format.
    
    Args:
        directory: Path to search for images (default: current directory)
        quality: WebP quality (1-100, default: 80)
    """
    image_extensions = {'.jpg', '.jpeg', '.png'}
    converted = 0
    
    for file_path in Path(directory).rglob('*'):
        if file_path.suffix.lower() in image_extensions:
            try:
                webp_path = file_path.with_suffix('.webp')
                image = Image.open(file_path)
                image.save(webp_path, 'WEBP', quality=quality)
                print(f"✓ Converted: {file_path} → {webp_path}")
                converted += 1
            except Exception as e:
                print(f"✗ Error converting {file_path}: {e}")
    
    print(f"\nTotal converted: {converted} files")

if __name__ == "__main__":
    convert_images_to_webp("assets/imgs", quality=95)