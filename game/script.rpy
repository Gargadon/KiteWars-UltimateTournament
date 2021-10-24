# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define kaito = Character("[playername]")
define mama = Character("Mamá")
define jk = Character("Justice Kiter")
define nagare = Character("Nagare")
define ai = Character("Ai")
define hayato = Character("Hayato")
define narr = Character("Réferi")
define mt1 = Character("Maruyama Trio 1")
define mt2 = Character("Maruyama Trio 2")
define mt3 = Character("Maruyama Trio 3")
define vag = Character("Vagabundo")
$ puntajefinal = 0
# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg street night

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    #show eileen happy

    # Presenta las líneas del diálogo.

    "¿Cómo fue que terminé en esto?"

    "Siempre quise tener un cometa totalmente mío, pero esta no era la
    forma en la que lo esperaba"

    jk "¡¿Qué esperas?! ¡Usa esos Kite Cores y pilotea ese cometa ya!"

    mt1 "Si te atreves a usar esos Kite Cores, no nos haremos responsables de lo que le pase a ese sujeto."

    jk "¡No les hagas caso, ellos necesitan a esa persona para sus planes malignos!"

    mt3 "..."

    "Coloqué un Kite Core en mi celular, otro en el cometa, y de inmediato el cometa que estaba inerte,
    comenzó a elevarse en el cielo."

jump Chapter01

return
