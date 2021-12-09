label Chapter01:

    scene bg kaito bedroom

    $ playername = renpy.input("Para continuar con esta aventura, debes poner tu nombre.")

    $ playername = playername.strip()

    if playername == "":
        $ playername="Kaito"


    mama "Es hora de ir a la escuela, [playername]."

    mama "¡No me hagas ir a tu cuarto y levantarte!"

    "Bien, supongo que no me puedo salvar de esta."

    "Mi mamá acaba de entrar a mi cuarto. No pudo ignorar la enorme cantidad
    de revistas relacionadas a Kite Wars sobre mi escritorio."

    mama "[playername], ¿otra vez leyendo esas revistas?"

    mama "Te he dicho varias veces que no quiero ver nada relacionado a Kite Wars
    en esta casa, me trae malos recuerdos sobre tu padre."

    "Así es, mi padre... Un gran investigador que trabajaba para Kite Incorporated.
    Llevamos alrededor de seis meses sin saber sobre él."

    "Ni la policía ni en Kite Inc. nos dan respuesta sobre su paradero.
    Es como si se hubiera esfumado de la faz de la tierra."

    "Desde entonces, mi madre no ha querido saber nada sobre los dichosos cometas."

    kaito "Supongo que podré ir temprano a la Kite Shop y..."

    mama "¿A dónde dijiste?"

    kaito "¡Nada, nada! Dije \"a la escuela\"."

    "No quiero que se entere que he estado juntando para comprar un cometa.
    Si llegara a enterarse, es capaz de llevarse todo mi dinero."

    "Tomo mi mochila y salgo de casa. En vez de tomar el camino directo,
    tomo un atajo que pasa por la Kite Shop."

    "En este mundo, se han creado cometas controlables a través de una aplicación
    para celular. Mi padre fue uno de los genios detrás de ese hito."

    scene bg kite shop

    "Y el lugar donde la magia se hace realidad es aquí, en la Kite Shop."

    "Esta es la Kite Shop más cercana a mi casa. La atiende un sujeto muy alegre
    llamado Nagare Boshi."

    nagare "Hola, [playername]. ¿Qué haces tan temprano por aquí?"

    "Nagare estaba barriendo la entrada de la tienda, es un verdadero conocedor
    de los cometas y de las Kite Wars."

    "Dice que ser dependiente de una Kite Shop es el sueño de su vida."

    kaito "Hola, Nagare. Quería saber si todavía tienes el modelo Gear 3000."

    nagare "Lo lamento, vendí el último ayer. ¿Por qué quieres un modelo tan viejo?"

    kaito "Es lo único que puedo pagar."

    nagare "Bueno... En realidad tengo uno más, pero..."

    kaito "¿Pero...?"

    nagare "Pero no tiene sus Kite Cores. Iba a devolverlo a Kite Inc. el día de
    hoy, pero si lo quieres sin Kite Cores..."

    "Los Kite Cores son como las tarjetas que se le meten a los celulares. Se
    venden en pares, uno para el cometa y otro para el celular donde se va a manejar."

    "No puede haber dos pares iguales, y cada par te identifica con el servidor
    de Kite Inc. para poder jugar y participar en los torneos oficiales."

    "Kite Inc. es la empresa que fabrica y sirve el sistema de cometas a nivel
    nacional."
    
    "Mi sueño es participar en un Ultimate Tournament, el torneo de
    cometas más grande de todo el país."

    kaito "¡NO LO VENDAS!"

    nagare "..."

    nagare "Está bien..."

    kaito "Vuelvo en la tarde para comprarlo. ¡PERO NO LO VENDAS!"

    nagare "De acuerdo, no lo venderé."

    "*Ding Dong*"

    "Suena la campana de la escuela, y estoy lejos de ella por haber tomado este
    \"atajo\"."

    kaito "Rayos, me tengo que ir. ¡Y no vendas ese cometa!"

    nagare "De acuerdo, no lo venderé."

    scene bg elementary front

    ai "Por fin llegas,  [playername]. ¿Ya viste la hora que es?"

    "*Slap*"

    "Ella es Ai Ikeda, tiene la misma edad que yo y es la jefa de la clase 5-2.
    La conozco desde que iniciamos la primaria."
    
    "Siempre lleva ese abanico a todos lados y, aunque no duele,
    es un tanto humillante."

    ai "Estoy segura de que no hiciste los deberes, ¿verdad?"

