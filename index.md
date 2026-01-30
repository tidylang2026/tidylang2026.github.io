---
layout: default
title: TidyLang 2026 Challenge
---



<img src="../images/TidyVoice.png" alt="TidyLang Challenge" width="1000">

<br>

<div style="background-color: #7c3aed; border: 3px solid #5b21b6; border-radius: 12px; padding: 30px; margin: 30px 0; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
  <h2 style="color: white; margin-bottom: 20px; font-size: 28px;">📋 Evaluation Platform (CodaBench)</h2>
  <p style="color: white; font-size: 18px; margin-bottom: 25px;">The link to submit results on CodaBench will be announced when the evaluation phase opens. Please check back later or follow the Important Dates page for updates.</p>
  <p style="color: white; font-size: 16px; font-style: italic;">Coming soon — stay tuned!</p>
</div>

<br>

# **TidyLang Challenge: Speaker-Controlled Language Recognition**

The **TidyLang Challenge** addresses the critical problem of **language recognition when the same speaker speaks multiple languages**. Language recognition systems are typically evaluated under the assumption that speaker identity is a nuisance variable. However, in realistic multilingual environments, speakers often switch languages across different contexts, creating a risk that models rely on speaker-specific traits (“shortcut learning”) rather than robust linguistic cues.

This challenge uses the **Tidy-X dataset**—the same curated, large-scale multilingual corpus derived from Mozilla Common Voice that emphasizes language switching, with **multi-lingual-per-speaker** data (each speaker contributes utterances in 2–10 languages). Participants will build systems that **disentangle speaker identity from language** and generalize to completely **unseen (zero-shot) languages**. Performance is evaluated with **macro-averaged F1/Accuracy** for closed-set language identification and **EER** for open-set/zero-shot recognition.

By providing standardized data, open-source baselines, and a rigorous evaluation protocol, this challenge aims to drive research towards trustworthy, identity-invariant, and linguistically grounded language recognition technologies.

<br>

## Challenge Overview

The TidyLang Challenge is a **Speaker-Controlled and Zero-Shot Language Recognition** challenge. The only permitted data from Mozilla Common Voice is the official **Tidy-X** training and validation partition; all other Common Voice data is strictly forbidden. The core task is **spoken language recognition** at the utterance level under controlled speaker-overlap conditions.

**Primary evaluation conditions:**
- **Closed-set identification:** Predict the correct language label among 40 languages seen during training (macro-averaged F1 / Accuracy).
- **Open-set / zero-shot recognition:** Handle additional languages not seen during training; evaluated with **Equal Error Rate (EER)** following standard protocols.

The challenge uses the **Tidy-X dataset**, a curated partition from Mozilla Common Voice featuring:
- Over 4,474 speakers across 40 languages
- Each speaker with utterances in between 2 and 10 languages
- Approximately 321,711 utterances totaling 457 hours
- Clearly defined training and validation splits
- Pseudonymized speaker identities for privacy

**Evaluation set:** Details about the evaluation data (including size, languages, and trial structure) are **not disclosed** before the evaluation phase to ensure a fair and unbiased benchmark. Information will be released when the evaluation phase opens.

## Challenge Phases

**Development Phase:** Participants use the provided **training and validation data** to develop and tune their systems. You can experiment with different approaches, architectures, and hyperparameters using the official Tidy-X splits.

**Evaluation Phase:** When the evaluation phase opens, the evaluation set and submission procedure (including the CodaBench link) will be announced. Participants will submit results according to the guidelines published at that time. Rankings will be determined based on performance on the evaluation set.

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

- [Odyssey 2026](https://odyssey2026.inesc-id.pt/)
- [Mozilla Common Voice](https://datacollective.mozillafoundation.org/datasets/cmihtsewu023so207xot1iqqw)
- **Contact: Aref Farhadipour (aref.farhadipour@uzh.ch)**

<br>

## Short Description of Image on Main Page

In each speech signal from a single person, we have multiple types of information: the identity of the speaker, the content of the speech, emotional information, language information, etc. In this challenge, we aim to develop systems that, when receiving a speech signal from a human, can **recognize the language** in a way that is **independent of speaker identity**—relying on phonetic and phonotactic cues rather than speaker-specific shortcuts, and generalizing to unseen languages.

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
