#********************************************************
# Proyecto del curso Sistemas Operativos
# Autores: Alejandro Peñaranda Agudelo - 201941008
#          Alejandro Escobar Tafurt    - 201941378
#********************************************************

import math
#**************************************************Zona de apertura del archivo txt******************************************************
# Aqui es donde se define el proceso que se va a ejecutar. Si se requiere ejecutar otro procesos se debe cambiar la direccion de la variable archivo
archivo = open("proceso7.txt") 
contenido = archivo.readlines()
archivo.close()

memoriaP = {}
registros = {'ACC':0, 'ICR':0, 'MAR':0, 'MDR':0, 'UC':0}
lista =[]

for fileline in contenido:
  fileline = fileline.replace("\n", "")
  lista.append(fileline)

instrucciones=[]
for i in range( len(lista) ):
  instrucciones.append( lista[i].split(" "))


#***************************************************************************************************************************************
# Procedimientos que ejecuta la instruccion que le sea ingresada.
def ejecutar (ins):
  registros['MDR'] = ins[0]
  registros['ICR'] = registros['MDR']
  registros['UC'] = registros['ICR']
  
  if ins[0] == "SET":
    SET(ins) 
  elif ins[0] == "ADD":
    ADD(ins)
  elif ins[0] == "SUB":
    SUB(ins)
  elif ins[0] == "MUL":
    MUL(ins)
  elif ins[0] == "DIV":
    DIV(ins)
  elif ins[0] == "INC":
    INC(ins)
  elif ins[0] == "DEC":
    DEC(ins)
  elif ins[0] == "MOV":
    MOV(ins) 
  elif ins[0] =="LDR":
    LDR(ins)
  elif ins[0] == "STR":
    STR(ins)
  elif ins[0] == "SUB":
    SUB(ins)
  elif ins[0] == "SHW":
    SHW(ins)
  elif ins[0] == "END":
    END(ins)
  elif ins[0] == "BEQ":
    BEQ(ins)  
  elif ins[0] == "AND":
    AND(ins)
  elif ins[0] == "OR":
    OR(ins)
  else:
    print('ERROR: La instruccion ingresada no hace parte del conjunto de instrucciones.')

# Logica de la instruccion SET
def SET (ins):
  direccion = ins[1]
  valor = int(ins[2])
  registros['MAR'] = direccion
  registros['MDR'] = valor
  memoriaP[registros['MAR']] = registros['MDR']
  
# Logica de la instruccion ADD
def ADD (ins):
  if ins[2] != 'NULL' and ins[3] != 'NULL':
    direccion1 = ins[1]
    direccion2 = ins[2]
    direccion3 = ins[3]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['MDR']
    registros['MAR'] = direccion2
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['ACC'] + registros['MDR']
    registros['MAR'] = direccion3
    registros['MDR'] = registros['ACC']
    memoriaP[registros['MAR']] = registros['MDR']
    registros['ACC'] = 0
  elif ins[2] != 'NULL':
     direccion1 = ins[1]
     direccion2 = ins[2]
     registros['MAR'] = direccion1
     registros['MDR'] = memoriaP[registros['MAR']]
     registros['ACC'] = registros['MDR']
     registros['MAR'] = direccion2
     registros['MDR'] = memoriaP[registros['MAR']]
     registros['ACC'] = registros['ACC'] + registros['MDR']
  else:
    direccion1 = ins[1]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['ACC'] + registros['MDR'] 

# Logica de la instruccion SUB
def SUB (ins):
  if ins[2] != 'NULL' and ins[3] != 'NULL':
    direccion1 = ins[1]
    direccion2 = ins[2]
    direccion3 = ins[3]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['MDR']
    registros['MAR'] = direccion2
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['ACC'] - registros['MDR']
    registros['MAR'] = direccion3
    registros['MDR'] = registros['ACC']
    memoriaP[registros['MAR']] = registros['MDR']
    registros['ACC'] = 0
  elif ins[2] != 'NULL':
     direccion1 = ins[1]
     direccion2 = ins[2]
     registros['MAR'] = direccion1
     registros['MDR'] = memoriaP[registros['MAR']]
     registros['ACC'] = registros['MDR']
     registros['MAR'] = direccion2
     registros['MDR'] = memoriaP[registros['MAR']]
     registros['ACC'] = registros['ACC'] - registros['MDR']
  else:
    direccion1 = ins[1]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['ACC'] - registros['MDR'] 
    
# Logica de la instruccion MUL   
def MUL (ins):
  if ins[2] != 'NULL' and ins[3] != 'NULL':
    direccion1 = ins[1]
    direccion2 = ins[2]
    direccion3 = ins[3]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['MDR']
    registros['MAR'] = direccion2
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['ACC'] * registros['MDR']
    registros['MAR'] = direccion3
    registros['MDR'] = registros['ACC']
    memoriaP[registros['MAR']] = registros['MDR']
    registros['ACC'] = 0
  elif ins[2] != 'NULL':
     direccion1 = ins[1]
     direccion2 = ins[2]
     registros['MAR'] = direccion1
     registros['MDR'] = memoriaP[registros['MAR']]
     registros['ACC'] = registros['MDR']
     registros['MAR'] = direccion2
     registros['MDR'] = memoriaP[registros['MAR']]
     registros['ACC'] = registros['ACC'] * registros['MDR']
  else:
    direccion1 = ins[1]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['ACC'] * registros['MDR'] 
    
