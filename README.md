# KIT PHANTOM X PINCHER

**Autor:** Johan Alejandro López Arias ([@ElJoho](https://github.com/ElJoho))


**Director:** Pedro Fabián Cárdenas Herrera 


![Vista general del kit en RViz](rvizKIT.png)

---
## VERSIONES DE ROS 2 (RAMAS DEL REPOSITORIO)

Este repositorio tiene una rama para cada versión de ROS 2. Use la rama que corresponde a la versión instalada en su Raspberry Pi o PC:

| Rama | Versión de ROS 2 | Ubuntu | Estado |
|---|---|---|---|
| `main` | ROS 2 Lyrical | 26.04 LTS | Rama principal. Probada con hardware simulado (fake); el robot real todavía no se ha probado en Lyrical |
| `jazzy` | ROS 2 Jazzy | 24.04 LTS | Código original para Jazzy, sin los cambios de Lyrical |

Si no sabe qué versión tiene instalada, ejecute en una terminal:

```bash
echo $ROS_DISTRO
```

**Clonar la rama para ROS 2 Lyrical (`main`):**

```bash
git clone https://github.com/ElJoho/ElJoho_KIT_Phantom_X_Pincher_ROS2.git
```

**Clonar la rama para ROS 2 Jazzy (`jazzy`):**

```bash
git clone -b jazzy https://github.com/ElJoho/ElJoho_KIT_Phantom_X_Pincher_ROS2.git
```

Si ya clonó el repositorio, puede cambiar de rama con `git switch jazzy` o `git switch main` (guarde o confirme sus cambios antes de cambiar de rama).

Principales diferencias de `main` (Lyrical) respecto a `jazzy`:

- Se quitaron las dependencias de Gazebo (no existen para Lyrical). El lanzamiento `view_gz.launch.py` ya no funciona.
- No es necesario ejecutar `vcs import` con `phantomx_pincher.repos`.
- `phantomx_pincher_commander_cpp` se corrigió para compilar en Lyrical.
- Se corrigió la configuración de ros2_control y de los spawners para que Plan & Execute funcione en Lyrical.
- RViz se adaptó a una pantalla pequeña (848x480): use `rviz_scale:=1.0` al lanzar si trabaja en un monitor normal.
- El modelo en RViz usa los colores de los `.dae`; para ver los bloques de colisión con colores use `collision_colors:=true` (ver [Colores del modelo y bloques de colisión](#colores-del-modelo-y-bloques-de-colisión-collision_colors)).

> **Nota:** las guías de instalación de la carpeta `guias/Setup` todavía describen la instalación de ROS 2 Jazzy en Ubuntu 24.04.

---
## EN CASO DE EMERGENCIA

Si han dañado el sistema operativo de la raspberry pi instalando algo, pueden reestablecer el sistema con ubuntu 24.04 y todo instalado y configurado (nomachine,ros2, opencv, etc) siguiendo el tutorial del repositorio ([UNPi5_Image_Ubuntu24_04](https://github.com/labsir-un/UNPi5_Image_Ubuntu24_04.git))

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=L0ZhnwBIGkc">Reestablecer sistema de raspberry pi 5 usando el backup</a>
  </summary>
</details>
<br>

## Iniciando

### Introduccion al Kit fisico

Se recomienda ver los siguientes videos introductorios al kit fisico:

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=fg1AXdiOE6Y">Introducción al Kit fisico del robot</a>
  </summary>
</details>
<br>

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=txS73u_q9bY">Como organizar el Kit en su contenedor</a>
  </summary>
</details>
<br>

### Conexión con Raspberry Pi para ver pantalla

Para observar la pantalla de la Raspberry Pi necesita realizar una conexión usando un cable ethernet y un programa conocido como NoMachine. El proceso de cómo hacerlo puede verlo en la guía en el siguiente enlace:

[Guia: Conexión NoMachine](guias/Setup/conexionNoMachine.md)

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=30KEEl1uhBM">Como conectarse a las raspberry pi usando NoMachine</a>
  </summary>
</details>
<br>

### Probar el funcionamiento del robot usando Dynamixel Wizard 2.0

Para probar el funcionamiento del robot se puede usar el programa Dynamixel Wizard que ya viene instalado en la raspberry pi. No se cuenta con una guia pero si con un video mostrando el funcionamiento del programa y como se prueba el robot con Dynamixel Wizard 2.0

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=VNw8zVJwRWo" >Como usar Dynamixel Wizard 2.0</a>
  </summary>
</details>
<br>


### Conexión SFTP en VS Code (Recomendado)

Es posible usar Visual Studio Code para editar y subir archivos a la Raspberry Pi usando una extensión de SSH. El proceso para realizar esto se encuentra en la siguiente guía:


[Guia: Edición remota con la extensión SFTP de VS Code](guias/Setup/sftp_vscode.md)

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=CL0vpqbWdjM">Como usar visual studio code SFTP para conectarse a raspberry pi</a>
  </summary>
</details>
<br>

> **Importante:** Este NO consume RAM de las raspberry pi
> PERO requiere sincronizar constantemente la carpeta de windows
> con la carpeta de la raspberry pi.

### Conexion usando Samba

La conexión mediante Samba permite acceder a los archivos de la Raspberry Pi desde Windows como si fueran una carpeta compartida en red. Esto facilita editarlos con IDEs de Windows, así como copiar, pegar o arrastrar archivos directamente. Aunque requiere instalar Samba en la Raspberry y configurarlo en Windows, una vez listo resulta muy cómodo, especialmente para proyectos grandes.


[Guia: Configuración Samba en Raspberry pi y windows](guias/Setup/guiaSamba.md)


<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=cnAaOMN6Adk">Como usar Samba para conectarse a raspberry pi</a>
  </summary>
</details>
<br>

> **Importante:** Este NO consume RAM de las raspberry pi
> PERO requiere de reconectar constantemente las raspberry 
> y windows por medio del uso de windows powershell cada vez
> que se conecta la raspberry al PC al usar el comando en 
> windows powershell (NO ejecutar como administrador):
> net use Z: \\192.168.10.2\unpi /user:unpi unpi /persistent:nes

### Conexión SSH en VS Code

Es posible usar Visual Studio Code para editar y subir archivos a la Raspberry Pi usando una extensión de SSH. El proceso para realizar esto se encuentra en la siguiente guía:


[Guia: Configuración SSH en VS Code](guias/Setup/sshVScode.md)

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=30KEEl1uhBM">Como conectarse a las raspberry pi usando NoMachine</a>
  </summary>
</details>
<br>

> **Importante:** Este metodo consume RAM de las raspberry pi
> pero permite modificar los archivos directamente.


---

## Setup

Para observar la guía de cómo hacer la instalación de ROS2 en Ubuntu 24.04 LTS puede dirigirse al siguiente archivo:

[Guia: Setup de ROS2](guias/Setup/readme.md)

---
## URDF y RVIZ

### Añadiendo elementos al robot


En la siguiente guia se encuentra una serie de pasos para añadir elementos xacro al robot para su visualizaci´on en rviz. Adicionalmente hay una serie de 10 videos explicando las distintas maneras en que se pueden añadir elementos para modificar la plataforma del robot o al brazo robotico. Adicionalmente se explica como usar la ventosa en el video final.

[Guia: Añadir elementos xacro al robot](guias/URDF/addingXacroElements.md)

<details>
  <summary>
    <b>Video tutorial. Ep. 1</b> — <a href="https://www.youtube.com/watch?v=12hgfwh_EL4">Introducción a URDF</a>
  </summary>
</details>
<br>

<details>
  <summary><b>Ep. 10</b> — <a href="https://www.youtube.com/watch?v=GsfinJpJwyY">Cambiar posición del TCP</a></summary>
</details>

> **Importante:** Para cambiar el TCP a suction puede usar la
> variable `use_suction_cup:=true` con el paquete bringup usando el
> siguiente comando:

> `ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py use_suction_cup:=true`

### Colores del modelo y bloques de colisión (`collision_colors`)

Por defecto el modelo en RViz se ve con los colores propios de los archivos `.dae` (los colores del modelo 3D). Si quiere revisar los bloques de colisión con colores, lance el robot con la variable `collision_colors:=true`:

```bash
ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py collision_colors:=true
```

Luego, en RViz, en la pestaña **Displays**, abra **MotionPlanning → Scene Robot** y active **Show Robot Collision**. Se recomienda desactivar **Show Robot Visual** mientras revisa las colisiones, para ver solo los bloques de colisión. También puede bajar **Robot Alpha** (por ejemplo a 0.5) para ver el modelo a través de ellos.

| `collision_colors` | Modelo visual | Bloques de colisión |
|---|---|---|
| `false` (por defecto) | Colores de los `.dae` | Casi todos en **rojo** |
| `true` | Colores planos del URDF | Colores del URDF (gris, negro, rojo, amarillo, ...) |

**¿Por qué las colisiones se ven rojas con `collision_colors:=false`?** RViz usa un solo color por link: el `<material>` del `<visual>` del link, y lo aplica tanto al modelo visual como a sus colisiones (RViz ignora el `<material>` que se ponga dentro de `<collision>`). Para que se vean los colores de los `.dae`, los visuales no llevan `<material>`, y entonces RViz pinta las colisiones con su color por defecto, que es rojo. Por eso no es posible ver al mismo tiempo los colores de los `.dae` y las colisiones con color.

- La canastilla y la zona circular de recolección conservan su color en ambos casos porque su modelo visual es un `.stl`, que no tiene colores propios, y siempre lleva `<material>`.
- En las canecas, el bloque de colisión (`canecaGrande.stl`) tiene casi la misma forma y posición que el modelo visual, por eso el rojo y el color original se mezclan a parches. Desactive **Show Robot Visual** para verlas bien.

> **Nota:** `collision_colors` se lee solo al arrancar, así que para cambiarlo hay que cerrar y volver a lanzar. Se puede combinar con otras variables, por ejemplo `use_suction_cup:=true collision_colors:=true`. También funciona con `view.launch.py` y `display.launch.py` del paquete `phantomx_pincher_description` (allí la opción se llama **Collision Enabled** en el display **RobotModel**).

---

## MoveIt

### Como mover el robot

Para mover el robot puede leer la guia o ver el video que se muestran a continuacion:

[Guia: Comandos de Movimiento](guias/Moveit/MOTION_COMMANDS.md)


<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=CDmSgoLtIdU">Como mover el robot (Mottion commands)</a>
  </summary>
</details>
<br>

### Calibración del gripper

[Guia: Calibración del gripper](guias/Setup/guia_calibracion_gripper.md)

---

## APRENDE ROS2

Se recomienda ver el [indice sobre las guias de ros2_basics](guias/ROS2_basics/README.md) el cual cuenta con enlaces a las guias disponibles asi como menciona videos tutoriales que pueden ver.

A continuacion se listan las guias disponibles:

1. [Guía:  Parte 1 — Publishers y subscribers](guias/ROS2_basics/ros2_basics_part1_publisher_and_subscriber.md)

2. [Guía: Parte 2 — Mover el robot](guias/ROS2_basics/ros2_basics_part2_moving_the_robot.md)


---

## REPOSITORIOS RELACIONADOS

### Repositorio con todos los modelos 3D usados en el desarrollo del kit

[3DModels_KIT_Phantom_Pincher_X100](https://github.com/labsir-un/3DModels_KIT_Phantom_Pincher_X100.git)

### Repositorio con el back up del sistema operativo de la raspberry pi 5

[UNPi5_Image_Ubuntu24_04](https://github.com/labsir-un/UNPi5_Image_Ubuntu24_04.git)


---

## Como hacer un Back up

Si el profesor, monitor o estudiantes fuesen a añadir o modificar el sistema operativo, es posible que necesiten hacer un back up del mismo. La siguiente guia y tutorial.

[Crear un backup del sistema de la Raspberry Pi 5 con Disks (Ubuntu 24.04)](guias/Setup/backupRaspberryPi.md)

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=gqHvcgRHNKI"> Crear Backup del sistema de raspberry pi 5 usando Disks en Ubuntu 24.04</a>
  </summary>
</details>
<br>