# Guía de uso de `phantomx_pincher_moveit_config`

Este paquete contiene la configuración de MoveIt 2 para el brazo robótico PhantomX Pincher. Incluye los archivos de lanzamiento, configuraciones de control y descripciones semánticas necesarios para planificar trayectorias y ejecutar movimientos tanto en simulación como sobre hardware real.

## Dependencias y compilación

1. Asegúrate de tener las dependencias de ejecución instaladas (MoveIt 2, `xacro`, `robot_state_publisher`, controladores `ros2_control`, etc.). El paquete declara sus dependencias en `package.xml` y se construye con `ament_cmake`.
2. Desde el workspace (`phantom_ws`), instala dependencias y compila:
   ```bash
   rosdep install --from-paths src -y --ignore-src
   colcon build --symlink-install --packages-select phantomx_pincher_moveit_config
   source install/setup.bash
   ```

## Archivos clave

- `launch/move_group.launch.py`: lanza `move_group`, RViz y (opcionalmente) `moveit_servo` para control continuo. Incluye argumentos para seleccionar el paquete de descripción URDF/SRDF, activar la colisión, escoger el plugin de `ros2_control` (`fake`, `ign`, `real`) y habilitar RViz o Servo.
- `launch/move_group_external_control.launch.py`: pensado para usar controladores ROS 1 a través de `ros1_bridge`. Publica descripciones, `move_group` y (si se desea) `moveit_servo`, dejando la gestión de controladores externos.
- `config/*.yaml`: límites articulares, cinemática, configuración de OMPL, controladores (`controllers_position.yaml`, `controllers_effort.yaml`) y parámetros de Servo (`servo.yaml`, `servo_real.yaml`).
- `srdf/phantomx_pincher.srdf.xacro`: descripción semántica paramétrica. Puede convertirse en SRDF estático con `scripts/xacro2srdf.bash`.

## Uso básico (simulación)

1. Lanza la configuración estándar con controladores falsos y RViz:
   ```bash
   ros2 launch phantomx_pincher_moveit_config move_group.launch.py
   ```
2. Argumentos útiles (se pueden pasar por línea de comandos):
   - `ros2_control_plugin:=fake|ign|real` — selecciona el backend de control.
   - `ros2_control_command_interface:=position|velocity|effort` — el tipo de comando para los controladores.
   - `enable_servo:=true|false` — habilita el nodo `moveit_servo` para teleoperación continua.
   - `enable_rviz:=true|false` — abre RViz con la configuración incluida (`rviz/moveit.rviz`).
   - `use_sim_time:=true|false` — usa reloj simulado (útil con Gazebo/Ignition).
   - `trajectory_resample_dt:=0.2` — segundos entre los puntos de las trayectorias (ver [Puntos de la trayectoria](#puntos-de-la-trayectoria-trajectory_resample_dt)).
   Consulta todos los argumentos disponibles con:
   ```bash
   ros2 launch --show-args phantomx_pincher_moveit_config move_group.launch.py
   ```
## Puntos de la trayectoria (`trajectory_resample_dt`)

Después de planificar, MoveIt calcula los tiempos de la trayectoria con el adaptador `AddTimeOptimalParameterization` y la vuelve a muestrear: genera **un punto cada `trajectory_resample_dt` segundos**. Por eso el número de puntos es aproximadamente:

```
puntos ≈ duración del movimiento / trajectory_resample_dt
```

Por ejemplo, un movimiento de 30 s tiene unos 300 puntos con `0.1` (valor original de MoveIt) y unos 150 con `0.2` (valor por defecto de este paquete).

El valor se pasa a MoveIt como el parámetro `ompl.totg.resample_dt` desde `launch/move_group.launch.py`. El launch de `phantomx_pincher_bringup` declara el mismo argumento y lo reenvía.

**Cómo cambiarlo**

- Solo para una ejecución:
  ```bash
  ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py trajectory_resample_dt:=0.5
  # o lanzando solo este paquete:
  ros2 launch phantomx_pincher_moveit_config move_group.launch.py trajectory_resample_dt:=0.5
  ```
- De forma permanente: cambie `default_value="0.2"` del argumento `trajectory_resample_dt` en `launch/move_group.launch.py` **y** en `phantomx_pincher_bringup/launch/phantomx_pincher.launch.py`, y vuelva a compilar ambos paquetes.

Para comprobar el valor que está usando MoveIt (con el launch en marcha):
```bash
ros2 param get /move_group ompl.totg.resample_dt
```

**Ventajas y desventajas**

| Valor | Puntos (movimiento de 30 s) | Comentario |
|---|---|---|
| `0.1` | ~300 | Valor original de MoveIt. Revisión de colisiones más fina. |
| `0.2` (por defecto) | ~150 | La mitad de puntos. En simulación el movimiento se ve igual de suave. |
| `0.5` | ~60 | Cinco veces menos puntos. Úselo solo con velocidades bajas. |

- **Colisiones:** la revisión final de MoveIt (`ValidateSolution`) solo comprueba los puntos de la trayectoria. Con valores grandes y velocidades altas (por ejemplo *Velocity Scaling* 1.0 en RViz) los puntos quedan muy separados y el brazo podría rozar la canastilla o las canecas entre dos puntos sin que MoveIt lo detecte.
- **Simulación:** el controlador `joint_trajectory_controller` interpola entre los puntos, así que con menos puntos el movimiento sigue siendo suave.
- **Robot real:** el nodo `pincher_control` envía a los servos solo la posición de cada punto, a una velocidad fija del servo (`moving_speed`), sin interpolar. Con menos puntos el movimiento podría verse a pasos; si pasa, use un valor más pequeño (por ejemplo `0.1`).

## Actualizar el SRDF

Para regenerar el SRDF desde el xacro semántico (por ejemplo, al modificar el efector final):
```bash
cd $(ros2 pkg prefix phantomx_pincher_moveit_config)/share/phantomx_pincher_moveit_config
./scripts/xacro2srdf.bash name:=phantomx_pincher use_real_gripper:=true
```
Esto actualizará `srdf/phantomx_pincher.srdf` con los argumentos indicados.
