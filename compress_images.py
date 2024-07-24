import os

from PIL import Image


def compress_images(input_folder, output_folder, compression_quality=85):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                # Open an image file
                with Image.open(file_path) as img:
                    # Compress the image and save to the output folder
                    output_file_path = os.path.join(output_folder, filename)
                    img.save(output_file_path, optimize=True, quality=compression_quality)
                    print(f"Compressed and saved {filename} to {output_file_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    input_folder = 'images'
    output_folder = 'images_compressed'
    compression_quality = 10  # Set the compression quality (1-100)

    compress_images(input_folder, output_folder, compression_quality)
