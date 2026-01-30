---
layout: page
title: Evaluation Plan
---

## Evaluation Metrics

System performance will be ranked based on the following metrics:

#### **Closed-set: Macro-averaged F1-Score / Accuracy**

For the **40-language closed-set** language identification task, we use **macro-averaged F1-score** and **accuracy** to ensure balanced performance across all languages regardless of sample size.

#### **Open-set / zero-shot: Equal Error Rate (EER)**

For the **open-set / zero-shot** recognition task (e.g., detecting whether an utterance belongs to a specific target unseen language), we use the **Equal Error Rate (EER)**, following standard NIST LRE-style protocols.

Further details on how these metrics are applied (e.g., number of conditions, trial structure) will be specified when the evaluation phase opens.

## Evaluation Protocol

The evaluation will be conducted with a focus on system performance, fairness, and adherence to the challenge protocol. The **official evaluation dataset and trial structure will be released when the evaluation phase opens**. No details about the evaluation set (size, languages, or trial format) are disclosed beforehand to ensure a fair and unbiased benchmark.

**Important:** Information about the evaluation set will not be disclosed until the evaluation phase begins.

## Development Phase: Validation Set

During the development phase, participants can use the provided **validation set** (Tidy-X Valid) to tune and compare systems. The validation set shares the same 40 languages and multi-lingual-per-speaker structure as the training set. Validation trial or evaluation protocols (if any) will be described on the Dataset Download and Baseline Systems pages.

For information about the official baseline systems, please see the [Baseline Systems]({{ site.baseurl }}/7_baseline_systems) page.
