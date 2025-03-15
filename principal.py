from cliente import cliente 
from saludo import saludo 

#+++ codigo principal +++

# creando objetos

objcliente = cliente()
objsaludo = saludo()
# udo los metodos de los objectos 
objcliente.tomar_datos()
aux_mensaje= objsaludo.hacer_saludo_forma()
objcliente.hacer_saludo(aux_mensaje)