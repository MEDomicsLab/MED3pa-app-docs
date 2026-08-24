---
description: >-
  A proof of concept taking one ICU mortality model through the whole MED3pa
  pipeline, from an unopened workspace to a deployed model answering for new
  patients.
---

# 🕹️ Demonstration

This is **proof of concept 1** for the MED3pa application: a complete run over the **MIMIC-95** cohort, one stage per page, with every screen shown.

Unlike the other MEDomics proofs of concept, nothing here trains a predictive model. The model already exists. What this walkthrough produces is an answer to a different question: **for which patients can that model be believed, and what does it cost to make it stay quiet about the rest?**

## About the dataset

**MIMIC-95** is a tabular ICU cohort derived from [MIMIC](https://mimic.mit.edu/). One row is one stay. Sixteen columns are used: fifteen features and the outcome.

| Column | What it holds | Role |
| --- | --- | --- |
| `deceased` | _fill in_ | **Target**, binary |
| `age` | _fill in_ | Feature |
| `pao2fio2` | _fill in_ | Feature |
| `uo` | _fill in_ | Feature |
| `admissiontype` | _fill in_ | Feature |
| `bicarbonate` | _fill in_ | Feature |
| `bilirubin` | _fill in_ | Feature |
| `bun` | _fill in_ | Feature |
| `chron_dis` | _fill in_ | Feature |
| `gcs` | _fill in_ | Feature |
| `hr` | _fill in_ | Feature |
| `potassium` | _fill in_ | Feature |
| `sbp` | _fill in_ | Feature |
| `sodium` | _fill in_ | Feature |
| `tempc` | _fill in_ | Feature |
| `wbc` | _fill in_ | Feature |

{% hint style="info" %}
MED3pa never interprets a feature. It reads the columns as numbers, and the only place their names surface is in the profile rules the APC tree produces, which is exactly where a clinical reading matters. Filling in the table above is therefore worth the effort: a rule such as `gcs <= 8 & age > 70` is only actionable to a reader who knows what `gcs` is.
{% endhint %}

{% hint style="danger" %}
Any categorical column has to be **numerically encoded in the CSV**, `admissiontype` included. The single-patient form on the Deployment page builds numeric input fields from the model's feature list, so a column holding text cannot be typed into it.
{% endhint %}

## Goal

This proof of concept shows how an existing ICU mortality model can be audited and deployed with the MED3pa application. Concretely, by the end of the walkthrough you will have:

* imported a cohort and an externally trained model into a workspace;
* estimated per patient and per profile how much that model can be trusted;
* read the declaration-rate curve to see what accuracy the model buys by abstaining, and on how many patients;
* found the profiles where the model consistently underperforms;
* frozen a declaration rate into a deployed model, and applied it to patients it has never seen;
* opened one patient and read the whole chain of reasoning behind their routing.

{% hint style="info" %}
The settings used throughout are the ones the application prefills. They are a deliberate starting point rather than a tuned configuration, so the walkthrough is reproducible: follow it with your own cohort and model, and only the numbers change.
{% endhint %}

## Steps

{% stepper %}
{% step %}
### [Workspace and inputs](setup.md)

Open a workspace, import the MIMIC-95 CSV, and import the base model with its feature list and target.
{% endstep %}

{% step %}
### [Configuring the run](configuration.md)

Point MED3pa at the model, the cohort and the `deceased` column, then set how confidence is to be estimated.
{% endstep %}

{% step %}
### [Reading the results](analysis.md)

Work through the declaration-rate curve and the profile tree, and choose the rate to deploy at.
{% endstep %}

{% step %}
### [Deploying and applying](deployment.md)

Freeze the session into a deployed model and run it over new patients, in batch and one at a time.
{% endstep %}

{% step %}
### [One patient in detail](patient.md)

Look a patient up and read why their prediction was accepted, flagged for caution, or withheld.
{% endstep %}
{% endstepper %}

## What to fill in

The walkthrough is written with the run's own figures left as tokens in double braces, so the prose can be completed in one pass once the analysis has been run. Every token appears in the table below.

| Token | Meaning |
| --- | --- |
| `{{N_PATIENTS}}` | Rows in the MIMIC-95 cohort used for the analysis |
| `{{MODEL_FILE}}` | File name of the base model, with its extension |
| `{{MODEL_ALGORITHM}}` | What the base model is, e.g. a random forest |
| `{{THRESHOLD}}` | The model's decision threshold, if not `0.5` |
| `{{SESSION_NAME}}` | Name given to the analysis session |
| `{{AUC_FULL}}` | AUC over the whole cohort, at declaration rate 100% |
| `{{SUGGESTED_DR}}` | Declaration rate the application suggests for the chosen metric |
| `{{AUC_AT_DR}}` | AUC at that declaration rate |
| `{{IMPROVEMENT}}` | Gain reported on the "Improvement at optimal DR" card |
| `{{CHOSEN_DR}}` | Declaration rate actually deployed, if different from the suggestion |
| `{{MIN_CONFIDENCE}}` | Minimum confidence matching the chosen rate |
| `{{POPULATION_KEPT}}` | Share of the cohort still answered for at that rate |
| `{{PROFILE_RULE_1}}`, `{{PROFILE_RULE_2}}` | Two profile rules worth discussing, one weak and one strong |
| `{{PROFILE_1_METRIC}}`, `{{PROFILE_2_METRIC}}` | The base model's performance inside each of them |
| `{{LOST_PROFILE_RULE}}`, `{{LOST_PROFILE_DR}}` | A profile that drops out, and the rate at which it goes |
| `{{DEPLOYMENT_NAME}}` | Name given to the deployed model |
| `{{HOLDOUT_FILE}}`, `{{N_HOLDOUT}}` | The held-out cohort the deployed model is applied to, and its size |
| `{{N_ACCEPT}}`, `{{N_CAUTION}}`, `{{N_FLAG}}` | How the batch split across the three routing outcomes |
| `{{PATIENT_ID}}` | The patient opened in the last stage |
| `{{PATIENT_PROB}}`, `{{PATIENT_IPC}}`, `{{PATIENT_APC}}`, `{{PATIENT_MPC}}` | That patient's base probability and three confidence values |
| `{{PATIENT_PROFILE}}`, `{{PATIENT_ROUTING}}` | The profile they fall into and how they were routed |

Screenshots are placeholders. Each one is a real file at `.gitbook/assets/demo/`, named for the figure it stands in for; replacing the file with the actual screenshot, keeping the name, needs no edit to any page.

## Beyond the application

The same experiment can be run as code against the [MED3pa package](../python-package.md). The package repository carries a complete one-year-mortality study as a notebook:

{% embed url="https://github.com/MEDomicsLab/MED3pa/blob/main/examples/oym_example.ipynb" %}
One-year-mortality example notebook
{% endembed %}

The full code behind the results published in the [JAMIA article](https://doi.org/10.1093/jamia/ocag034) is available in [study\_3pa](https://github.com/MEDomicsLab/study_3pa).
