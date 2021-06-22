def read(choosen_file):
    the_file = open(choosen_file,'r')
    text = the_file.readlines()
    the_file.close()
    return text

def save(filename,message):
    the_file = open("Database/" + str(filename),'w')
    the_file.write(message)
    the_file.close()