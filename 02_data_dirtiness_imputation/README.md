# Impact of Data Dirtiness and Imputation Techniques on Model Performance

Group project with **Ksenia Krasikova**, **Payal Priyadarshini** and **Philipp Harlos** (equal contribution).
Part of the lab seminar *Machine Learning and AI in the Life Sciences: Methods and
Applications*, Freie Universität Berlin.

## Goal

Measure how robust two machine learning models are to progressively dirtier
data, and how well different imputation techniques recover performance. Every
dataset is derived from the same source, so dirtiness is the only variable.

## Result

Performance degrades measurably as dirtiness increases; the original
informative features can still be recovered from the dirty datasets.

## Contents

| File | What it is |
|---|---|
| [`dirty_data_imputation.ipynb`](dirty_data_imputation.ipynb) | Dirtiness simulation, imputation and model comparison |
| [`report.pdf`](report.pdf) | Project report |

**Stack:** scikit-learn, pandas, NumPy, matplotlib
