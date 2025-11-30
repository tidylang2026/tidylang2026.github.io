---
layout: default
title: TidyVoice2026 Challenge
---



<img src="../images/TidyVoice.png" alt="WildSpoof Image" width="1000">

 

# **TidyVoice Challenge: Cross-Lingual Speaker Verification**

The **TidyVoice Challenge** addresses the critical open problem of speaker verification under language mismatch. The performance of speaker verification systems degrades significantly under language mismatch, a critical challenge exacerbated by the field's reliance on English-centric data. 

This challenge leverages the **TidyVoiceX dataset** from the novel TidyVoice benchmark, a large-scale, multilingual corpus derived from Mozilla Common Voice dataset, and specifically curated to isolate the effect of language switching across around 40 languages. Participants will be tasked with building systems robust to this mismatch, with performance primarily evaluated using the Equal Error Rate (EER) on cross-language trials.

By providing standardized data, open-source baselines, and a rigorous evaluation protocol, this challenge aims to drive research towards fairer, more inclusive, and language-independent speaker recognition technologies.



<br>



## Why Participate

- **Address a Key Scientific Gap**: The TidyVoice dataset uniquely isolates the impact of language switching by offering curated data from the same speaker across different languages, enabling focused investigation into truly language-independent speaker embeddings.
- **Promote Fairness and Inclusivity**: Built upon a dataset encompassing approximately 80 distinct languages and around 7000 multilingual speakers, motivating systems that are not biased towards a single language.
- **Access a New Public Resource**: Unlike proprietary benchmarks, the TidyVoice dataset, evaluation protocols, and baseline models will be made publicly available, promoting reproducible research.
- **Establish a Benchmark**: By being based on Mozilla Common Voice, this challenge focuses on read speech, providing a controlled setting for precise analysis of cross-lingual acoustic modeling.
- **Benchmark Your Models**: Compare your systems alongside international teams in an official Interspeech 2026 challenge.



<br>



## Challenge Overview

The TidyVoice Challenge is an **open-condition challenge** where participants are permitted to use any public or private datasets to train their systems, in addition to the provided TidyVoiceX training partition. Participants are also encouraged to use pre-trained models (e.g., ResNet, SSL models such as wav2vec2, HuBERT, etc.). The only restriction is that **only the official TidyVoiceX training partition may be used from the Mozilla Common Voice dataset**; all other Common Voice data is strictly forbidden. The core task is **speaker verification** - systems must output log-likelihood ratio (LLR) scores indicating whether enrollment and test recordings are from the same person.

**Primary Evaluation Metric**: Equal Error Rate (EER) on same-speaker, cross-language trials.

**Secondary Metric**: Minimum Detection Cost Function (minDCF) for comprehensive performance analysis.

The challenge uses the **TidyVoiceX dataset**, a curated partition from Mozilla Common Voice featuring:
- Over 4,474 speakers across 40 languages
- Approximately 321,711 utterances totaling 457 hours
- Clearly defined training and test splits
- Pseudonymized speaker identities for privacy protection



<br>



## Relevant Links

- [Interspeech2026](https://interspeech2026.org/en-AU)
- [Mozilla Common Voice](https://datacollective.mozillafoundation.org/datasets/cmihtsewu023so207xot1iqqw)
- Contact: Aref Farhadipour (aref.farhadipour@uzh.ch)



<br>



## Collaborating Organizations

<div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 30px; margin: 40px 0; padding: 20px;">
  <div style="text-align: center;">
    <img src="images/logo/Universität_Zürich_logo.svg" alt="University of Zürich" style="height: 160px; max-width: 500px; object-fit: contain;">
  </div>
  <div style="text-align: center;">
    <img src="images/logo/OVGU-Logo.svg" alt="Otto-von-Guericke University Magdeburg" style="height: 80px; max-width: 200px; object-fit: contain;">
  </div>
  <div style="text-align: center;">
    <img src="images/logo/ANU_Primary_Horizontal_Black.png" alt="Australian National University" style="height: 80px; max-width: 200px; object-fit: contain;">
  </div>
  <div style="text-align: center;">
    <img src="images/logo/Indiana_University_logotype.svg" alt="Indiana University" style="height: 80px; max-width: 200px; object-fit: contain;">
  </div>
  <div style="text-align: center;">
    <img src="images/logo/logo.png" alt="Collaborating Institution" style="height: 80px; max-width: 200px; object-fit: contain;">
  </div>
</div>





