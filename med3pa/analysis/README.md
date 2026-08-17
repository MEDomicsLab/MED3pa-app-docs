---
description: >-
  This section gives a brief tutorial on how to use our software to run a MED3pa
  experiment and read its results.
---

# Analysis

{% hint style="success" %}
All confidence estimators, profile extraction and declaration-rate metrics are computed by the [MED3pa package](https://github.com/MEDomicsLab/MED3pa), the reference implementation of the method published in [JAMIA](https://doi.org/10.1093/jamia/ocag034).
{% endhint %}

An analysis is a single unit of work called a **session**. It is described entirely by the configuration you fill in, and everything it produces — the trained IPC and APC models, the metrics at every declaration rate, the profile tree, the lost profiles — is written to the local MongoDB under the session name and can be reopened at any time.

The two upcoming sections cover the two halves of the workflow:

* [**Configuration**](configuration.md) — declaring the inputs and the confidence settings, then running the experiment.
* [**Analysis Workspace**](analysis-workspace.md) — reading the results and choosing the declaration rate to deploy at.

### Sessions

Every completed run appears in **Session History**, with its date, base model, dataset, target column, cohort size and status. Clicking a row opens that session in the Analysis Workspace, exactly as it was.

Sessions are cheap to keep and easy to compare: running the same cohort twice under two different confidence configurations, and reading the two MDR curves side by side, is the normal way of deciding which configuration to trust.
