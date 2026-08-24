---
description: >-
  Reading the declaration-rate curve and the profile tree, and choosing the rate
  to deploy at.
---

# Reading the results

Step 2. This is where the proof of concept earns its name: everything up to here was setup, and everything after depends on the rate chosen on this page. The figures come from `session1`.

## The session

A run launched from the Configuration page opens here already loaded. Older ones are picked from the selector, or from Session History.

<figure><img src="../.gitbook/assets/demo/14-session-loaded.png" alt=""><figcaption><p>Figure 14: <code>session1</code> loaded in the Analysis Workspace. Screenshot not captured yet.</p></figcaption></figure>

**⚙ Saved configuration** unfolds the settings the run was made with. It is worth opening once even when you have just configured the run yourself, because it is the record that makes two sessions comparable weeks later, which matters here: this workspace ended up holding three.

<figure><img src="../.gitbook/assets/demo/15-saved-config.png" alt=""><figcaption><p>Figure 15: the saved configuration recorded with the session. Screenshot not captured yet.</p></figcaption></figure>

## What the headline figures say

<figure><img src="../.gitbook/assets/demo/16-kpi-cards.png" alt=""><figcaption><p>Figure 16: patients analysed, suggested declaration rate, and improvement at that rate. The cards are dimmed because the deployment dialog of Figure 23 was open when this was captured.</p></figcaption></figure>

With `Auc` selected as the metric:

| Card | Value |
| --- | --- |
| Patients analysed | 2,473, from `Holdout_h1_encoded.csv` |
| Suggested declaration rate | **100%** |
| Improvement at optimal DR | **+0.0%**, `Auc: 0.863 → 0.863` |

This is the honest and slightly awkward result, and it is worth stating plainly rather than dressing up: **on AUC, this model gains nothing by abstaining.** The optimum sits at 100%, which is the application saying that withholding the least confident predictions does not improve the ranking quality of the ones that remain.

{% hint style="warning" %}
A flat curve is a real finding, not a failed run. It says the confidence estimate carries little signal *for this metric on this cohort*, and the right response is to interrogate it rather than to lower the rate anyway. Try another metric in the dropdown, since optimal rates differ per metric and a model judged on F1 may want to abstain far more than the same model judged on AUC. Then look at whether the IPC is underfitting: the configuration here used `max_depth` 5 against a cohort 244 features wide.
{% endhint %}

## The declaration-rate curve

At a declaration rate of 100% the model answers for everyone, and the curve reports what ordinary validation reports.

<figure><img src="../.gitbook/assets/demo/17-dr-100.png" alt=""><figcaption><p>Figure 17: declaration rate at 100%. Screenshot not captured yet.</p></figcaption></figure>

Lowering the rate withholds the least confident predictions first. Reading the curve from right to left answers the deployment question directly: what does accuracy become if the model is allowed to stay quiet about the hardest cases, and how many patients does that silence cost?

<figure><img src="../.gitbook/assets/demo/18-mdr-curve.png" alt=""><figcaption><p>Figure 18: metrics by declaration rate across the full range. Screenshot not captured yet.</p></figcaption></figure>

Two readings matter more than the shape itself:

* **A curve that rises as the rate falls** is a model whose own uncertainty is informative. The predictions it is unsure about really are the ones it gets wrong, which is what makes abstention worth anything.
* **A flat curve** is the case above: withholding predictions is buying nothing on that metric.

This run was taken to a declaration rate of **65%**, below the suggested optimum, where the slider reports a minimum confidence of **0.852** and **64.1%** of the cohort still answered for. Deploying below the suggested rate is a defensible choice when the goal is caution rather than a better headline metric, but it should be a decision made in the open: it silences roughly a third of the cohort in exchange for no measured AUC gain.

<figure><img src="../.gitbook/assets/demo/19-mdr-at-dr.png" alt=""><figcaption><p>Figure 19: the curve at 65%, with the lost-profile markers on the DR axis. Screenshot not captured yet.</p></figcaption></figure>

{% hint style="info" %}
Population kept is not the same number as the declaration rate, which is why 65% and 64.1% differ here. It is measured at the operating point immediately below the current threshold, so it describes what is really retained rather than the nominal rate.
{% endhint %}

## The profiles

The tree partitions the same cohort into readable rules. Colouring by mean confidence level gives the fastest read of where the model is comfortable.

<figure><img src="../.gitbook/assets/demo/20-tree-full.png" alt=""><figcaption><p>Figure 20: the APC profile tree over the whole population. Screenshot not captured yet.</p></figcaption></figure>

At depth 3 over 244 features, the tree split on age and on two cancer flags. The rules this run produced, visible later in the deployment output, are:

```
age_original <= 77.5 & adm_lung_cancer <= 0.5 & dx_metastatic_solid_cancer <= 0.5
age_original <= 77.5 & adm_lung_cancer > 0.5
```

That is the payoff of keeping the tree shallow. Out of 244 columns, the profile boundaries land on three that a clinician can reason about immediately.

Lowering the declaration rate fades profiles out as they lose their patients. A profile that disappears early is one the model is uniformly unsure about, not merely one that is small.

<figure><img src="../.gitbook/assets/demo/21-tree-faded.png" alt=""><figcaption><p>Figure 21: the same tree at 65%, with lost profiles faded. Screenshot not captured yet.</p></figcaption></figure>

Clicking a node opens its detail: the profile path, its share of the population, its mean confidence, and a bar per metric for the base model's performance **inside that profile**.

<figure><img src="../.gitbook/assets/demo/22-node-detail.png" alt=""><figcaption><p>Figure 22: base-model performance within one profile. Screenshot not captured yet.</p></figcaption></figure>

{% hint style="success" %}
Per-profile performance is the deliverable a model owner can act on. A weak profile is a concrete instruction: gather more of these patients, or retrain with them weighted, or route them to a human by policy rather than by threshold. The lung-cancer profile above is the obvious candidate to inspect first, since it is the one whose patients get flagged at deployment.
{% endhint %}

## Choosing the rate

The suggested rate optimises one metric. The rate you deploy is a judgement that also weighs how many patients you are willing to leave unanswered, and who they turn out to be. A rate that looks excellent on the curve but silences an entire profile is a different proposition from one that thins every profile evenly, and the tree beside the curve is what makes the difference visible.

**▶ Create Model** freezes the decision. The dialog restates exactly what is being frozen, so it is recorded rather than implied.

<figure><img src="../.gitbook/assets/demo/23-create-model.png" alt=""><figcaption><p>Figure 23: freezing <code>session1</code> at 65% into a deployed model named <code>med3pa_model1</code></p></figcaption></figure>

Continue to [Deploying and applying](deployment.md).
