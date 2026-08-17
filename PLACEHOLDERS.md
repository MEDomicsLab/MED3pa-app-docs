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
| `SettingsPage.png` | `interface-overview.md` → System page | The System page: Go server status, python environment path, seed, MongoDB status |
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

## Videos

Every video embed from the source GitBook was removed rather than left pointing at
radiomics content. Two places are written to accept one when it exists:

- `quick-start.md`: install walkthroughs per OS. There is no packaged installer
  yet, so there is nothing to film until the first release.
- `demonstration.md`: carries a written run-through and a warning hint that the
  video is not available yet. Replace the hint with the embed.

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
