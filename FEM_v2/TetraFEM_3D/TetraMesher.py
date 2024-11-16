"""
    Tetrahedric FEM mesh constructor using open3D & TetGen
"""


#import tetgen, meshio, numpy as np
from Misc import *


def build_tetramesh(stl_path, max_volume, elem_quality = 1.5):
    """
    calls TetGen to build a volumetric tetrahedron mesh from given 
    STL surface

    args:
        stl_path (str):       path to desired STL file
        max_volume (float):   maximum tetrahedron volume
        elem_quality (float): element quality marker from 1.0 (worst) to 2.0 (best)

    returns:
        mesh (list): tetra mesh nodes and cells data
    """
    pass

import tetgen
import numpy as np
import open3d as o3d

# Define sample vertices and faces for a simple triangular mesh (e.g., a tetrahedron)
# Replace with your actual mesh vertices and faces
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

faces = np.array([
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 3],
    [1, 2, 3]
])

# Create a TetGen object and set up the mesh
tet = tetgen.TetGen(vertices, faces)

# Perform tetrahedral meshing with quality and max volume control
# Use the `a` flag for maximum tetrahedron volume and `q` for quality mesh
tet.tetrahedralize(switches='pq1.8a0.0005')
#print(res)
tet.write('debug.vtk')
    
#stl_path = r'C:\Users\Михаил\Desktop\Prog\Python\FEM_Pract\FEM_v2\Data\Bunny_v1.stl'
#build_tetramesh(stl_path, max_volume = 0.1, elem_quality = 1.5)