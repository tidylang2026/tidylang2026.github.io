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

## Evaluation Tasks

The challenge has **two evaluation tasks**:

### 1. Language identification (35 seen languages)

- **Data:** Utterances from the **35 languages** covered in the training data.
- **Task:** Predict the language of each utterance.
- **Metric:** Participants must report **Macro accuracy** (per-language accuracy averaged over the 35 seen languages).

### 2. Unseen language recognition (40 unseen languages)

- **Data:** Enrollment-based verification. Each **enrollment ID** is represented by **several audio files** whose total duration is **about 20 seconds to at most 65 seconds** per enrollment ID. Each trial compares one enrollment ID with a **test utterance**.
- **Task:** For each trial (enrollment ID, test utterance), output a **similarity or probability score** (e.g. by comparing the test utterance embedding with each enrollment utterance and averaging, or by your own method).
- **Metric:** Results are reported as **Equal Error Rate (EER)**. This task concerns **40 unseen languages** (not seen in the training set).

**More detail** on protocols, trial formats, and submission will be given in the [Evaluation Plan]({{ site.baseurl }}/6_evaluation_plan).

---

### Quick Start

1. **Setup:** Create a virtual environment, install dependencies with `pip install -r requirements.txt`. Dataset and checkpoint paths are set inside the scripts; edit them to match your setup.
2. **Train:** Run `bash train.sh` with default parameters (or override GPU, batch size, epochs, margin, scale, hidden dim as needed).
3. **Evaluate (identification):** Run `bash eval.sh` to evaluate language identification on the validation manifest (flag=2); reports Micro and Macro accuracy.
4. **Evaluate (unseen-language verification):** Edit paths in `eval_enrollment.sh`, then run `bash eval_enrollment.sh` to compute EER on enrollment-based trials (enrollment IDs with 20–65 s of audio, trial pairs).

See the [repository README](https://github.com/areffarhadi/TidyLang2026-baseline) for detailed usage and file formats (manifest, enrollment manifest, trial file).

---

### Model Architecture (Summary)

- **Input:** 16 kHz audio (~4 s per utterance).
- **Backbone:** Wav2Vec2-Large; extract layers 17–24 (1024D each), aggregate with learned weights → 1024D.
- **Projection head:** Linear → LayerNorm → GELU → Dropout(0.1) → Linear → LayerNorm → L2-normalized **256D embeddings**.
- **Classifier:** ArcFace (margin 0.3, scale 30.0) over the number of languages (for identification).

---

### Baseline Results (Default Hyperparameters)

| Task | Metric | Result |
|------|--------|--------|
| **Language identification (35 seen languages)** | Micro Accuracy | **75.76%** |
| **Language identification (35 seen languages)** | Macro Accuracy | **40.25%** |
| **Unseen language recognition (enrollment-based)** | EER | **34.7%** |

- **Identification** is evaluated with `eval.sh` on the validation split (flag=2) of the training manifest (35 languages).
- **Unseen language recognition** is evaluated with `eval_enrollment.sh` using enrollment-based trials: each enrollment ID has 20–65 s of audio (multiple files); for each trial, the test utterance is compared with the enrollment ID (e.g. average similarity over enrollment utterances); EER is computed over the trial scores.

Training uses **flag=1** data only. Validation during training is reported on **flag=2** (identification accuracy, language-recognition EER) and **flag=3** (cross-lingual accuracy). No trials file is used during training; verification (unseen-language EER) is run separately with `eval_enrollment.sh`.

---

### Support

For help and technical support regarding the baseline, contact: **aref.farhadipour@uzh.ch**
