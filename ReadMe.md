
# WebP to PNG Converter

This script converts all WebP images in a specified folder to PNG format using Pillow and then deletes the original WebP files.

����ű�ʹ��Pillow��ָ���ļ����е�����WebPͼ��ת��ΪPNG��ʽ��Ȼ��ɾ��ԭʼ��WebP�ļ���

## Features

- Converts all WebP images in the specified folder to PNG format.
- Deletes the original WebP files after conversion.
- �����ã�ֻ��ָ��Ŀ¼·����

## Requirements

- Python 3.x
- Pillow

## Installation

1. Clone the repository:

    ��¡�ֿ⣺

    ```sh
    git clone https://github.com/yourusername/webp-to-png-converter.git
    cd webp-to-png-converter
    ```

2. Install the required Python packages:

    ��װ�����Python����

    ```sh
    pip install pillow
    ```

## Usage

1. Modify the script to specify the directory containing the WebP images:

    �޸Ľű���ָ������WebPͼ���Ŀ¼��

    ```python
    folder_path = r'D:\path\to\your\directory'
    ```

2. Run the script:

    ���нű���

    ```sh
    python convert_webp_to_png.py
    ```

3. The converted PNG images will be saved in the specified directory, and the original WebP files will be deleted.

    ת�����PNGͼ�񽫱�����ָ��Ŀ¼�У�ԭʼ��WebP�ļ�����ɾ����

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

            # ʹ��Pillow����ת��
            try:
                image = Image.open(webp_file_path)
                image.save(png_file_path, 'PNG')
                print(f"Converted {filename} to {png_file_path}")

                # ɾ��ԭʼ�� WebP �ļ�
                os.remove(webp_file_path)
                print(f"Deleted original WebP file: {webp_file_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

# �������·���滻Ϊ����ļ���·��
folder_path = r'D:\path\to\your\directory'
convert_webp_to_png(folder_path)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ���֤

�����Ŀ�Ǹ���MIT���֤��Ȩ�� - ���[LICENSE](LICENSE)�ļ���
