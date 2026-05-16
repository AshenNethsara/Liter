import os
from PIL import Image, UnidentifiedImageError

def select_input_format():
    selections = {
    1 : ["Convert all the files", None],
    2 : ["PNG files Only", "PNG"],
    3 : ["JPEG files Only", "JPEG"],
    4 : ["WEBP files Only", "WEBP"],
    5 : ["ICO files Only", "ICO"]
    #6 : ["Custom (Not yet available!)"]
    }
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nWhat file formats need to be converted?")
    for i, option in selections.items():
        print(f"{i}. {option[0]}")
    selected_option = int(input("Enter number: "))
    input_format = selections.get(selected_option)[1]
    if input_format:
        return input_format

def select_output_format():
    output_formats = {1 : "PNG", 2 : "JPEG", 3 : "WEBP", 4 : "ICO"}
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nAvailable Output formats,")
    for number, format_name in output_formats.items():
        print(f"\t{number}. {format_name}")
    output_format_id = int(input("Enter the number: "))

    if output_formats.get(output_format_id):
        output_format = f".{output_formats.get(output_format_id).lower()}"
        return output_format
    else:
        print("\n-----------------\n| Wrong option! |\n-----------------\n")
        return None

def image_convert(file_path, input_format=None, output_format=None, batch_mode=False):
    try:
        img = Image.open(fp=file_path, formats=input_format)
        if not batch_mode:
            print(f"\nFile name: {os.path.basename(file_path)}\nFormat: {img.format}\nFile path: {os.path.normpath(file_path)}")
        
        if not output_format:
            output_format = select_output_format()

        output_file = os.path.splitext(file_path)[0]+ "_converted" + output_format
        img.save(output_file)
        print("File saved successfully!")
        img.close()

    except FileNotFoundError:
        print("\n-------------------\n| File not found! |\n-------------------\n")
    except UnidentifiedImageError:
        print("\n-----------------------------\n| Can't identify the format |\n-----------------------------\n")
    except Exception as ex:
        print(f"\n*Error: {ex}\n")

# List files in the directory
def open_folder():
    folder_path = input("\nEnter the folder path: ")
    if not folder_path or not os.path.isdir(folder_path): # if input is empty space or wrong
        folder_path = os.getcwd() # Automatically select the current folder
        if not os.path.isdir(folder_path):
            print("\nWrong directory!\nAutomatically seleted the current folder!")
    return folder_path

def file_paths_listing(folder_path):
    files_list = os.listdir(folder_path)
    file_paths_list = []
    # Iterate over the list
    for file in files_list:
        file_paths_list.append(os.path.join(folder_path, file))
    return file_paths_list

def is_image(file_path):
    try:
        with Image.open(file_path) as image:
            if image.format is not None:
                return True
    except UnidentifiedImageError:
        return False
    except FileNotFoundError:
        return False
    except Exception as e:
        return False

def batch_files_handler(file_paths_list):
    input_format = select_input_format()
    output_format = select_output_format()
    for file_path in file_paths_list:
        if is_image(file_path):
            image_convert(file_path, input_format, output_format, True)
        else: print(f"Can't convert this file.\nLocation: {file_path}")

def single_file_processing():
    file_path = input("\nEnter the file path (with extension): ")
    image_convert(file_path)

def batch_files_processing():
    folder_path = open_folder()
    file_paths_list = file_paths_listing(folder_path)
    batch_files_handler(file_paths_list)