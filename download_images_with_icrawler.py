from icrawler.builtin import BingImageCrawler

def download_images_with_icrawler(query, num_images=5):
    """
    Downloads images from Bing using icrawler.
    """
    crawler = BingImageCrawler(storage={'root_dir': './images'})
    crawler.crawl(keyword=query, max_num=num_images)

if __name__ == "__main__":
    query = input("Enter the keyword for image search: ")
    num_images = int(input("Enter the number of images to download: "))
    download_images_with_icrawler(query, num_images)
