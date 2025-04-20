from evdev import UInput, ecodes as e
import time

# Mapeo NES: A, B, Start, Select, y la cruceta (D-Pad)
capabilities = {
    e.EV_KEY: [
        e.BTN_A,        # NES A
        e.BTN_B,        # NES B
        e.BTN_START,    # NES Start
        e.BTN_SELECT,   # NES Select
        e.BTN_DPAD_UP,
        e.BTN_DPAD_DOWN,
        e.BTN_DPAD_LEFT,
        e.BTN_DPAD_RIGHT,
    ]
}

            # vendor=0x1234,
            # product=0x5678,
            # version=0x0001,
# Crear el dispositivo virtual
ui = UInput(events=capabilities,
            name="NES Virtual Gamepad",
            bustype=e.BUS_USB)

input("hola")
print("✅ Gamepad virtual NES creado. Presionando botones de prueba...")

# Prueba: simular presionar A, B y Arriba
time.sleep(1)
ui.write(e.EV_KEY, e.BTN_A, 1)  # Presionar A
ui.write(e.EV_SYN, e.SYN_REPORT, 0)
time.sleep(0.1)
ui.write(e.EV_KEY, e.BTN_A, 0)  # Soltar A
ui.write(e.EV_SYN, e.SYN_REPORT, 0)

time.sleep(0.1)
ui.write(e.EV_KEY, e.BTN_B, 1)  # Presionar B
ui.write(e.EV_SYN, e.SYN_REPORT, 0)
time.sleep(0.1)
ui.write(e.EV_KEY, e.BTN_B, 0)  # Soltar B
ui.write(e.EV_SYN, e.SYN_REPORT, 0)

time.sleep(0.1)
ui.write(e.EV_KEY, e.BTN_DPAD_UP, 1)  # Arriba
ui.write(e.EV_SYN, e.SYN_REPORT, 0)
time.sleep(0.2)
ui.write(e.EV_KEY, e.BTN_DPAD_UP, 0)  # Soltar
ui.write(e.EV_SYN, e.SYN_REPORT, 0)

print("🎮 Botones simulados.")
print("🛑 Ctrl+C para salir y liberar el dispositivo.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    ui.close()
    print("\n👋 Gamepad virtual cerrado.")
