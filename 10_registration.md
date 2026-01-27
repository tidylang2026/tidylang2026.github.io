---
layout: page
title: Registration
---





You can fill and submit the registration form through [this link](https://forms.gle/uV3zoapEe4A8knc16)!


If you are registering during the Evaluation phase (26 Jan - 10 Feb), this information lets you join the competition faster.


1. You can download the evaluation data [https://datacollective.mozillafoundation.org/datasets/cmkv32i5e02tumg07j79d3c35]. The easiest way to download the files is described [here].

2. The trial pairs files can be downloaded [https://drive.google.com/file/d/1tIFjYnRHGLypciX4Dl7IBX86vymAnVRP/view?usp=sharing]. There are two trial pair files:
tv26_eval-A.txt – contains trial pairs of speakers in a mix of All languages compared to the training set.
tv26_eval-U.txt – contains trial pairs of speakers where all utterances are in Unseen languages compared to the training set.

3. During the evaluation phase, you can monitor the performance of your system. Please visit the Codabench page for the TidyVoice Challenge [https://www.codabench.org/competitions/13187/] and register for the evaluation. Each team has 5 tokens to submit the scores of their proposed systems, allowing up to 5 submissions. The final score for each team will be based on its best-performing submission.

4. Please read the submission guidelines carefully to understand the required format of the submission file and how to view the results (EER and minDCF) for both trial pair files. Participants must submit a single zip file containing two txt score files, one for each trial file. Each score file must include only the scores, listed in the same order as the trial pairs, without file names or headers. The score files must have the same names as their corresponding trial files. Due to the Codabench submission mechanism, if the required format is not followed correctly, the system will return an error instead of results, and one submission token will be consumed. To help avoid this issue, we have prepared a Python code that allows you to create and validate your submission file by checking the file order, naming, and final submission structure using your score file. Please refer to the code [here] for detailed instructions.

5. During the evaluation phase, participants can only see their own results. The results of other teams will not be visible.

6. After the evaluation phase, we will release the final rankings. We will have a separate leaderboard for each trial pair file. However, to be included in the ranking, results for both trial pairs must be submitted. The announcement will be made anonymously with an identity code. Participants can share their team code in their papers or share the paper with us, and we can feature it on our website for their team.

7. The deadline for the evaluation phase is February 10, 2026.

Please feel free to contact us if you need any help.
Good luck and enjoy the challenge!

Best regards,
TidyVoice Organization Team