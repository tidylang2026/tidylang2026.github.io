---
layout: page
title: Registration
---

<div style="text-align: center; padding: 24px; margin-bottom: 24px; border: 2px solid #7c3aed; border-radius: 8px; background-color: #f5f3ff;">
  <p style="margin: 0; font-size: 1.1em;"><strong>Registration form</strong></p>
  <p style="margin: 12px 0 0 0;">You can fill and submit the registration form through <a href="https://forms.gle/uV3zoapEe4A8knc16">this link</a>.</p>
</div>

<hr style="border: none; border-top: 2px solid #7c3aed; margin: 2em 0;">

If you are registering during the Evaluation phase (26 Jan – 10 Feb), this information lets you join the competition faster.

1. **Evaluation data:** You can download the evaluation data from [TidyVoiceX2_ASV](https://datacollective.mozillafoundation.org/datasets/cmkv32i5e02tumg07j79d3c35). The easiest way to download the files is described on the [Dataset Download](https://tidyvoice2026.github.io/2_dataset_download/) page.

2. **Trial pairs:** The trial pairs files can be downloaded [here](https://drive.google.com/file/d/1tIFjYnRHGLypciX4Dl7IBX86vymAnVRP/view?usp=sharing). There are two trial pair files:
   - **tv26_eval-A.txt** — trial pairs in a mix of All languages (compared to the training set)
   - **tv26_eval-U.txt** — trial pairs where all utterances are in Unseen languages (compared to the training set)

3. **CodaBench:** During the evaluation phase, you can monitor the performance of your system. Please visit the [CodaBench page for the TidyVoice Challenge](https://www.codabench.org/competitions/13187/) and register for the evaluation. Each team has 5 tokens to submit the scores of their proposed systems (up to 5 submissions). The final score for each team will be based on its best-performing submission.

4. **Submission format:** Please read the [Submission Guidelines](https://tidyvoice2026.github.io/4_submission_guidelines/) carefully to understand the required format of the submission file and how to view the results (EER and minDCF) for both trial pair files. Participants must submit a single zip file containing two score files (one per trial file). Each score file must contain only the scores, in the same order as the trial pairs, without file names or headers, and must use the same names as the corresponding trial files. If the format is incorrect, CodaBench will return an error and one submission token will be used. We provide a [prepare_submission.py](https://github.com/tidyvoice2026/tidyvoice2026.github.io/blob/main/prepare_submission.py) script to build and validate your submission file; we recommend using it.

5. **Privacy:** During the evaluation phase, participants can only see their own results. The results of other teams are not visible.

6. **Rankings:** After the evaluation phase, we will release the final rankings. There will be a separate leaderboard for each trial pair file. To be included, you must submit results for both trial pairs. The announcement will be made anonymously with an identity code. Participants may share their team code in their papers or with us, and we can feature it on the website.

7. **Deadline:** The evaluation phase ends on **February 10, 2026**.

Please feel free to contact us if you need any help.

Good luck and enjoy the challenge!

Best regards,  
TidyVoice Organization Team