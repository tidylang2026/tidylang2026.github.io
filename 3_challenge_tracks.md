---
layout: page
title: Challenge Task
---

## Challenge Task

The core task of the **TidyLang Challenge** is **utterance-level Spoken Language Recognition (SLR)** under controlled speaker-overlap conditions. Systems must predict the language of each utterance. We define two primary evaluation conditions:

- **Closed-set identification:** Participants must predict the correct language label for a set of **40 languages** seen during training. Test utterances may come from speakers already known to the system but speaking different languages.
- **Open-set / zero-shot recognition:** Systems must process **additional languages not seen during training**. This focuses on the model’s ability to generalize to unknown linguistic structures while ignoring familiar speaker-specific acoustic traits.

## Challenge Phases

The TidyLang Challenge consists of two phases:

**Development Phase:** This phase is conducted **offline** by participants. You use the provided training and validation datasets to develop, train, and tune your systems locally. You can experiment with different approaches and evaluate on the validation set without any online submission.

**Evaluation Phase:** This phase involves **online ranking** on the CodaBench website. The **link to the challenge on CodaBench will be shared when the evaluation phase opens**. At that time, the evaluation set and submission procedure will be announced. Rankings will be determined based on performance on the evaluation set, and participants can view their position on the leaderboard.

## Provided Dataset: Tidy-X

The TidyLang Challenge is built upon a curated data partition derived from the Mozilla Common Voice (MCV) corpus: **Tidy-X**. This dataset is specifically designed to emphasize language switching and contains multilingual speakers.

**Important:** The use of any other data from the MCV corpus is strictly forbidden. Only the official Tidy-X training and validation partitions may be used from MCV.

#### **Dataset statistics (training and validation only)**

| Dataset        | # Spkr | # Lang | # Utt  | Duration (h) | Domain |
|----------------|--------|--------|--------|--------------|--------|
| **Tidy-X (Total)** | 4,474  | 40     | 321,711| 457          | Read   |
| **Tidy-X: Train** | 3,666  | 40     | 262K   | 370          | Read   |
| **Tidy-X: Valid** | 808    | 40     | 60K    | 87           | Read   |

Details about the **evaluation set** (e.g., number of languages, speakers, or trials) are **not disclosed** before the evaluation phase. This ensures a fair and unbiased benchmark. Information will be released when the evaluation phase opens.

#### **Training data regulations**

This is an **open-condition challenge**: participants are permitted to use any public or private datasets to train their systems, in addition to the provided Tidy-X training partition. The use of all non-challenge data must be fully disclosed in the system description paper.

**Strict restriction on Common Voice data:** The only data permitted from the Mozilla Common Voice (MCV) dataset is the official **Tidy-X training (and validation) partition**. The use of any other data from the MCV corpus is strictly forbidden.

**Pre-trained models:** Participants are encouraged to use publicly available pre-trained models (e.g., XLS-R, Whisper, wav2vec2, HuBERT, WavLM). All pre-trained models must be explicitly declared in the system description paper.
