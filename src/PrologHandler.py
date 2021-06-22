from pyswip import Prolog

def text_to_prolog(text):
    result = ""
    text_list = list(text)
    for i in range(len(text_list)):
        line = "index(" + str(i) + ",'" + text_list[i] + "')\n"
        result += line
    return result

def prolog_to_text(prolog_list):
    result = ""
    prolog = Prolog()
    for i in range(len(prolog_list)):
        prolog.assertz(prolog_list[i])
        prolog_results = list(prolog.query('index(' + str(i) + ',X)'))
        result += prolog_results[0]['X']
    return result