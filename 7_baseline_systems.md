---
layout: page
title: Baseline Systems
---

## Baseline Systems

To provide a strong starting point for participants and ensure a fair and reproducible evaluation, we will publicly release an official baseline system. This system represents an approach that uses a pre-trained model fine-tuned on the provided data. The goal is to lower the barrier to entry and allow participants to benchmark their own novel methods against this robust baseline.

The official baseline system is implemented using the **WeSpeaker toolkit**, a popular and widely-used toolbox for Automatic Speaker Verification (ASV) tasks. By leveraging this established framework, participants can more easily develop new achievements and build upon existing implementations, as the baseline provides a solid foundation within a familiar ecosystem.

### Baseline Architecture

The baseline system uses a **SimAM-ResNet34** architecture that is:
1. **Pretrained** on VoxBlink2 and VoxCeleb2 datasets
2. **Fine-tuned** on the TidyVoiceX training set using large-margin training

### Baseline Results

The baseline achieves the following overall performance on the TidyVoice development set:

| Architecture | Pretraining Data | Fine-tuning Data | EER (%) | MinDCF | Model |
|:-------------|:----------------|:----------------|:-------:|:------:|:-----:|
| SimAM-ResNet34 | VoxBlink2 + VoxCeleb2 | TidyVoiceX Train | 3.07 | 0.82 | [🤗 Download](https://huggingface.co/areffarhadi/Resnet34-tidyvoiceX-ASV) |

#### Detailed Analysis by Trial Pair Categories

To better understand the baseline system's behavior, we analyze performance across four distinct trial pair scenarios that capture different combinations of speaker identity and language matching:

1. **Target: Same Speaker, Different Languages** vs **Non-target: Different Speakers, Different Languages**
2. **Target: Same Speaker, Different Languages** vs **Non-target: Different Speakers, Same Language**
3. **Target: Same Speaker, Same Language** vs **Non-target: Different Speakers, Different Languages**
4. **Target: Same Speaker, Same Language** vs **Non-target: Different Speakers, Same Language**

The following table presents the Equal Error Rate (EER) for each scenario:

| Trial Pair Category | EER (%) |
|:-------------------|:-------:|
| Target: Same Speaker, Different Languages vs Non-target: Different Speakers, Different Languages | 1.79 |
| Target: Same Speaker, Different Languages vs Non-target: Different Speakers, Same Language | 5.19 |
| Target: Same Speaker, Same Language vs Non-target: Different Speakers, Different Languages | 0.88 |
| Target: Same Speaker, Same Language vs Non-target: Different Speakers, Same Language | 2.97 |
| **Overall (All Targets vs All Non-targets)** | **3.07** |

#### Language Dependency Analysis

The detailed results reveal an important finding: the baseline system exhibits a significant dependency on language information, which should not be a discriminative factor in speaker verification. This is evident from the performance differences across the four scenarios:

- **Best performance (EER: 0.88%)**: When target pairs share the same language and non-target pairs use different languages, the system can leverage language mismatch as a discriminative cue to separate targets from non-targets.

- **Worst performance (EER: 5.19%)**: When target pairs use different languages but non-target pairs share the same language, the system struggles because it cannot rely on language differences to distinguish between target and non-target pairs.

This pattern indicates that the system is relying on language characteristics rather than focusing solely on speaker characteristics, which is problematic for cross-lingual speaker verification. The challenge requires systems to verify speaker identity regardless of language, meaning that language should not serve as a discriminative parameter. This analysis highlights the difficulty of the cross-lingual speaker verification task and provides a clear direction for improvement.

The score distributions for these four trial pair categories are visualized below:

<iframe src="{{ site.baseurl }}/images/speaker_verification_distributions-5.pdf" width="100%" height="600px" style="border: none;"></iframe>

### Resources

We release the complete training recipe (using the WeSpeaker toolkit), evaluation scripts, and the pre-trained checkpoint for this model to the public:

- **Baseline Code Repository**: [https://github.com/areffarhadi/wespeaker/tree/master/examples/tidyvocie](https://github.com/areffarhadi/wespeaker/tree/master/examples/tidyvocie)
- **Model Repository**: [https://huggingface.co/areffarhadi/Resnet34-tidyvoiceX-ASV](https://huggingface.co/areffarhadi/Resnet34-tidyvoiceX-ASV)

This system and its results serve as a robust reference point against which participants can benchmark their own approaches. The use of the WeSpeaker toolkit ensures that participants can easily extend and modify the baseline system to develop novel methods for the challenge.
