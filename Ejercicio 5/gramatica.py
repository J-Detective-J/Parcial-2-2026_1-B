import re


# GRAMATICA

gramatica = {
    "programa": [["lista_sentencias"]],
    "lista_sentencias": [["sentencia", "lista_sentencias"], ["ε"]],
    "sentencia": [["asignacion"], ["condicional"]],
    "asignacion": [["id", "=", "expresion", ";"]],
    "condicional": [["si", "(", "expresion", ")", "entonces", "sentencia", "sino", "sentencia"]],
    "expresion": [["termino", "expresion_prima"]],
    "expresion_prima": [["+", "termino", "expresion_prima"],
                        ["-", "termino", "expresion_prima"],
                        ["ε"]],
    "termino": [["id"], ["num"]]
}

no_terminales = set(gramatica.keys())

def es_terminal(simbolo):
    return simbolo not in no_terminales and simbolo != "ε"



# PRIMEROS

def calcular_primeros():
    primeros = {nt: set() for nt in gramatica}

    cambio = True
    while cambio:
        cambio = False
        for nt in gramatica:
            for prod in gramatica[nt]:
                for simbolo in prod:
                    if simbolo == "ε":
                        if "ε" not in primeros[nt]:
                            primeros[nt].add("ε")
                            cambio = True
                        break
                    elif es_terminal(simbolo):
                        if simbolo not in primeros[nt]:
                            primeros[nt].add(simbolo)
                            cambio = True
                        break
                    else:
                        antes = len(primeros[nt])
                        primeros[nt] |= (primeros[simbolo] - {"ε"})
                        if "ε" not in primeros[simbolo]:
                            break
                        if len(primeros[nt]) > antes:
                            cambio = True
                else:
                    if "ε" not in primeros[nt]:
                        primeros[nt].add("ε")
                        cambio = True

    return primeros



# SIGUIENTES

def calcular_siguientes(primeros):
    siguientes = {nt: set() for nt in gramatica}
    siguientes["programa"].add("$")

    cambio = True
    while cambio:
        cambio = False
        for nt in gramatica:
            for prod in gramatica[nt]:
                for i, simbolo in enumerate(prod):
                    if simbolo in no_terminales:
                        resto = prod[i+1:]

                        if resto:
                            first_resto = set()
                            for s in resto:
                                if es_terminal(s):
                                    first_resto.add(s)
                                    break
                                else:
                                    first_resto |= (primeros[s] - {"ε"})
                                    if "ε" not in primeros[s]:
                                        break
                            else:
                                first_resto.add("ε")

                            antes = len(siguientes[simbolo])
                            siguientes[simbolo] |= (first_resto - {"ε"})

                            if "ε" in first_resto:
                                siguientes[simbolo] |= siguientes[nt]

                            if len(siguientes[simbolo]) > antes:
                                cambio = True
                        else:
                            antes = len(siguientes[simbolo])
                            siguientes[simbolo] |= siguientes[nt]
                            if len(siguientes[simbolo]) > antes:
                                cambio = True

    return siguientes



# PREDICCION

def calcular_prediccion(primeros, siguientes):
    pred = {}

    for nt in gramatica:
        for prod in gramatica[nt]:
            clave = (nt, tuple(prod))
            pred[clave] = set()

            if prod == ["ε"]:
                pred[clave] |= siguientes[nt]
            else:
                for simbolo in prod:
                    if es_terminal(simbolo):
                        pred[clave].add(simbolo)
                        break
                    else:
                        pred[clave] |= (primeros[simbolo] - {"ε"})
                        if "ε" not in primeros[simbolo]:
                            break
                else:
                    pred[clave] |= siguientes[nt]

    return pred



# TOKENIZADOR

def tokenize(codigo):
    especificacion = [
        ('NUM', r'\d+'),
        ('ID', r'[a-zA-Z_]\w*'),
        ('MAS', r'\+'),
        ('MENOS', r'-'),
        ('IGUAL', r'='),
        ('PYC', r';'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('ESPACIO', r'\s+'),
    ]

    tokens = []
    pos = 0

    while pos < len(codigo):
        match = None
        for tipo, regex in especificacion:
            patron = re.compile(regex)
            match = patron.match(codigo, pos)
            if match:
                texto = match.group(0)

                if tipo != 'ESPACIO':
                    if texto == 'si':
                        tokens.append(('SI', texto))
                    elif texto == 'entonces':
                        tokens.append(('ENTONCES', texto))
                    elif texto == 'sino':
                        tokens.append(('SINO', texto))
                    elif tipo == 'ID':
                        tokens.append(('ID', texto))
                    else:
                        tokens.append((tipo, texto))

                pos = match.end(0)
                break

        if not match:
            raise SyntaxError(f"Token no válido: {codigo[pos]}")

    tokens.append(('EOF', '$'))
    return tokens



# PARSER

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.actual = tokens[self.pos]

    def avanzar(self):
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
            self.actual = self.tokens[self.pos]

    def emparejar(self, tipo):
        if self.actual[0] == tipo:
            if tipo != 'EOF':
                self.avanzar()
        else:
            raise SyntaxError(f"Se esperaba {tipo} y se encontró {self.actual}")

    def programa(self):
        self.lista_sentencias()
        self.emparejar('EOF')

    def lista_sentencias(self):
        if self.actual[0] in ('ID', 'SI'):
            self.sentencia()
            self.lista_sentencias()

    def sentencia(self):
        if self.actual[0] == 'ID':
            self.asignacion()
        elif self.actual[0] == 'SI':
            self.condicional()
        else:
            raise SyntaxError("Sentencia inválida")

    def asignacion(self):
        self.emparejar('ID')
        self.emparejar('IGUAL')
        self.expresion()
        self.emparejar('PYC')

    def condicional(self):
        self.emparejar('SI')
        self.emparejar('LPAREN')
        self.expresion()
        self.emparejar('RPAREN')
        self.emparejar('ENTONCES')
        self.sentencia()
        self.emparejar('SINO')
        self.sentencia()

    def expresion(self):
        self.termino()
        self.expresion_prima()

    def expresion_prima(self):
        if self.actual[0] == 'MAS':
            self.emparejar('MAS')
            self.termino()
            self.expresion_prima()
        elif self.actual[0] == 'MENOS':
            self.emparejar('MENOS')
            self.termino()
            self.expresion_prima()

    def termino(self):
        if self.actual[0] == 'ID':
            self.emparejar('ID')
        elif self.actual[0] == 'NUM':
            self.emparejar('NUM')
        else:
            raise SyntaxError("Error en termino")



# EJECUCION

def analizar(codigo):
    tokens = tokenize(codigo)
    parser = Parser(tokens)
    parser.programa()
    print("Cadena valida")



def mostrar_tablas(first, follow, pred):
    print("\nPrimeros")
    for nt in first:
        print(f"{nt:20} -> {first[nt]}")

    print("\nSiguientes")
    for nt in follow:
        print(f"{nt:20} -> {follow[nt]}")

    print("\nPrediccion")
    print(f"{'No Terminal':20} {'| Produccion':50} {'| Prediccion'}")
    print("-"*100)

    for (nt, prod), valores in pred.items():
        prod_str = " ".join(prod)
        print(f"{nt:20} {prod_str:50} {valores}")


if __name__ == "__main__":
    with open("grama.txt", encoding="utf-8") as f:
        codigo = f.read()

    analizar(codigo)

    primeros = calcular_primeros()
    siguientes = calcular_siguientes(primeros)
    pred = calcular_prediccion(primeros, siguientes)

    mostrar_tablas(primeros, siguientes, pred)