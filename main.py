import sys
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS


def create_exif_table(img):
    exif_table = {}
    for k, v in img.getexif().items():
        tag = TAGS.get(k)
        exif_table[tag] = v
    return exif_table


def sort(argv):
    format_list = {
        '.jpeg': 'Image',
        '.jpg': 'Image',
        '.png': 'Image',
        '.CR2': 'Raw',

    }
    folder_to_sort = Path('/home/jonathan')
    folder_to_sort = folder_to_sort / argv[1]

    for f in folder_to_sort.iterdir():
        if f.suffix in format_list:
            # Get image to check if exif exist
            img = Image.open(folder_to_sort / f.name)
            if create_exif_table(img):
                output_dir = folder_to_sort / format_list.get(f.suffix, 'autres')
                output_dir.mkdir(exist_ok=True)
                f.rename(output_dir / f.name)
            else:
                output_dir = folder_to_sort / format_list.get(f.suffix, 'autres') / 'noExif'
                output_dir.mkdir(exist_ok=True)
                f.rename(output_dir / f.name)


sort(argv=True)
