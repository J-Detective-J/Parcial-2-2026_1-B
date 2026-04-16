# Parcial-2-2026_1-B

## Requisitos previos

Con instrucciones para instalar en
#### Linux (Debian)
- Python 3.8 o superior
<br>`sudo apt install python3 python3-pip -y`<br>
- Graphviz 14 o superior
<br>`sudo apt install graphviz -y`<br>

#### Windows
- Python 3.8 o superior
Descargar y ejecutar el `.exe` en su pagina web `https://www.python.org/downloads/?hl=ES` o a traves de Microsoft Store

- Graphviz 14 o superior
Descargar y ejecutar el `.exe` en su pagina web `https://graphviz.org/download/`<br>
Luego ejecuta en Powershell o Cmd el siguiente comando `pip install graphviz`<br>

## Para la ejecucion
Simplemente ejecutar el archivo `.py`, la entrada fue la dada en los ejemplos (archivo `.txt` modificable para pruebas).

-------------------------------------------------------------------------------------------------------------------------
# Documentacion de las actividades
# 1, 2. Gramática de un lenguaje CRUD base de datos NO relacional. 

Diseño de la gramática 

La gramática define un lenguaje con cuatro operaciones principales: 

Todo el lenguaje se guardó en gramaticaBNR.g4 para ejecutarlo en ANTLR4. 
```
INSERT -> Crear documentos  
FIND -> Consultar documentos  
UPDATE -> Modificar documentos  
DELETE -> Eliminar documentos 
```
 
#### CREATE (Insert) 

`INSERT INTO usuarios { nombre: "Juan", edad: 25 }; `
- Inserta un documento en una colección 

#### READ (Find) 

`FIND usuarios WHERE edad > 18; `<br>
Soporta condiciones con operadores: 
- `==, !=, >, <, >=, <= `
- `AND, OR, NOT `

 
#### UPDATE 
`UPDATE usuarios SET edad = 30 WHERE nombre == "Juan"; `
- Modifica campos de documentos existentes 
- Permite múltiples asignaciones 

 

#### DELETE 
`DELETE FROM usuarios WHERE edad < 18; `
- Elimina documentos según una condición


# 3. Ambiguedad 

Voy a crear la cadena <br>

`if Pedro then if Escamoso then otras else otras `
<br>

Se puede definir de 2 maneras 

- Primera manera <br>

`(if Pedro then if Escamoso then otras) else otras `

- Segunda manera <br>

`if Pedro then (if Escamoso then otras else otras) `<br>

 

Esto lleva a 2 derivaciones y por lo tanto a 2 ramas, entonces sigue siendo ambiguo <br>

 

Se puede corregir asi: 

```
completo -> todos los if tienen su else 

incompleto -> hay un if sin else 
```

Se fuerza que el else siempre se una al if más cercano <br>

` if Pedro then (if Escamoso then otras else otras)`

----------------------------------------------------------------- 
```

inicio -> completo | incompleto 
completo -> if expr then completo else completo 
         | otras 
incompleto -> if expr then inicio 
           | if expr then completo else incompleto 
```
 

# 4. El ejercicio se tomó y adapto de una actividad hecha anteriormente, asi que posee tambien la funcion de graficar el recorrido del parser, puedes añadir este codigo en `def process_file():` para crear las graficas .
```
        # Recorrido LL  
        dot_trav = graph_traversal(tree) 
        dot_trav.render(f"LL-cadena_{contador}", format="png", cleanup=True) 

        # Grafo CYK  
        dot_cyk = graph_cyk(trace) 
        dot_cyk.render(f"CYK-cadena_{contador}", format="png", cleanup=True)
```
-------------------------------------------------------------------------------------------------------------------------------
### Recorrido del árbol (LL(0))
Este analizador sintactico recorre el arbol de izquierda a derecha profundizando los nodos, ademas de que tiene una complejidad de o(n). 
Se divide en 3 metodos (E, T y F), exactamente iguales a los de la tarea 1 <br>
<img width="425" height="765" alt="image" src="https://github.com/user-attachments/assets/39cb9247-f708-4b04-9869-773739acaeeb" /><br>
pero lo mas importante es como recorre el arbol sintactico:<br>
<img width="391" height="341" alt="image" src="https://github.com/user-attachments/assets/aa7d57cb-e703-4759-9853-e068dd26b1b4" /><br>
implemente un recorrido DFS que enumera cada nodo en orden de visita, esto permite ver como el parser recorrio la expresion


### Algoritmo CYK
Este algoritmo combina subcadenas y llena la tabla dinámicamente, por esta razon no se puede graficar su recorrido en forma de arbol y esto lo registre asi:<br> `(i, j, símbolo, dependencias)`<br><br>
<img width="626" height="796" alt="image" src="https://github.com/user-attachments/assets/f218a835-60ee-4cea-bf5e-87a3062f16e2" /><br>


### Medicion de tiempos
Para saber cuanto se tarda cada algoritmo en recorrer el arbol sintactico vamos a utilizar `time.perf_counter()`<br>
<img width="573" height="443" alt="image" src="https://github.com/user-attachments/assets/41977967-107f-4192-babf-d825e957555a" />
<br>

# 5. Gramatica
El ejercicio se tomó de una actividad hecha anteriormente continuacion-ASDR y se adapto <br>

Gramatica: 
```
programa -> lista_sentencias 
lista_sentencias -> sentencia lista_sentencias 
lista_sentencias -> ε 
sentencia -> asignacion 
sentencia -> condicional 
asignacion -> id = expresion ; 
condicional -> si ( expresion ) entonces sentencia sino sentencia 
expresion -> termino expresion_prima 
expresion_prima -> + termino expresion_prima 
expresion_prima -> ε 
termino -> id 
termino -> num
```
--------------------------------------------------------------------------------------------------
## 1. Lectura de la gramática
leer_gramatica()
Lee el archivo `.txt`
- Divide cada línea en lado izquierdo y derecho

- Construye un diccionario:
`{NoTerminal: [producciones]}`

## 2. Identificación de símbolos
`obtener_simbolos()`
Separa:
- No terminales (lado izquierdo)
- Terminales (símbolos restantes)

## 3. Cálculo de primeros
`calcular_first()`
Aplica reglas:
- Si inicia con terminal -> se agrega
- Si inicia con no terminal -> se agregan sus primeros
- Maneja epsilon (ε)
E itera hasta que no haya cambios

## 4. Cálculo de siguentes
`calcular_follow()`
Reglas:
- $ al símbolo inicial
- Se agregan `primeros` de los símbolos siguientes
- Si hay epsilon -> se agrega `siguiente` del padre
E Itera hasta converger

## 5. FIRST de una producción
`first_de_produccion()`
Calcula `primero` específico para una producción

## 6. Cálculo de predecir
`calcular_predict()`<br>
Si produccion NO tiene ε:<br>
-` prediccion = primero(producción)`<br>
Si contiene ε:<br>
-` prediccion = primero - {ε} ∪ siguiente`

## 7. Verificación de gramática LL(1)

Evalúa si la gramática cumple condiciones LL(1):

Regla principal:

- Para un mismo no terminal, los conjuntos PREDICT no deben intersectarse

Proceso:
- Se construye una “tabla” (NoTerminal, Terminal)
- Se agrupan producciones por cada entrada
- Si una entrada tiene más de una producción "->" hay conflicto
