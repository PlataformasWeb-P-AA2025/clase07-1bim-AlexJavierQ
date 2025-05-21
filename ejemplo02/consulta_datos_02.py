from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Sacar las matriculas con su estudiante y módulo
matriculas = session.query(Matricula).all()

#for m in matriculas:
 #   print(m, m.estudiante, m.modulo)
    
# Obtener todos los modulos que tengan matriculas de estudiantes cuyo nombre sea tony
#Usando la relacion entre matriculas y estudiantes podemos buscar desde el query todas las matriculas donde el #estudiante asociado sea "Tony", se usa matricula.estudiante.has ya que entre modulos y estudiantes hay una #relacion muchos a muchos y .has permite aplicar filtros a este tipo de objetos y finalmente luego de recorrer #todas las matriculas filtradas podemos obtener el nombre del los modulos.
modulos = session.query(Matricula).filter(
    Matricula.estudiante.has(nombre='Tony')
).all()
for m in modulos:
    print(m.modulo.nombre) 
    
