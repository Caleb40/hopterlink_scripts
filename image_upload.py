import os
import random

import requests

# BASE_URL = "http://hopterlink.us-east-1.elasticbeanstalk.com"
BASE_URL = "http://localhost:8000"
IMAGE_DIR = "./images_compressed"
BUSINESS_IDS = range(1, 23)  # Assuming there are 50 businesses
NUM_IMAGES_PER_BUSINESS = 5


def upload_images_to_business(business_id, image_paths):
    for image_path in image_paths:
        with open(image_path, 'rb') as image_file:
            files = {'image': image_file}
            response = requests.post(f"{BASE_URL}/businesses/{business_id}/images", files=files)
            print(f"Uploading {image_path} to business {business_id}: {response.status_code} - {response.text}")


def main():
    images = [os.path.join(IMAGE_DIR, img) for img in os.listdir(IMAGE_DIR) if img.endswith(('.png', '.jpg', '.jpeg'))]
    for business_id in BUSINESS_IDS:
        selected_images = random.sample(images, NUM_IMAGES_PER_BUSINESS)
        upload_images_to_business(business_id, selected_images)


if __name__ == "__main__":
    main()
