import sys
import ply.yacc as yacc
from lexer import tokens

# PARSER
def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

def p_statement_expression(p):
    'statement : expression SEMICOLON'
    p[0] = p[1] 

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES power'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE power'
    p[0] = p[1] / p[3]

def p_term_modulo(p):
    'term : term MODULO power'
    p[0] = p[1] % p[3]

def p_term_power(p):
    'term : power'
    p[0] = p[1]

def p_power_exp(p):
    'power : factor EXP power'
    p[0] = p[1] ** p[3]

def p_power_factor(p):
    'power : factor'
    p[0] = p[1]

def p_factor_integer(p):
    'factor : INTEGER'
    p[0] = int(p[1])

def p_factor_float(p):
    'factor : FLOAT'
    p[0] = float(p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error message for syntax errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

