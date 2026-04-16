grammar gramatica;



program
    : statement* EOF
    ;


// CRUD


statement
    : insert ';'
    | find ';'
    | update ';'
    | delete ';'
    ;

// CREATE
insert
    : INSERT INTO ID document
    ;

// READ
find
    : FIND ID (WHERE condition)?
    ;

// UPDATE
update
    : UPDATE ID SET assignments (WHERE condition)?
    ;

// DELETE
delete
    : DELETE FROM ID (WHERE condition)?
    ;


// DOCUMENTOS (JSON-like)


document
    : '{' pair (',' pair)* '}'
    ;

pair
    : ID ':' value
    ;


// ASIGNACIONES

assignments
    : assignment (',' assignment)*
    ;

assignment
    : ID '=' value
    ;


// CONDICIONES

condition
    : expression
    ;

expression
    : expression AND expression
    | expression OR expression
    | NOT expression
    | comparison
    | '(' expression ')'
    ;

comparison
    : ID operator value
    ;

operator
    : '==' 
    | '!=' 
    | '>' 
    | '<' 
    | '>=' 
    | '<='
    ;


// VALORES
value
    : STRING
    | NUMBER
    | document
    | array
    ;

array
    : '[' value (',' value)* ']'
    ;


// TOKENS

INSERT : 'INSERT';
INTO   : 'INTO';
FIND   : 'FIND';
WHERE  : 'WHERE';
UPDATE : 'UPDATE';
SET    : 'SET';
DELETE : 'DELETE';
FROM   : 'FROM';

AND    : 'AND';
OR     : 'OR';
NOT    : 'NOT';

ID     : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER : [0-9]+;
STRING : '"' (~["\\] | '\\' .)* '"';

WS : [ \t\r\n]+ -> skip;