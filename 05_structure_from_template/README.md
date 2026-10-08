# Structure from Template

Group project with **Ksenia Krasikova**, **Payal Priyadarshini** and **Philipp Harlos** (equal contribution).
Part of the lab seminar *Machine Learning and AI in the Life Sciences: Methods and
Applications*, Freie Universität Berlin.

## Goal

Reconstruct 3D keypoints from a single image plus a known template using the
Shape-from-Template algorithm, building on Brunet et al. and related classical
work.

## Result

Overall shape is reconstructed accurately, but RMSE stays high because of
spatial misalignment — the shape is right, its placement is not.

## Contents

| File | What it is |
|---|---|
| [`sft_pipeline.ipynb`](sft_pipeline.ipynb) | End-to-end SfT pipeline |
| [`src/registration_2d_3d.py`](src/registration_2d_3d.py) | 2D–3D registration |
| [`src/calculate_sightlines.py`](src/calculate_sightlines.py) | Sightline computation |
| [`src/optimization.py`](src/optimization.py) | Optimisation routines |
| [`src/test_registration_2d_3d.py`](src/test_registration_2d_3d.py) | Tests for the registration module |
| [`data/`](data/) | 2D observations, 3D ground truth and the camera intrinsics `K` |
| [`results/`](results/) | Reconstruction figures and the RMSE comparison |
| [`report.pdf`](report.pdf) | Project report |

**Stack:** NumPy, SciPy, Open3D, matplotlib
