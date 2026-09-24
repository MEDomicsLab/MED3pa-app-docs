---
description: Opening a workspace and importing the cohort and the base model.
---

# Workspace and inputs

**Objective.** Create a workspace, import the two cohorts, and import the base model to be audited. On completion the workspace holds everything the analysis requires.

Download the files listed on the [demonstration overview](./) before beginning.

## Opening the workspace

1. Launch MED3pa. The application opens on the workspace screen.
2. Click **Open workspace…** ① and select an empty folder. Folders opened previously are listed under _Recent_.

<figure><img src="../.gitbook/assets/demo/01-workspace-gate.png" alt=""><figcaption><p>Figure 1: the workspace screen</p></figcaption></figure>

A workspace holds the imported datasets under `DATA/`, the imported models under `MODELS/`, and the MongoDB instance in which sessions, deployments and patient records are stored. An empty folder is used here so that the output of this walkthrough remains separate from other studies.

3. Confirm that the header reports **Server ready** ①.

<figure><img src="../.gitbook/assets/demo/02-workspace-overview.png" alt=""><figcaption><p>Figure 2: the Overview page of a new workspace, with the status indicator in the header</p></figcaption></figure>

{% hint style="warning" %}
A red indicator means the Go server is not answering, which is most often caused by a Python environment without MED3pa installed. Resolve this before continuing: see the [System page](../interface-overview.md#system-page) and [Quick start](../quick-start.md#id-3.-python-environment).
{% endhint %}

## Importing the cohorts

4. Click **Data & Models** in the header ①.
5. Select the **Datasets** tab ②.
6. Click **Import CSV…** ③.
7. Select [`Holdout_prepared.csv`](../.gitbook/assets/Holdout_prepared.csv) and [`Deploy3_newmodel.csv`](../.gitbook/assets/Deploy3_newmodel.csv), then click **Open** ④.

<figure><img src="../.gitbook/assets/demo/03-import-csv.png" alt=""><figcaption><p>Figure 3: importing the cohorts. Both counters read zero because the workspace is new.</p></figcaption></figure>

The two files serve different stages:

| File | Rows | Used for |
| --- | --- | --- |
| `Holdout_prepared.csv` | 2,473 | The cohort the analysis is run over, in stage 2 |
| `Deploy3_newmodel.csv` | 3 | Unseen stays, applied to the deployed model in stage 4 |

Importing copies each file into the workspace, so subsequent edits to the original have no effect on the imported copy. See [Datasets](../med3pa/data-and-models/datasets.md).

## Importing the base model

8. Select the **Base models** tab ①.
9. Click **Choose file…** ② and select [`homr_oym_rf.onnx`](../.gitbook/assets/homr_oym_rf.onnx).
10. Enter `homr_oym_rf` in **Model name** ③.
11. Enter `oym` in **Target column** ④.
12. Open [`features.txt`](../.gitbook/assets/features.txt), copy its entire contents, and paste them into **Features, in the order the model expects them** ⑤.

<figure><img src="../.gitbook/assets/demo/04-import-model-form.png" alt=""><figcaption><p>Figure 4: the import form, with the model file, name and target column supplied</p></figcaption></figure>

The file holds the 244 column names in the order the model expects them, comma separated, which is the format this field takes. Order is significant, because rows are assembled in the order given here.

{% hint style="danger" %}
`oym` is the quantity the model predicts and is therefore absent from the feature list. Adding it would supply the outcome as an input and invalidate every confidence estimate that follows.
{% endhint %}

13. Leave **Decision threshold** at `0.5` ①.
14. Leave **Outputs are raw logits** unticked ②.
15. Leave **Probability output name** empty ③.
16. Click **Import model** ④.

<figure><img src="../.gitbook/assets/demo/05-onnx-options.png" alt=""><figcaption><p>Figure 5: the decision threshold and the two ONNX options, none of which is modified here</p></figcaption></figure>

Both ONNX options are left at their defaults because `homr_oym_rf.onnx` was exported with its final activation intact and exposes a single, recognisable probability output. The circumstances in which either applies are described under [ONNX options](../med3pa/data-and-models/base-models.md#onnx-options).

## What this produced

The workspace now contains two cohorts under `DATA/` and one `.medmodel` under `MODELS/`. The model is validated at import: the application calls it on a sample row before saving, so a model that cannot be called is rejected here rather than during the analysis.

## Next

Open **Configuration** in the module sidebar and continue with [Configuring the run](configuration.md).
