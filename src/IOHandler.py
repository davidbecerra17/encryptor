# IOHandler module

# Returns the raw text of the specified file
# Retorna el texto plano del archivo indicado
def read(choosen_file):
    the_file = open(choosen_file,'r')
    text = the_file.readlines()
    the_file.close()
    return text

# Saves the message to the specified path
# Guarda el mensaje en la ruta especificada
def save(filename,message):
    the_file = open("Database/" + str(filename),'w')
    the_file.write(message)
    the_file.close()