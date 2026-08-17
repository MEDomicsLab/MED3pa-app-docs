---
description: >-
  The aim of this demonstration is to illustrate the comprehensive utilization
  of our software, from a trained model to a deployed one.
---

# 🕹️ Demonstration

{% hint style="warning" %}
A video walkthrough is not available yet. Until it is, the written run-through below covers the same ground.
{% endhint %}

The scenario used throughout this documentation is an **ICU in-hospital mortality** model: a binary classifier trained elsewhere, evaluated here on a held-out cohort. The question is not whether the model is good on average, but on which patients it can be relied upon.

### The run, end to end

1. **Import the cohort.** _Data & Models → Datasets → Import CSV…_ with the evaluation set. One row per stay, the feature columns the model expects, and a `deceased` column holding the outcome. See [Datasets](med3pa/data-and-models/datasets.md).
2. **Import the model.** _Data & Models → Base models_, pointing at the exported classifier (`.onnx`, `.pkl` or `.joblib`). Declare its target column and the features in the order it expects them. See [Base Models](med3pa/data-and-models/base-models.md).
3. **Configure.** On the Configuration page, select the model and the dataset, set the target column to `deceased`, and name the session. The prefilled confidence settings (random-forest IPC, an APC tree of depth 3, `minimum` as the MPC strategy) are a reasonable first pass. See [Configuration](med3pa/analysis/configuration.md).
4. **Run.** The progress bar reports each stage; the session opens in the Analysis Workspace when it completes.
5. **Read the curves.** The MDR chart shows what the model's accuracy becomes as it is allowed to abstain. Move the declaration-rate slider and watch both numbers that matter: the metric, and the population kept. See [Analysis Workspace](med3pa/analysis/analysis-workspace.md).
6. **Inspect the profiles.** Click nodes in the APC tree to see the base model's performance inside each profile. Nodes that grey out as the DR falls are profiles the model is uniformly unsure about.
7. **Deploy.** With the declaration rate where the trade-off is acceptable, **▶ Create Model** freezes the session into a deployed model.
8. **Apply.** On the Deployment page, run the deployed model over a batch of new stays, or type in a single patient. Each prediction comes back routed as _accept_, _caution_ or _flag_. See [Deployment](deployment.md).
9. **Look one up.** Any scanned patient can be reopened from [Patient lookup](patient-lookup.md), with the full decomposition of why the prediction was or was not trusted.

### A worked example in code

The package repository contains a complete one-year-mortality study as a notebook, which follows the same stages without the interface:

{% embed url="https://github.com/MEDomicsLab/MED3pa/blob/main/examples/oym_example.ipynb" %}
One-year-mortality example notebook
{% endembed %}

The full code behind the results published in the [JAMIA article](https://doi.org/10.1093/jamia/ocag034) is available in [study\_3pa](https://github.com/MEDomicsLab/study_3pa).

For any further inquiries, please do not hesitate to [contact us](forms/contact-us.md).
