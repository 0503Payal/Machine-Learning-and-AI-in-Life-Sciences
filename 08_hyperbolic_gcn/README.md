# Hyperbolic GCN for Drug-like Molecule Property Prediction

Group project with **Ksenia Krasikova**, **Payal Priyadarshini** and **Philipp Harlos** (equal contribution).
Part of the lab seminar *Machine Learning and AI in the Life Sciences: Methods and
Applications*, Freie Universität Berlin.

## Goal

Implement a hyperbolic graph convolutional network for the same QM9 dipole
moment task, embedding the graph in hyperbolic rather than Euclidean space.

## Result

Improved performance across all losses compared with the Euclidean GCN of
project 07.

## Contents

| File | What it is |
|---|---|
| [`hyperbolic_gcn.ipynb`](hyperbolic_gcn.ipynb) | Hyperbolic GCN implementation and evaluation |
| [`report.pdf`](report.pdf) | Project report |

**Stack:** JAX, Flax, Jraph, Morphomatics
