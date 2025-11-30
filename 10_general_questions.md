---
layout: default
title: General Questions
---

Frequently asked questions will be listed below.

<br>

#### **Q1. What is the core task of the TidyVoice Challenge?**

The core task is **speaker verification**. Systems must output log-likelihood ratio (LLR) scores indicating whether enrollment and test recordings are from the same person.

#### **Q2. Can I use external datasets for training?**

Yes, this is an **open-condition challenge**. Participants are permitted to use any public or private datasets to train their systems, in addition to the provided TidyVoiceX training partition. However, the use of all non-challenge data must be fully disclosed in the system description paper.

#### **Q3. What is the restriction regarding Mozilla Common Voice (MCV) data?**

**Strict restriction**: The only data permitted from the MCV dataset is the official **TidyVoiceX training partition**. The use of any other data from the MCV corpus is strictly forbidden.

#### **Q4. Can I use pre-trained models?**

Yes, the use of publicly available, pre-trained models is permitted and encouraged. This includes:
- Pre-trained speaker recognition models (e.g., models trained on VoxCeleb, VoxBlink, etc.)
- Pre-trained ResNet architectures
- Self-supervised learning (SSL) models (e.g., wav2vec2, HuBERT, WavLM, etc.)
- Any other publicly available pre-trained models

All pre-trained models used must be explicitly and thoroughly declared in the system description paper, including their source, training data, and how they were integrated into the system.

#### **Q5. Is data augmentation allowed?**

Yes, the use of external, non-speech data for data augmentation (e.g., noise or reverberation from public corpora like MUSAN) is permitted and encouraged, but has to be explicitly and thoroughly disclosed in the system description paper.

#### **Q6. How many submissions can I make?**

Each participating team is allowed to submit scores for a maximum of **three distinct systems** per trial list.

#### **Q7. What evaluation metrics will be used?**

- **Primary Metric**: Equal Error Rate (EER) on same-speaker, cross-language trials
- **Secondary Metric**: Minimum Detection Cost Function (minDCF) with Cmiss = Cfa = 1.0 and Ptar = 0.01

#### **Q8. What is the submission format?**

Participants must submit a tab-separated text file (.txt format) where each line contains:
```
enrollment_file    test_file    score
```

The file must follow the same order as the trial file provided by the organizers.

#### **Q9. Is speaker identification part of this challenge?**

No. This challenge evaluates speaker verification (same/different identity) only. Speaker identification (closed-set or open-set classification among K speakers) is out of scope and will not be scored.

#### **Q10. Can I manually correct or re-label the challenge data?**

No. Manual correction or re-labeling of the officially provided challenge data is strictly prohibited.

#### **Q11. What happens if I try to re-identify speakers or link them to external datasets?**

Any attempt to determine the real-world identity of a speaker, or to link speakers in the challenge data to individuals or records in external datasets, services, or metadata ("data recombination") is strictly forbidden. Violations result in disqualification and notification to the organizers and hosting institutions.

#### **Q12. Do I need to submit a system description paper?**

Yes. To be eligible for inclusion in the final ranking and challenge results, participants must submit a system description paper to the dedicated Interspeech 2026 special session.

#### **Q13. What must be included in the system description paper?**

The system description paper must specify:
- All data usage (including external sets) and preprocessing techniques
- Model architecture and all of its components
- Computational resources and a comprehensive training setup

#### **Q14. What are the reproducibility requirements?**

The top-performing team must submit their trained model and an inference script in a single .zip archive, sufficient to reproduce the reported scores. If results cannot be reproduced, the team will be disqualified and this requirement will pass to the next highest-ranked team.

#### **Q15. Will language information be provided during evaluation?**

No. Information about the language of each utterance will not be disclosed during evaluation to ensure fair assessment of language-independent systems.

#### **Q16. Where can I find the baseline systems?**

Official baseline systems will be released publicly, including complete training recipes (using the WeSpeaker toolkit), evaluation scripts, and pre-trained checkpoints. These will be available on the challenge GitHub repository.

<br>

# Contact

If you have any other questions, please email the organizing committee: **Aref Farhadipour** (aref.farhadipour@uzh.ch).
