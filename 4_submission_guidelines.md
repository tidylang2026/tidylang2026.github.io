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

#### **Trial File Format**

The evaluation trial list will be provided as a tab-separated text file. Each line in this file represents a single trial pair to be scored. The format for each line is:

```
enrollment_file    test_file
```

**Example:**
```
spk_A_enroll.wav    test_001.wav
spk_A_enroll.wav    test_002.wav
```

#### **System Output Format**

Participants must submit a output file (.txt format) containing a score for every trial specified in the trial file. The output file must follow the same order as the trial file and add a third column with the similarity score. The format for each line is:

```
enrollment_file    test_file    score
```

**Example:**
```
spk_A_enroll.wav    test_001.wav    0.862
spk_A_enroll.wav    test_002.wav    0.124
```


#### **Contact for Technical Issues**

Should any technical issues arise during the submission process, participants may alternatively submit their results via email. Please contact the organizers (aref.farhadipour@uzh.ch) for further assistance.
