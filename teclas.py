from pynput import keyboard as kb

#Funciones que leen la tecla tanto cuando se toca como cuando se suelta y se sale cuando se toca la tecla f
"""def pulsa (tecla):
    print("Pulso la tecla: ", tecla)

def suelta(tecla):
    print("Solto la tecla", tecla)
    if tecla==kb.KeyCode.from_char("f"):
        return False
kb.Listener(pulsa, suelta).run()"""

#Funciones que devuelve un msj en 2 combinaciones de teclas
"""def pulsa_ctrl_h():
    print('Esta combinacion de teclas (ctrl+h) muestra/oculta archivos ocultos')

def pulsa_ctrl_d():
    print('Esta combinación de teclas (ctrl+d) finaliza una sesión')

def pulsa_ctrl_alt_t():
    print("Esta combinacion de teclas (ctrl+alt+t) abre una nueva terminal")

hotkeys = { '<ctrl>+h': pulsa_ctrl_h,
                '<ctrl>+d': pulsa_ctrl_d,
                '<ctrl>+<alt>+t': pulsa_ctrl_alt_t }

with kb.GlobalHotKeys(hotkeys) as escuchador:
    escuchador.join()"""



# funciona que devuelve combinaciones de teclas con el msj dentro de un diccionario
def pulsa(msj):
    print("Esta combinacion de teclas: ", msj)
    return
hotkeys = {"<ctrl>+h": pulsa("muestra/oculta archivos ocultos"), 
            "<ctrl>+<alt>+t": pulsa("abre una nueva terminal")
            }
                
with kb.GlobalHotKeys(hotkeys) as escuchador: #CREO QUE EL PROBLEMA ESTA AQUI, en la funcion de GlobalHotkey
    escuchador.join()

