# Machine Learning and AI in the Life Sciences

Nine projects from the lab seminar *[Machine Learning and AI in the Life
Sciences: Methods and Applications](https://www.fu-berlin.de/vv/de/lv/935203)*
at Freie Universität Berlin. Each project pairs an implementation with a written
scientific report.

The seminar runs across three quite different areas — **applied ML on omics
data**, **3D computer vision**, and **geometric deep learning on molecular
graphs** — so the collection covers tabular classification, reconstruction from
images, and learning on graphs.

| # | Project | Area | Code | Report |
|---|---|---|---|---|
| 01 | [Comparative analysis of ML models for binary classification in metabolomics](01_metabolomics_binary_classification) | Omics / ML | 3 notebooks | [pdf](01_metabolomics_binary_classification/report.pdf) |
| 02 | [Impact of data dirtiness and imputation on model performance](02_data_dirtiness_imputation) | Data quality | notebook | [pdf](02_data_dirtiness_imputation/report.pdf) |
| 03 | [Binary vs multiclass classification on transcriptomics data](03_binary_vs_multiclass) | Omics / ML | notebook | [pdf](03_binary_vs_multiclass/report.pdf) |
| 04 | [Non-rigid structure from motion](04_nonrigid_structure_from_motion) | 3D vision | notebook | [pdf](04_nonrigid_structure_from_motion/report.pdf) |
| 05 | [Structure from template](05_structure_from_template) | 3D vision | notebook + package | [pdf](05_structure_from_template/report.pdf) |
| 06 | [X-Gaussian splatting](06_xray_gaussian_splatting) | 3D vision | review only | [pdf](06_xray_gaussian_splatting/report.pdf) |
| 07 | [GCN for molecule dipole moment prediction](07_gcn_dipole_moment) | Geometric DL | notebook | [pdf](07_gcn_dipole_moment/report.pdf) |
| 08 | [Hyperbolic GCN for drug-like molecule properties](08_hyperbolic_gcn) | Geometric DL | notebook | [pdf](08_hyperbolic_gcn/report.pdf) |
| 09 | [Equivariant GCN for dipole moment prediction](09_equivariant_gcn) | Geometric DL | notebook | [pdf](09_equivariant_gcn/report.pdf) |

## Three projects worth reading together

Projects **07, 08, 09** attack the same problem ie. predicting the electric
dipole moment of molecules from the QM9 dataset. 

The useful conclusion is in that last comparison: encoding the physical symmetry
of the problem buys roughly what the change of geometry bought, from a different
direction.

## Projects 04 and 05

Both reconstruct 3D keypoints from 2D observations, with different assumptions.
**Non-rigid structure from motion** (04) recovers shape and motion from a
sequence of images of a deforming object. **Structure from template** (05)
reconstructs from a single image given a known template of the object.
Project 05 tests and result figures, so it runs end to end.

## Attribution

All nine are group projects with equal contribution **Ksenia** and **Philipp**: Reports are written in the eLife article template.

Where a notebook is based on a practical skeleton provided by the course, the
scaffolding is the course's and the implementation is ours.
