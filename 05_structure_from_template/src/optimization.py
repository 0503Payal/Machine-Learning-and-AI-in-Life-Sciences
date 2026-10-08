"""
------------------------------------------------------------------------------------
This function estimates 3D structure from sightlines based on inextensibility
constraints, inspired by the following paper:

1. Brunet, F., Hartley, R., Bartoli, A., Navab, N., & Malgouyres, R. 
   "Monocular template-based reconstruction of smooth and inextensible surfaces."
   ACCV 2010.

2. Chhatkuli, A., Pizarro, D., Collins, T., & Bartoli, A.
   "Inextensible non-rigid structure-from-motion by second-order cone programming."
   IEEE TPAMI, 2017.

Originally implemented by Dilara Kus and adapted by Agniva Sengupta for ZIB SoSe2025.
------------------------------------------------------------------------------------
"""

import numpy as np
import cvxpy as cp
from scipy.spatial import distance_matrix
from tqdm import tqdm 

def estimate_depths_from_sightlines(u_vectors, template_points, k):
    print("Estimating depths from sightlines...")
    M = u_vectors.shape[0]
    delta = cp.Variable(M, nonneg=True)
    # Compute pairwise geodesic distances on template shape
    d_target = distance_matrix(template_points, template_points) # Indented correctly

    constraints = []
    print(f"Building inextensibility constraints for {M} points...")

    for i in tqdm(range(M), desc="Setting up constraints"):
        # Find k-nearest neighbors for point i (excluding itself)
        sorted_indices = np.argsort(d_target[i])
        neighbors = sorted_indices[1:k+1]

        for j in neighbors:
            X_i = delta[i] * u_vectors[i]
            X_j = delta[j] * u_vectors[j]
            diff = X_i - X_j
            constraints.append(cp.norm(diff, 2) <= d_target[i, j])  # SOC constraint

    # Optimization: maximize total depth while satisfying inextensibility
    objective = cp.Maximize(cp.sum(delta))
    problem = cp.Problem(objective, constraints)
    problem.solve(solver=cp.SCS)

    # Reconstruct 3D coordinates from optimized depths
    X_reconstructed = np.array([delta.value[i] * u_vectors[i] for i in range(M)])
    return X_reconstructed, delta.value