---
description: >-
  This is a tutorial on how to declare the inputs of a MED3pa experiment and
  configure how confidence is estimated.
---

# Configuration

The Configuration page is step 1 of the workflow. Its left column declares **what** is being analysed; its right column declares **how** confidence is estimated.

<figure><img src="../../.gitbook/assets/ConfigurationPage.png" alt=""><figcaption><p><em>Configuration</em> page: inputs on the left, confidence method on the right</p></figcaption></figure>

## Inputs

### Baseline prediction model

Two mutually exclusive sources are offered:

* **Base model**: an imported `.medmodel` (see [Base Models](../data-and-models/base-models.md)). MED3pa calls it to obtain a probability per patient.
* **Predicted probabilities**: a column of the chosen dataset that already holds the predicted probability of the positive class, plus the **decision threshold** above which a prediction counts as positive. Use this when the model that produced them lives outside the application.

### Dataset, target and session

| Field | Meaning |
| --- | --- |
| **Training Data (.csv)** | The evaluation cohort, imported through [Data & Models](../data-and-models/datasets.md) |
| **Target column** | The column holding the ground-truth label, e.g. `deceased` |
| **Session Name** | The name this run is saved under. It is how you find the results again |

## Confidence method configuration

Four collapsible sections hold the rest. Every field carries a ⓘ hover hint in the interface; the tables below repeat them.

### IPC: Individualized Predictive Confidence

Hyperparameters of the regressor that learns to predict, from a patient's features alone, how much the base model can be trusted for that patient.

| Field | Prefilled | Description |
| --- | --- | --- |
| `n_estimators` | 100 | Number of trees. More trees give a smoother, more stable confidence estimate but take longer to train. Ignored when a grid-search range is set. Only shown for forest-based regressors |
| `max_depth` | 5 | Maximum depth of each tree. Deeper trees capture finer patterns in confidence but overfit more easily. Blank means unlimited |
| `min_samples_split` | 2 | Minimum number of samples a node must hold before it may split. Higher values give a coarser, more conservative confidence surface |

**Confidence metric formulation (cᵢ)** defines what the IPC is trained to predict. It is computed per patient from the base model's probability `p` and the true label `y`, and the IPC then learns to reproduce that value from features alone:

| Option | Formula |
| --- | --- |
| **Sigmoidal** _(default)_ | `1 / (1 + e^(10·ln3·(|yᵢ − ŷᵢ| − |t − yᵢ|)))` |
| **Absolute** | `1 − |ŷᵢ − yᵢ|` is near 1 when the model was right about a patient, near 0 when it was confidently wrong |
| **Custom function** | Any expression `f(p, y)` you write |

{% hint style="info" %}
A custom expression may use the variables `p` (predicted probability), `y` (true label), `t` (threshold) and `x` (features), and the functions `abs`, `exp`, `log`, `sqrt`, `clip`, `where`, `minimum`, `maximum` and similar. It must return a **confidence in \[0, 1]**, where 1 means the prediction is trustworthy.
{% endhint %}

**IPC regressor** (`ipc_type`) selects which model implements the IPC:

| Value | Notes |
| --- | --- |
| `RandomForestRegressor` | The default |
| `EnsembleRandomForestRegressor` | Cannot be grid-searched; see the warning below |
| `DecisionTreeRegressor` | Not a forest, so `n_estimators` does not apply and the field is hidden |

{% hint style="warning" %}
MED3pa cannot grid-search an ensemble of random forests: its optimizer stores the tuned model where that ensemble's `predict()` never reads it. Anything entered in the grid fields is ignored, and the IPC is trained directly with the hyperparameters above.
{% endhint %}

**Grid-search ranges** run a cross-validated search instead of training directly. Leave every field blank to skip the search; filling in any one field turns it on. Values are comma-separated, e.g. `50, 100, 200` for `n_estimators`, `2, 3, 4, 5` for `max_depth`, `1, 2, 4` for `min_samples_leaf`.

### APC: Aggregated Predictive Confidence

Hyperparameters of the decision tree that splits patients into profiles.

| Field | Prefilled | Description |
| --- | --- | --- |
| **Tree depth** (`max_depth`) | 3 | The main control on how many profiles you get: depth _d_ yields at most 2^_d_ leaves. Shallower trees give fewer, broader, more interpretable profiles |
| `min_samples_leaf` | 5 | Minimum number of patients in a leaf. Raising it prevents tiny profiles whose metrics are too noisy to act on |
| `ccp_alpha` | 0.001 | Cost-complexity pruning strength. Higher values prune more aggressively, giving a smaller tree and fewer profiles. `0` disables pruning |

The APC has its own grid-search fields, with the same semantics as the IPC's.

### MPC: Mixed Predictive Confidence

How the per-patient IPC and per-profile APC confidences combine into the single value used for declaration:

| Strategy | Formula | Behaviour |
| --- | --- | --- |
| **Minimum** _(default)_ | `min(IPC, APC)` | Conservative; a patient is trusted only when both agree |
| **Average** | `mean(IPC, APC)` | More permissive |
| **Custom function** | `f(IPC, APC)` | Lets you weight them, e.g. `0.6 * IPC + 0.4 * APC` |

Custom expressions accept the variables `IPC` and `APC` and the same function set as the IPC metric, and must likewise return a confidence in `[0, 1]`.

### Experiment settings

| Field | Prefilled | Description |
| --- | --- | --- |
| **Samples ratio sweep** (min / max / step) | 0 / 10 / 5 | The smallest share of the cohort a profile must cover to be reported, as a percentage. The experiment repeats profile extraction at every value from min to max, so you obtain profile sets at several levels of granularity rather than just one. `0` keeps every profile, however small; smaller steps give more profile sets and a longer run |
| **Evaluate models** | on | Also score the IPC and APC models themselves and store the result under `models_evaluation`. Adds to the runtime, and is useful for checking that the confidence models actually fit |

## Running

Click **⚡ Run Analysis**. A progress bar reports each stage as the Go server streams it back from the Python process. When the run finishes, the application saves the session and switches straight to the [Analysis Workspace](analysis-workspace.md) with it loaded.

{% hint style="warning" %}
A run that fails immediately is almost always an environment problem rather than a configuration one. Check the Python interpreter on the System page; it must have MED3pa installed. See [Quick start](../../quick-start.md#id-3.-python-environment).
{% endhint %}
