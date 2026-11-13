#!/usr/bin/env python3
"""
Deja SIN contraseña el llavero "Inicio de sesión" (Login keyring) de GNOME.

Para qué sirve: con el inicio de sesión automático, GNOME no conoce la
contraseña del usuario y no puede desbloquear el llavero. Ahí guarda las
credenciales del Escritorio remoto (RDP), así que sin esto el escritorio
remoto no funciona después de reiniciar.

La aplicación "Contraseñas y claves" (Seahorse) de Ubuntu 26.04 ya no tiene
la opción de cambiar esa contraseña, por eso se hace con este script.

Uso (en la Raspberry Pi, con la sesión gráfica abierta):
    python3 vaciar_contrasena_llavero.py
Pide la contraseña actual del usuario (la misma con la que inicia sesión).
"""
import getpass
import subprocess
import sys

import dbus

bus = dbus.SessionBus()
svc_obj = bus.get_object("org.freedesktop.secrets", "/org/freedesktop/secrets")
service = dbus.Interface(svc_obj, "org.freedesktop.Secret.Service")
internal = dbus.Interface(svc_obj, "org.gnome.keyring.InternalUnsupportedGuiltRiddenInterface")

_, session = service.OpenSession("plain", dbus.String("", variant_level=1))
collection = dbus.ObjectPath("/org/freedesktop/secrets/collection/login")


def secret(text):
    return dbus.Struct(
        (session, dbus.ByteArray(b""), dbus.ByteArray(text.encode()), "text/plain"),
        signature="oayays",
    )


if sys.stdin.isatty():
    old = getpass.getpass("Contraseña actual del usuario: ")
else:
    # Sin terminal (por ejemplo, lanzado desde otro programa): ventana emergente
    r = subprocess.run(
        ["zenity", "--password", "--title=Contraseña actual del usuario"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        sys.exit("Cancelado.")
    old = r.stdout.rstrip("\n")

try:
    internal.ChangeWithMasterPassword(collection, secret(old), secret(""))
except dbus.DBusException as e:
    sys.exit(f"Falló (¿contraseña incorrecta?): {e.get_dbus_message() or e}")
print("Listo: el llavero 'Inicio de sesión' ya no tiene contraseña.")
