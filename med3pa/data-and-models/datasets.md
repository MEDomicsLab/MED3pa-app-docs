---
description: How to bring a patient cohort into the workspace.
---

# Datasets

MED3pa reads tabular cohorts. A dataset is a **CSV file** in which one row is one patient, the feature columns are the ones the base model expects, and one column holds the ground-truth label.

### Importing

1. Open **Data & Models** from the header and select the **Datasets** tab.
2. Click **Import CSV…** and pick one or more files.
3. The files are copied into `DATA/` inside your workspace and the workspace is re-scanned, which loads them into the local MongoDB.

Once that is done, the file appears in the list and becomes selectable in the dataset pickers on the Configuration and Deployment pages.

{% hint style="warning" %}
Importing copies the file. Editing the original afterwards has no effect on the imported copy — re-import it instead.
{% endhint %}

### What the file must contain

| For | Requirement |
| --- | --- |
| **Analysis** | Every feature column the base model declares, plus the **target column** holding the true label (0/1) |
| **Deployment (batch)** | Every feature column the deployed model declares. Ground truth is not needed — that is the point |
| **Patient identification** | Optionally a patient-id column. If none is given, identifiers are generated |

Column names must match those declared when the base model was imported, and are matched by name, not by position.

### Using predicted probabilities instead of a model

If the model that produced the predictions cannot be exported at all, MED3pa can work from its output alone: add a column holding the **predicted probability of the positive class** to the CSV, and select _Predicted probabilities_ rather than _Base model_ on the [Configuration](../analysis/configuration.md) page.

This is enough to run the whole analysis. Such a session can still be deployed, but since there is no model to call, every new batch you apply it to must itself carry that same probability column.
