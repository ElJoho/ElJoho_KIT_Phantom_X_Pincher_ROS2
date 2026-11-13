# 🛠️ Setup para el Kit de Phantom X Pincher

Esta guía instala **ROS 2 Lyrical** en **Ubuntu 26.04 LTS** (probada en una Raspberry Pi 5 de 4 GB) y compila el workspace `phantom_ws` de este repositorio.

> 📌 **¿Usa ROS 2 Jazzy en Ubuntu 24.04?** La guía original para Jazzy está en la rama `jazzy` de este repositorio: [`guias/Setup/readme.md` (rama jazzy)](https://github.com/ElJoho/ElJoho_KIT_Phantom_X_Pincher_ROS2/blob/jazzy/guias/Setup/readme.md).

Este repositorio requiere el uso de [Git LFS (Large File Storage)](https://git-lfs.com/) para gestionar archivos pesados como `.stp`, `.stl`, `.ipt`, entre otros, que superan los 100 MB y no pueden ser subidos directamente a GitHub.

---

## Índice

1. Configurar Git LFS para este repositorio  
   1.1 Instalación de Git LFS (Large File Storage)  
   1.2 Clasificación de tipos de archivos  
   1.3 Confirmar seguimiento con `.gitattributes`  
2. Instalar ROS 2 Lyrical en Ubuntu 26.04  
3. Hacer que ROS 2 siempre esté listo para usarse en terminal  
4. Instalación y configuración adicionales  
   4.1 Actualizar el sistema  
   4.2 Instalar un terminal mejorado (Terminator)  
   4.3 Paquetes ROS 2 necesarios usados en el curso  
   4.4 Paquetes de Python necesarios  
   4.5 Paquetes adicionales para comunicación serie en C++  
5. Instalar Kamoso (para ver video)  
6. OpenCV: ya viene instalado  
7. Clonar y compilar `phantom_ws`  
8. Referencia rápida de "¿Qué hace cada línea?"  
9. Qué cambió respecto a Jazzy

---

## 1. Configurar Git LFS para este repositorio

### 1.1 ✅ Instalación Git LFS (Large File Storage)

1. **Instalar Git LFS**  
   Abre la terminal y ejecuta:

   ```bash
   sudo apt update
   sudo apt install git-lfs
   ```

2. **Inicializar Git LFS** (solo una vez por usuario):

   ```bash
   git lfs install
   ```

3. **Track de los distintos tipos de archivos** (solo si va a añadir archivos nuevos de estos tipos al repositorio)  
   Ejecuta el siguiente comando en la raíz del repositorio:

   ```bash
   git lfs track "*.ipt" "*.iam" "*.idw" "*.ipn" "*.stl" "*.step" "*.stp" "*.igs" "*.iges" "*.dwg" "*.dxf" "*.3ds" "*.obj" "*.fbx" "*.mp4" "*.mov" "*.avi" "*.mkv" "*.zip" "*.rar" "*.7z"
   ```

---

### 1.2 📂 Clasificación de tipos de archivos

| Categoría      | Extensiones                                                                      |
|----------------|----------------------------------------------------------------------------------|
| **Inventor**   | `.ipt`, `.iam`, `.idw`, `.ipn`                                                   |
| **CAD/3D**     | `.stl`, `.step`, `.stp`, `.igs`, `.iges`, `.dwg`, `.dxf`, `.3ds`, `.obj`, `.fbx` |
| **Video**      | `.mp4`, `.mov`, `.avi`, `.mkv`                                                   |
| **Compresión** | `.zip`, `.rar`, `.7z`                                                            |

---

### 1.3 🧩 Confirmar seguimiento con `.gitattributes`

1. Asegúrate de estar en la raíz del repositorio.
2. Agrega el archivo `.gitattributes` al repositorio:

   ```bash
   git add .gitattributes
   git commit -m "Tracking CAD, video, and archive files with Git LFS"
   ```

---

> ⚠️ **Importante:** Asegúrate de hacer `git add` a los archivos rastreados con LFS **después** de configurar el `git lfs track`, para que el seguimiento sea efectivo.

---

## 2. Instalar ROS 2 Lyrical en Ubuntu 26.04

Para instalar **ROS 2 Lyrical** en **Ubuntu 26.04**, siga la guía oficial:

👉 [Guía oficial de instalación de ROS 2 Lyrical en Ubuntu](https://docs.ros.org/en/lyrical/Get-Started/Installation/Ubuntu-Install-Debs.html)

> ⚠️ **Importante:** Se debe usar la opción **"Desktop Install"** (`ros-lyrical-desktop`) y **NO** la opción **"ros-base (Bare Bones)"**.

Estos son los comandos de esa guía, en orden:

```bash
# Idioma (Ubuntu Desktop ya usa UTF-8; esto solo lo confirma)
locale
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# Activar el repositorio Universe
sudo apt install software-properties-common
sudo add-apt-repository universe

# Añadir el repositorio de ROS 2
sudo apt update && sudo apt install curl -y
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb

# Herramientas de desarrollo (colcon, rosdep, vcstool). Necesarias para compilar phantom_ws
sudo apt update && sudo apt install ros-dev-tools

# ROS 2 Lyrical Desktop
sudo apt update
sudo apt upgrade
sudo apt install ros-lyrical-desktop
```

- **ros-dev-tools**: instala `colcon` (para compilar), `rosdep` (para instalar dependencias, ver §7) y `vcstool`.
- **ros-lyrical-desktop**: ROS 2 con RViz y las herramientas gráficas. También instala OpenCV (ver §6).

Para probarlo, abra dos terminales:

```bash
source /opt/ros/lyrical/setup.bash
ros2 run demo_nodes_cpp talker
```
```bash
source /opt/ros/lyrical/setup.bash
ros2 run demo_nodes_py listener
```

---

## 3. Hacer que ROS 2 siempre esté listo para usarse en terminal

Añada el `source` de ROS 2 al final del archivo `.bashrc`:

```bash
echo '# Inicializar siempre ROS 2' >> ~/.bashrc
echo 'source /opt/ros/lyrical/setup.bash' >> ~/.bashrc
source ~/.bashrc
```

También puede abrir el archivo con `gnome-text-editor ~/.bashrc` o `nano ~/.bashrc` y añadir `source /opt/ros/lyrical/setup.bash` al final.

> ⚠️ En Ubuntu 26.04 `gedit` ya no viene instalado (el editor es `gnome-text-editor`). Tampoco use `sudo` para editar su propio `.bashrc`: el archivo puede quedar como propiedad de root.

---

## 4. 🧰 Instalación y configuración adicionales

### 4.1 Actualizar el sistema

```bash
sudo apt-get update && sudo apt-get upgrade
```
- **¿Qué hace?** Actualiza el índice de paquetes de Ubuntu y aplica las actualizaciones disponibles para mantener el sistema al día.

---

### 4.2 Instalar un terminal mejorado (Terminator)

```bash
sudo apt-get install terminator
```
- **¿Qué hace?** Instala **Terminator**, un emulador de terminal que permite dividir paneles, guardar disposiciones y trabajar con varias consolas en una sola ventana.

---

### 4.3 Paquetes ROS 2 necesarios usados en el curso

```bash
sudo apt-get install -y \
  ros-lyrical-ros2-control \
  ros-lyrical-ros2-controllers \
  ros-lyrical-xacro \
  ros-lyrical-joint-state-publisher-gui \
  ros-lyrical-tf-transformations \
  ros-lyrical-moveit \
  ros-lyrical-moveit-servo \
  ros-lyrical-pymoveit2 \
  ros-lyrical-dynamixel-sdk
```

- **ros-lyrical-ros2-control**: Framework para administrar hardware y controladores en ROS 2 (back-end de `ros2_control`).
- **ros-lyrical-ros2-controllers**: Conjunto de controladores listos (p. ej., `joint_state_broadcaster`, `joint_trajectory_controller`) que usarás en simulación y/o hardware real.
- **ros-lyrical-xacro**: Procesador de macros Xacro para generar URDF a partir de archivos `.xacro`.
- **ros-lyrical-joint-state-publisher-gui**: Interfaz gráfica para publicar estados de articulaciones y probar cinemática sin hardware.
- **ros-lyrical-tf-transformations**: Utilidades para transformaciones espaciales (TF) en Python. También instala `transforms3d`.
- **ros-lyrical-moveit**: MoveIt y sus componentes (planificación de movimiento, plugins de RViz, etc.).
- **ros-lyrical-moveit-servo**: Control continuo (teleoperación) con MoveIt Servo.
- **ros-lyrical-pymoveit2**: Interfaz de MoveIt 2 para Python. En Jazzy se compilaba desde el archivo `.repos`; en Lyrical viene como paquete.
- **ros-lyrical-dynamixel-sdk**: SDK de los servos Dynamixel (incluye el módulo de Python `dynamixel_sdk`). En Jazzy se instalaba con `pip`.

> 💡 Use los nombres exactos en lugar de comodines como `ros-lyrical-moveit*`: ese comodín instala 85 paquetes, 34 de ellos de símbolos de depuración (`-dbgsym`), que ocupan espacio en la tarjeta SD.

> ℹ️ Ya no se instalan los paquetes de **Gazebo** (`ros-gz-*`, `*-ros2-control`): el kit usa RViz con hardware simulado (fake) o el robot real.

---

### 4.4 Paquetes de Python necesarios

```bash
sudo apt-get install -y python3-flask python3-serial
```

- **python3-flask**: Micro-framework web para crear servicios y dashboards ligeros.
- **python3-serial** (pyserial): Comunicación serie en Python; útil para hablar con microcontroladores (p. ej., Arduino).
- **transforms3d** ya queda instalado con `ros-lyrical-tf-transformations` (§4.3).

> ⚠️ En Ubuntu 26.04, `pip install` fuera de un entorno virtual está **bloqueado** (error `externally-managed-environment`). Por eso los paquetes de Python se instalan con `apt` (`python3-...`). Si necesita un paquete que solo existe en PyPI, use un entorno virtual que vea los paquetes de ROS:
> ```bash
> sudo apt-get install -y python3-venv
> python3 -m venv --system-site-packages ~/venvs/phantom
> source ~/venvs/phantom/bin/activate
> pip install <paquete>
> ```

> ℹ️ Los paquetes de Alexa (`flask-ask-sdk`, `ask-sdk`) ya no forman parte de esta guía.

---

### 4.5 Paquetes adicionales para comunicación serie en C++

```bash
sudo apt-get install libserial-dev
```

- **¿Qué hace?** Instala los headers y librerías de **libserial** para aplicaciones C++ que se comuniquen por puerto serie (p. ej., ROS 2 ↔ Arduino).

---

## 5. Instalar Kamoso (para ver video)

```bash
sudo apt update
sudo apt install kamoso
```

---

## 6. OpenCV: ya viene instalado

`ros-lyrical-desktop` ya instala OpenCV 4.10 de Ubuntu con los módulos contrib (`libopencv-dev`, `libopencv-contrib-dev` y `python3-opencv`), junto con `cv_bridge`. **No hace falta compilar OpenCV**; una segunda copia compilada en `/usr/local` podría incluso causar conflictos con `cv_bridge`. Ver [setupOpenCV/readme.md](setupOpenCV/readme.md).

Para comprobarlo:

```bash
pkg-config --modversion opencv4
python3 -c "import cv2; print(cv2.__version__)"
```

---

## 7. Clonar y compilar `phantom_ws`

### 7.1 Clonar el repositorio

```bash
mkdir -p ~/ros2 && cd ~/ros2
git clone https://github.com/ElJoho/ElJoho_KIT_Phantom_X_Pincher_ROS2.git KIT_Phantom_X_Pincher_ROS2
```

- La rama `main` es para ROS 2 Lyrical; la rama `jazzy`, para ROS 2 Jazzy.
- El último argumento mantiene el nombre de carpeta `KIT_Phantom_X_Pincher_ROS2`, que es el que usan las guías.

> ⚠️ **No ejecute `vcs import` con `phantomx_pincher.repos`.** En Lyrical no se necesita nada de ese archivo: `gz_ros2_control` y `ros_ign` son de Gazebo, `pymoveit2` se instala con apt (§4.3) y el `ros2_controllers` modificado solo sirve para control por esfuerzo.

### 7.2 ¿Qué es rosdep y dónde se ejecuta cada comando?

`rosdep` lee las dependencias que declara cada `package.xml` y las traduce a paquetes de apt (por ejemplo `xacro` → `ros-lyrical-xacro`).

| Comando | ¿`sudo`? | Cuándo | Dónde |
|---|---|---|---|
| `sudo rosdep init` | sí | una sola vez por computador | en cualquier carpeta |
| `rosdep update` | no | una vez, y de nuevo de vez en cuando para actualizar la lista | en cualquier carpeta |
| `rosdep check --from-paths src --ignore-src -r` | no | para ver qué falta | **dentro de `phantom_ws`** (lee `src/`) |
| `rosdep install --from-paths src --ignore-src -r -y` | lo pide | para instalar lo que falta | **dentro de `phantom_ws`** |

- `--from-paths src`: revisa los paquetes que hay en `src/`.
- `--ignore-src`: no intenta instalar dependencias que ya son paquetes de `src/`.
- `-r`: continúa aunque haya errores.
- `-y`: responde "sí" automáticamente a apt.

```bash
sudo rosdep init        # solo una vez por computador
rosdep update
cd ~/ros2/KIT_Phantom_X_Pincher_ROS2/phantom_ws
rosdep check --from-paths src --ignore-src -r
rosdep install --from-paths src --ignore-src -r -y
```

`rosdep check` debe terminar con `All system dependencies have been satisfied`.

### 7.3 Compilar

La Raspberry Pi tiene 4 GB de RAM, así que cierre el navegador y otros programas antes de compilar, y compile un paquete a la vez:

```bash
cd ~/ros2/KIT_Phantom_X_Pincher_ROS2/phantom_ws
MAKEFLAGS="-j2" colcon build --parallel-workers 1
source install/setup.bash
```

- `MAKEFLAGS="-j2"`: usa 2 núcleos para compilar cada paquete (menos RAM).
- `--parallel-workers 1`: compila un paquete a la vez.
- La compilación completa tarda alrededor de 1 minuto en la Raspberry Pi 5.

> ⚠️ Después de cada compilación, **abra una terminal nueva** o ejecute `source install/setup.bash`; si no, ROS sigue usando la versión anterior.

**Advertencias de compilación que se pueden ignorar:**

- La advertencia de CMake sobre compatibilidad con versiones anteriores a 3.10 (aparece en todos los paquetes).
- xacro "failed to determine deps" para `phantomx_pincher.srdf.xacro` (el SRDF se genera igual).
- `computeCartesianPath` con `jump_threshold` está obsoleto (`test_moveit.cpp`, `commander_template.cpp`).

### 7.4 Probar

```bash
# Simulación (hardware fake) con MoveIt y RViz
ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py

# Robot real
ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py use_real_robot:=true
```

Los argumentos de lanzamiento (`rviz_scale`, `collision_colors`, `trajectory_resample_dt`, etc.) se explican en el [readme de `phantomx_pincher_bringup`](../../phantom_ws/src/phantomx_pincher_bringup/readme.md#argumentos-de-lanzamiento).

**Mensajes que se pueden ignorar al lanzar:**

- `Action server: /recognize_objects not available`
- `Could not enable FIFO RT scheduling policy ... Operation not permitted`
- `Joint 'phantomx_pincher_gripper_joint' marked as passive is not known to the URDF`
- `No 3D sensor plugin(s) defined for octomap updates`
- `move_group` termina con un *segfault* **solo al cerrarlo con Ctrl+C**.

> ℹ️ `phantomx_pincher_description/launch/view_gz.launch.py` no funciona porque necesita Gazebo.

---

## 8. 📌 Referencia de "¿Qué hace cada línea?" (resumen rápido)

- `sudo apt-get update && sudo apt-get upgrade`: sincroniza índices e instala actualizaciones.
- `sudo apt install ros-dev-tools`: instala `colcon`, `rosdep` y `vcstool`.
- `sudo apt install ros-lyrical-desktop`: instala ROS 2 Lyrical con RViz y OpenCV.
- `sudo apt-get install terminator`: emulador de terminal con paneles múltiples.
- `sudo apt-get install ros-lyrical-ros2-control`: instala el back-end de `ros2_control`.
- `sudo apt-get install ros-lyrical-ros2-controllers`: controladores genéricos (broadcasters/controladores de articulaciones).
- `sudo apt-get install ros-lyrical-xacro`: utilidades Xacro para generar URDF.
- `sudo apt-get install ros-lyrical-joint-state-publisher-gui`: GUI para publicar estados articulares.
- `sudo apt-get install ros-lyrical-tf-transformations`: helpers de transformaciones TF en Python (incluye transforms3d).
- `sudo apt-get install ros-lyrical-moveit ros-lyrical-moveit-servo ros-lyrical-pymoveit2`: MoveIt, MoveIt Servo y la interfaz de Python.
- `sudo apt-get install ros-lyrical-dynamixel-sdk`: SDK de los servos Dynamixel.
- `sudo apt-get install python3-flask python3-serial`: paquetes de Python (en lugar de `pip install`).
- `sudo apt-get install libserial-dev`: librería C++ para comunicación serie.
- `sudo rosdep init` / `rosdep update`: preparan rosdep (una vez).
- `rosdep install --from-paths src --ignore-src -r -y`: instala las dependencias de `phantom_ws` (dentro de `phantom_ws`).
- `MAKEFLAGS="-j2" colcon build --parallel-workers 1`: compila `phantom_ws` usando poca RAM.

---

## 9. Qué cambió respecto a Jazzy

| Tema | Jazzy (Ubuntu 24.04) | Lyrical (Ubuntu 26.04) |
|---|---|---|
| Prefijo de paquetes | `ros-jazzy-*` | `ros-lyrical-*` |
| Archivo de setup | `/opt/ros/jazzy/setup.bash` | `/opt/ros/lyrical/setup.bash` |
| `pip install` en el sistema | funcionaba (con advertencia) | **bloqueado**: se usa `apt install python3-...` |
| Dynamixel SDK | `pip install dynamixel-sdk` | `ros-lyrical-dynamixel-sdk` |
| pymoveit2 | compilado desde `.repos` | `ros-lyrical-pymoveit2` |
| OpenCV | compilado desde el código fuente | ya viene con `ros-lyrical-desktop` |
| Gazebo | `ros-jazzy-ros-gz-*` | no se instala |
| Editor de texto | `gedit` | `gnome-text-editor` |
| Python | 3.12 | 3.14 |

El código de `phantom_ws` también necesitó cambios para Lyrical (dependencias de Gazebo, compilación de `phantomx_pincher_commander_cpp`, `ros2_control`, spawners, RViz, planificación, etc.). Ya están en la rama `main`.
