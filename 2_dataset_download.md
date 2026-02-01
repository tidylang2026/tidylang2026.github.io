---
layout: page
title: Download Tidy-X Dataset
---

Here you can access the **training data** and **validation data** needed to participate in the TidyLang 2026 Challenge. Only the official Tidy-X partition may be used from the Mozilla Common Voice dataset.

<br>

## Dataset Components

### Tidy-X Dataset (Train + Validation)

The complete dataset package containing both training and validation data for the TidyLang 2026 Challenge. This is the only official data from Mozilla Common Voice that participants may use.

**Contents:**
- **Tidy-X Train:** Training dataset with multi-lingual speaker recordings (40 languages)
- **Tidy-X Valid:** Validation dataset for system tuning and validation
- Speaker identity labels and language annotations
- Cross-lingual speaker samples across both splits (each speaker with 2–10 languages)

**Download:**
- **Size:** ~50 GB (approximate)
- **Format:** .wav files, 16 kHz sampling frequency

<div style="background-color: #f8f9fa; border: 2px solid #7c3aed; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #5b21b6; margin-bottom: 15px;">📥 Tidy-X Complete Dataset (Train + Validation)</h4>
  <p style="margin-bottom: 15px;">Click the link below to access the dataset page or download the API script:</p>
  <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; margin-top: 20px;">
    <a href="https://datacollective.mozillafoundation.org/datasets/cmihtsewu023so207xot1iqqw" target="_blank" style="display: inline-block; background-color: #7c3aed; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
      🔗 View Dataset Page
    </a>
    <a href="https://raw.githubusercontent.com/tidylang2026/tidylang2026.github.io/main/download_tidyvoice.py" download style="display: inline-block; background-color: #7c3aed; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
      📥 Download Script
    </a>
  </div>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Available via Mozilla Data Collective</em>
  </p>
</div>

<br>

### Trial Pairs for Validation (Development)

Trial pairs file containing the evaluation protocol for the development/validation set.

<div style="background-color: #f8f9fa; border: 2px solid #ffc107; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #856404; margin-bottom: 15px;">📥 Trial Pairs Download (Development)</h4>
  <p style="margin-bottom: 15px;">Click the link below to download the trial pairs file for the validation set:</p>
  <a href="https://drive.google.com/file/d/1OLEKewhcGi_W_gmqEDpjx-fZwQGz2kWU/view?usp=sharing" target="_blank" style="display: inline-block; background-color: #ffc107; color: #212529; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
    🔗 Download Trial Pairs (trial_pairs_dev.txt)
  </a>
  <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
    <em>Available via Google Drive</em>
  </p>
</div>

<br>

### Evaluation Data

**The evaluation set is not released before the evaluation phase.** Details about the evaluation data (including size, languages, format, and trial structure) are kept confidential to ensure a fair and unbiased benchmark. **We will release the evaluation data and the evaluation trial pair lists when the evaluation phase opens.** At that time, registered participants will receive instructions on how to access the evaluation set and submit results. Please follow the [Important Dates]({{ site.baseurl }}/5_important_dates) and [Registration]({{ site.baseurl }}/10_registration) pages for updates.

<br>

### Trial Pairs for Evaluation

The evaluation trial pair list will be released together with the evaluation data when the evaluation phase opens.

<div style="background-color: #f8f9fa; border: 2px solid #6c757d; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center;">
  <h4 style="color: #495057; margin-bottom: 15px;">📋 Evaluation Trial Pairs</h4>
  <p style="margin-bottom: 15px;">We will release the evaluation data and the evaluation trial pair lists when the evaluation phase opens. The submission format will be published at that time. No details are disclosed beforehand.</p>
  <p style="margin: 0; font-style: italic; color: #6c757d;">Coming soon — stay tuned!</p>
</div>

<br>

## Download Instructions

1. **Registration:** Please complete the [registration process]({{ site.baseurl }}/10_registration/) before downloading the dataset.

2. **Create Mozilla Data Collective API Key:**
   - Visit [https://datacollective.mozillafoundation.org/api-reference](https://datacollective.mozillafoundation.org/api-reference)
   - Navigate to **Profile > API** to create your API credentials
   - Save your API key securely

3. **Install Required Package:**
   ```bash
   pip install datacollective
   ```

4. **Download Using Python Script:**
   Download the [`download_tidyvoice.py`](https://github.com/tidylang2026/tidylang2026.github.io/blob/main/download_tidyvoice.py) script from the dataset download section above, then:
   - Replace `YOUR_API_KEY_HERE` with your Mozilla Data Collective API key
   - Update `OUTPUT_DIR` to your desired download location
   - Run: `python download_tidyvoice.py`

<br>

## Data Structure

The dataset is organized with **speakerID** folders directly inside each dataset folder, which then contain **languageID** subfolders with the corresponding audio files for that speaker in that specific language.

```
Tidy-X_Train/Valid
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

**Structure explanation:**
- **Tidy-X Train:** Training data with speakerID folders at the root
- **Tidy-X Valid:** Validation data with speakerID folders at the root
- Each **speakerID** folder contains all recordings for that speaker
- **languageID** subfolders organize recordings by language (en, fa, fr, de, it, etc.)
- This structure enables easy access to multi-lingual-per-speaker data for language recognition under controlled speaker overlap

<br>

## Support

If you encounter any issues with the dataset download or have questions about the data format, please contact:

- **Email:** aref.farhadipour@uzh.ch

<br>

## Citation

If you use the Tidy-X / TidyVoice dataset in your research, please cite:

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
