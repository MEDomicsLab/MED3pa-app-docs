---
description: >-
  How to import a model trained outside the application so MED3pa can study its
  behaviour.
---

# Base Models

The **base model** is the classifier under study. MED3pa never trains it; it only calls it. Any model can be used as long as it can be exported and can return a probability for the positive class.

<figure><img src="../../.gitbook/assets/DataAndModels.png" alt=""><figcaption><p><em>Data &#x26; Models</em> panel: importing an external model</p></figcaption></figure>

### Supported formats

| Format | Extensions | Notes |
| --- | --- | --- |
| Pickled estimator | `.pkl`, `.pickle`, `.joblib` | Any scikit-learn-style estimator exposing `predict_proba` |
| ONNX graph | `.onnx` | Must expose a probability output, or be declared as producing raw logits |

The import wraps the file as a `.medmodel` object stored under `MODELS/` in the workspace, which is what the rest of the application consumes.

{% hint style="info" %}
The model must expose a **binary** `predict_proba`; that probability is what every confidence estimate is computed from. The import tests it on a sample row before anything is saved, so a model that cannot be called is rejected at import time rather than halfway through an analysis.
{% endhint %}

### Fields

Open **Data & Models → Base models** and fill in:

1. **Model file**: the pickled estimator or ONNX graph.
2. **Model name**: saved as `<name>.medmodel`.
3. **Target column**: the name of the label column the model predicts.
4. **Features, in the order the model expects them**: one per line, or comma-separated. Order matters: rows are assembled in the order given here. Leave blank for a pickled model that records its own feature names; the import reads them and fails if it cannot.
5. **Decision threshold** _(optional)_: the probability above which a prediction counts as positive. Defaults to `0.5`.

### ONNX options

Two extra fields appear for `.onnx` files:

* **Outputs are raw logits**: 
  A classifier normally ends with a sigmoid or a softmax, the step that squashes its internal score into a probability between 0 and 1. Some export pipelines strip that final layer off, so the graph returns the **raw logit** instead: an unbounded score where 0 means an even chance, large positive numbers mean likely, and large negative numbers mean unlikely.

  MED3pa needs a probability, because every confidence estimate is computed from one. Ticking this box tells the application to apply the missing sigmoid itself.

  {% hint style="danger" %}
  Nothing can detect this automatically. A logit of 2.5 and a probability of 2.5 are indistinguishable to the importer, so getting the box wrong produces confidence scores that look entirely plausible and are wrong throughout. Tick it only when you know the graph was exported without its final activation.
  {% endhint %}
  
* **Probability output name**: 
  Some graphs expose several outputs, typically a hard label alongside the probabilities. When none of them is named in a way the importer recognises, this field names the one to read. It can be left blank otherwise.

### After importing

The model appears under _Already imported_ in the panel and becomes selectable as the **Base Model Source Architecture** on the [Configuration](../analysis/configuration.md) page. Its declared feature list is what the deployment form later uses to build the manual single-patient entry fields.
