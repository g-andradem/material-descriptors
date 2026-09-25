import pandas as pd
import numpy

# READ CSV
def read_file(name_file):
    file = pd.read_csv(name_file)
    materials = file.iloc[:, :-2].to_numpy()
    # print(vetores)
    return materials

# CREATE DATA CSV
def write_data(name_file):
    pass

# NUMBER OF ELEMENTS
def create_descritor_one(materials):

    number_of_elements = [0] * len(materials)

    for i, elements_values in enumerate(materials):
        for element in elements_values:
            if element != 0:
                number_of_elements[i] += 1

    return number_of_elements

# MEAN ATOMIC MASS
def create_descritor_two(materials):

    mean_atomic_mass = 1
    
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
    
    vetores = read_file('test.csv')
    # vetores = read_file('unique_m.csv')

    descritor_1 = create_descritor_one(vetores)
    # descritor_2 = create_descritor_two(vetores)

    print(descritor_1)
    # print(descritor_2)

if __name__ == '__main__':
    main()