from dotenv import load_dotenv
from pathlib import Path
import os
import requests

my_dotenv_path = Path(".env")
load_dotenv(dotenv_path=my_dotenv_path)

base_url = os.getenv("FIRST_PIC_LINK")
source_folder_name = os.getenv("SOURCE_FOLDER_NAME")
download_folder_name = f"disposable-pics-{source_folder_name}"
start_index = 1
end_index = 40

if not os.path.exists(download_folder_name):
    os.mkdir(download_folder_name)


# Defining a download of any image according to the website. Doesn't include iteration loop
def download_image(image_number):
    image_name = f"{source_folder_name}{image_number:04d}.jpg"
    image_url = f"{base_url}{image_name}"
    # unfortunately the site isn't https so verify nust be false. Sketchy af ik
    response = requests.get(image_url, verify=False)
    if response.status_code == 200:
        with open(os.path.join(download_folder_name, image_name), "wb") as file:
            file.write(response.content)  # assuming that the response is automatically a downloaded file
        print(f"Downloaded image {image_name}")
    else:
        print(f"Failed to download image {image_name} (status code: {response.status_code})")


for i in range(start_index, end_index + 1):
    download_image(i)


print(f"All {end_index} are now complete")
