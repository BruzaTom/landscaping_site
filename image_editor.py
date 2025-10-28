from PIL import Image, ImageOps
import os

path = 'static/images/texas.webp'
lst = path.split(".")
format = lst[1]
print(f"format: {format}")
filename = lst[0]
#print(format)
#print(filename)

# Open the original image
original_image = Image.open(path)

img_width, img_height = original_image.size
# Define the new size
new_width = img_width / 7# 768 * 1.5 = 1152
new_height = img_height / 7  # 768 * 1.5 = 1152
#new_width = 60
#new_height = 60

def get_format(filename):
    format_map = {
    'jpg': 'JPEG',
    'jpeg': 'JPEG',
    'png': 'PNG',
    'webp': 'WEBP'
    }
    ext = filename.split(".")[1] 
    format = format_map.get(ext, format_map['jpeg'])
    print(f"ext: {ext}-{format}")
    return ext, format

def gen_dir_name(path, op='modified'):
    dirs = path.split("/")
    last_index = len(dirs) - 1
    if dirs[last_index] == "":
        last_index -= 1
#    print("\n", dirs, f"\nlast name: {dirs[last_index]}")
    name = dirs[last_index][:3] + "_" + op
    dirs[last_index] = name
    new_path = "/".join(dirs) 
#    print(f"gened name: {name}\nnew_path: {new_path}\n")
    return new_path

def comp_dir_files(folder_path):
    output_folder = gen_dir_name(folder_path, op='compressed')
    files = os.listdir(folder_path)
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(folder_path):
        print(f"filename: {filename}")
        ext, format = get_format(filename)
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        # Save with lower quality
        output_path = os.path.join(output_folder, filename)
        img = ImageOps.exif_transpose(img)  # Correct orientation
        img.save(output_path, format, quality=60, optimize=True)
        print(f"Compressed: {img_path}")
        print(f"To: {output_path}\n")

def index_dir(folder_path):
    files = os.listdir(folder_path)
    # Loop and rename
    for index, filename in enumerate(files):
        print(f"filename: {filename}")
        ext = get_format(filename)[0]
#        ext = 'jpg'
        new_name = f"{str(index+1).zfill(3)}.{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path}\nto: {new_path}\n")

def main():
    uinput = input('option: ')
    if uinput == 'compress':
        comp_dir_files('static/images/carisail/')
    if uinput == 'rename':
        index_dir('static/images/landscaping/')
    if uinput == 'r':
        # Resize the image
        resized_image = original_image.resize((int(new_width), int(new_height)), Image.Resampling.LANCZOS)
        # Save the resized image
        resized_image.save(filename + "_rs." + format, format=format)
    if uinput == 'f':
        flipped_image = original_image.transpose(Image.FLIP_TOP_BOTTOM)
        # Save or display the flipped image
        flipped_image.save(filename + "_f." + format, format=format)
        flipped_image.show()
    if uinput == 's':
        img_width, img_height = original_image.size
        # Define the number of rows and columns
        rows = 9
        cols = 9
        # Calculate the width and height of each tile
        tile_width = img_width // cols
        tile_height = img_height // rows
        # Loop through the image and save each tile
        index = 0
        for row in range(rows):
            for col in range(cols):
                left = col * tile_width
                upper = row * tile_height
                right = (col + 1) * tile_width
                lower = (row + 1) * tile_height
                # Crop the image
                tile = original_image.crop((left, upper, right, lower))
                # Save the tile
                tile.save(f'sprites/explo_frames/{index}.png')
                index += 1

main()
#gen_dir_name("static/images/landscaping/")
