from evdev import UInput, AbsInfo, ecodes as e
import asyncio
import websockets
import json


print(e)

# Mapeo entre teclas y botones del gamepad virtual
KEY_MAPPING = {
    'a': e.BTN_A,
    'b': e.BTN_B,
    'Enter': e.BTN_START,
    'Shift': e.BTN_SELECT,
    'ArrowLeft': e.ABS_X,
    'ArrowRight': e.ABS_X,
    'ArrowUp': e.ABS_Y,
    'ArrowDown': e.ABS_Y,
}

ABS_VALUE = {
    'ArrowLeft': -1,
    'ArrowRight': 1,
    'ArrowUp': -1,
    'ArrowDown': 1
}

capabilities = {
    e.EV_KEY: [e.BTN_A, e.BTN_B, e.BTN_START, e.BTN_SELECT],
    e.EV_ABS: [
        (e.ABS_X, AbsInfo(value=0, min=0, max=255,fuzz=0, flat=0, resolution=0)),
        (e.ABS_Y, AbsInfo(0, 0, 255, 0, 0, 0)),
        (e.ABS_MT_POSITION_X, (0, 128, 255, 0)) ]
}


ui = UInput(capabilities, name="VirtualGamepad1")


# Variables para llevar el registro de teclas presionadas
pressed_keys = set()


    # while True: 
    #     message = await websocket.recv()
    #     print(f'message: {message}')
    #     if message == "press_A":
    #         ui.write(e.EV_KEY, e.BTN_A, 1)
    #         ui.syn()
    #     elif message == "release_A":
    #         ui.write(e.EV_KEY, e.BTN_A, 0)
    #         ui.syn()
async def handler(websocket):
    async for message in websocket:
        try:
            data = json.loads(message)
            key = data.get("key")
            event = data.get("event")

            if key in pressed_keys and event == 'keydown':
                continue  # Evita repetir si ya está presionado
            print("aca")
            print(e)

            if event == "keydown":
                pressed_keys.add(key)

                if key in KEY_MAPPING:
                    code = KEY_MAPPING[key]
                    if code in [e.BTN_A, e.BTN_B, e.BTN_START, e.BTN_SELECT]:
                        ui.write(e.EV_KEY, code, 1)
                    elif code in [e.ABS_X, e.ABS_Y]:
                        ui.write(e.EV_ABS, code, ABS_VALUE[key])
                    ui.syn()

            elif event == "keyup":
                pressed_keys.remove(key)

                if key in KEY_MAPPING:
                    code = KEY_MAPPING[key]
                    if code in [e.BTN_A, e.BTN_B, e.BTN_START, e.BTN_SELECT]:
                        ui.write(e.EV_KEY, code, 0)
                    elif code in [e.ABS_X, e.ABS_Y]:
                        ui.write(e.EV_ABS, code, 0)
                    ui.syn()

        except Exception as ex:
            print("Error:", ex)


async def main():
    print(f'runninc main...')
    async with websockets.serve(handler,"",8090):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())