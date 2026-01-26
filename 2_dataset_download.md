---
layout: page
title: Download TidyVoiceX Dataset
---

Here you can access the training data, development data, and trial pairs needed to participate in the challenge.

<br>


## Dataset Components

### TidyVoiceX Dataset (Train + Dev)

The complete dataset package containing both training and development data for the TidyVoice2026 Challenge.

**Contents:**
- **TidyVoiceX_Train/**: Training dataset with multi-lingual speaker recordings
- **TidyVoiceX_Dev/**: Development dataset for system tuning and validation
- Speaker identity labels and language annotations
- Cross-lingual speaker samples across both splits

**Download:**
- **Size:** 50 GB
- **Format:** .wav file with 16KHz sampling Frequency

<div style="background-color: #f8f9fa; border: 2px solid #7c3aed; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #5b21b6; margin-bottom: 15px;">📥 TidyVoiceX Complete Dataset</h4>
  <p style="margin-bottom: 15px;">Click the link below to access the dataset page or download the API script:</p>
  <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; margin-top: 20px;">
    <a href="https://datacollective.mozillafoundation.org/datasets/cmihtsewu023so207xot1iqqw" target="_blank" style="display: inline-block; background-color: #7c3aed; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
      🔗 View Dataset Page
    </a>
    <a href="https://raw.githubusercontent.com/tidyvoice2026/tidyvoice2026.github.io/main/download_tidyvoice.py" download style="display: inline-block; background-color: #7c3aed; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
      📥 Download Script
    </a>
  </div>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Available via Mozilla Data Collective</em>
  </p>
</div>

<br>

### Trial Pairs for Dev Data

Trial pairs file containing the evaluation protocol for the development set.


<div style="background-color: #f8f9fa; border: 2px solid #ffc107; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #856404; margin-bottom: 15px;">📥 Trial Pairs Download</h4>
  <p style="margin-bottom: 15px;">Click the link below to download the trial pairs file:</p>
  <a href="https://drive.google.com/file/d/1OLEKewhcGi_W_gmqEDpjx-fZwQGz2kWU/view?usp=sharing" target="_blank" style="display: inline-block; background-color: #ffc107; color: #212529; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
    🔗 Download Trial Pairs (trial_pairs_dev.txt)
  </a>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Available via Google Drive</em>
  </p>
</div>

<br>

### TidyVoiceX2_ASV (Evaluation Dataset)

The official evaluation dataset for the TidyVoice2026 Challenge.

**Contents:**
- **TidyVoiceX2_ASV/**: Evaluation dataset with multi-lingual speaker recordings covering approximately 40 additional languages
- Cross-lingual speaker samples for evaluation

**Download:**
- **Size:** 32 GB
- **Format:** .wav file with 16KHz sampling Frequency

<div style="background-color: #f8f9fa; border: 2px solid #dc3545; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #c82333; margin-bottom: 15px;">📥 TidyVoiceX2_ASV Evaluation Dataset</h4>
  <p style="margin-bottom: 15px;">Click the link below to access the dataset page or download the API script:</p>
  <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; margin-top: 20px;">
    <a href="https://datacollective.mozillafoundation.org/datasets/cmkv32i5e02tumg07j79d3c35" target="_blank" style="display: inline-block; background-color: #dc3545; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
      🔗 View Dataset Page
    </a>
    <a href="https://raw.githubusercontent.com/tidyvoice2026/tidyvoice2026.github.io/main/download_tidyvoice2.py" download style="display: inline-block; background-color: #dc3545; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
      📥 Download Script
    </a>
  </div>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Available via Mozilla Data Collective</em>
  </p>
</div>

<br>

### Evaluation Trial Files

Official trial pairs for the evaluation dataset.

**Trial Files Included:**
- **tv26_eval-A.txt**: Evaluation trial pairs for All languages
- **tv26_eval-U.txt**: Evaluation trial pairs for Unseen languages


<div style="background-color: #f8f9fa; border: 2px solid #28a745; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #218838; margin-bottom: 15px;">📥 Evaluation Trial Files Download</h4>
  <p style="margin-bottom: 15px;">Click the link below to download the trial pairs file (contains both tv26_eval-A.txt and tv26_eval-U.txt):</p>
  <a href="https://drive.google.com/file/d/1tIFjYnRHGLypciX4Dl7IBX86vymAnVRP/view?usp=sharing" target="_blank" style="display: inline-block; background-color: #28a745; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
    🔗 Download Evaluation Trial Pairs (ZIP)
  </a>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Available via Google Drive</em>
  </p>
</div>

<br>

## Download Instructions

1. **Registration Required:** Please complete the [registration process](https://tidyvoice2026.github.io/10_registration/) before downloading the dataset.

2. **Create Mozilla Data Collective API Key:** 
   - Visit [https://datacollective.mozillafoundation.org/api-reference](https://datacollective.mozillafoundation.org/api-reference)
   - Navigate to **Profile > API** to create your API credentials
   - Save your API key securely

3. **Install Required Package:**
   ```bash
   pip install datacollective
   ```

4. **Download Using Python Script:**
   
   Download the [`download_tidyvoice.py`](https://github.com/tidyvoice2026/tidyvoice2026.github.io/blob/main/download_tidyvoice.py) script from the dataset download section above, then:
   
   - Replace `YOUR_API_KEY_HERE` with your Mozilla Data Collective API key
   - Update `OUTPUT_DIR` to your desired download location
   - Run: `python download_tidyvoice.py` and `python download_tidyvoice2.py`



<br>

## Data Structure

The dataset is organized with **speakerID** folders directly inside each dataset folder, which then contain **languageID** subfolders with the corresponding audio files for that speaker in that specific language.

```
TidyVoiceX_Train/Dev
├── speaker_001/
│   ├── en/          # English recordings
│   │   ├── file1.wav
│   │   ├── file2.wav
│   │   └── ...
│   ├── fa/          # Persian recordings
│   │   ├── file1.wav
│   │   └── ...
│   └── fr/          # French recordings
│       └── ...
├── speaker_002/
│   ├── de/          # German recordings
│   ├── it/          # Italian recordings
│   └── ...
└── ...


```

**Structure Explanation:**
- **TidyVoiceX_Train/**: Contains training data with speakerID folders directly at the root
- **TidyVoiceX_Dev/**: Contains development data with speakerID folders directly at the root
- Each **speakerID** folder contains all recordings for that specific speaker
- **languageID** subfolders organize recordings by language (en, fa, fr, de, it, etc.)
- Audio files for each language are stored in their respective languageID folders
- This structure enables easy access to cross-lingual data for the same speaker

<br>

## Support

If you encounter any issues with the dataset download or have questions about the data format, please contact:

- **Email:** aref.farhadipour@uzh.ch

<br>

## Citation

If you use the TidyVoice dataset in your research, please cite:

```
@misc{farhadi2026tidy,
      title={TidyVoice: A Curated Multilingual Dataset for Speaker Verification Derived from Common Voice}, 
      author={Aref Farhadipour and Jan Marquenie and Srikanth Madikeri and Eleanor Chodroff},
      year={2026},
      journal={ICASSP2026},
      url={https://arxiv.org/abs/2601.16358}, 
}
```

<br>

---
