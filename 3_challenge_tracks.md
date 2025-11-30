---
layout: page
title: Challenge Task and Dataset
---

## Challenge Task

The core task of the **TidyVoice Challenge** is **speaker verification**. A system is provided with trial pairs consisting of enrollment data from a target speaker and a test audio segment. The system must then output a single score indicating the likelihood that the two recordings are from the same person. This score must be in the form of a **log-likelihood ratio (LLR)**.

The LLR for a given test segment *s* is formally defined as:

```
LLR(s) = log[P(s|H₀) / P(s|H₁)]
```

where *H₀* is the hypothesis that the segment is from the target speaker, and *H₁* is the hypothesis that it is from a different speaker.

## Provided Dataset: TidyVoiceX

The TidyVoice Challenge is built upon a curated data partition derived from the Mozilla Common Voice (MCV) corpus: **TidyVoiceX**.

#### **Official Challenge Dataset (TidyVoiceX)**

The primary and official dataset for this challenge is the **TidyVoiceX partition**. It serves as the core resource for both training and evaluation. TidyVoiceX provides a large-scale, multilingual benchmark specifically designed for cross-lingual speaker verification, featuring a clearly defined training and test split across 40 languages.

**Important**: The use of any other data from the MCV corpus is strictly forbidden. Only the official TidyVoiceX training partition may be used from MCV.

#### **Dataset Statistics**

| Dataset | # Speakers | # Languages | # Utterances | Duration (hours) | Domain |
|---------|------------|------------|--------------|------------------|--------|
| **TidyVoiceX: Train** | 3,666 | 40 | 262K | 370 | Read |
| **TidyVoiceX: Dev** | 808 | 40 | 60K | 87 | Read |
| **Final Eval Set** | 2,000 | 38 | 200K | 300 | Read |

#### **Dataset Characteristics**

- **Multilingual**: Covers approximately 80 distinct languages with around 7,000 multilingual speakers
- **Read Speech**: Based on Mozilla Common Voice, focusing on read speech to minimize stylistic and phonetic variability
- **Privacy-Preserving**: All speaker identities are pseudonymized to protect contributor privacy
- **Cross-Lingual Design**: Specifically curated to isolate the effect of language switching by offering data from the same speaker across different languages
- **Public and Open**: Unlike proprietary benchmarks, TidyVoiceX will be made publicly available alongside the challenge

#### **Training Data Regulations**

This is an **open-condition challenge**, and participants are permitted to use any public or private datasets to train their systems, in addition to the provided TidyVoiceX training partition. The use of all non-challenge data must be fully disclosed in the system description paper. 

**Strict restriction on Common Voice data**: The only data permitted from the Mozilla Common Voice (MCV) dataset is the official **TidyVoiceX training partition**. The use of any other data from the MCV corpus is strictly forbidden. The official training data list will be provided on the challenge website.

**Pre-trained models**: Participants are encouraged to use publicly available pre-trained models, including ResNet architectures, self-supervised learning (SSL) models (e.g., wav2vec2, HuBERT, WavLM), and other pre-trained speaker recognition models. All pre-trained models must be explicitly declared in the system description paper.
