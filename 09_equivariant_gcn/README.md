# Equivariant GCN for Molecule Dipole Moment Prediction

Group project with **Ksenia Krasikova**, **Payal Priyadarshini** and **Philipp Harlos** (equal contribution).
Part of the lab seminar *Machine Learning and AI in the Life Sciences: Methods and
Applications*, Freie Universität Berlin.

## Goal

Implement an equivariant graph convolutional network that uses 3D atom
positions and is invariant/equivariant under rigid body motions — rotation and
translation — for dipole moment prediction on QM9.

## Result

Outperforms the base GCN and is comparable to the hyperbolic GCN, showing that
building the symmetry into the architecture buys most of what the hyperbolic
geometry bought.

## Contents

| File | What it is |
|---|---|
| [`equivariant_gcn.ipynb`](equivariant_gcn.ipynb) | Equivariant GCN implementation and evaluation |
| [`report.pdf`](report.pdf) | Project report |

**Stack:** JAX, Flax, Jraph, PyTorch Geometric
