---
layout: page
title: Challenge Description
---



The **TidyLang Challenge** introduces **Speaker-Controlled and Zero-Shot Language Recognition**: a challenge that targets language recognition in the realistic regime where each speaker contributes speech in multiple languages and models are tested on unseen languages. The central scientific question is: *How can we develop language recognition systems that disentangle speaker identity from linguistic structure to ensure robust generalization across individuals and languages?*

We aim to catalyze discussion and benchmarking around:

- **Representation disentanglement:** Designing training objectives that decouple speaker-specific acoustic traits from language-discriminative phonetic and phonotactic patterns.
- **Zero-shot generalization:** Evaluating the limits of modern multilingual and self-supervised models when encountering languages absent from the training set.
- **Mitigating shortcut learning:** Identifying and reducing the reliance on “shortcuts” (such as speaker-specific artifacts or recording conditions) to improve real-world reliability.
- **Fairness and trustworthiness:** Ensuring that language recognition performance remains robust and independent of speaker identity, aligning with the Odyssey 2026 theme of trustworthy identity and speech technology.

This proposal is closely aligned with the **Odyssey 2026** theme, *“Speech beyond words: Trustworthy Identity, Health, Emotion and more,”* by advancing the development of trustworthy, identity-invariant, and linguistically grounded speech technologies.

We believe that by building this challenge on a large-scale, public, and multilingual dataset (Tidy-X) with multi-lingual-per-speaker structure, we can create a more inclusive and rigorous benchmark for language recognition. This initiative will advance the field toward systems that rely on true linguistic cues rather than speaker-specific shortcuts.

#### **Why this challenge is significant?**

- **Addresses a key scientific gap:** Most language recognition benchmarks assume speaker identity is a nuisance variable. In reality, the same speaker often speaks multiple languages. Standard benchmarks allow models to “cheat” by using speaker-specific cues. The Tidy-X dataset is uniquely designed so that the *same speaker* appears across *multiple languages*, forcing models to disentangle language from identity.

- **Multi-lingual-per-speaker evaluation:** Unlike standard language recognition benchmarks, our dataset allows for controlled trials where the same speaker appears across multiple languages, explicitly stress-testing speaker–language entanglement.

- **Hard zero-shot scenario:** We introduce evaluation conditions that include identifying a new language spoken by a known speaker, isolating the model’s ability to generalize beyond memorized identity.

- **Pushing the boundaries of SSL:** The challenge provides a rigorous testbed for large-scale self-supervised models, moving beyond simple classification toward language-agnostic representation learning.

- **Trustworthy identity alignment:** By focusing on identity-invariant language cues, this challenge directly addresses the theme of “Trustworthy Identity,” ensuring that systems do not conflate *who* is speaking with *what language* is being spoken.

#### **Why this challenge is timely?**

- **Growing need for multilingual systems:** As speech technology becomes increasingly global, the demand for language recognition that works across speakers and languages has never been greater.

- **Advancements in multilingual modeling:** Recent advances in multilingual and self-supervised speech processing make this an opportune time to establish benchmarks that push the boundaries of speaker-invariant language recognition.

- **Open science:** The use of a public dataset (Mozilla Common Voice) and the commitment to standardized evaluation align with the movement toward more accessible and transparent scientific practices in speech technology.
