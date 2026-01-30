---
layout: page
title: Baseline Systems
---



## Baseline Systems

To provide a strong starting point for participants and ensure a fair and reproducible evaluation, we plan to release an official baseline system for **language recognition** on the Tidy-X dataset. This system will represent a standard approach (e.g., pre-trained SSL or classifier fine-tuned on the provided data) to lower the barrier to entry and allow participants to benchmark their own methods.

**Baseline resources (code, recipes, and checkpoints) will be published on this page when available.** We will release training recipes, evaluation scripts, and pre-trained checkpoints (where licensing allows) to ensure long-term accessibility.

*Baseline details will be added here as the challenge progresses. Please check back or follow the [Important Dates]({{ site.baseurl }}/5_important_dates) for updates.*

<br>

### Planned Contents

- **Baseline architecture:** e.g., self-supervised model (XLS-R, Whisper, wav2vec2, etc.) with a language classification head, fine-tuned on Tidy-X Train
- **Training recipe:** Scripts and configuration for reproducing the baseline
- **Validation set results:** Macro F1 / Accuracy on Tidy-X Valid (closed-set) and any validation protocol we provide
- **Evaluation:** Evaluation set results will be reported after the evaluation phase, in line with the challenge timeline

If you have questions about baselines or evaluation scripts, please contact the organizers (see [Organizers]({{ site.baseurl }}/8_organizers)).
