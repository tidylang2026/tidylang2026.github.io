---
layout: default
title: TidyVoice2026 Challenge
---



<img src="../images/TidyVoice.png" alt="WildSpoof Image" width="1000">

<br>

<div style="background-color: #7c3aed; border: 3px solid #5b21b6; border-radius: 12px; padding: 30px; margin: 30px 0; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
  <h2 style="color: white; margin-bottom: 20px; font-size: 28px;">🚀 Submit Your Results on CodaBench!</h2>
  <p style="color: white; font-size: 18px; margin-bottom: 25px;">The evaluation phase is now open. Submit your system's results and compete on the leaderboard!</p>
  <a href="https://www.codabench.org/competitions/13187/" target="_blank" style="display: inline-block; background-color: white; color: #7c3aed; padding: 15px 40px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 20px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);">
    📊 Go to CodaBench Evaluation Platform
  </a>
</div>

<div style="background-color: #f0fdf4; border-left: 5px solid #22c55e; padding: 20px; margin: 25px 0; border-radius: 5px;">
  <p style="margin: 0; color: #166534; font-size: 16px;">
    <strong>📢 [UPDATE] [26.1.2026]</strong> Evaluation set released! Please follow 
    <a href="https://tidyvoice2026.github.io/2_dataset_download/" style="color: #16a34a; text-decoration: underline;">Dataset Download page</a> 
    for downloading the Eval data and 
    <a href="https://tidyvoice2026.github.io/4_submission_guidelines/" style="color: #16a34a; text-decoration: underline;">Submission Guidelines page</a> 
    for submission instructions.
  </p>
</div>

<br>

# **TidyVoice Challenge: Cross-Lingual Speaker Verification**

The **TidyVoice Challenge** addresses the critical open problem of speaker verification under language mismatch. The performance of speaker verification systems degrades significantly under language mismatch, a critical challenge exacerbated by the field's reliance on English-centric data. 

This challenge leverages the **TidyVoiceX dataset** from the novel TidyVoice benchmark, a large-scale, multilingual corpus derived from Mozilla Common Voice dataset, and specifically curated to isolate the effect of language switching across around 40 languages. Participants will be tasked with building systems robust to this mismatch, with performance primarily evaluated using the Equal Error Rate (EER) on cross-language trials.

By providing standardized data, open-source baselines, and a rigorous evaluation protocol, this challenge aims to drive research towards fairer, more inclusive, and language-independent speaker recognition technologies.



<br>



## Challenge Overview

The TidyVoice Challenge is an **open-condition challenge** where participants are permitted to use any public or private datasets to train their systems, in addition to the provided TidyVoiceX training partition. Participants are also encouraged to use pre-trained models (e.g., ResNet, SSL models such as wav2vec2, WavLM, etc.). The only restriction is that **only the official TidyVoiceX training partition may be used from the Mozilla Common Voice dataset**; all other Common Voice data is strictly forbidden. The core task is **speaker verification** - systems must output similarity score.

**Primary Evaluation Metric**: Equal Error Rate (EER).

**Secondary Metric**: Minimum Detection Cost Function (minDCF) for comprehensive performance analysis.

The challenge uses the **TidyVoiceX dataset**, a curated partition from Mozilla Common Voice dataset featuring:
- Over 4,474 speakers across 40 languages
- Approximately 321,711 utterances totaling 457 hours
- Clearly defined training and test splits
- Pseudonymized speaker identities for privacy protection

For evaluation, the challenge provides **TidyVoiceX2_ASV**, an evaluation dataset with:
- Approximately 2,000 speakers across 38 additional languages
- 32 GB of audio data in .wav format (16KHz sampling frequency)
- Two trial pair lists: tv26_eval-A.txt (4M trials) and tv26_eval-U.txt (1.28M trials)
- Coverage of unseen languages for robust cross-lingual evaluation

## Challenge Phases

The TidyVoice Challenge is organized in two main phases:

**Development Phase**: During this phase, participants will use the provided **training and development datasets** to develop and tune their systems. Participants can experiment with different approaches, architectures, and hyperparameters using both the training and development data.

**Validation Phase**: In this phase, the development dataset will be released with ground truth labels. Participants will submit their results on the development set by uploading them to the **CodaBench website**. The ranking will be determined based on the performance on the development set, allowing participants to compare their systems against others on the leaderboard.

## Trial Pair Structure

**Development Phase**: The development trial pairs include four types to help participants assess how well their systems distinguish between speakers versus languages:
- Target pairs (same speaker, same language)
- Target pairs (same speaker, different languages)
- Non-target pairs (different speakers, same language)
- Non-target pairs (different speakers, different languages)

**Evaluation Phase**: Participants will evaluate and submit results for two trial pair lists:
- **tv26_eval-A.txt** (All languages): Mix of seen and unseen languages (All the languages)
- **tv26_eval-U.txt** (Unseen languages): Both enrollment and test from unseen languages (38 unseen languages)

These trial structures are designed to evaluate systems' ability to eliminate language effects and perform robust speaker verification across languages, including languages not encountered during training.

## Learn More

- **Challenge Description**: [Challenge Description]({{ site.baseurl }}/1_challenge_description)
- **Dataset Download**: [Dataset Download]({{ site.baseurl }}/2_dataset_download)
- **Challenge Task**: [Challenge Task]({{ site.baseurl }}/3_challenge_tracks)
- **Submission Guidelines**: [Submission Guidelines]({{ site.baseurl }}/4_submission_guidelines)
- **Important Dates**: [Important Dates]({{ site.baseurl }}/5_important_dates)
- **Evaluation Plan**: [Evaluation Plan]({{ site.baseurl }}/6_evaluation_plan)
- **Baseline Systems**: [Baseline Systems]({{ site.baseurl }}/7_baseline_systems)
- **Organizers**: [Organizers]({{ site.baseurl }}/8_organizers)
- **Registration**: [Registration]({{ site.baseurl }}/10_registration)

<br>



## Relevant Links

- [Interspeech2026](https://interspeech2026.org/en-AU)
- [Mozilla Common Voice](https://datacollective.mozillafoundation.org/datasets/cmihtsewu023so207xot1iqqw)
- **Contact: Aref Farhadipour (aref.farhadipour@uzh.ch)**


<br>

## Short Description of Image on Main Page

In each speech signal from a single person, we have multiple types of information: the identity of the speaker, the content of the speech, emotional information, language information, etc. In this challenge, we aim to develop systems that, when receiving a speech signal from a human, can **eliminate the language effect** in the speech utterance and perform speaker verification in a language-independent manner.

*This image was generated and edited using Runway and Qwen-VL models.*

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





