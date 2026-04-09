Este proyectito se llama ghostTalker, es una breve idea que se me ocurrio en la mañana de crear un codigo que creara un propio idioma el cual permite ofuscar codigo.

Esta pensado para pentesting en general, tengo que desarrollar la forma de poder utilizar este lenguaje para automatizar alguna carga de codigo, ejecutar cosas en 2do plano etc...

La idea es buscar ideas que evadan antivirus y EDR's. ya que estos funcionan con sistemas de firmas y obviamente te van a pillar un codigo ofuscado porque ya tienen patrones predefinidos.

Al crear un diccionario aleatorio unico no existen huellas de esto, por consecuente este payload seria solamente una cadena de texto para antivirus, ahi baja la chance de ser detecado.

Igual el archivo desofuscado.py utilizo la funcion exec() asique igual este codigo lo van a detectar.

Espero poder crear algo mas robusto con la misma idea, pero con mas validaciones y ya orientado definitivamente a ser utilizado en pentesting real (En entornos controlados o.O)

Cuando ejecutes el script.py se va a generar un Json, ese json es el idioma donde se va a indicar la letra y al equivalente.
Ejemplo
* "a" = "xx#s"
* "b" = "4Rc/"

y asi consecutivamente.

