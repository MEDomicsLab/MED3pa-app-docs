# 👩‍💻 Contributing

As **MED3pa-app** has not yet been officially released, the [**Quick Start**](quick-start.md) guide also serves as the contribution guide.

There are two codebases, and which one to touch depends on the change:

| Repository | What belongs there |
| --- | --- |
| [MED3paApp](https://github.com/Thedetektive/MED3paApp) | The desktop application: interface, Go dispatcher, Python glue scripts |
| [MED3pa](https://github.com/MEDomicsLab/MED3pa) | The library: confidence estimators, profile extraction, declaration-rate metrics |

A change to how a confidence value is computed belongs in the package. A change to how it is configured or displayed belongs in the app.

{% hint style="info" %}
If you are developing against both at once, install the library in editable mode into the app's Python environment:

```bash
bash pythonEnv/create_conda_env.sh med3pa_app ../packages/MED3pa
```
{% endhint %}

Found a bug rather than a fix? Go to [Report an issue](forms/report-an-issue.md).
