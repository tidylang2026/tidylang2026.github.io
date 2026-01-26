---
layout: page
title: Submission Guidelines
---

## Rules for Participation

To ensure a fair and standardized evaluation, all participants must adhere to the following rules:

#### **1. Training Data Regulations**

- This is an **open-condition challenge**, and participants are permitted to use any public or private datasets to train their systems, in addition to the provided TidyVoiceX training partition. The use of all non-challenge data must be fully disclosed in the system description paper.
- **Strict restriction on Common Voice data**: The only data permitted from the Mozilla Common Voice (MCV) dataset is the official **TidyVoiceX dataset**, as defined in the Challenge Task and Dataset section. The use of any other data from the MCV corpus is strictly forbidden. 

#### **2. Prohibition of Re-identification and Data Recombination**

Any attempt to determine the real-world identity of a speaker, or to link speakers in the challenge data to individuals or records in external datasets, services, or metadata ("data recombination") is strictly forbidden. This includes (but is not limited to) voiceprint matching against external corpora, cross-dataset record linkage, or the use of personally identifying metadata. Violations result in disqualification and notification to the organizers and hosting institutions.

#### **3. Scope of Tasks: Verification Only**

This challenge evaluates speaker verification (same/different identity) on the provided splits. Speaker identification (closed-set or open-set classification among K speakers) is out of scope and will not be scored.

#### **4. Data Integrity**

Manual correction or re-labeling of the officially provided challenge data is strictly prohibited.

#### **5. Use of Pre-trained Models**

The use of publicly available, pre-trained models is permitted and encouraged. This includes (but is not limited to):
- Pre-trained speaker recognition models (e.g., models trained on VoxCeleb, VoxBlink, etc.)
- Self-supervised learning (SSL) models (e.g., wav2vec2, HuBERT, WavLM, etc.)
- Any other publicly available pre-trained models

All pre-trained models used must be explicitly and thoroughly declared in the system description paper, including their source, training data, and how they were integrated into the system.

#### **6. Data Augmentation**

The use of external, non-speech data for data augmentation (e.g., noise or reverberation from public corpora like MUSAN) is permitted and encouraged, but has to be explicitly and thoroughly disclosed in the system description paper.

#### **7. Submission Process**

Each participating team should submit the results on the **evaluation set** to the CodaBench platform that will be shared during the evaluation phase.

#### **8. Eligibility for Final Ranking**

To be eligible for inclusion in the final ranking and challenge results, participants must submit a system description paper to the dedicated Interspeech 2026 special session.

#### **9. System Description**

Each submission must be accompanied by a detailed system description paper in the [Interspeech format](https://www.overleaf.com/latex/templates/interspeech-paper-kit/svqkgcpdbxfg) that specifies:
- All data usage (including external sets) and preprocessing techniques
- Model architecture and all of its components
- Computational resources and a comprehensive training setup



## Submission Format

The following guidelines for preparing submission files and viewing results apply to the **TidyVoice Challenge 2026** competition on CodaBench: [https://www.codabench.org/competitions/13187/](https://www.codabench.org/competitions/13187/). Please submit your results and check the leaderboard on that page.

### Overview
Participants must submit a **single ZIP file** containing similarity scores for both trial lists. To minimize file size, submissions contain **only the scores** (one per line), without the trial pair names. Scores must be in the **exact same order** as the trial lists.

### Required Files
Your submission ZIP must contain exactly **two files**:

```
submission.zip
├── tv26_eval-A.txt    # Scores for Trial List 1 (4,000,000 lines)
└── tv26_eval-U.txt    # Scores for Trial List 2 (1,280,000 lines)
```

### File Format
Each file contains **one score per line**:
- `tv26_eval-A.txt`: 4,000,000 scores (one per trial in Trial List 1)
- `tv26_eval-U.txt`: 1,280,000 scores (one per trial in Trial List 2)

**Example (first 5 lines of tv26_eval-A.txt):**

```
0.012345
0.123456
0.234567
0.345678
0.456789
```

#### Format Requirements

| Requirement | Description |
|-------------|-------------|
| **Score format** | Floating point number (e.g., `0.862541` or `-1.234`) |
| **One score per line** | No additional columns, tabs, or spaces |
| **Exact line count** | Must match the trial list exactly |
| **No header** | Start directly with scores |
| **Correct order** | Scores must correspond to trials in the same order as provided |

⚠️ **Important:** Higher scores indicate higher likelihood that the two utterances are from the same speaker.

### Validation Script (Recommended)

**Because the website is sensitive to the exact format, naming, and folder structure of submission files**, we strongly recommend using our automated validation script to generate your submission file.

#### Using the Validation Script

The validation script is available at:  
[prepare_submission.py](https://github.com/tidyvoice2026/tidyvoice2026.github.io/blob/main/prepare_submission.py)

#### How It Works

This script assumes your score file contains **three columns** (enrollment, test, score) **without headers**. The script will:

1. Read your score file with three columns (space separated): `enroll`, `test`, `score`
2. Compare it with the original trial pair files we provided
3. Generate the correct submission format
4. Verify the order of scores matches the trial lists
5. Create properly formatted `tv26_eval-A.txt` and `tv26_eval-U.txt` files
6. Create the .zip file


**We highly recommend using this code to generate your submission file to avoid formatting issues that could result in error on the CodaBench website.**

### After Submission

Submit your ZIP file on the [TidyVoice Challenge 2026 CodaBench competition page](https://www.codabench.org/competitions/13187/). If your submission is correctly formatted, you will see the **EER% for `tv26_eval-A.txt`** displayed automatically.

#### Viewing Complete Results

To view the **EER% for `tv26_eval-U.txt`** and **minDCFs** for both trial lists on CodaBench:

1. Go to [https://www.codabench.org/competitions/13187/](https://www.codabench.org/competitions/13187/)
2. Click on the **"File name"** of your submission
3. Navigate to **"LOGS"**
4. Open **"Scoring logs"**

This will display the complete evaluation metrics for your submission.

#### **Contact for Technical Issues**

Should any technical issues arise during the submission process, participants may alternatively submit their results via email. Please contact the organizers (aref.farhadipour@uzh.ch) for further assistance.