# Logica de la instruccion DIV 
def DIV (ins):
  if ins[2] != 'NULL' and ins[3] != 'NULL':
    direccion1 = ins[1]
    direccion2 = ins[2]
    direccion3 = ins[3]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['MDR']
    registros['MAR'] = direccion2
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = math.floor(registros['ACC'] / registros['MDR'])
    registros['MAR'] = direccion3
    registros['MDR'] = registros['ACC']
    memoriaP[registros['MAR']] = registros['MDR']
    registros['ACC'] = 0
  elif ins[2] != 'NULL':
     direccion1 = ins[1]
     direccion2 = ins[2]
     registros['MAR'] = direccion1
     registros['MDR'] = memoriaP[registros['MAR']]
     registros['ACC'] = registros['MDR']
     registros['MAR'] = direccion2
     registros['MDR'] = memoriaP[registros['MAR']]
     registros['ACC'] = math.floor(registros['ACC'] / registros['MDR'])
  else:
    direccion1 = ins[1]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = math.floor(registros['ACC'] / registros['MDR'])
    
# Logica de la instruccion INC 
def INC (ins):
  direccion = ins[1]
  registros['MAR'] = direccion
  registros['MDR'] = memoriaP[registros['MAR']]
  registros['ACC'] = registros['MDR'] + 1
  registros['MDR'] = registros['ACC']
  memoriaP[registros['MAR']] = registros['MDR']

# Logica de la instruccion DEC
def DEC (ins):
  direccion = ins[1]
  registros['MAR'] = direccion
  registros['MDR'] = memoriaP[registros['MAR']]
  registros['ACC'] = registros['MDR'] - 1
  registros['MDR'] = registros['ACC']
  memoriaP[registros['MAR']] = registros['MDR']

# Logica de la instruccion MOV
def MOV (ins):
  direccion1 = ins[1]
  direccion2 = ins[2]
  registros['MAR'] = direccion1
  registros['MDR'] = memoriaP[registros['MAR']]
  registros['MAR'] = direccion2
  memoriaP[registros['MAR']] = registros['MDR']
  registros['MAR'] = direccion1
  memoriaP[registros['MAR']] = 0

# Logica de la instruccion LDR
def LDR (ins):
  direccion = ins[1]
  registros['MAR'] = direccion
  registros['MDR'] = memoriaP[registros['MAR']]
  registros['ACC'] = registros['MDR']

# Logica de la instruccion STR
def STR (ins):
  direccion = ins[1]
  registros['MAR'] = direccion
  registros['MDR'] = registros['ACC']
  memoriaP[registros['MAR']] = registros['MDR']
  registros['ACC'] = 0

# Logica de la instruccion SHW
def SHW (ins):
  if ins[1] == 'ACC':
    print(registros['ACC'])
  elif ins[1] == 'ICR':
    print(registros['ICR'])
  elif ins[1] == 'MAR':
    print(registros['MAR'])
  elif ins[1] == 'MDR':
    print(registros['MDR'])
  elif ins[1] == 'UC':
    print(registros['UC'])
  else:
    direccion = ins[1]
    registros['MAR'] = direccion
    print(memoriaP[registros['MAR']])

# Logica de la instruccion END
def END (ins):
  return 0

# Logica de la instruccion BEQ 
def BEQ (ins):
  if ins[2] != 'NULL' and ins[3] != 'NULL':
    direccion1 = ins[1]
    direccion2 = ins[2]
    direccion3 = ins[3]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    registros['ACC'] = registros['MDR']
    registros['MAR'] = direccion2
    registros['MDR'] = memoriaP[registros['MAR']]
    if registros['MDR'] - registros['ACC'] == 0:
      registros['MAR'] = direccion3
      memoriaP[registros['MAR']] = 0
      registros['ACC'] = 0
  elif ins[2] != 'NULL':
     direccion1 = ins[1]
     direccion2 = ins[2]
     registros['MAR'] = direccion1
     registros['MDR'] = memoriaP[registros['MAR']]
     registros['ACC'] = registros['MDR']
     registros['MAR'] = direccion2
     registros['MDR'] = memoriaP[registros['MAR']]
     if registros['MDR'] - registros['ACC'] == 0:
      registros['ACC'] = 0
  else:
    direccion1 = ins[1]
    registros['MAR'] = direccion1
    registros['MDR'] = memoriaP[registros['MAR']]
    if registros['MDR'] - registros['ACC'] == 0:
      registros['MDR'] = 0
      memoriaP[registros['MAR']] = registros['MDR']
# Logica de la instruccion AND     
def AND (ins):
  direccion1 = ins[1]
  direccion2 = ins[2]
  registros['MAR'] = direccion1
  registros['MDR'] = memoriaP[registros['MAR']]
  registros['ACC'] = registros['MDR']
  registros['MAR'] = direccion2
  registros['MDR'] = memoriaP[registros['MAR']]
  if registros['ACC'] > 0 and registros['MDR'] > 0:
    registros['ACC'] = True
  else:
    registros['ACC'] = False
    
# Logica de la instruccion OR 
def OR (ins): 
  direccion1 = ins[1]
  direccion2 = ins[2]
  registros['MAR'] = direccion1
  registros['MDR'] = memoriaP[registros['MAR']]
  registros['ACC'] = registros['MDR']
  registros['MAR'] = direccion2
  registros['MDR'] = memoriaP[registros['MAR']]
  if registros['ACC'] > 0 or registros['MDR'] > 0:
    registros['ACC'] = True
  else:
    registros['ACC'] = False
   
# Procedimiento que inicia la ejecucion del simulator
def simulator (ins):
  for j in ins:
    ejecutar(j)

# Llamada al procedimeinto simulator
simulator(instrucciones)
