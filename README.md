![EDUCACION](img/EDUCACION.png)

**Instituto Tecnológico de Tijuana**    
**Subdirección Académica**  
**Departamento de Sistemas y Computación**  

**Periodo:** *Febrero - Junio*  
**Carrera:** *Ing. Sistemas Computacionales*

**Programación Lógica y funcional**     
**Alumno:** *David Enrique Becerra Ramírez* **Clave:** *17211502*   
**Docente:** Diego Saul Vázquez Rios    

---

# ENCRYPTOR

### DISCLAIMER
Este script es con fines educativos y demostrativos, no ha sido probado en modo producción ni debe usarse como tal.

---

### INTRODUCCION    
**Encryptor** en un pequeño script que encripta y desencripta un mensaje dado por el usuario. Toma el mensaje original y cambiará cada caracter por otro de forma *pseudo-aleatoria*, siendo la contraseña la unica forma de acceder al mensaje original. Lo que hace interesante a este script es que en **ningun momento se guarda la contraseña en la base de datos**. Este programa hace uso de la librería ***PySwi*** para establecer los hechos en lenguaje **PROLOG** y finalmente los consulta.

---

### REQUERIMIENTOS
- Python 3.4 o superior
- SWI-Prolog 7.2.x o superior
- Funciona unicamente en Windows
- Git (para instalarlo desde la consola)

---

### INSTALACIÓN
Abra la consola donde desee que se instale el script
````
git clone https://github.com/davidbecerra17/encryptor.git
````

---

### USO
Una vez descargado el repositorio, hay que entrar en la carpeta y ejecutar el archivo [Main.py](Main.py).     

````
cd encryptor
python Main.py
````

Al ejecutar el script [Main.py](Main.py), se imprimirá el siguiente menú

````
1 -- Nuevo Mensaje
2 -- Abrir Mensaje
3 -- Salir
>> 1
````

En caso que el usuario desde crear un nuevo mensaje, se tomará el siguiente ejemplo:

````
Ingrese el mensaje: este es un mensaje secreto
Ingrese una contraseña: 1q2w3e
Ingrese el nombre del archivo: ms.pl
````

Es importante que el nombre del archivo tenga terminación pl. Una vez ingresados los anteriores campos, se regresará al menú, donde podrá seleccionar la opción 2.

````
1 -- Nuevo Mensaje
2 -- Abrir Mensaje
3 -- Salir
>> 2
````

Se imprimirán los archivos guardados en la carpeta Database

````
Mensajes guardados
1 -- Database\ms.pl
>> 1
Ingrese la contraseña: 1q2w3e
Mensaje: este es un mensaje secreto
Ingrese cualquier tecla para continuar
````

En caso de ingresar una contraseña erronea, el mensaje será el siguiente

````
Mensajes guardados
1 -- Database\ms.pl
>> 1
Ingrese la contraseña: 0o9i8u
Mensaje: n96n5n95k45zn49t?n59n2mn6b
Ingrese cualquier tecla para continuar
````

---

### DETALLES

Ademas del script [Main.py](Main.py), existen otros 3 módulos que proporcionan los metodos y funciones para guardar y abrir los archivos, para escribir los hechos en sintaxis de PROLOG y viceversa; y para encriptar y desencriptar los mensajes.

- Detalles de [IOHandler.py](src/IOHandler.py)    
- Detalles de [PrologHandler.py](src/PrologHandler.py)    
- Detalles de [EncryptHandler.py](src/EncryptHandler.py)  

---

### CONCLUSION

Este programa ha sido desarrollado como una demostración del uso de la programación funcional en interacción con Python, como se mencionó anteriormente no es totalmente seguro usar en un entorno de producción, solo con fines educativos y demostrativos.