menu:

    "¿Deberes?":
        jump chapter01_terrible

    "Claro que los hice, ¿qué te crees que soy?":
        jump chapter01_milagro

label chapter01_terrible:

        kaito "¿Deberes?"

        ai "Lo sabía, nunca cambiarás."

        jump continuacap1

label chapter01_milagro:

        kaito "Claro que los hice, ¿qué te crees que soy?"

        ai "¿E-Estás enfermo, [playername]?"

        kaito "¿Por qué lo dices?"

        ai "Es que..."

        "Ai sonaba muy desconcertada."

        ai "Es que nunca haces tus deberes, es como si los planetas se hubieran
        alineado para provocar este milagro."

        jump continuacap1

label continuacap1:

    kaito "Eso no importa. Lo importante es que por fin hoy tendré mi cometa."

    "En eso, todo el salón volteó."

    "\"[playername] por fin tendrá un cometa...\", mencionaban casi al mismo
    tiempo."

    "Creo que no está de más mencionar que todos los chicos de la clase tienen un
    cometa a excepción mía."

    ai "¿Para qué quieres un cometa?"

    kaito "Quiero entrar al Ultimate Tournament, el torneo de cometas más grande
    del país."

    ai "Deberías estar más preocupado en hacer tus deberes que en otra cosa."
    
    ai "El año pasado estuviste todas las vacaciones haciendo deberes justo por
    ese asunto de los cometas."

    ai "No querrás repetir eso, ¿o sí?"

    kaito "No lo entenderías, el ver y pilotear un cometa en el aire es la
    mejor sensación que hay."

    kaito "Piensa que es estar en libertad cuando en tierra estás encadenado.
    Es revivir después de un día ajetreado."

    ai "Sigo sin entender, pero bueno. Mejor terminemos de limpiar el salón
    antes de que el prefecto vuelva a regañarnos."

    scene bg kite shop

    "Entré corriendo y deprisa a la Kite Shop, esperando que el señor Nagare
    no hubiera devuelto el cometa defectuoso al fabricante."

    kaito "NO LO DEVOLVISTE, ¿VERDAD?"

    nagare "Te dije que no lo iba a devolver, [playername]. Sabes bien que
    nunca rompo una promesa."

    nagare "...Nunca lo he hecho..."

    kaito "¿Dijiste algo?"

    nagare "Ven al taller para que armes tu cometa."

    kaito "¿Las Kite Shops tienen talleres?"

    nagare "¡Claro que sí! Siempre están abiertos a los clientes, solo pagas
    los aditamentos necesarios y listo."

    "Nagare me acompañó a la trastienda, que es donde se encontraba el taller."

    scene bg workshop

    "Todo estaba impecablemente en su lugar, y Nagare me enseñaba las herramientas
    que utilizaría para armar el cometa."

    "Mientras Nagare traía los desarmadores y las pinzas, no pude evitar notar
    una fotografía colgada en la pared. Parecía estar algo vieja."

    $ renpy.pause(3.0)

    "Me acerqué a ella sin siquiera darme cuenta, y la miré detenidamente. Era
    un chico sosteniendo un enorme trofeo, y un cometa muy peculiar."

    "Parecía tener una edad mayor a la mía, pero se le veía contento recibiendo
    ese enorme trofeo entre sus manos."

    kaito "Este es..."

    nagare "Ryuusei Ichinose. Fue el campeón del primer Ultimate Tournament
    realizado hace 15 años."

    kaito "He escuchado de él, dicen que tiene el récord con 10 segundos del
    duelo de cometas más corto. ¿Qué pasó con él?"

    nagare "Lamentablemente se esfumó, como dice su nombre."
    
    nagare "Al poco tiempo de ganar el Ultimate Tournament, sus padres
    murieron en un accidente automovilístico, siendo él el único sobreviviente."

    nagare "Después del funeral, desapareció sin dejar rastro. Lo que es una
    lástima ya que era una promesa de las Kite Wars."

    kaito "Me gustaría conocerlo algún día, estoy seguro de que está en algún
    lugar, esperando surgir de nuevo."

    nagare "Tal vez, pero mejor deberías apurarte en armar tu cometa. Cierro en
    dos horas y el armado lleva tiempo."

    $ renpy.pause(3.0)

    "El trabajo de armado de cometa fue tan hermoso, que ni siquiera noté el paso
    del tiempo."

    nagare "¡[playername], es hora de cerrar!"

    "Nagare gritaba desde la caja de la Kite Shop."
    
    kaito "¡Ya voy!"

    "El modelo de hace 3 años, el Gear 3000 finalmente era mío, pero..."

    "Había un pequeño inconveniente."

    kaito "¿Cuánto cuestan los Kite Cores?"

    nagare "Son alrededor de 700 Py."

    kaito "¡¿700?!"

    nagare "Es un componente muy importante y que no suele venderse por separado."

    kaito "Pero... Está bien. Será para la próxima."

    scene bg street night

    "Salí de la tienda algo decepcionado. Intenté tomar mi celular tratando de
    emparejarlo con mi cometa. Era inútil."

    "Sabía que nada iba a suceder sin un Kite Core, pero quería hacer el intento."

    vag "Eso no funciona así, ¿sabes?"

    "Una voz cerca de mí habló en ese instante."

    "Volteé a mi alrededor y lo vi a él, un señor con ropas andrajosas."
    
    "Tenía una pinta de no haberse bañado en varios días, y frente a él una
    pequeña mesita con tres cartas puestas boca abajo."

    vag "Puedo leerte el futuro si así lo deseas."

    "Por alguna razón sentía que conocía a aquel señor. A pesar de su apariencia,
    su figura no me daba miedo o repulsión."

