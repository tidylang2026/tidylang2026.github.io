#!/usr/bin/env python3
"""TidyVoice 2026 Dataset Downloader"""

import os
import requests
from tqdm import tqdm



# --------------------------------------------------------
#
# 1. make your API Key here: https://datacollective.mozillafoundation.org/api-reference
#  
# https://datacollective.mozillafoundation.org/datasets/cmihtsewu023so207xot1iqqw
#
# --------------------------------------------------------


# Configuration
API_KEY = "YOUR_API_KEY_HERE"
OUTPUT_DIR = "./TidyVoiceX_ASV"
DATASET_ID = "cmihtsewu023so207xot1iqqw"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "TidyVoiceX_ASV.tar.gz")

    # Get download URL
    response = requests.post(
        f"https://datacollective.mozillafoundation.org/api/datasets/{DATASET_ID}/download",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    )
    response.raise_for_status()
    download_url = response.json().get("downloadUrl")

    # Download file
    response = requests.get(download_url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))

    with open(output_path, 'wb') as f:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading") as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                pbar.update(len(chunk))

    print(f"\nDone! Saved to: {output_path}")

if __name__ == "__main__":
    main()

