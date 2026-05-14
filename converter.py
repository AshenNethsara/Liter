# Liter -  Simple Image Converter
# Version 1.1
# 2026.5.2 Ashen Nethsara

import sys, os
from PIL import Image, UnidentifiedImageError

output_formats = {
    1 : "PNG",
    2 : "JPEG",
    3 : "WEBP",
    4 : "ICO"
}


def image_convert(f_path):
    try:
        img = Image.open(f_path)

        print(f"\nFile name: {os.path.basename(f_path)}\nFormat: {img.format}\nFile path: {os.path.normpath(f_path)}")
        print("\nAvailable Output formats,")

        for number, Fname in output_formats.items():
            print(f"\t{number}. {Fname}")

        desired_format_no = int(input("Enter the number: "))

        if output_formats.get(desired_format_no):
            desired_format = f".{output_formats.get(desired_format_no).lower()}"
            output_file = os.path.splitext(f_path)[0]+ "_converted" + desired_format
            img.save(output_file)
            print("File saved successfully!")
        else:
            print("\n-----------------\n| Wrong option! |\n-----------------\n")

        img.close()

    except FileNotFoundError:
        print("\n-------------------\n| File not found! |\n-------------------\n")
        
    except UnidentifiedImageError:
        print("\n-----------------------------\n| Can't identify the format |\n-----------------------------\n")

    except Exception as ex:
        print(f"\n*Error: {ex}\n")