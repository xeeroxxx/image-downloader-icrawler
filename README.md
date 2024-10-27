# Image Downloader with iCrawler

## Overview
This Python script uses the `icrawler` library to download images from Bing based on a search keyword and user-defined number of images. It’s ideal for quickly gathering images for testing or building datasets.

## Features
- Downloads images from Bing using the `icrawler` library.
- Allows users to specify a search keyword and the number of images to download.
- Saves downloaded images in a local directory (`./images`).

## Installation
### Prerequisites
- Python 3.x installed on your system
- Install required dependencies:
    ```bash
    pip install icrawler
    ```

### Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/xeeroxxx/image-downloader-icrawler.git
    ```
2. Navigate to the project directory:
    ```bash
    cd image-downloader-icrawler
    ```

## How to Use
1. Run the script using the following command:
    ```bash
    python download_images_with_icrawler.py
    ```
2. Enter a search keyword and the number of images you want to download when prompted.

## Example
If you enter:

Keyword: "cats" Number of images: 5

The script will download 5 images of cats and save them in the `./images` directory.

## Contributing
Feel free to fork the repository and submit pull requests for new features, bug fixes, or improvements.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements
- Built using the `icrawler` library for image crawling and downloading.
