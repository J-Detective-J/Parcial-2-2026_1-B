import sys
sys.path.append("./generados")

from gramaticaBNRLexer import gramaticaBNRLexer
from gramaticaBNRParser import gramaticaBNRParser
from gramaticaBNRVisitor import gramaticaBNRVisitor


from antlr4 import *
from gramaticaBNRLexer import gramaticaBNRLexer
from gramaticaBNRParser import gramaticaBNRParser
from gramaticaBNRVisitor import gramaticaBNRVisitor


class MyVisitor(gramaticaBNRVisitor):

    def __init__(self):
        self.db = {}


    # INSERT

    def visitInsert(self, ctx):
        collection = ctx.ID().getText()
        
        if collection not in self.db:
            self.db[collection] = []

        doc = {}
        for pair in ctx.document().pair():
            key = pair.ID().getText()
            value = self.getValue(pair.value())
            doc[key] = value

        self.db[collection].append(doc)

        print(f"\n[INSERT]")
        print(f"Colección: {collection}")
        print(f"Documento insertado: {doc}")

        return self.visitChildren(ctx)


    # FIND

    def visitFind(self, ctx):
        collection = ctx.ID().getText()

        print(f"\n[FIND]")
        print(f"Colección: {collection}")

        if collection not in self.db:
            print("No existe la colección")
            return

        results = self.db[collection]

        if ctx.condition():
            results = [doc for doc in results if self.evaluateCondition(ctx.condition(), doc)]

        print("Resultados:")
        for r in results:
            print(r)

        return self.visitChildren(ctx)


    # UPDATE

    def visitUpdate(self, ctx):
        collection = ctx.ID().getText()

        print(f"\n[UPDATE]")
        print(f"Colección: {collection}")

        if collection not in self.db:
            print("No existe la colección")
            return

        for doc in self.db[collection]:
            if not ctx.condition() or self.evaluateCondition(ctx.condition(), doc):
                
                for assign in ctx.assignments().assignment():
                    key = assign.ID().getText()
                    value = self.getValue(assign.value())
                    
                    print(f"Modificando {key}: {doc.get(key)} -> {value}")
                    doc[key] = value

        return self.visitChildren(ctx)


    # DELETE

    def visitDelete(self, ctx):
        collection = ctx.ID().getText()

        print(f"\n[DELETE]")
        print(f"Colección: {collection}")

        if collection not in self.db:
            print("No existe la colección")
            return

        nuevos = []
        for doc in self.db[collection]:
            if ctx.condition() and self.evaluateCondition(ctx.condition(), doc):
                print(f"Eliminando: {doc}")
            else:
                nuevos.append(doc)

        self.db[collection] = nuevos

        return self.visitChildren(ctx)


    # HELPERS


    def getValue(self, ctx):
        text = ctx.getText()
        
        if text.startswith('"'):
            return text.strip('"')
        elif text.isdigit():
            return int(text)
        return text

    def evaluateCondition(self, ctx, doc):
        expr = ctx.getText()

        # Ejemplo simple: edad>18
        for key in doc:
            expr = expr.replace(key, str(doc[key]))

        try:
            return eval(expr)
        except:
            return False
def main():
    input_stream = FileStream("ejemplo.txt", encoding="utf-8")
    
    lexer = gramaticaBNRLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    parser = gramaticaBNRParser(stream)
    tree = parser.program()  
    
    visitor = MyVisitor()
    visitor.visit(tree)
 


if __name__ == "__main__":
    main()
