import pandas as pd
import numpy as np
from pymatgen.core import Element

# READ CSV
def read_file(path_file):
    file = pd.read_csv(path_file)
    materials = file.iloc[:, :-2]
    return materials

# CREATE DATA CSV
def write_file(path_file):
    pass

# NUMBER OF ELEMENTS
def create_descritor_one(materials):

    number_of_elements = np.count_nonzero(materials, axis=1)

    return number_of_elements

# MEAN ATOMIC MASS
def create_descritor_two(materials):

    elements = materials.columns
    atomic_masses = np.array([
        float(Element(element).atomic_mass)
        for element in elements
    ])

    number_of_elements = materials.to_numpy()

    total_mass = number_of_elements @ atomic_masses
    total_atoms = number_of_elements.sum(axis=1)

    mean_atomic_mass = total_mass / total_atoms

    return mean_atomic_mass

# RANGE ATOMIC MASS
# max(massa) - min(massa)
def create_descritor_three(materials):
    range_atomic_mass = 1

    return range_atomic_mass

# MEAN FIE
# média da primeira energia de ionização dos elementos.
def create_descritor_four(materials):
    mean_fie = 1

    return mean_fie

# RANGE FIE
# diferença entre a maior e menor energia de ionização.
def create_descritor_five(materials):
    range_fie = 1

    return range_fie

# MEAN ATOMIC RADIUS
# média dos raios atômicos.
def create_descritor_six(materials):
    mean_atomic_radius = 1

    return mean_atomic_radius

# RANGE ATOMIC RADIUS
# maior raio − menor raio.
def create_descritor_seven(materials):
    range_atomic_radius = 1

    return range_atomic_radius

# MEAN DENSITY
# média das densidades dos elementos presentes.
def create_descritor_eight(materials):
    mean_density = 1

    return mean_density

def main():
    
    materials = read_file('data/input/test.csv')

    descritor_1 = create_descritor_one(materials)
    descritor_2 = create_descritor_two(materials)

    print(descritor_1)
    print(descritor_2)

    # write_file('data/output/saida.txt')

if __name__ == '__main__':
    main()