
# WebP to PNG Converter

This script converts all WebP images in a specified folder to PNG format using Pillow and then deletes the original WebP files.

这个脚本使用Pillow将指定文件夹中的所有WebP图像转换为PNG格式，然后删除原始的WebP文件。

## Features

- Converts all WebP images in the specified folder to PNG format.
- Deletes the original WebP files after conversion.
- 简单易用，只需指定目录路径。

## Requirements

- Python 3.x
- Pillow

## Installation

1. Clone the repository:

    克隆仓库：

    ```sh
    git clone https://github.com/yourusername/webp-to-png-converter.git
    cd webp-to-png-converter
    ```

2. Install the required Python packages:

    安装所需的Python包：

    ```sh
    pip install pillow
    ```

## Usage

1. Modify the script to specify the directory containing the WebP images:

    修改脚本以指定包含WebP图像的目录：

    ```python
    folder_path = r'D:\path\to\your\directory'
    ```

2. Run the script:

    运行脚本：

    ```sh
    python convert_webp_to_png.py
    ```

3. The converted PNG images will be saved in the specified directory, and the original WebP files will be deleted.

    转换后的PNG图像将保存在指定目录中，原始的WebP文件将被删除。

## Script

```python
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
folder_path = r'D:\path\to\your\directory'
convert_webp_to_png(folder_path)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 许可证

这个项目是根据MIT许可证授权的 - 详见[LICENSE](LICENSE)文件。
