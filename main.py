# Liter -  Simple Image Converter
# Version 1.0
# 2026.5.2 Ashen Nethsara
import sys, os
from PIL import Image

output_formats = {
    1 : "PNG",
    2 : "JPEG",
    3 : "WEBP",
    4 : "ICO"
}

file_path = input("\nEnter the file path (with extension): ")

try:
    img = Image.open(file_path)

    print(f"\nFile name: {os.path.basename(file_path)}\nFormat: {img.format}\nFile path: {os.path.normpath(file_path)}")
    print("\nAvailable Output formats,")

    for number, Fname in output_formats.items():
        print(f"\t{number}. {Fname}")

    desired_format_no = int(input("Enter the number: "))

    if output_formats.get(desired_format_no):
        desired_format = f".{output_formats.get(desired_format_no).lower()}"
        output_file = os.path.splitext(file_path)[0]+ "_converted" + desired_format
        img.save(output_file)
        print("File saved successfully!")
    else:
        print("\n-----------------\n| Wrong option! |\n-----------------\n")


    img.close()
except OSError:
    print("\n-------------------\n| File not found! |\n-------------------\n")