menu chapter01_leercartas:

        "Está bien, pero no se tarde.":
            
            jump chapter01_continua2

        "No, debo irme a casa ya.":

            vag "¿Seguro? Dicen que soy muy bueno leyendo las cartas. No te cobraré."

            jump chapter01_leercartas

label chapter01_continua2:

    kaito "De acuerdo... Pero por favor, no tarde mucho, debo irme a casa."

    "Aquel señor le dio la vuelta a las tres cartas y las examinó una a una."

    vag "La primera carta revela tu pasado. Dice que has perdido a alguien
    importante en tu vida, y que esa herida todavía no ha sanado."

    "¿Cómo supo eso? No pude mencionar ni una sola palabra."

    vag "La segunda carta revela tu presente. Dice que un evento importante
    sucederá pronto que cambiará tu vida y la de tus amigos."

    "¿Un evento importante? ¿Qué clase de evento importante además de ir a casa
    y dormir?"

    vag "Y la tercera carta es la de tu futuro. Habrá muchos obstáculos para
    llegar, pero tu meta de ser el mejor se cumplirá."

    vag "Pero debes saber que el futuro no está escrito por completo, depende
    de ti llegar a tus metas y permitirte esos cambios."

    kaito "Señor... ¿Usted cree que algún día pueda volver a ver a mi padre?"

    "Aquel señor no dijo nada. Hizo una pausa muy larga hasta que finalmente
    logró pronunciar algo."

    vag "No conozco a tu padre, pero te puedo decir que está vivo."

    "No dije nada, no quería hacerme ilusiones. Tal vez era uno de esos estafadores
    de los que siempre habla mamá, que solo le sacan dinero a la gente."

    vag "Kenta Ichihara, así se llama. Él no está muerto, logró escaparse de
    sus captores y ahora está escondido."

    kaito "¿Cómo dijo? ¿Mi padre está vivo?"

    vag "No puedo mencionar más al respecto."

    kaito "Ya veo..."

    "Lo que había dicho el adivino había sido muy revelador. Era como si me conociera
    desde hacía mucho. Por alguna razón sentía que quería abrazarlo, pero..."

    "¿Abrazar a un desconocido? ¿Por qué? ¿Qué tenía ese señor que me incitaba
    a abrazarlo, como si se tratara de una figura conocida?"

    mt1 "Aquí estás, maldito."

    "Una voz de mujer gritó justo frente a nosotros. Eran tres sujetos vestidos
    en trajes negros, cuyos rostros en la oscuridad estaban ocultos."

    kaito "¿Quiénes son ustedes?"

    mt2 "Eso no te incumbe."

    mt3 "..."

    mt1 "Mira niño, lo mejor es que te vayas de aquí de inmediato, sin hacer
    ruido y sin decirle nada a tus padres."

    "Quería irme, por alguna razón esos sujetos estaban dándome la oportunidad
    de correr y escapar. Pero algo en mi interior me decía que debía quedarme
    ahí."

    "Los otros dos sujetos eran hombres, uno de ellos no hablaba para nada."

    kaito "¡No! ¡No dejaré que le hagan nada a este vagabundo!"

    mt2 "Así que quieres hacerte el héroe. Eso te va a costar muy caro, mocoso."

    jk "¡No se atrevan a tocar a ese niño!"

    "Los cuatro (¿o cinco?) volteamos hacia donde provenía esa voz. Venía de encima
    de uno de los postes de concreto."

    "Allí se encontraba una figura, como los ninjas de esos videojuegos, con un
    cometa en la espalda."

    "Su atuendo, totalmente negro, cubría casi totalmente su cuerpo, a excepción de
    sus ojos y sus brazos."
    
    "Dejaba ver en el hombro izquierdo una especie de tatuaje que parecía tener forma
    de Kite Core con huesos entrecruzados."

    "¿Será acaso uno de esos raros de esas convenciones?"

    mt2 "El \"Justice Kiter\"... Sabía que vendrías aquí."

    mt3 "..."

    jk "Niño, voy a necesitar tu ayuda."

    kaito "¿Eh?"

    "Ese tal \"Justice Kiter\" se estaba dirigiendo a mí, como si necesitara de
    mi ayuda."

    jk "Esos sujetos de traje negro son sujetos malos que causan problemas allá
    a donde van."
    
    jk "Puedo pelear contra dos de ellos, pero necesitaré de tu ayuda para acabar
    con el tercero."

    jk "Usa ese cometa que tienes en tus manos y pelea contra uno de ellos."

    kaito "Pero... Mi cometa no tiene Kite Cores."

    jk "Entonces usa estos, te los regalo."

    "El \"Justice Kiter\" me lanzó un par de Kite Cores, los cuales tomé con rapidez
    y sin dejar que se cayeran."

    mt1 "¡Así que tú tenías esos Kite Cores!"

    "¿Cómo fue que terminé en esto?"

    "Siempre quise tener un cometa totalmente mío, pero esta no era la
    forma en la que lo esperaba"

    jk "¡¿Qué esperas?! ¡Usa esos Kite Cores y pilotea ese cometa ya!"

    mt1 "Si te atreves a usar esos Kite Cores, no nos haremos responsables de lo que le pase a ese sujeto."

    jk "¡No les hagas caso, ellos necesitan a esa persona para sus planes malignos!"

    mt3 "..."

    "Coloqué un Kite Core en mi celular, otro en el cometa, y de inmediato el cometa que estaba inerte,
    comenzó a elevarse en el cielo."

