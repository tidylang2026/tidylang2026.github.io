---
layout: page
title: Challenge Task
---

## Challenge Task

The core task of the **TidyVoice Challenge** is **speaker verification**. A system is provided with trial pairs consisting of enrollment data from a target speaker and a test audio segment. The system must then output a single similarity score indicating the likelihood that the two recordings are from the same person. 

## Challenge Phases

The TidyVoice Challenge consists of two phases:

**Development Phase**: This phase is conducted **offline** by participants. During this phase, participants use the provided training and development datasets to develop, train, and tune their systems locally. Participants can experiment with different approaches and evaluate their systems on the development set without any online submission.

**Evaluation Phase**: This phase involves **online ranking** on the CodaBench website. During the evaluation phase, participants will submit their results on the development set through the CodaBench platform. The link to the challenge on CodaBench will be shared with participants during the evaluation phase. Rankings will be determined based on performance on the development set, and participants can view their position on the public leaderboard.

## Provided Dataset: TidyVoiceX

The TidyVoice Challenge is built upon a curated data partition derived from the Mozilla Common Voice (MCV) corpus: **TidyVoiceX**.


**Important**: The use of any other data from the MCV corpus is strictly forbidden. Only the official TidyVoiceX training partition may be used from MCV.

#### **Dataset Statistics**

| Dataset | #Spkr | #Lang | #Utt | Duration (H) | Domain |
|---------|------------|------------|--------------|------------------|--------|
| **TidyVoiceX: Train** | 3,666 | 40 | 262K | 370 | Read |
| **TidyVoiceX: Dev** | 808 | 40 | 60K | 87 | Read |
| <span style="color: #6c757d;">**Final Eval Set**</span> | <span style="color: #6c757d;">2,000</span> | <span style="color: #6c757d;">38</span> | <span style="color: #6c757d;">200K</span> | <span style="color: #6c757d;">300</span> | <span style="color: #6c757d;">Read</span> |


#### **Training Data Regulations**

This is an **open-condition challenge**, and participants are permitted to use any public or private datasets to train their systems, in addition to the provided TidyVoiceX training partition. The use of all non-challenge data must be fully disclosed in the system description paper. 

**Strict restriction on Common Voice data**: The only data permitted from the Mozilla Common Voice (MCV) dataset is the official **TidyVoiceX training partition**. The use of any other data from the MCV corpus is strictly forbidden. The official training data list will be provided on the challenge website.

**Pre-trained models**: Participants are encouraged to use publicly available pre-trained models, including ResNet architectures, self-supervised learning (SSL) models (e.g., wav2vec2, HuBERT, WavLM), and other pre-trained speaker recognition models. All pre-trained models must be explicitly declared in the system description paper.


