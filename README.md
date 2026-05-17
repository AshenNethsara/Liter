# Liter

Liter is a simple and easy-to-use image converter built with Python. It lets you change the format of a single image or process many images in a folder at the same time (batch processing).

Right now, Liter can convert between PNG, JPEG, WEBP, and ICO file types.

## Setup

To run Liter on your computer, you need to have Python installed. You also need to install the library that handles the images.

1. Download or clone this project to your computer.
2. Open your terminal or command prompt and go to the project folder.
3. Install the required image library by typing this command:
```bash
pip install Pillow
```

## How to Use

To start the converter, just run the main file:

```bash
python main.py

```

When the program starts, you will see a menu with two options:

1. **Convert a single file:** Type the path to one image, and the program will convert it.
2. **Batch processing:** Type the path to a folder. You can choose to convert all the images inside, or only specific types (like just the PNG files).

After you choose, the program will ask which output format you want. The new images will be saved in the same folder, with `_converted` added to their name so your original pictures stay safe.

## Credits

This project uses the [Pillow (PIL)](https://github.com/python-pillow/Pillow) library to power all of the image converting and processing features.

## License

This project is licensed under the Apache License 2.0.
