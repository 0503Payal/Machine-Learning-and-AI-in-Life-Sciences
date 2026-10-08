# Comparative Analysis of ML Models for Binary Classification in Metabolomics

Group project with **Ksenia Krasikova** and **Payal Priyadarshini** (equal contribution).
Part of the lab seminar *Machine Learning and AI in the Life Sciences: Methods and
Applications*, Freie Universität Berlin.

## Goal

Compare four machine learning models on binary classification of a
metabolomics dataset, following Mendez et al. (2019), and identify the
metabolites that drive the prediction.

## Result

Model-by-model comparison of classification performance, plus a ranked list of
the metabolites most important to the prediction.

## Contents

| File | What it is |
|---|---|
| [`pls_regression_analysis.ipynb`](pls_regression_analysis.ipynb) | Partial least squares regression and the comparative model analysis |
| [`plsda_mtbls90.ipynb`](plsda_mtbls90.ipynb) | PLS-DA workflow on the MTBLS90 dataset |
| [`ann_linsig_mtbls90.ipynb`](ann_linsig_mtbls90.ipynb) | Artificial neural network (linear-sigmoid) workflow on MTBLS90 |
| [`report.pdf`](report.pdf) | Project report |
| [`report.html`](report.html) | The report as a web page |

**Stack:** scikit-learn, cimcb, pandas, NumPy
