---
layout: page
title: Challenge Task
---

## Challenge Task

The core task of the **TidyLang Challenge** is **utterance-level Spoken Language Recognition (SLR)** under controlled speaker-overlap conditions. Systems must predict the language of each utterance and/or score language verification trial pairs.

**Submission:** Participants **must** submit results for the **closed-condition**. The **open-condition** is **optional**.

**Final evaluation (per condition)** includes two tasks:

- **Identification:** A set of utterances → predict the language of each → reported as **accuracy** (and/or macro F1).
- **Verification:** A set of trial pairs → output a score per pair → reported as **EER**.

During **validation** (development phase), both identification and verification sets are provided so participants can evaluate both tasks locally. See the [Evaluation Plan]({{ site.baseurl }}/6_evaluation_plan) for details.

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

Details about the **evaluation set** (e.g., number of languages, speakers, or trials) are **not disclosed** before the evaluation phase. This ensures a fair and unbiased benchmark. We will release the evaluation data and the evaluation trial pair lists when the evaluation phase opens.

#### **Training data regulations: Closed vs Open condition**

- **Closed-condition (required submission):** Only the official **Tidy-X training (and validation) data** may be used. No other Common Voice data and no LID-specific datasets (e.g., NIST LRE, FLEURS, VoxLingua) are allowed.
- **Open-condition (optional submission):** Still no extra Common Voice data. Participants may use **other data originally intended for LID** (public or private). All such data must be fully disclosed in the system description paper.

**Strict restriction on Common Voice data:** The only data permitted from the Mozilla Common Voice (MCV) dataset is the official **Tidy-X training (and validation) partition**. The use of any other data from the MCV corpus is strictly forbidden in both conditions.

**Pre-trained models:** Participants are free to use publicly available pre-trained/SSL models (e.g., XLS-R, Whisper, wav2vec2, HuBERT, WavLM). All pre-trained models must be explicitly declared in the system description paper.
