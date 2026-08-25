# Things to fill in

This file is for maintainers, not readers; GitBook publishes the pages listed in
`SUMMARY.md`, and this file is not one of them.

## Screenshots that do not exist yet

Six real screenshots of the app were carried over from the MED3pa website and are
already used in the pages. The ones below are still missing; each is named with
the page that wants it and what it should show. Drop a PNG at
`.gitbook/assets/<name>.png` and add the `<figure>` block to the page.

| Suggested file | Page | Should show |
|---|---|---|
| `OpeningPage.png` | `interface-overview.md` → Opening page | The workspace gate: "Choose a workspace folder to begin", with the Recent list |
| `AppHeader.png` | `interface-overview.md` → Header | The header bar: workspace path, server status light, Data & Models, System, Change workspace |
| `OverviewPage.png` | `interface-overview.md` → The MED3pa module | The Overview dashboard: the three KPI cards and the recent-activity feed |
| `DatasetImport.png` | `med3pa/data-and-models/datasets.md` | The Datasets tab of the Data & Models panel with a few imported CSVs listed |
| `SessionHistory.png` | `patient-lookup.md` → Session History | The session log table |
| `DeploymentBatch.png` | `deployment.md` | The Batch processing tab with a dataset selected (the current figure shows manual entry) |

## Screenshots already in place

| File | Source | Used by |
|---|---|---|
| `ConfigurationPage.png` | website `tutos/configuration.png` | `interface-overview.md`, `med3pa/analysis/configuration.md` |
| `AnalysisWorkspace.png` | website `tutos/mdr-curve.png` | `med3pa/README.md`, `med3pa/analysis/analysis-workspace.md` |
| `ApcTree.png` | website `tutos/apc-tree.png` | `med3pa/README.md`, `med3pa/analysis/analysis-workspace.md` |
| `DataAndModels.png` | website `tutos/data-and-models.png` | `med3pa/data-and-models/base-models.md` |
| `DeploymentPage.png` | website `tutos/deployment.png` | `deployment.md` |
| `PatientLookup.png` | website `tutos/patient-lookup.png` | `patient-lookup.md`; it is the patient **detail** dashboard, not the search list |
| `SettingsPage.png` | cropped from `proof of concept 3` | `interface-overview.md` → System page |

## Videos

Every video embed from the source GitBook was removed rather than left pointing at
radiomics content. Two places are written to accept one when it exists:

- `quick-start.md`: install walkthroughs per OS. There is no packaged installer
  yet, so there is nothing to film until the first release.
- `demonstration/`: the proof of concept is written out stage by stage. A video
  would sit naturally at the top of `demonstration/README.md`.

## The proof of concept

`demonstration/` is a five-stage walkthrough with 25 figures, all under
`.gitbook/assets/demo/`, numbered in reading order. Twenty-four are real
screenshots. Replace a placeholder card with the real screenshot, keeping the file
name, and the page picks it up with no edit.

One slot is still a placeholder:

| File | Page | Should show |
|---|---|---|
| `19-single-patient.png` | deployment | The single-patient manual entry tab |

Its caption is the only one ending "Screenshot not captured yet". Because the model
is 244 features wide, that form is long; a crop of the first row or two of fields
plus the Apply button would do.

## Files shipped for the proof of concept

`.gitbook/assets/` also carries the four artefacts the walkthrough links for
download: `homr_oym_rf.onnx` (18 MB), `Holdout_prepared.csv`, `Deploy3_newmodel.csv`
and `features.txt`. The cohort is synthetic, published on Zenodo under CC BY 4.0
(`10.5281/zenodo.12954673`), so it can be redistributed here.

Screenshot sources, for anyone re-cropping: `proof of concept 3/third_pics` holds
the single-window captures behind figures 1, 2, 4, 5 and 9 to 14 and 25;
`med32papocpics` and `second_pics` hold the earlier dual-monitor captures behind the
rest, which is why a few of those show other session or deployment names.
