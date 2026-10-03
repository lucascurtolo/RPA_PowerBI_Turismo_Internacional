    
from pynput import mouse

# Função de callback que será chamada quando o mouse for movido
def on_move(x, y):
    print(f'Mouse moved to ({x}, {y})')

# Configura o listener para o movimento do mouse
with mouse.Listener(on_move=on_move) as listener:
    listener.join()
