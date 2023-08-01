1- Si deseas ver como esta ordenado el codigo, este es el orden:

- En views.py podras encontrar todas las funciones de la aplicacion
- En urls.py podras encontrar todas las rutas que responden a una funcion dentro de la aplicacion
- En models.py podras encontrar todos los modelos creados a partir de la consigna entregada (En este caso: Medico, Paciente, Hospital, HistorialClinico)
- En forms.py podras encontrar todos los formularios creados para aparecer dentro de cada template correspondiente.
- En la Carpeta "templates" podras encontrar todos los templates utilizados dentro de la aplicacion, aquellos que responden a un model.py y aquellos que responden a un form.py
- En los templates que responden a models.py puedes comprobar la herencia de templates a partir de bloques creados en el template /base/

2- Si deseas comprobar el funcionamientto de la aplicacion en la pagina web te recomiendo:

- Ingresa en tu consola y escribe el comando "python manage.py runserver"
- Una vez que el programa ya esté en linea abrelo desde la url "localhost:8000/aplicacion/inicio
- Cuando estés dentro de la aplicación parado sobre inicio ya tienes la libertad de moverte libremente sobre los diferentes botones de la aplicacion
- El boton medicos te mostrara una tabla de los medicos ingresados
- El boton Pacientes te mostrara una tabla de los pacientes ingresados
- El boton Historial Clinico te mostrara una tabla de cada historial ingresado
- El boton Hospitales te mostrara una tabla con cada hospital ingresado
- El boton Administracion te permitira entrar al area administracion

3- Para acceder a administracion deberas logearte, para esto necesitas:

- En tu consola ingresar "python manage.py createsuperuser", luego enter, el campo del mail es opcional y la contraseña deberas ingresarla dos veces
- Vuelve a acceder al boton Administracion y logeate
- Una vez dentro de la administracion tienes acceso a ver y modificar lo que quieras

4- Para probar los formularios solo ingresa en el url /aplicacion/:
- Medico_Form1/
- Paciente_Form1/
- Hospital_Form1/
- Historial_Form1/

5- El formulario hecho para buscar algo dentro de la base de datos es el boton FORM BUSCAR

- Atiende a la peticion de /aplicacion/buscar_medico/
- Usalo para buscar un medico dentro de la base de datos introduciendo su nombre


