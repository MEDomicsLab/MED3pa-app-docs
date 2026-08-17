---
description: >-
  This is a tutorial on how to read the results of a MED3pa experiment and pick
  the declaration rate to deploy at.
---

# Analysis Workspace

The Analysis Workspace is step 2. It loads one saved session and lets you explore it; nothing here re-runs the experiment.

<figure><img src="../../.gitbook/assets/AnalysisWorkspace.png" alt=""><figcaption><p><em>Analysis Workspace</em> — declaration-rate slider, MDR curves and APC profile tree</p></figcaption></figure>

### Loading a session

Pick a session from the **📂 Session** selector at the top. A run launched from the Configuration page opens here automatically; older ones are reachable from this selector or from Session History.

Once loaded, **⚙ Saved configuration** unfolds the exact settings the session was run with — base model, dataset, target column and every IPC / APC / MPC parameter. This is what makes two sessions comparable after the fact.

### The three headline figures

| Card | What it reports |
| --- | --- |
| **Patients analyzed** | Size of the evaluation cohort |
| **Suggested declaration rate** | The declaration rate at which the selected metric is best |
| **Improvement at optimal DR** | How much that metric gains against the full-population baseline, e.g. `Auc: 0.812 → 0.904` |

The metric behind the last two cards is chosen from the dropdown inside the card; changing it moves the active declaration rate to that metric's optimum.

### The declaration-rate slider

The slider sets the **active DR threshold**, and everything below it reacts. Alongside it the page reports:

* **min confidence** — the MPC value a patient must reach to be declared at this rate;
* **population kept** — the share of the cohort that actually clears that threshold.

{% hint style="info" %}
Population kept is the size of the population at the operating point immediately below the current threshold, so it reflects what is really retained rather than the nominal rate. The metrics displayed beside it are computed on the at-or-above population, so the two describe slightly different sets of patients.
{% endhint %}

### 📈 Metrics by declaration rate

The MDR chart draws each selected metric against the declaration rate; use the **Show metrics** panel on the left to choose which curves are drawn. A vertical marker follows the active DR.

Dots on the DR axis mark where each profile drops out of the tree — hover one for details. They use the same samples ratio as the tree beside them, so a dot marks exactly the point at which that profile greys out.

### 🌿 APC profile tree

The tree shows the profiles extracted by the APC. Controls above it:

| Control | Effect |
| --- | --- |
| **Color by** | Colours nodes by mean confidence level or by any per-profile metric |
| **Min samples ratio** | Selects which profile set from the samples-ratio sweep is displayed |
| **Show on nodes** | Prints the chosen metrics directly on each node |

Profiles fade out when they are lost below the active DR. Clicking a node opens a detail dialog with the profile path, its node information — node %, population %, mean confidence level, positive % — and a bar per metric for the **base model's performance within that profile**. The ⤢ button expands the tree to full screen with the same controls.

<figure><img src="../../.gitbook/assets/ApcTree.png" alt=""><figcaption><p>Expanded profile tree with a node's detail open; the two greyed-out nodes are lost at this DR</p></figcaption></figure>

### Creating a deployed model

When the declaration rate is where you want it, click **▶ Create Model**. The dialog restates what is being frozen — the session, the base model, the declaration rate and the minimum confidence it corresponds to — and asks for a name.

What is created is a **deployment**: the base model, the trained IPC and APC of that session, the MPC strategy, and the confidence threshold at the chosen DR. New patients whose confidence falls below that threshold will be flagged for human review rather than answered. The application then moves to the [Deployment](../../deployment.md) page.
