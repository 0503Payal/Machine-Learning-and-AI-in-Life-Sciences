# Non-Rigid Structure from Motion

Group project with **Ksenia Krasikova**, **Payal Priyadarshini** and **Philipp Harlos** (equal contribution).
Part of the lab seminar *Machine Learning and AI in the Life Sciences: Methods and
Applications*, Freie Universität Berlin.

## Goal

Reconstruct 3D keypoints from 2D observations using the Non-Rigid Structure
from Motion algorithm, across three sequences.

## Result

Reconstruction matches the reference for the Hulk sequence, and normalisation
measurably improves reconstruction for Seq_23 and Seq_27.

## Contents

| File | What it is |
|---|---|
| [`nrsfm_reconstruction.ipynb`](nrsfm_reconstruction.ipynb) | K-nearest neighbours, direction vectors, geodesic distance and depth, 3D reconstruction |
| [`report.pdf`](report.pdf) | Project report |

**Stack:** scikit-learn, NumPy, matplotlib (3D)
