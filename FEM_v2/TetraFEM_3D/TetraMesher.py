"""
    Tetrahedric FEM mesh constructor using open3D & TetGen
"""


import tetgen, meshio, numpy as np
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

    log_msg(f'Input file for meshing: [{stl_path}]')

    stl_mesh = meshio.read(stl_path)
    stl_verts = np.array(stl_mesh.points)
    stl_faces = np.array(stl_mesh.cells[0].data)

    log_msg(f'Original STL Surface: N_verts = {len(stl_verts)}, N_faces = {len(stl_faces)}')

    tet = tetgen.TetGen(stl_verts, stl_faces)
    nodes, cells = tet.tetrahedralize(switches = f'pq{elem_quality}a{max_volume}')

    log_msg(f'Mesh built: N_verts = {len(nodes)}, N_tetra = {len(cells)}')

    save_path = r'Mesh.vtk'
    tet.write(save_path)
    log_msg(f'Mesh saved into [{save_path}]')

    return nodes, cells


