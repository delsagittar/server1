import evdev
from evdev import InputDevice, categorize, ecodes

def detect_ps4_controller():
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

    for device in devices:
        if "Wireless Controller" in device.name:
            return device

def process_event(event):
    if event.type == ecodes.EV_ABS:
        if event.code == ecodes.ABS_X:
            print(f"Left Stick X: {event.value}")
        elif event.code == ecodes.ABS_Y:
            print(f"Left Stick Y: {event.value}")
        # Add more cases for other axes as needed

def main():
    ps4_controller = detect_ps4_controller()

    if not ps4_controller:
        print("PS4 controller not found")
        return

    print(f"Using PS4 controller: {ps4_controller.name}")

    for event in ps4_controller.read_loop():
        if event.type == ecodes.EV_KEY and event.value == 1:
            print(f"Button {categorize(event).keycode} pressed")

        if event.type == ecodes.EV_ABS:
            process_event(event)

if __name__ == "__main__":
    main()
