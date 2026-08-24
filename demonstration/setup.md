---
description: Opening a workspace and bringing the cohort and the model into it.
---

# Workspace and inputs

Nothing in MED3pa can run before a workspace exists, and no analysis can be configured before a dataset and a model are in it. This stage covers both. The figures come from `session1`.

## Opening the workspace

On first launch the application asks for a **workspace folder**. For this proof of concept a fresh, empty folder is the right choice: the workspace is where `DATA/` and `MODELS/` are created, and where the local MongoDB stores the sessions, deployments and patient records this walkthrough produces. Keeping the demo in its own folder keeps its sessions from mixing with other studies.

<figure><img src="../.gitbook/assets/demo/01-workspace-gate.png" alt=""><figcaption><p>Figure 1: choosing the workspace folder. Screenshot not captured yet.</p></figcaption></figure>

Once a folder is chosen, the module opens behind a thin header carrying the workspace path, a status light for the Go server, and the buttons for **Data & Models** and **System**.

<figure><img src="../.gitbook/assets/demo/02-header.png" alt=""><figcaption><p>Figure 2: the header. Screenshot not captured yet.</p></figcaption></figure>

{% hint style="warning" %}
If the light is red, stop here. Open **System** and check the Python environment: the interpreter must have MED3pa installed, or every analysis will fail before it starts. See [Interface overview](../interface-overview.md#system-page) for what that page shows, and [Quick start](../quick-start.md#id-3.-python-environment) for how to build the environment.
{% endhint %}

## Importing the cohort

Open **Data & Models** from the header and stay on the **Datasets** tab. **Import CSV…** copies the chosen files into `DATA/` inside the workspace and re-scans it, which loads them into the local MongoDB and makes them selectable everywhere else.

<figure><img src="../.gitbook/assets/demo/03-import-csv.png" alt=""><figcaption><p>Figure 3: importing the cohort. The panel reports zero datasets and zero base models, because this workspace is new.</p></figcaption></figure>

Two files sit in the folder, and the analysis uses the smaller of them:

| File | Size | Used for |
| --- | --- | --- |
| `Holdout_homr_any_visit_10pct.csv` | 1.3 MB | The cohort the analysis is run over |
| `Learning_homr_any_visit_10pct.csv` | 5.3 MB | The companion learning split, not used by MED3pa here |

{% hint style="info" %}
Importing takes a copy. Editing the original CSV afterwards changes nothing in the workspace, so re-import it if the cohort is regenerated.
{% endhint %}

<figure><img src="../.gitbook/assets/demo/04-datasets-list.png" alt=""><figcaption><p>Figure 4: the cohort listed in the Datasets tab after import. Screenshot not captured yet.</p></figcaption></figure>

## Importing the base model

Switch to the **Base models** tab. The model audited in `session1` is a pickled scikit-learn `BaggingClassifier`, exported as a 134 MB `.pkl` and imported straight from the file picker.

<figure><img src="../.gitbook/assets/demo/05-import-model-form.png" alt=""><figcaption><p>Figure 5: the Import External Model form, with the pickled estimator being chosen</p></figcaption></figure>

Four fields carry the demo:

| Field | Value used here |
| --- | --- |
| **Model file** | `BaggingClassifier_model_sklearn.pkl` |
| **Model name** | `BaggingClassifier_model_sklearn`, saved as `<name>.medmodel` |
| **Target column** | `oym` |
| **Decision threshold** | `0.5`, the default |

The **features** field is the one that repays care. This model expects its columns in a specific order, and rows are assembled in exactly the order given here, so the whole list goes in: `patient_id`, `visit_id`, `age_original`, `ed_visit_count`, `ho_ambulance_count`, `total_duration`, then the 84 `dx_*` columns, the 147 `adm_*` columns, and the rest.

<figure><img src="../.gitbook/assets/demo/06-feature-list.png" alt=""><figcaption><p>Figure 6: the filled import form. The feature box holds the model's full column list, in model order.</p></figcaption></figure>

{% hint style="danger" %}
`oym` is the target and is **not** a feature. Including it in this list would hand the model the answer and make every confidence estimate meaningless.
{% endhint %}

{% hint style="info" %}
A pickled estimator that records its own feature names can be imported with the field left blank; the import reads the names from the model and fails loudly if it cannot. Typing them in is still the safer route, since it makes the expected order explicit in the record.
{% endhint %}

Import writes the model into `MODELS/` as a `.medmodel`. Before saving anything, the application calls the model on a sample row, so a model whose `predict_proba` cannot be reached is rejected here rather than halfway through an analysis.

<figure><img src="../.gitbook/assets/demo/07-model-imported.png" alt=""><figcaption><p>Figure 7: the base model under "Already imported". Screenshot not captured yet.</p></figcaption></figure>

{% hint style="info" %}
The second run in this walkthrough, `session3`, imports a different artifact the same way: `homr_oym_rf.onnx`, an 18 MB ONNX random forest. The form gains two extra fields for ONNX graphs, covered in [Base Models](../med3pa/data-and-models/base-models.md#onnx-options).
{% endhint %}

With a cohort and a model in the workspace, the analysis can be configured. Continue to [Configuring the run](configuration.md).
