# phantomx_pincher_bringup

Este paquete inicia el brazo PhantomX Pincher tanto en simulación con `ros2_control` como conectado al hardware real. Provee el archivo de lanzamiento principal y configuraciones de controladores que se instalan junto con el paquete.

## Contenido
- `launch/phantomx_pincher.launch.py`: lanza los nodos comunes (publicador de estado del robot y *commander* MoveIt), la pila de simulación (`ros2_control`, controladores y MoveIt con RViz) o la pila para hardware real (nodo `pincher_control` y MoveIt apuntando a ese *action server*).
- `config/controllers_position.yaml` y `config/controllers_effort.yaml`: ejemplos de parámetros para `controller_manager` con control de trayectoria para el brazo y la garra en modo de posición o de esfuerzo.
- `package.xml` y `CMakeLists.txt`: declarativos del paquete y la instalación de los recursos anteriores.

## Requisitos
- ROS 2 Lyrical (Ubuntu 26.04) con soporte para `colcon`. Para ROS 2 Jazzy usar la rama `jazzy`.
- Dependencias en tiempo de ejecución: `phantomx_pincher_description`, `phantomx_pincher_moveit_config`, `robot_state_publisher`, `controller_manager`, `rviz2` y `pincher_control` (para el modo de hardware real). Asegúrate de resolver dependencias con `rosdep` dentro del *workspace*.

## Compilación
1. Desde la raíz del *workspace* (`phantom_ws`):
   ```bash
   colcon build --packages-select phantomx_pincher_bringup
   source install/setup.bash
   ```

## Uso
- **Simulación (predeterminado)**
  ```bash
  ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py
  ```
  Esto inicia `ros2_control` con controladores de trayectoria, `move_group` de MoveIt (sin su `ros2_control` interno) y RViz listo para interactuar.

- **Hardware real**
  ```bash
  ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py use_real_robot:=true
  ```
  En este modo no se inicia `ros2_control`. El nodo `pincher_control` expone la acción `follow_joint_trajectory` y MoveIt se conecta directamente a ella.

## Argumentos de lanzamiento
Se pasan al final del comando con `nombre:=valor` y se pueden combinar. Para ver todos con su descripción:
```bash
ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py --show-args
```

| Argumento | Por defecto | Para qué sirve |
|---|---|---|
| `use_real_robot` | `false` | `true` usa el robot real (`pincher_control`); `false` usa la simulación. |
| `use_suction_cup` | `false` | `true` añade la ventosa al modelo. |
| `collision_colors` | `false` | `true` usa los colores del URDF para revisar los bloques de colisión en RViz; `false` muestra los colores de los `.dae`. |
| `rviz_scale` | `0.75` | Tamaño del texto de RViz. `0.75` cabe en la pantalla de 848x480 de la Raspberry Pi; use `1.0` en un monitor normal. |
| `trajectory_resample_dt` | `0.2` | Segundos entre los puntos de las trayectorias que genera MoveIt (ver abajo). |

### Puntos de la trayectoria (`trajectory_resample_dt`)
MoveIt genera un punto de la trayectoria cada `trajectory_resample_dt` segundos, así que el número de puntos es aproximadamente **duración del movimiento / `trajectory_resample_dt`**. Por defecto es `0.2` (MoveIt usa `0.1`, es decir, el doble de puntos).

Para probar otro valor sin modificar archivos:
```bash
# Menos puntos (uno cada 0.5 s)
ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py trajectory_resample_dt:=0.5

# Más puntos (valor original de MoveIt, uno cada 0.1 s)
ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py trajectory_resample_dt:=0.1

# También funciona con el robot real
ros2 launch phantomx_pincher_bringup phantomx_pincher.launch.py use_real_robot:=true trajectory_resample_dt:=0.1
```

Para cambiar el valor por defecto de forma permanente, edite `default_value="0.2"` del argumento `trajectory_resample_dt` en **los dos** archivos de lanzamiento y vuelva a compilar:
- `phantomx_pincher_bringup/launch/phantomx_pincher.launch.py`
- `phantomx_pincher_moveit_config/launch/move_group.launch.py`

```bash
colcon build --packages-select phantomx_pincher_bringup phantomx_pincher_moveit_config
source install/setup.bash
```

Antes de cambiarlo, lea las ventajas y desventajas en [la guía de `phantomx_pincher_moveit_config`](../phantomx_pincher_moveit_config/readme.md#puntos-de-la-trayectoria-trajectory_resample_dt).

## Ajustes de controladores
- Para modificar ganancias o cambiar entre control por posición y por esfuerzo, edita los archivos en `config/` y actualiza la ruta usada en el lanzamiento si lo requieres. El valor actual cargado para simulación en `phantomx_pincher.launch.py` apunta al archivo `controllers_position.yaml` del paquete `phantomx_pincher_moveit_config`.
- Si utilizas tu propio hardware o simulador, adapta las interfaces de comando/estado y los nombres de articulación en las listas `joints` de los archivos YAML.

## Depuración
- Verifica que `robot_state_publisher` publique el TF del robot y que los controladores estén activos con:
  ```bash
  ros2 control list_controllers
  ```
- Si MoveIt no puede controlar el robot, revisa que el servidor de acción `follow_joint_trajectory` esté disponible (en hardware real) o que los controladores de `ros2_control` estén en estado `active` (simulación).
