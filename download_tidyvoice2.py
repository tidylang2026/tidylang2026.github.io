#!/usr/bin/env python3

import os
from datacollective import DataCollective

# --------------------------------------------------------
#
# 1. install the package:   pip install datacollective
# 2. make your API Key here: https://datacollective.mozillafoundation.org/api-reference
# 3. https://datacollective.mozillafoundation.org/datasets/cmkv32i5e02tumg07j79d3c35
#
# --------------------------------------------------------

API_KEY = "YOUR_API_KEY_HERE"   # <-- put your Mozila API key here
OUTPUT_DIR = "/home/machine/TidyVoiceX2_ASV"    # <-- where the dataset will be saved
# --------------------------------------------------------

DATASET_ID = "cmkv32i5e02tumg07j79d3c35"  # <-- Dont change it for downloading the TidyVoice2 Eval sets

def main():
    print("TidyVoice 2026 Challenge Auto-Downloader")
    print("==========================================")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.environ["MDC_API_KEY"] = API_KEY
    os.environ["MDC_DOWNLOAD_PATH"] = OUTPUT_DIR

    print(f"Saving to: {OUTPUT_DIR}")

    try:
        client = DataCollective()
        client.get_dataset(DATASET_ID)

        print("\nDownload completed successfully!")
        print(f"Dataset saved in: {OUTPUT_DIR}\n")

    except Exception as e:
        print("\nERROR while downloading:")
        print(str(e))
        print("\nMake sure your API key and dataset ID are correct.\n")

if __name__ == "__main__":
    main()

