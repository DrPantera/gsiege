# Instrucciones de instalación #

A continuación se indican las instrucciones para instalar Gades Siege en un sistema GNU/Linux basado en paquetería Debian. Para otros sistemas la instalación sería equivalente.

## Descargar Gades Siege del repositorio ##

Suponiendo que tenemos instalado SVN, abrimos un terminal y escribimos lo siguiente
```
svn checkout http://gsiege.googlecode.com/svn/trunk gsiege
```

Esto creará una carpeta `gsiege` con el contenido del programa.

## Descargar Python-Clips ##
### Usuarios de Python 2.6 y versiones anteriores ###
El siguiente paso será descargar el paquete del motor de Clips para Python. Será necesario entrar en la [web oficial](http://sourceforge.net/projects/pyclips/files/debian%20packages/) y elegir el paquete apropiado para nuestra arquitectura. Una vez descargado, podréis instalarlo usando el gestor de paquetes interactivo de vuestra distribución o mediante la línea de comandos, usando la expresión:
```
sudo dpkg -i nombre_paquete.deb
```

### Usuarios de Python 2.7 y posteriores versiones ###
El motor de Clips para Python no se encuentra empaquetado para versiones posteriores de Python, por lo que la instalación debe hacerse manualmente.
Primero, instalamos las dependencias:
```
sudo apt-get install libclips-dev python-dev build-essential
```

Seguidamente, entramos en la web oficial y descargamos el [código fuente de la distribución](http://sourceforge.net/projects/pyclips/files/pyclips/pyclips-1.0/pyclips-1.0.7.348.tar.gz/download). Descomprimimos el paquete, entramos en el directorio que se genera y ejecutamos lo siguiente:
```
cd pyclips
sudo python setup.py install
```

Con esto, ya estará instalado el motor de Clips para Python en nuestro sistema.

## Instalar el resto de dependencias ##
Gades Siege tiene, como dependencias principales, **pycha** para pintar gráficas estadísticas y **pygame** para mostrar gráficos (utilizados al pintar las partidas). Ambas bibliotecas suelen estar en los repositorios principales, así que su instalación se limita al siguiente comando:
```
sudo apt-get install python-pycha python-pygame
```




## Ejecución ##
La ejecución de Gades Siege se realiza lanzando el script principal, localizado en la carpeta base del proyecto:
```
./gsiege.py
```