label narrador1:

    scene bg special battle

    narr "Es hora de tu primer pelea. Y yo seré quien te guíe en este duelo."

    kaito "¿Eh? ¿Quién eres tú?"

    narr "No me preguntes, solo soy el réferi oficial de las Kite Wars. ¿Hay algún
    problema con eso?"

    kaito "Pero es que..."

    narr "Mira niño, a mí solo me contrataron para esto, así que déjame hacer
    mi trabajo."

    narr "¿Quieres leer el tutorial de peleas?"

menu:

    "¡Gúiame en el camino a las Kite Wars!":
        jump situtorial

    "Los jugadores de verdad no necesitamos instrucciones":
        jump notutorial

label situtorial:

    narr "¡Entonces comencemos!"

    narr "Los duelos de cometas comienzan con 5000 puntos para cada jugador.
    Cada golpe certero puede provocar un daño de 500 a 1000 puntos."

    narr "Si tu golpe falla, son 300 puntos menos para ti."

    narr "Se te mostrarán cuatro opciones en cada turno, dos de ellas son golpes
    y las otras son para esquivar."

    narr "Si tu oponente llega primero a los 0 puntos, eres el ganador."

    narr "Con eso debe ser suficiente, si quieres de todos modos leer las
    instrucciones en un futuro, estarán disponibles en la página oficial del
    juego."

    jump continuacap1otravez

label notutorial:

    narr "Bien, respeto tu decisión.

    Si quieres de todos modos leer las instrucciones en un futuro, estarán
    disponibles en la página oficial del juego."

    jump continuacap1otravez

