# 👩‍💻 Contributing

MED3pa-app is published as pre-releases rather than a stable version, and the [**Quick Start**](quick-start.md) guide doubles as the contribution guide: its install-from-source steps are the ones a contributor follows.

MED3pa is one application of the MEDomics platform, and follows its conventions: branching model, commit naming, pull-request expectations and code review. They are documented once, for every module, in the [MEDomicsLab contributing guide](https://medomicslab.gitbook.io/medomics-docs/contributing).

There are two codebases, and which one to touch depends on the change:

| Repository | What belongs there |
| --- | --- |
| [MED3pa-app](https://github.com/MEDomicsLab/MED3pa-app) | The desktop application: interface, Go dispatcher, Python glue scripts |
| [MED3pa](https://github.com/MEDomicsLab/MED3pa) | The library: confidence estimators, profile extraction, declaration-rate metrics |

A change to how a confidence value is computed belongs in the package. A change to how it is configured or displayed belongs in the app.

{% hint style="info" %}
If you are developing against both at once, build the app's environment first, then replace the pinned MED3pa inside it with an editable install of your checkout:

```bash
bash pythonEnv/create_conda_env.sh med3pa_app 3.12
conda run -n med3pa_app pip install -e ../packages/MED3pa
```
{% endhint %}

Found a bug rather than a fix? Go to [Report an issue](forms/report-an-issue.md).
