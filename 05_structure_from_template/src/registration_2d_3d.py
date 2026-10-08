"""
==========================================================================================
This script implements a Shape-from-Template (SfT) 3D reconstruction method based on a 
combination of the following classical works:

1. Brunet, F., Hartley, R., Bartoli, A., Navab, N., & Malgouyres, R. 
   "Monocular template-based reconstruction of smooth and inextensible surfaces."
   ACCV 2010.

2. Chhatkuli, A., Pizarro, D., Collins, T., & Bartoli, A.
   "Inextensible non-rigid structure-from-motion by second-order cone programming."
   IEEE TPAMI, 2017.

Originally implemented by Dilara Kus and adapted by Agniva Sengupta for ZIB SoSe2025.

==========================================================================================
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from setuptools.command.install import install

from optimization import estimate_depths_from_sightlines
from calculate_sightlines import find_sightlines


def main():
    print("Hello, world!")
    script_dir = os.path.dirname(os.path.abspath('/Users/payalpriyadarshini/Downloads/vscode_ML'))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    # ------------------------------- SETUP: Paths and Frame Indices ------------------------------- #
    

    TARGET_FRAME = 10  # Frame to reconstruct
    TEMPLATE_FRAME = 8  # Frame used as template

    # ------------------------------------- LOAD DATA --------------------------------------------- #

    # Camera intrinsic matrix
    project_root = '/Users/payalpriyadarshini/Downloads/vscode_ML'
    
    camera_matrix_path = os.path.join(project_root, 'K.txt')
    print("Loading camera matrix from:", camera_matrix_path)
    camera_matrix = np.loadtxt(os.path.join(project_root, 'K.txt'), delimiter=',')

    # Load ground-truth 3D points (Target frame)
    points_3D_path = os.path.join(project_root, f'Points3D_gt_{TARGET_FRAME}.txt')
    points3D_gt = np.loadtxt(points_3D_path, delimiter=',').T

    # Load template 3D points
    template_3D_path = os.path.join(project_root, f'Points3D_gt_{TEMPLATE_FRAME}.txt')
    points3D_template = np.loadtxt(template_3D_path, delimiter=',')

    # Load 2D projections from Target frame
    points_2D_path = os.path.join(project_root, f'Points2D_{TARGET_FRAME}.txt')
    points2D = np.loadtxt(points_2D_path, delimiter=',').T

    # ---------------------- COMPUTE SIGHTLINES & RECONSTRUCT 3D POINTS --------------------------- #

    # Estimate unit sightline vectors from 2D points
    sightlines = np.array([find_sightlines(pt, camera_matrix) for pt in points2D])

    # Ensure sightlines shape is (N, 3) for downstream processing
    #sightlines = sightlines.squeeze()

    # Estimate 3D structure using a sightline-based optimization
    # This returns the reconstructed 3D points and the estimated depth values
    
    print("u_vectors shape:", sightlines.squeeze().shape)
    print("template_points shape:", points3D_template.shape)
    X_recon, _ = estimate_depths_from_sightlines(sightlines, points3D_template.T, k=5)
    X_reconstructed, delta = estimate_depths_from_sightlines(sightlines.squeeze(),points3D_template.T,k=7)

    # ------------------------------- EVALUATION: Error Metrics ------------------------------------ #accuracy

    mse = np.mean((X_reconstructed.squeeze() - points3D_gt) ** 2)
    rmse = np.sqrt(mse)
    print(f"Reconstruction RMSE: {rmse:.6f}")

    # --------------------------------- VISUALIZATION: Plotting ----------------------------------- #
    #In comparison to above this calculates the error for each point
    errors = np.linalg.norm(X_reconstructed.squeeze() - points3D_gt, axis=1)
    # Normalize to [0, 1] for colormap
    errors_normalized = (errors - np.min(errors)) / np.ptp(errors)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(X_reconstructed[:, 0], X_reconstructed[:, 1], X_reconstructed[:, 2],
                    c=errors_normalized, cmap='jet', label='Reconstructed (colored by RMSE)', s=10)
    ax.scatter(points3D_gt[:, 0], points3D_gt[:, 1], points3D_gt[:, 2],
               c='black', alpha=0.3, marker='^', label='Ground Truth', s=10)
    cbar = plt.colorbar(sc, ax=ax, shrink=0.5)
    cbar.set_label("Per-point RMSE")

    ax.set_title("Reconstructed 3D Points vs Ground Truth (Colored by Error)")
    ax.legend()
    plt.show()

    ######################triang. mesh

    import open3d as o3d

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(X_reconstructed)
    pcd.estimate_normals()
    pcd.orient_normals_consistent_tangent_plane(30)

    mesh, dens = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8)

    #nice colouring
    densities = np.asarray(dens)
    colors = plt.get_cmap("viridis")((densities - densities.min()) / (densities.max() - densities.min()))
    mesh.vertex_colors = o3d.utility.Vector3dVector(colors[:, :3])

    # Save to PNG (offscreen)
    vis = o3d.visualization.Visualizer()
    vis.create_window(visible=False)
    vis.add_geometry(mesh)
    vis.get_render_option().mesh_show_back_face = True

    vc = vis.get_view_control()
    vc.set_front([-0.5, -0.5, 1])
    vc.set_lookat(mesh.get_center())
    vc.set_up([0, 0, 1])
    vc.set_zoom(1)

    vis.poll_events()
    vis.update_renderer()
    vis.capture_screen_image(f"mesh_frame_{TARGET_FRAME}.png")
    vis.destroy_window()




    #########################################
    # ------------------------- RMSE FOR ALL FRAMES ---------------------------------- #
    rmse_list = []
    processed_frames = []
    frame_range = range(1, 11)  # Frames 1 to 10

    for frame_id in frame_range:
        try:
            print(f"Processing frame {frame_id}...")
            pts2D = np.loadtxt(os.path.join(project_root, f'Points2D_{frame_id}.txt'), delimiter=',').T
            pts3D_gt = np.loadtxt(os.path.join(project_root, f'Points3D_gt_{frame_id}.txt'), delimiter=',').T
            sightlines = np.array([find_sightlines(pt, camera_matrix) for pt in pts2D])
            X_recon, _ = estimate_depths_from_sightlines(sightlines.squeeze(), points3D_template.T, k=5)
            mse = np.mean((X_recon.squeeze() - pts3D_gt) ** 2)
            rmse = np.sqrt(mse)
            rmse_list.append(rmse)
            processed_frames.append(frame_id)
        except Exception as e:
            print(f"Failed to process frame {frame_id}: {e}")

    plt.figure(figsize=(10, 5))
    plt.bar(frame_range, rmse_list, color='mediumseagreen')
    plt.xlabel("Frame Number")
    plt.ylabel("RMSE (mm)")
    plt.title("3D Reconstruction RMSE per Frame")
    plt.xticks(frame_range)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("rmse_barplot.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
