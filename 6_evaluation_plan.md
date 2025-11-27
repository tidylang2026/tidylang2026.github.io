---
layout: page
title: Evaluation Plan
---

## Evaluation Metrics

System performance will be ranked based on the following metrics, calculated from the submitted LLR scores:

#### **Primary Metric: Equal Error Rate (EER)**

The primary metric for ranking will be the **Equal Error Rate (EER)**. This will be evaluated on the most challenging condition: **same-speaker, cross-language trials**. Evaluations will be performed on both pooled and per-language subsets to assess overall robustness and language-specific performance.

#### **Secondary Metric: Minimum Detection Cost Function (minDCF)**

The secondary metric is the **Minimum Detection Cost Function (minDCF)**, which provides a cost-weighted combination of false acceptance and false rejection errors. It is defined as:

```
DCF = Cmiss × Pmiss × Ptar + Cfa × Pfa × (1 - Ptar)
```

where:
- *Cmiss* and *Cfa* are the costs of a miss and a false alarm, respectively
- *Pmiss* and *Pfa* are the corresponding error probabilities
- *Ptar* is the prior probability of a target trial

The minimum value of this function over all possible decision thresholds is reported as minDCF.

**Evaluation Setting**: We set *Cmiss* = *Cfa* = 1.0 and *Ptar* = 0.01. This configuration serves as our evaluation setting and is used as a secondary metric for tie-breaking and comprehensive performance analysis.

## Evaluation Protocol

The evaluation will be conducted with a focus on system performance, fairness, and adherence to the challenge protocol. The official test data, along with two trial pair lists for the final evaluation, will be clearly defined and documented on the challenge website.

**Important**: Information about the language of each utterance will not be disclosed during evaluation to ensure fair assessment of language-independent systems.

## Baseline Systems

To provide a strong starting point for participants and ensure a fair and reproducible evaluation, we will publicly release official baseline systems. These systems represent a range of approaches, from training from scratch on the provided data to fine-tuning large, pre-trained models. The goal is to lower the barrier to entry and allow participants to benchmark their own novel methods against these robust baselines.

The three official baseline systems are:
- **ResNet-34 (VB2)**: A powerful model pre-trained on VoxBlink2 (VB2)
- **ResNet-34 (fine-tuned)**: A powerful model pre-trained on VoxBlink2 (VB2) and then fine-tuned on the Tidy-X training partition

We will release the complete training recipes (using the WeSpeaker toolkit), evaluation scripts, and the pre-trained checkpoints for each of these models to the public. These systems and their results serve as a robust reference point against which participants can benchmark their own approaches.
