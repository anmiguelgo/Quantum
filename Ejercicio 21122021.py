# Problema de satisfaccion de restricciones 

# Importamos Solver y EmbeddingComposite

import dwavebinarycap
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Donde y con que maquina quiero ejecutar mi pgm, por ejemplo estos dos de mas abajo

sampler = EmbeddingComposite(DWaveSampler())
# sampler = EmbeddingComposite(DWaveSampler(solver='DW_2000_6'))
# sampler = EmbeddingComposite(DWaveSampler(solver=dict(topology__type='pegasus')))

# Definicion de variables
#####################################################################
## horario      --> 1: Trabajo      0: Fuera de trabajo
## ubicacion    --> 1: Presencial   0: Remoto
## duracion     --> 1: Corta        0: Larga
## asistencia   --> 1: Obligatoria  0: Opcional
#####################################################################

# Definicion cuerpo principal

def planifica(horario, ubicacion, duracion, asistencia):
if horario:
# en horario de oficina
    return (ubicacion and asistencia)
else:
    # fuera de horario
    return (not ubicacion and duracion)

csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constarint(planifica, ['horario', 'ubicacion', 'duracion', 'asistencia'])

bqm = dwavebinarycsp.stitch(csp)
print(bqm)
