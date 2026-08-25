---
description: >-
  A proof of concept taking a hospital one-year mortality model through the whole
  MED3pa pipeline, from an unopened workspace to a deployed model answering for
  new patients.
---

# 🕹️ Demonstration

This is **proof of concept 1** for the MED3pa application: a complete run over a hospital cohort of 2,473 stays, one stage per page, with the real screens shown throughout.

Unlike the other MEDomics proofs of concept, nothing here trains a predictive model. The model already exists. What this walkthrough produces is an answer to a different question: **for which patients can that model be believed, and what does it cost to make it stay quiet about the rest?**

## Files used

Everything this walkthrough needs is downloadable, so the whole run can be reproduced click for click.

| File | What it is |
| --- | --- |
| [`homr_oym_rf.onnx`](../.gitbook/assets/homr_oym_rf.onnx) | The base model: a random forest predicting one-year mortality, exported to ONNX |
| [`features.txt`](../.gitbook/assets/features.txt) | The model's 244 feature names, in the order it expects them |
| [`Holdout_prepared.csv`](../.gitbook/assets/Holdout_prepared.csv) | The cohort the analysis is run over, 2,473 stays |
| [`Deploy3_newmodel.csv`](../.gitbook/assets/Deploy3_newmodel.csv) | Three unseen stays, used at the deployment stage |

{% hint style="info" %}
A few screenshots were taken during earlier runs and show other session, deployment or file names. The walkthrough itself is written against the four files above, and the steps are identical either way.
{% endhint %}

## About the dataset

The cohort is drawn from **Leveraging patients' longitudinal data to improve the Hospital One-year Mortality Risk**, published on Zenodo by Laribi, Raymond, Taseen, Poenaru and Vallières (2024) under CC BY 4.0: [https://doi.org/10.5281/zenodo.12954673](https://doi.org/10.5281/zenodo.12954673).

The published dataset is **synthetic**, generated with the AVATAR method in partnership with Octopize: 248,485 synthetic visits from 123,646 synthetic patients across 248 columns. That matters for a public demonstration, because it means the files above can be shipped and re-run by anyone without a data use agreement.

`Holdout_prepared.csv` is a prepared slice of it: one row per hospital stay, **2,473 stays** across **245 columns**, being 244 features and the outcome.

| Group | Count | Examples |
| --- | --- | --- |
| `adm_*` | 147 | `adm_lung_cancer`, `adm_pneumonia`, `adm_metastasis` |
| `dx_*` | 84 | `dx_metastatic_solid_cancer`, `dx_chronic_resp_failure`, `dx_home_o2` |
| `is_*` | 3 | `is_ambulance`, `is_icu_start_ho`, `is_urg_readm` |
| Encounter and demographic | 10 | `age_original`, `ed_visit_count`, `ho_ambulance_count`, `total_duration`, `has_dx`, `gender`, `flu_season`, `living_status`, `admission_group`, `service_group` |
| **Outcome** | 1 | `oym`, one-year mortality |

Everything is numerically encoded already, which matters at the far end of the pipeline: the single-patient form on the Deployment page builds numeric input fields, so a column holding text could not be typed into it.

{% hint style="info" %}
MED3pa never interprets a feature. It reads the columns as numbers, and the only place their names surface is in the profile rules the APC tree produces, which is exactly where a clinical reading matters. A rule such as `age_original <= 78.5 & adm_lung_cancer > 0.5`, which is one this run really produced, is only actionable to a reader who knows what those columns hold.
{% endhint %}

## Goal

This proof of concept shows how an existing mortality model can be audited and deployed with the MED3pa application. Concretely, by the end of the walkthrough you will have:

* imported a cohort and an externally trained model into a workspace;
* estimated per patient and per profile how much that model can be trusted;
* read the declaration-rate curve to see what accuracy the model buys by abstaining, and on how many patients;
* found the profiles where the model consistently underperforms;
* frozen a declaration rate into a deployed model, and applied it to patients it has never seen;
* opened one patient and read the whole chain of reasoning behind their routing.

The confidence settings are the ones the application prefills. They are a deliberate starting point rather than a tuned configuration, so the walkthrough is reproducible: follow it with your own cohort and model, and only the numbers change.

## Steps

{% stepper %}
{% step %}
### [Workspace and inputs](setup.md)

Open a workspace, import `Holdout_prepared.csv`, and import `homr_oym_rf.onnx` with its feature list and target.
{% endstep %}

{% step %}
### [Configuring the run](configuration.md)

Point MED3pa at the model, the cohort and the `oym` column, then set how confidence is to be estimated.
{% endstep %}

{% step %}
### [Reading the results](analysis.md)

Work through the declaration-rate curve and the profile tree, and choose the rate to deploy at.
{% endstep %}

{% step %}
### [Deploying and applying](deployment.md)

Freeze the session into a deployed model and run it over the three unseen stays.
{% endstep %}

{% step %}
### [One patient in detail](patient.md)

Look a patient up and read why their prediction was accepted or withheld.
{% endstep %}
{% endstepper %}

## Beyond the application

The same experiment can be run as code against the [MED3pa package](../python-package.md). The package repository carries a complete one-year-mortality study as a notebook:

{% embed url="https://github.com/MEDomicsLab/MED3pa/blob/main/examples/oym_example.ipynb" %}
One-year-mortality example notebook
{% endembed %}

The full code behind the results published in the [JAMIA article](https://doi.org/10.1093/jamia/ocag034) is available in [study\_3pa](https://github.com/MEDomicsLab/study_3pa).
