---
layout: page
title: General Questions
---

Frequently asked questions will be listed below.

<br>

#### **Q1. Can participants join both tracks?**
Each team can participate in **only one track** — either **TTS** or **SASV**. Participants cannot join both tracks at the same time.

#### **Q2. When will the test data for evaluation be released?**
For the SASV track, the **test dataset** will be released **after November 15th**, once we receive outputs from the TTS track teams.

#### **Q3. There seems to be an error in Table 1 of the paper regarding TITW-Easy and TITW-Hard sample counts. Which one is correct?**
Yes, there is a typo in **Table 1** of the paper.
The numbers of samples for **TITW-Easy** and **TITW-Hard** are **reversed**.
The correct statistics are:

| **Set**       | **samples** | **Avg dur (s)** | **Tot dur (h)** | **Avg # words** |
| ------------- | ----------- | --------------- | --------------- | --------------- |
| **TITW-Easy** | **248,024** | 2.51            | 173             | 10.55           |
| **TITW-Hard** | **282,606** | 2.42            | 189             | 10.84           |

<br>

# For TTS Track

#### **Q4. Are pretrained datasets and pretrained models allowed on the TTS track?**

Yes, pretrained datasets and models are allowed. However, the **final submitted model must be fine-tuned on the TITW dataset** in the last phase.

#### **Q5. Is it allowed to combine multiple independently trained models during inference (e.g., averaging scores or using stacking)?**

Yes, combining multiple models during inference is allowed.

#### **Q6. Which evaluation metrics will be used for TTS track.**

We will use Versa as our evaluation tool. WER, UTMOS, DNSMOS, and speaker similarity will be calculated using this tool automatically.

<br>

# For SASV Track

#### **Q7. Is it allowed to use external datasets for the SASV track?**
Only the **VoxCeleb2** dataset can be used, as it does not overlap with the **SpoofCeleb** test set.
No other external datasets are permitted for the SASV track.

#### **Q8. Are SSL (Self-Supervised Learning) models allowed?**
Yes, SSL models are allowed.

#### **Q9. Can SSL models be pre-trained on public datasets other than SpoofCeleb and VoxCeleb2?**
Yes, SSL models pre-trained on other **public datasets** are permitted.

#### **Q10. Are there restrictions on the type of SSL models that can be used?**
No, any model that applies self-supervised learning (SSL) is allowed, including but not limited to **wav2vec 2.0**, **HuBERT**, and other SSL-based models.

#### **Q11. Can we use foundation models from other modalities, such as large language models (LLMs) for text processing?**
Yes, the use of **multimodal foundation models**, including **LLMs**, is allowed.

#### **Q12. Can MUSAN/RIR be used for data augmentation?**
Yes, the use of **MUSAN** and **RIR** is permitted for data augmentation.

#### **Q13. Can we use other data augmentation methods beyond MUSAN/RIR (e.g., TTS-based data generation)?**
Yes, it’s acceptable as long as **no additional external datasets** are introduced.

#### **Q14. How will the evaluation score be calculated?**
Each **test utterance** will be paired with one **registration utterance**, following the provided **evaluation protocol** format (a list of <**enroll test_trial** > pairs).

<br>

# Contact

If you have any other questions, please email the organizing committee: **Yihan Wu** (yihanwu@ruc.edu.cn).
