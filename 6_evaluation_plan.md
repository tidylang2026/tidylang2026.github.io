---
layout: page
title: Evaluation Plan
---

## Final Evaluation (per condition)

Participants **must** submit for the **closed-condition**; **open-condition** submission is **optional**. For **each condition** (closed and, if submitted, open), the final evaluation consists of **two tasks**:

### 1. Language identification (35 seen languages)

- **Data:** A set of utterances from the **35 languages** covered in the training data.
- **Task:** Predict the language of each utterance.
- **Metric:** Participants must report **Macro accuracy** (per-language accuracy averaged over the 35 seen languages).

### 2. Unseen language recognition (40 unseen languages)

- **Data:** **Enrollment-based** verification. Each **enrollment ID** is represented by several audio files totaling **about 20 to at most 65 seconds** per ID. Each trial compares one enrollment ID with a **test utterance**.
- **Task:** For each trial (enrollment ID, test utterance), output a **similarity or probability score**.
- **Metric:** Results are reported as **Equal Error Rate (EER)**. This task concerns **40 unseen languages**.

More detail on protocols, trial formats, and submission will be specified in the full evaluation plan and on the [Baseline Systems]({{ site.baseurl }}/7_baseline_systems) page.

Rankings may be computed per task and/or per condition; details will be specified when the evaluation phase opens.

## Evaluation Protocol

The evaluation will be conducted with a focus on system performance, fairness, and adherence to the challenge protocol. **We will release the evaluation data and the evaluation trial pair lists when the evaluation phase opens.** No details about the evaluation set (size, languages, or trial format) are disclosed beforehand to ensure a fair and unbiased benchmark.

**Important:** Information about the evaluation set will not be disclosed until the evaluation phase begins.

## Development Phase: Validation Set

During the development phase, participants have access to **both**:

- **Identification set:** A set of validation utterances (35 seen languages) to evaluate language identification (**Macro accuracy**).
- **Verification set:** An **enrollment-based** set: enrollment IDs (20–65 s of audio per ID) and a **trial file** (enrollment ID, test utterance) to evaluate unseen language recognition (**EER**).

The validation set shares the same 40 languages and multi-lingual-per-speaker structure as the training set. Validation protocols and trial formats are described on the [Dataset Download]({{ site.baseurl }}/2_dataset_download) and [Baseline Systems]({{ site.baseurl }}/7_baseline_systems) pages.

For information about the official baseline systems, please see the [Baseline Systems]({{ site.baseurl }}/7_baseline_systems) page.
