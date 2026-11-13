# KIT PHANTOM X PINCHER

**Autor:** Johan Alejandro López Arias ([@ElJoho](https://github.com/ElJoho))


**Director:** Pedro Fabián Cárdenas Herrera 


![Vista general del kit en RViz](rvizKIT.png)

---
## EN CASO DE EMERGENCIA

Si han dañado el sistema operativo de la raspberry pi instalando algo, pueden reestablecer el sistema con ubuntu 24.04 y todo instalado y configurado (nomachine,ros2, opencv, etc) siguiendo el tutorial del repositorio ([UNPi5_Image_Ubuntu24_04](https://github.com/labsir-un/UNPi5_Image_Ubuntu24_04.git))

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=L0ZhnwBIGkc">Reestablecer sistema de raspberry pi 5 usando el backup</a>
  </summary>
</details>

> 🎥 **Nota:** Este video se hizo inicialmente para la rama `jazzy` (ROS 2 Jazzy, Ubuntu 24.04), pero puede seguir siendo útil en la rama actual `main` (ROS 2 Lyrical, Ubuntu 26.04).

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

> 🎥 **Nota:** Estos videos se hicieron inicialmente para la rama `jazzy` (ROS 2 Jazzy, Ubuntu 24.04), pero pueden seguir siendo útiles en la rama actual `main` (ROS 2 Lyrical, Ubuntu 26.04).

<br>

### Conexión con Raspberry Pi para ver pantalla

Para observar y controlar la pantalla de la Raspberry Pi se usa un cable Ethernet y el Escritorio remoto (RDP): en Windows con **Conexión a Escritorio remoto** (`mstsc`, ya viene con Windows) y en Linux con **Remmina** (software libre). El proceso, incluida la configuración de red del PC, está en la siguiente guía:

[Guia: Conexión por Escritorio remoto (RDP) desde Windows y Linux](guias/Setup/conexionEscritorioRemoto.md)


### Probar el funcionamiento del robot usando Dynamixel Wizard 2.0

Para probar el funcionamiento del robot se puede usar el programa Dynamixel Wizard que ya viene instalado en la raspberry pi. No se cuenta con una guia pero si con un video mostrando el funcionamiento del programa y como se prueba el robot con Dynamixel Wizard 2.0

<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=VNw8zVJwRWo" >Como usar Dynamixel Wizard 2.0</a>
  </summary>
</details>

> 🎥 **Nota:** Este video se hizo inicialmente para la rama `jazzy` (ROS 2 Jazzy, Ubuntu 24.04), pero puede seguir siendo útil en la rama actual `main` (ROS 2 Lyrical, Ubuntu 26.04).

<br>


### Conexion usando Samba

La conexión mediante Samba permite acceder a los archivos de la Raspberry Pi desde Windows o Linux como si fueran una carpeta compartida en red, sin gastar CPU ni RAM de la Raspberry. Esto facilita editarlos con los programas de tu PC, así como copiar, pegar o arrastrar archivos directamente. Aunque requiere instalar Samba en la Raspberry y configurar la conexión en el PC, una vez listo resulta muy cómodo, especialmente para proyectos grandes. En Linux basta con abrir `smb://192.168.10.2/unpi` en el explorador de archivos (sección 16 de la guía).


[Guia: Configuración Samba en Raspberry pi, Windows y Linux](guias/Setup/guiaSamba.md)


<details>
  <summary>
    <b>Video tutorial</b> — <a href="https://www.youtube.com/watch?v=cnAaOMN6Adk">Como usar Samba para conectarse a raspberry pi</a>
  </summary>
</details>

> 🎥 **Nota:** Este video se hizo inicialmente para la rama `jazzy` (ROS 2 Jazzy, Ubuntu 24.04), pero puede seguir siendo útil en la rama actual `main` (ROS 2 Lyrical, Ubuntu 26.04).

<br>

> **Importante:** Este NO consume RAM de las raspberry pi
> PERO requiere de reconectar constantemente las raspberry 
> y windows por medio del uso de windows powershell cada vez
> que se conecta la raspberry al PC al usar el comando en 
> windows powershell (NO ejecutar como administrador):
> net use Z: \\192.168.10.2\unpi /user:unpi unpi /persistent:nes

---

## Setup

Para observar la guía de cómo hacer la instalación de ROS 2 Lyrical en Ubuntu 26.04 LTS y compilar `phantom_ws` puede dirigirse al siguiente archivo (la guía para ROS 2 Jazzy en Ubuntu 24.04 está en la rama `jazzy`):

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

> 🎥 **Nota:** Estos videos se hicieron inicialmente para la rama `jazzy` (ROS 2 Jazzy, Ubuntu 24.04), pero pueden seguir siendo útiles en la rama actual `main` (ROS 2 Lyrical, Ubuntu 26.04).


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

> 🎥 **Nota:** Este video se hizo inicialmente para la rama `jazzy` (ROS 2 Jazzy, Ubuntu 24.04), pero puede seguir siendo útil en la rama actual `main` (ROS 2 Lyrical, Ubuntu 26.04).

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

> 🎥 **Nota:** Este video se hizo inicialmente para la rama `jazzy` (ROS 2 Jazzy, Ubuntu 24.04), pero puede seguir siendo útil en la rama actual `main` (ROS 2 Lyrical, Ubuntu 26.04).

<br>