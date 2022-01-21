# Problema de satisfaccion de restricciones 

# Importamos Solver y EmbeddingComposite

import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# importamos la posibilidad de inspeccionar
import dwave.inspector

# Donde y con que maquina quiero ejecutar mi pgm,

sampler = EmbeddingComposite(DWaveSampler())
# sampler = EmbeddingComposite(DWaveSampler(solver='DW_2000_6'))
# sampler = EmbeddingComposite(DWaveSampler(solver=dict(topology__type='pegasus')))

# Definición de variables
#####################################################################
## horario      --> 1: Trabajo      0: Fuera de trabajo
## ubicación    --> 1: Presencial   0: Remoto
## duración     --> 1: Corta        0: Larga
## asistencia   --> 1: Obligatoria  0: Opcional
#####################################################################

# Definicion cuerpo principal

def planifica(horario, ubicacion, duracion, asistencia):
    if horario:
    # en horario de oficina
        return (ubicacion and asistencia)
    else:
        # fuera de horario
        return (not ubicacion and not duracion)

csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(planifica, ['horario', 'ubicacion', 'duracion', 'asistencia'])

bqm = dwavebinarycsp.stitch(csp)
print(bqm.linear)
print(bqm.quadratic)

response = sampler.sample(bqm, num_reads = 5000)
min_energy = next(response.data(['energy']))[0]

print(response)

# habilitamos el inspeccionador
dwave.inspector.show(response)

dwave.inspector.show(response)
total = 0
for sample, energy, occurences in response.data(['sample', 'energy', 'num_occurrences']):
    total = total + occurences
    # if energy == min_energy:
    horario = 'Horario de Trabajo' if sample['horario'] else 'fuera de horario'
    ubicacion = 'presencial' if sample['ubicacion'] else 'remota'
    duracion = 'corta' if sample['duracion'] else 'larga'
    asistencia = 'obligatoria' if sample['asistencia'] else 'opcional'
    print("{}: {} sesion de tipo {}, de duracion {} con asistencia {}"
        .format(occurences, horario, ubicacion, duracion, asistencia))