label continuacap1otravez:

    mt1 "¡Yo seré tu oponente! Y no creas que por ser mujer, no puedo ser una
    estupenda Kiter."

    $ oponente = 5000
    $ tu = 5000
    $ penalizacion = 300

    while tu > 0 or oponente > 0:

        menu:

            "Esquivar a la izquierda/derecha":
                jump pelea1_1

            "Esquivar arriba/abajo":
                jump pelea1_2

            "Atacar de frente":
                jump pelea1_3

            "Ataque lateral":
                jump pelea1_4

        label pelea1_1:

            "[playername] decidió moverse a un lado."

            $ esquiva = bool(renpy.random.getrandbits(1))

            if esquiva is True:
                $ oponente = oponente - penalizacion
                "Tu oponente no pudo seguirte el paso."

            else:
                "Tu oponente ha atacado con un golpe directo."
                $ danotuyo = renpy.random.randint(500,1000)
                $ tu = tu - danotuyo

            jump fin1

        label pelea1_2:

            "[playername] decidió moverse a un lado."
            $ esquiva = bool(renpy.random.getrandbits(1))

            if esquiva is True:
                $ oponente = oponente - penalizacion
                "Tu oponente no pudo seguirte el paso."

            else:
                "Tu oponente ha atacado con un golpe directo."
                $ danotuyo = renpy.random.randint(500,2000)
                $ tu = tu - danotuyo

            jump fin1

        label pelea1_3:

            "[playername] decidió atacar certeramente."
            $ esquiva = bool(renpy.random.getrandbits(1))

            if esquiva is True:
                $ tu = tu - penalizacion
                "Tu oponente esquivó tu ataque."

            else:
                "Tu oponente trató de esquivar, pero tú fuiste más rápido."
                $ danoop = renpy.random.randint(500,2000)
                $ oponente = oponente - danoop

            jump fin1

        label pelea1_4:

            "[playername] decidió atacar certeramente."
            $ esquiva = bool(renpy.random.getrandbits(1))

            if esquiva is True:
                $ tu = tu - penalizacion
                "Tu oponente esquivó tu ataque."

            else:
                "Tu oponente trató de esquivar, pero tú fuiste más rápido."
                $ danoop = renpy.random.randint(500,2000)
                $ oponente = oponente - danoop

            jump fin1

        label fin1:

            "Ahora tienes %(tu)s puntos.\nTu oponente ahora tiene %(oponente)s puntos."

            if tu <= 0:
                jump bad_end_1

            elif oponente <= 0:
                jump good_end_1

label bad_end_1:

    narr "Oh, perdiste..."

    narr "No importa, puedes intentarlo de nuevo a partir de ahora."

    jump narrador1

label good_end_1:

    narr "Felicidades, es tu primer duelo ganado con éxito."

    jump continuacap1_3
    $ puntajefinal = puntajefinal + tu

label continuacap1_3:

    scene bg street night

    mt1 "Maldita sea, ese mocoso nos ganó."

    "Aquella chica estaba sumamente molesta por mi victoria."

    mt2 "¡Rayos!"

    mt1 "¿Te ganó nuevamente el Justice Kiter? ¡Vámonos de aquí!"

    mt3 "¡...!"

    kaito "¡Ganamos! ¡Les ganamos a esos sujetos! ¡Justice Kiter, gracias por...!"

    "Pero miré a mi alrededor, y tanto el vagabundo, como el que se hacía
    llamar \"Justice Kiter\", desaparecieron tan pronto como habían aparecido."

    "Estaba pensando que todo era un sueño, pero no..."

    "La aplicación de Kite Wars en mi celular me estaba pidiendo registro de mis
    datos y los de mi cometa. Los Kite Cores funcionaban sin problemas."

    "Recibo una llamada en mi celular."

    mama "[playername], ¿dónde estás? ¡Ya pasó la hora de cenar!"

    kaito "Ya voy, estoy a dos cuadras."

    scene bg house night

    "Llego a mi casa y veo a mi mamá en la entrada con un cucharón en sus manos."

    mama "[playername], ¿dónde te habías metido? ¿No ves la hora que...?"

    "Mi mamá hizo un gesto de descontento al instante, estoy seguro de que vio
    mi cometa. Después de eso, lo único que hizo fue suspirar."

    mama "Supongo que no puedo quitarte esa afición de la cabeza. Solo te pido que
    no te metas en problemas."

    "Fin del capítulo 1."

    jump Chapter02

