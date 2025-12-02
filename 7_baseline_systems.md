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

The baseline achieves the following performance on the TidyVoice development set:

| Architecture | Pretraining Data | Fine-tuning Data | EER (%) | MinDCF | Model |
|:-------------|:----------------|:----------------|:-------:|:------:|:-----:|
| SimAM-ResNet34 | VoxBlink2 + VoxCeleb2 | TidyVoiceX Train | 3.07 | 0.82 | [🤗 Download](https://huggingface.co/areffarhadi/Resnet34-tidyvoiceX-ASV) |

These results demonstrate the baseline's capability to handle cross-lingual speaker verification tasks.

### Resources

We release the complete training recipe (using the WeSpeaker toolkit), evaluation scripts, and the pre-trained checkpoint for this model to the public:

- **Baseline Code Repository**: [https://github.com/areffarhadi/wespeaker/tree/master/examples/tidyvocie](https://github.com/areffarhadi/wespeaker/tree/master/examples/tidyvocie)
- **Model Repository**: [https://huggingface.co/areffarhadi/Resnet34-tidyvoiceX-ASV](https://huggingface.co/areffarhadi/Resnet34-tidyvoiceX-ASV)

This system and its results serve as a robust reference point against which participants can benchmark their own approaches. The use of the WeSpeaker toolkit ensures that participants can easily extend and modify the baseline system to develop novel methods for the challenge.
