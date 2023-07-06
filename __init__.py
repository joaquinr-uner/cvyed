import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from .surf2stl.py import tri_write
from scipy.spatial import Delaunay

from .dominio.py import dominio
from .esfera.py import esfera
from .fig_ejes3d_cv.py import fig_ejes3d_cv
from .fig_ejes_cv.py import fig_ejes_cv
from .gradiente.py import gradiente
from .intervalo.py import intervalo
from .dominio import dominio
