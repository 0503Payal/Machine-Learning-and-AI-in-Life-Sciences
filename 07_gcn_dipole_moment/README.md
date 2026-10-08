# GCN for Molecule Dipole Moment Prediction

Group project with **Ksenia Krasikova**, **Payal Priyadarshini** and **Philipp Harlos** (equal contribution).
Part of the lab seminar *Machine Learning and AI in the Life Sciences: Methods and
Applications*, Freie Universität Berlin.

## Goal

Implement a graph convolutional network for graph-level prediction of
molecular properties on QM9, predicting the electric dipole moment.

## Result

A trained GCN evaluated with MSE, MAE and related losses — the baseline the
next two projects are measured against.

## Contents

| File | What it is |
|---|---|
| [`gcn_dipole_moment.ipynb`](gcn_dipole_moment.ipynb) | GCN implementation, training and evaluation on QM9 |
| [`report.pdf`](report.pdf) | Project report |

**Stack:** JAX, Flax, Jraph, PyTorch Geometric
