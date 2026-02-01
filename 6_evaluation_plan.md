---
layout: page
title: Evaluation Plan
---

## Final Evaluation (per condition)

Participants **must** submit for the **closed-condition**; **open-condition** submission is **optional**. For **each condition** (closed and, if submitted, open), the final evaluation consists of **two tasks**:

### 1. Identification task

- **Data:** A set of utterances.
- **Task:** Predict the language of each utterance.
- **Metric:** Results are reported as **accuracy** (and/or **macro-averaged F1-score**) to ensure balanced performance across languages regardless of sample size.

### 2. Verification task

- **Data:** A set of **trial pairs** (e.g., same-language vs different-language).
- **Task:** Output a similarity or score for each pair.
- **Metric:** Results are reported as **Equal Error Rate (EER)**, following standard verification protocols.

Rankings may be computed per task and/or per condition; details will be specified when the evaluation phase opens.

## Evaluation Protocol

The evaluation will be conducted with a focus on system performance, fairness, and adherence to the challenge protocol. **We will release the evaluation data and the evaluation trial pair lists when the evaluation phase opens.** No details about the evaluation set (size, languages, or trial format) are disclosed beforehand to ensure a fair and unbiased benchmark.

**Important:** Information about the evaluation set will not be disclosed until the evaluation phase begins.

## Development Phase: Validation Set

During the development phase, participants have access to **both**:

- **Identification set:** A set of validation utterances to evaluate language identification (accuracy / macro F1).
- **Verification set:** A set of **trial pairs** to evaluate verification performance (EER).

The validation set shares the same 40 languages and multi-lingual-per-speaker structure as the training set. Validation protocols and trial formats are described on the [Dataset Download]({{ site.baseurl }}/2_dataset_download) and [Baseline Systems]({{ site.baseurl }}/7_baseline_systems) pages.

For information about the official baseline systems, please see the [Baseline Systems]({{ site.baseurl }}/7_baseline_systems) page.
