import sys
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS


def createExifTable(img):
    exif_table = {}
    for k, v in img.getexif().items():
        tag = TAGS.get(k)
        exif_table[tag] = v
    return exif_table

def sort(argv):
    formatList = {
        '.jpeg': 'Image',
        '.jpg': 'Image',
        '.png': 'Image',
        '.CR2': 'Raw',

    }
    folderToSort = Path('/home/jonathan')
    folderToSort = folderToSort / sys.argv[1]

    for f in folderToSort.iterdir():
        if f.suffix in formatList:
            # Get image to check if exif exist
            img = Image.open(folderToSort / f.name)
            if createExifTable(img):
                output_dir = folderToSort / formatList.get(f.suffix, 'autres')
                output_dir.mkdir(exist_ok=True)
                f.rename(output_dir / f.name)
            else:
                output_dir = folderToSort / formatList.get(f.suffix, 'autres') / 'noExif'
                output_dir.mkdir(exist_ok=True)
                f.rename(output_dir / f.name)

sort(argv=True)
