# Liter -  Simple Image Converter
# Batch processing is supported
# Version 1.2, 2026/5/16
# 2026.5.2 Ashen Nethsara

import time, os, converter

print(f"\nMenu\n1. Convert a single file\n2. Batch processing\n")
time.sleep(0.2)
option = int(input("Enter number: "))

if option == 1:
    time.sleep(0.5)
    #print("\033[H\033[J", end="") speed way for clear the text in terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    converter.single_file_processing()
elif option == 2:
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    converter.batch_files_processing()