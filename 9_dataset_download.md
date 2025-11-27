---
layout: page
title: Dataset Download
---

# Dataset Download

Welcome to the TidyVoice Challenge dataset download page. Here you can access the training data, development data, and trial pairs needed to participate in the challenge.

<br>

## Overview

The TidyVoice Challenge uses the **Tidy-X dataset**, a curated partition from Mozilla Common Voice featuring:
- Over 4,474 speakers across 40 languages
- Approximately 321,711 utterances totaling 457 hours
- Clearly defined training and test splits
- Pseudonymized speaker identities for privacy protection

<br>

## Dataset Components

### TidyVoiceX Dataset (Train + Dev)

The complete dataset package containing both training and development data for the TidyVoice Challenge.

**Contents:**
- **TidyVoiceX_Train/**: Training dataset with multi-lingual speaker recordings
- **TidyVoiceX_Dev/**: Development dataset for system tuning and validation
- Speaker identity labels and language annotations
- Audio files in standard format
- Cross-lingual speaker samples across both splits

**Download:**
- **Size:** ~ 50GB 
- **Format:** .wav file with 16KHz sampling Frequency
- **Package:** Combined archive containing both train and dev folders

<div style="background-color: #f8f9fa; border: 2px solid #007bff; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #007bff; margin-bottom: 15px;">📥 TidyVoiceX Complete Dataset</h4>
  <p style="margin-bottom: 15px;">Download the complete dataset package (includes both train and dev data):</p>
  <a href="#" style="display: inline-block; background-color: #007bff; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
    🔗 Download TidyVoiceX Dataset (Train + Dev)
  </a>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Link will be activated upon dataset release</em>
  </p>
</div>

<br>

### Trial Pairs for Dev Data

Trial pairs file containing the evaluation protocol for the development set.

**Contents:**
- Enrollment-test pairs
- Same-speaker and different-speaker trials
- Cross-lingual trial specifications
- Ground truth labels

**Download:**
- **File:** trial_pairs_dev.txt
- **Format:** Text file with trial specifications

<div style="background-color: #f8f9fa; border: 2px solid #ffc107; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #856404; margin-bottom: 15px;">📥 Trial Pairs Download</h4>
  <p style="margin-bottom: 15px;">Click the link below to download the trial pairs file:</p>
  <a href="#" style="display: inline-block; background-color: #ffc107; color: #212529; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
    🔗 Download Trial Pairs (trial_pairs_dev.txt)
  </a>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Link will be activated upon dataset release</em>
  </p>
</div>

<br>

### TidyVoiceX_Evaluation (Coming Soon)

The evaluation dataset will be released closer to the evaluation phase of the challenge.

**Contents:**
- Final evaluation recordings
- Test set for official challenge scoring
- Cross-lingual evaluation samples

**Download:**
- **Size:** [To be announced]
- **Format:** [To be announced]

<div style="background-color: #f8f9fa; border: 2px dashed #6c757d; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #6c757d; margin-bottom: 15px;">⏳ TidyVoiceX_Evaluation</h4>
  <p style="margin-bottom: 15px; color: #6c757d;">Evaluation dataset will be available here during the evaluation phase</p>
  <button style="display: inline-block; background-color: #6c757d; color: white; padding: 12px 24px; border: none; border-radius: 5px; font-weight: bold; cursor: not-allowed;" disabled>
    🔒 Coming Soon
  </button>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Will be released during evaluation phase</em>
  </p>
</div>

<br>

### Evaluation Trial Files (Coming Soon)

Trial files for the official evaluation phase will be made available here.

**Contents:**
- **Evaluation Trial File 1:** Primary evaluation protocol
- **Evaluation Trial File 2:** Secondary evaluation protocol
- Official scoring pairs for final rankings

**Download:**
- **Files:** evaluation_trials_1.txt, evaluation_trials_2.txt
- **Format:** Text files with trial specifications

<div style="background-color: #f8f9fa; border: 2px dashed #6c757d; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #6c757d; margin-bottom: 15px;">⏳ Evaluation Trial Files</h4>
  <p style="margin-bottom: 15px; color: #6c757d;">Official evaluation trial files will be available here</p>
  <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
    <button style="background-color: #6c757d; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-weight: bold; cursor: not-allowed;" disabled>
      🔒 Evaluation Trial File 1
    </button>
    <button style="background-color: #6c757d; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-weight: bold; cursor: not-allowed;" disabled>
      🔒 Evaluation Trial File 2
    </button>
  </div>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Will be released during evaluation phase</em>
  </p>
</div>

<br>

## Download Instructions

1. **Registration Required:** Please complete the [registration process](6_registration.html) before downloading the dataset.

2. **License Agreement:** By downloading the dataset, you agree to use it solely for the TidyVoice Challenge and research purposes.

3. **File Formats:** 
   - Audio files: WAV format, 16kHz sampling rate
   - Metadata: CSV and TXT formats
   - Trial pairs: Text format with space-separated values

4. **System Requirements:**
   - Minimum 50GB free disk space
   - Stable internet connection for download

<br>

## Data Structure

The dataset is organized with **speakerID** folders directly inside each dataset folder, which then contain **languageID** subfolders with the corresponding audio files for that speaker in that specific language.

```
TidyVoiceX_Train/
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

TidyVoiceX_Dev/
├── speaker_001/
│   ├── en/          # English recordings
│   │   └── audio_files.wav
│   ├── fa/          # Persian recordings
│   │   └── audio_files.wav
│   └── ...
├── speaker_002/
│   ├── de/          # German recordings
│   │   └── audio_files.wav
│   └── ...
└── ...
```

**Structure Explanation:**
- **TidyVoiceX_Train/**: Contains training data with speakerID folders directly at the root
- **TidyVoiceX_Dev/**: Contains development data with speakerID folders directly at the root
- Each **speakerID** folder contains all recordings for that specific speaker
- **languageID** subfolders organize recordings by language (en, es, fr, de, it, etc.)
- Audio files for each language are stored in their respective languageID folders
- This structure enables easy access to cross-lingual data for the same speaker

<br>

## Support

If you encounter any issues with the dataset download or have questions about the data format, please contact:

- **Email:** aref.farhadipour@uzh.ch
- **GitHub Issues:** [TidyVoice Challenge GitHub](https://github.com/tidyvoice-challenge)

<br>

## Citation

If you use the TidyVoice dataset in your research, please cite:

```
[Citation information will be provided upon dataset release]
```

<br>

---

**Note:** Dataset links will be activated closer to the challenge start date. Please check back regularly for updates.
