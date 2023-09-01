# img-conv

Is a Python script used to convert .jpg, .jpeg and .png files to Web Picture Images (.webp).

The main goal is to provide high-quality images while keeping small file sizes

## How to use

python main.py --help
python main.py <mode> <starting_path> <target_path>
python main.py convert ~/repos/danielmacuare.github.io/assets/img/posts ~/Desktop/outputs
python main.py show tests/images

### Args

mode = Can be "show" or "convert"
starting_path = Directory Path where images will be read from
target_path = Directory Path to which images will saved to

## Features

- Check all images recursively from an Input Dir. You can print a table with sizes
- Convert all images recursively from an Input Dir and saves them to an output_dir
  - It will the show you a summary of
    - Size Saved
    - ..

## TO-DO

- Improve variable naming
- Refactor code
- Add gifts to the README.md
- Add testing for edge cases