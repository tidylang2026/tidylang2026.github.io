---
layout: page
title: Baseline Systems
---

## Baseline Systems

We provide an **official baseline** for the TidyLang 2026 Challenge: a complete toolbox for training and evaluating a **Language Identification (LID)** model. The baseline uses **Wav2Vec2 (Layers 17–24)** + a simple projection head + **ArcFace loss**, and achieves strong performance on the TidyLang dataset.

### GitHub Repository

**Code, recipes, and documentation:**  
**[https://github.com/areffarhadi/TidyLang2026-baseline](https://github.com/areffarhadi/TidyLang2026-baseline)**

Clone the repository for training scripts, evaluation scripts, ArcFace loss implementation, and full setup instructions.

---

### Quick Start

1. **Setup:** Create a virtual environment, install dependencies with `pip install -r requirements.txt`. Dataset paths are pre-configured; no environment variables are required.
2. **Train:** Run `bash train.sh` with default parameters (or override GPU, batch size, epochs, margin, scale, hidden dim as needed).
3. **Evaluate:** Run `bash eval.sh` to evaluate with default settings.

See the [repository README](https://github.com/areffarhadi/TidyLang2026-baseline) for detailed usage and optional arguments.

---

### Model Architecture (Summary)

- **Input:** 16 kHz audio (~4 s).
- **Backbone:** Wav2Vec2-Large; extract layers 17–24 (1024D each), aggregate with learned weights → 1024D.
- **Projection head:** Linear → LayerNorm → GELU → Dropout(0.1) → Linear → LayerNorm → L2-normalized **256D embeddings**.
- **Classifier:** ArcFace (margin 0.3, scale 30.0) over the number of languages.

---

### Baseline Results (Default Hyperparameters)

| Metric | Result |
|--------|--------|
| **Classification (flag=2, new speakers)** | Micro Acc: 75.8%, Macro Acc: 40.3% |
| **Cross-lingual (flag=3, known speakers, different language)** | Micro Acc: 58.5%, Macro Acc: 57.7% |
| **Language verification EER (flag=2, same vs different language)** | EER: 23.68%, Threshold: 0.745 |
| **Speaker verification EER (5-language trials)** | EER: 30.7%, Threshold: 0.754 |

The **challenge evaluation** uses **language verification** (same-language vs different-language trial pairs, EER). The baseline reports language identification (accuracy), language verification EER, and optionally speaker verification EER for related analysis. Training uses **flag=1** data only; validation is reported on **flag=2** (new speakers) and **flag=3** (cross-lingual). The repo includes manifest/trial formats and verification trial details.

---

### Support

For help and technical support regarding the baseline, contact: **aref.farhadipour@uzh.ch**

For general challenge questions, see [Organizers]({{ site.baseurl }}/8_organizers).
