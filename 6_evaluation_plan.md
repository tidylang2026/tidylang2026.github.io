---
layout: page
title: Evaluation Plan
---

## Evaluation Metrics

System performance will be ranked based on the following metrics, calculated from the submitted score file:

#### **Primary Metric: Equal Error Rate (EER)**

The primary metric for ranking will be the **EER**. Evaluations will be reported on both pooled and four types of trial pair subsets to assess overall robustness and language-specific performance. In the evaluation phase, we have two different trial pair lists that all participants must evaluate and submit results for both trial lists. 

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

## Trial Pair Structure

### Development Phase Trial Pairs

The development trial pairs cover four types of pairs to help participants understand how well their systems distinguish between speakers versus languages:

- **Target pairs in the same language**: Same speaker, same language
- **Target pairs in different languages**: Same speaker, different languages
- **Non-target pairs in the same language**: Different speakers, same language
- **Non-target pairs in different languages**: Different speakers, different languages

This variation allows participants to assess how much their system can distinguish between speakers versus how much it is influenced by language differences.

### Evaluation Phase Trial Pairs

In the evaluation phase, participants will be provided with **two different trial pair lists** that all participants must evaluate and submit results for:

1. **Trial List 1**: Contains enrollment utterances from **seen languages** (languages present in the training and development data) and test utterances from **unseen languages** (languages not present in the training and development data).

2. **Trial List 2**: Contains enrollment and test utterances from **unseen languages** only. This list includes 38 unseen languages that are not present in the training and development data.

These trial pair structures are designed to evaluate the ability of systems to eliminate language effects and perform robust speaker verification across languages, including languages that were not encountered during training.

For information about the official baseline systems, please see the [Baseline Systems]({{ site.baseurl }}/7_baseline_systems) page.
