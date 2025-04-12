import os
from PIL import Image
import pillow_avif

PILLOW_FORMATS = {
    'png': 'PNG',
    'jpg': 'JPEG',
    'jpeg': 'JPEG',
    'ico': 'ICO',
    'webp': 'WEBP',
    'tif': 'TIFF',
    'tiff': 'TIFF',
    'gif': 'GIF',
    'avif': 'AVIF',
    'bmp': 'BMP'
}

SUPPORTED_INPUT_FORMATS = ['.png', '.jpg', '.jpeg', '.ico', '.webp', '.tif', '.tiff', '.gif', '.avif', '.bmp', '.raw']

def img_convert(file_path, output_format):
    base, ext = os.path.splitext(file_path)
    ext = ext.lower()
    output_path = f"{base}_converted.{output_format}"
    if ext not in SUPPORTED_INPUT_FORMATS:
        raise ValueError("Unsupported File Type.")
    if ext == '.raw':
        width, height = 256, 256
        with open(file_path, 'rb') as f:
            raw_data = f.read()
        img = Image.frombytes('RGB', (width, height), raw_data)
    else:
        img = Image.open(file_path)
        img.load()
    if output_format == 'raw':
        img = img.convert("RGB")
        raw_data = img.tobytes()
        with open(output_path, 'wb') as f:
            f.write(raw_data)
    elif output_format in PILLOW_FORMATS:
        img = img.convert("RGB") if output_format not in ['png', 'gif', 'webp', 'bmp', 'ico'] else img
        try:
            img.save(output_path, PILLOW_FORMATS[output_format])
        except Exception:
            raise ValueError(f"{output_format.upper()} Format Not Supported.")
    else:
        raise ValueError("Unsupported Output Format.")
    return output_path