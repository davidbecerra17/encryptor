# PrologHandler module

# Prolog lib
from pyswip import Prolog

# Returns facts in PROLOG syntax
# Retorna los hechos en la sintaxis PROLOG
def text_to_prolog(text):
    result = ""
    text_list = list(text)
    for i in range(len(text_list)):

        # Do not include the last dot '.'
        # No incluir el ultimo puntito '.'
        line = "index(" + str(i) + ",'" + text_list[i] + "')\n"
        result += line
    return result

# Returns in plain text all characters read by PROLOG
# Retorna en texto plano todos los caracteres leidos por PROLOG
def prolog_to_text(prolog_list):
    result = ""
    prolog = Prolog()
    for i in range(len(prolog_list)):
        prolog.assertz(prolog_list[i])
        prolog_results = list(prolog.query('index(' + str(i) + ',X)'))
        result += prolog_results[0]['X']

        # Important to retract the fact entered above, since the Prolog class is a singleton and therefore must be cleaned before being used again.
        # Importante retractar el hecho antes ingresado, dado que la clase Prolog es un singleton y por lo tanto debe ser limpiada antes de ser usada otra vez.
        prolog.retract(prolog_list[i])
    return result