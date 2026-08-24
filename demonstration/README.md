---
description: >-
  A proof of concept taking a hospital mortality model through the whole MED3pa
  pipeline, from an unopened workspace to a deployed model answering for new
  patients.
---

# 🕹️ Demonstration

This is **proof of concept 1** for the MED3pa application: a complete run over a hospital cohort of 2,473 stays, one stage per page, with the real screens shown throughout.

Unlike the other MEDomics proofs of concept, nothing here trains a predictive model. The model already exists. What this walkthrough produces is an answer to a different question: **for which patients can that model be believed, and what does it cost to make it stay quiet about the rest?**

## About the dataset

The cohort is a wide tabular extract, one row per hospital stay. `Holdout_h1_encoded.csv` carries **2,473 stays** across **245 columns**: 244 features and the outcome.

| Group | Count | Examples |
| --- | --- | --- |
| `adm_*` | 147 | `adm_lung_cancer`, `adm_pneumonia`, `adm_anemia` |
| `dx_*` | 84 | `dx_metastatic_solid_cancer`, `dx_chronic_resp_failure`, `dx_home_o2` |
| `is_*` | 3 | `is_ambulance`, `is_icu_start_ho`, `is_urg_readm` |
| Encounter and demographic | 9 | `age_original`, `ed_visit_count`, `ho_ambulance_count`, `total_duration`, `has_dx`, `gender`, `flu_season`, `living_status`, `admission_group`, `service_group` |
| **Outcome** | 1 | `oym` |

Everything is numerically encoded already, which matters at the far end of the pipeline: the single-patient form on the Deployment page builds numeric input fields, so a column holding text could not be typed into it.

{% hint style="warning" %}
**To fill in:** what `oym` records, where the extract comes from, and how the binary outcome is defined. The walkthrough deliberately does not guess.
{% endhint %}

{% hint style="info" %}
MED3pa never interprets a feature. It reads the columns as numbers, and the only place their names surface is in the profile rules the APC tree produces, which is exactly where a clinical reading matters. A rule such as `age_original <= 77.5 & adm_lung_cancer > 0.5`, which is one this run really produced, is only actionable to a reader who knows what those columns hold.
{% endhint %}

## Goal

This proof of concept shows how an existing mortality model can be audited and deployed with the MED3pa application. Concretely, by the end of the walkthrough you will have:

* imported a cohort and an externally trained model into a workspace;
* estimated per patient and per profile how much that model can be trusted;
* read the declaration-rate curve to see what accuracy the model buys by abstaining, and on how many patients;
* found the profiles where the model consistently underperforms;
* frozen a declaration rate into a deployed model, and applied it to patients it has never seen;
* opened one patient and read the whole chain of reasoning behind their routing.

{% hint style="warning" %}
**The figures come from two runs of the same pipeline.** Stages 1 to 3 show `session1`, built on a pickled `BaggingClassifier`; stages 4 and 5 show the deployment `medpa_model2`, built from `session3` on an ONNX random forest, `homr_oym_rf`. The pipeline is identical either way, and each page says which run its figures belong to. Consolidating the walkthrough onto a single run is a matter of re-shooting a handful of screens.
{% endhint %}

The confidence settings are the ones the application prefills. They are a deliberate starting point rather than a tuned configuration, so the walkthrough is reproducible: follow it with your own cohort and model, and only the numbers change.

## Steps

{% stepper %}
{% step %}
### [Workspace and inputs](setup.md)

Open a workspace, import the cohort, and import the base model with its feature list and target.
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

Freeze the session into a deployed model and run it over new patients.
{% endstep %}

{% step %}
### [One patient in detail](patient.md)

Look a patient up and read why their prediction was accepted or withheld.
{% endstep %}
{% endstepper %}

## Still to come

Sixteen screens have not been captured yet. Until they are, those figures show a placeholder card naming what belongs there, and the surrounding text says plainly that the figure is missing rather than describing something the reader cannot see. The list is in `PLACEHOLDERS.md` at the root of this repository.

Two numbers are also still open, both on the [analysis page](analysis.md): the base model's performance inside individual profiles, which needs a node-detail screenshot, and the rate at which the first profile drops out of the tree.

## Beyond the application

The same experiment can be run as code against the [MED3pa package](../python-package.md). The package repository carries a complete one-year-mortality study as a notebook:

{% embed url="https://github.com/MEDomicsLab/MED3pa/blob/main/examples/oym_example.ipynb" %}
One-year-mortality example notebook
{% endembed %}

The full code behind the results published in the [JAMIA article](https://doi.org/10.1093/jamia/ocag034) is available in [study\_3pa](https://github.com/MEDomicsLab/study_3pa).
