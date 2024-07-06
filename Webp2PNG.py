import os
import subprocess
from PIL import Image

def convert_webp_to_png(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.webp'):
            webp_file_path = os.path.join(folder_path, filename)
            png_file_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.png')

            # 使用Pillow进行转换
            try:
                image = Image.open(webp_file_path)
                image.save(png_file_path, 'PNG')
                print(f"Converted {filename} to {png_file_path}")

                # 删除原始的 WebP 文件
                os.remove(webp_file_path)
                print(f"Deleted original WebP file: {webp_file_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

# 将下面的路径替换为你的文件夹路径
folder_path = r'C:\Desktop\test'
convert_webp_to_png(folder_path)
