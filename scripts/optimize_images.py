import os
import re
from PIL import Image

def replace_references(docs_dir, old_name, new_name):
    """
    Searches for references to old_name in docs_dir and replaces them with new_name.
    """
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.lower().endswith(('.md', '.yml', '.css', '.js')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if old_name in content:
                        new_content = content.replace(old_name, new_name)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated references in {file}: {old_name} -> {new_name}")
                except Exception as e:
                    print(f"Skipping {file} due to error: {e}")

def optimize_to_webp(directory, docs_dir, max_width=1280, quality=80):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # We target the png files we want to convert
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                original_size = os.path.getsize(file_path)
                
                # New webp filename
                new_file = os.path.splitext(file)[0] + ".webp"
                new_file_path = os.path.join(root, new_file)
                
                try:
                    with Image.open(file_path) as img:
                        # Resize if too wide
                        if img.width > max_width:
                            new_height = int(max_width * img.height / img.width)
                            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                        
                        # Convert to RGB if needed (png can be RGBA but WebP supports alpha too)
                        # We save as WebP
                        img.save(new_file_path, "WEBP", quality=quality)
                        
                        new_size = os.path.getsize(new_file_path)
                        reduction = (original_size - new_size) / original_size * 100
                        print(f"Converted {file} to WebP: {original_size/1024:.2f}KB -> {new_size/1024:.2f}KB ({reduction:.1f}% reduction)")
                        
                        # Replace references in all docs
                        replace_references(docs_dir, file, new_file)
                        
                        # Delete the original PNG
                        os.remove(file_path)
                        print(f"Deleted original {file}")
                        
                except Exception as e:
                    print(f"Failed to process {file}: {e}")

if __name__ == "__main__":
    image_dir = r"docs\images"
    docs_dir = "docs"
    if os.path.exists(image_dir):
        optimize_to_webp(image_dir, docs_dir)
    else:
        print(f"Directory {image_dir} not found.")
