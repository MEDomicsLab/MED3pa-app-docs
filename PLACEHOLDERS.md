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

`demonstration/` is a five-stage walkthrough with 33 figures, all under
`.gitbook/assets/demo/`. Seventeen are real, cropped from the captures in
`proof of concept 3`. Sixteen are still generated placeholder cards; each of those
figures has a caption ending "Screenshot not captured yet", and the surrounding
prose is written so it never describes something the reader cannot see. Replace a
file with the real screenshot, keeping the name, and the page picks it up with no
edit; then drop that sentence from the caption.

Still to capture:

| File | Page | Should show |
|---|---|---|
| `01-workspace-gate.png` | setup | The workspace gate before a folder is chosen |
| `02-header.png` | setup | The header bar once a workspace is open |
| `04-datasets-list.png` | setup | The Datasets tab with the cohorts listed after import |
| `07-model-imported.png` | setup | The base model under "Already imported" |
| `12-apc-settings.png` | configuration | The APC section expanded |
| `13-run-progress.png` | configuration | MPC and experiment settings, plus the progress bar mid-run |
| `14-session-loaded.png` | analysis | The session selector with a session loaded |
| `15-saved-config.png` | analysis | "Saved configuration" unfolded |
| `17-dr-100.png` | analysis | The DR slider at 100% |
| `18-mdr-curve.png` | analysis | The MDR curve, undimmed and with no dialog over it |
| `19-mdr-at-dr.png` | analysis | The curve at the deployed rate, with lost-profile markers |
| `20-tree-full.png` | analysis | The APC tree at DR 100% |
| `21-tree-faded.png` | analysis | The same tree at the deployed rate, profiles faded |
| `22-node-detail.png` | analysis | A node's detail dialog, showing per-profile metrics |
| `27-single-patient.png` | deployment | The single-patient manual entry tab |
| `32-session-history.png` | patient | The Session History table |

The analysis page carries the two facts that depend on those captures: the
per-profile performance figures (needs `22`) and the rate at which the first
profile drops out (needs `19`).

## Links to confirm

- **Repository URL.** Every link points at `https://github.com/Thedetektive/MED3paApp`,
  which is where the app currently lives. Update everywhere if it moves under the
  MEDomicsLab organization.
- **Contact form** in `forms/contact-us.md` is the Google Form carried over from the
  source GitBook. Confirm it is the right one for MED3pa.
- **Discord invite** in `SUMMARY.md` is the MEDomicsLab invite from the source GitBook.
- **`README.md` cover image** is `cancer-ai.jpg`, inherited from the source GitBook.
  It is generic AI-in-medicine art, not MED3pa-specific, so swap it if you have
  something better.

## Assets

`.gitbook/assets/` was emptied of everything radiomics-specific. What is left is
either MED3pa material copied from the website and the package, or generic
material from the source GitBook that still applies (`cancer-ai.jpg`,
`MEDomicsLab-Principles-1.png`, `NewIssue*.png`, `AffiliationsMartin.png`,
`github-logo.png`, `linkedin-logo.png`; the last two are currently unused).

`MED3paPackage.svg` and `MED3paSubpackage.svg` come from the package docs and have
hard-coded white backgrounds, so they need a white container to look right in dark
mode.
