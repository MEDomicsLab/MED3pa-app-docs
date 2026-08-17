---
description: >-
  Everything a MED3pa study needs has to be in the workspace first: a cohort to
  analyse, and the model whose behaviour is being studied. Two functionalities
  are available to assist you in both of these steps.
---

# Data & Models

The **Data & Models** button in the header opens a single panel with two tabs, one per kind of input:

| Tab | What it holds |
| --- | --- |
| **Datasets** | CSV files copied into `DATA/` in your workspace and recensed into the local MongoDB |
| **Base models** | Models trained outside the application and wrapped as `.medmodel` objects under `MODELS/` |

Nothing on the [Configuration](../analysis/configuration.md) page can be selected until it has been imported here first.

{% hint style="info" %}
Both kinds of object live in the workspace folder, not in the application. Moving to a different workspace gives you a different set of datasets, models, sessions and deployments, which is a convenient way to keep separate studies apart.
{% endhint %}
