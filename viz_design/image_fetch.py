import argparse
import os

import matplotlib.pyplot as plt
from PIL import Image
from icrawler.builtin import BingImageCrawler


arg_parser = argparse.ArgumentParser(description="Download and display first image for a query.")
arg_parser.add_argument("query", nargs="*", help="Search query, e.g. allende meteorite")
args = arg_parser.parse_args()

query = "hoba meteorite"
folder = "images"

# Ensure target folder exists and is clean so we only display this query's result
os.makedirs(folder, exist_ok=True)
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

# Download exactly one image using Bing only
crawler = BingImageCrawler(storage={"root_dir": folder})
crawler.crawl(keyword=query, max_num=1)

files = sorted(
    file for file in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, file))
)

if not files:
    raise RuntimeError(f"No image found for query: {query} (Bing)")

first_image_path = os.path.join(folder, files[0])
img = Image.open(first_image_path).convert("RGB")

plt.figure(figsize=(7, 5))
plt.imshow(img)
plt.title(f'Query: "{query}" (Bing)')
plt.axis("off")
plt.tight_layout()
plt.show()
