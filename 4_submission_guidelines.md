---
layout: page
title: Submission Guidelines
---

## Rules for Participation

To ensure a fair and standardized evaluation, all participants must adhere to the following rules:

#### **1. Training Data Regulations**

- This is an **open-condition challenge**. Participants are permitted to use any public or private datasets to train their systems, in addition to the provided Tidy-X training partition. The use of all non-challenge data must be fully disclosed in the system description paper.
- **Strict restriction on Common Voice data:** The only data permitted from the Mozilla Common Voice (MCV) dataset is the official **Tidy-X dataset** (train and validation), as defined on the Challenge Task and Dataset pages. The use of any other data from the MCV corpus is strictly forbidden.

#### **2. Prohibition of Re-identification and Data Recombination**

Any attempt to determine the real-world identity of a speaker, or to link speakers in the challenge data to individuals or records in external datasets, services, or metadata (“data recombination”) is strictly forbidden. This includes (but is not limited to) voiceprint matching against external corpora, cross-dataset record linkage, or the use of personally identifying metadata. Violations result in disqualification and notification to the organizers and hosting institutions.

#### **3. Scope of Tasks: Language Recognition**

This challenge evaluates **spoken language recognition** on the provided splits. Participants **must** submit for the **closed-condition**; **open-condition** submission is **optional**. For each condition, the final evaluation consists of **two tasks**: (1) **Identification**—predicting the language of each utterance (accuracy / macro F1); (2) **Verification**—scoring trial pairs (same-language vs different-language) with results reported as EER. The exact submission format (e.g., language labels for identification, scores for verification) will be specified when the evaluation phase opens.

#### **4. Data Integrity**

Manual correction or re-labeling of the officially provided challenge data is strictly prohibited.

#### **5. Use of Pre-trained Models**

The use of publicly available, pre-trained models is permitted and encouraged. This includes (but is not limited to):
- Self-supervised learning (SSL) models (e.g., wav2vec2, HuBERT, WavLM, XLS-R, Whisper)
- Other publicly available speech or language models

All pre-trained models used must be explicitly and thoroughly declared in the system description paper, including their source, training data, and how they were integrated into the system.

#### **6. Data Augmentation**

The use of external, non-speech data for data augmentation (e.g., noise or reverberation from public corpora like MUSAN) is permitted and encouraged, but must be explicitly and thoroughly disclosed in the system description paper.

#### **7. Submission Process**

Each participating team must submit results on the **evaluation set** via the **CodaBench platform**. The **link to the CodaBench competition will be announced when the evaluation phase opens**. Until then, submission format, file names, and exact procedures are not finalized. Please check the [Important Dates]({{ site.baseurl }}/5_important_dates) and this page for updates.

#### **8. Eligibility for Final Ranking**

To be eligible for inclusion in the final ranking and challenge results, participants must submit a system description paper to the dedicated Odyssey 2026 workshop.

#### **9. System Description**

Each submission must be accompanied by a detailed system description paper in the [Odyssey / Interspeech format](https://www.overleaf.com/latex/templates/interspeech-paper-kit/svqkgcpdbxfg) that specifies:
- All data usage (including external sets) and preprocessing techniques
- Model architecture and all of its components
- Computational resources and a comprehensive training setup

<br>

## Submission Format (Evaluation Phase)

**The exact submission format (file names, structure, and content) will be published when the evaluation phase opens.** At that time we will provide:

- The **CodaBench competition link** for the TidyLang 2026 Challenge
- Required file format(s) for both tasks: **identification** (e.g., language labels per utterance) and **verification** (e.g., scores per trial pair), as specified when the evaluation phase opens
- Validation scripts (if any) to check submissions locally

We will release the evaluation data and the evaluation trial pair lists when the evaluation phase opens. Until then, we do not disclose details about the evaluation set or submission files. Please check back when the evaluation phase begins (see [Important Dates]({{ site.baseurl }}/5_important_dates)).

<br>

## CodaBench

The **CodaBench platform** will host the leaderboard and submission system for the TidyLang 2026 Challenge. The competition link is **not yet available** and will be shared with registered participants when the evaluation phase opens. We will post the link on this website and communicate it via the registration contact information.

*Coming soon — stay tuned!*
