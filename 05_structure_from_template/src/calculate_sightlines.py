import numpy as np

def find_sightlines(pt, camera_matrix):
    pt = np.hstack([pt,[1]]).reshape(3,1)
    pt = np.linalg.inv(camera_matrix) @ pt
    return pt / np.linalg.norm(pt)