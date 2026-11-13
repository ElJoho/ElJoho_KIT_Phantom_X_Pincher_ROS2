# OpenCV en Ubuntu 26.04 con ROS 2 Lyrical: no hace falta instalarlo

Con **ROS 2 Lyrical** no hay que compilar ni instalar OpenCV aparte. El paquete `ros-lyrical-desktop` (ver la [guía de Setup](../readme.md)) ya instala:

- `ros-lyrical-cv-bridge`, que depende de:
- `libopencv-dev`: OpenCV 4.10 de Ubuntu para C++ (que a su vez instala `libopencv-contrib-dev`, los módulos contrib).
- `python3-opencv`: OpenCV para Python, con los módulos contrib.

> ⚠️ No compile otra copia de OpenCV en `/usr/local`: puede entrar en conflicto con la versión que usa `cv_bridge`.

> 📌 La guía anterior para **Ubuntu 24.04 / ROS 2 Jazzy** (compilar OpenCV desde el código fuente con los módulos contrib) está en la rama `jazzy`: [`guias/Setup/setupOpenCV/readme.md` (rama jazzy)](https://github.com/ElJoho/ElJoho_KIT_Phantom_X_Pincher_ROS2/blob/jazzy/guias/Setup/setupOpenCV/readme.md).

---

## Verificar la instalación

Después de instalar ROS 2 Lyrical:

Ver la versión instalada con pkg-config.

```bash
pkg-config --modversion opencv4
```

Verificar que Python pueda importar OpenCV e imprimir la versión.

```bash
python3 -c "import cv2; print(cv2.__version__)"
```

Ambos comandos deben mostrar una versión 4.10.
