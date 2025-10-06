# Universidad Internacional del Ecuador (UIDE)
# Trabajo Autónomo 2
# Lógica de Programación 2-ECC-1B
# Nombre del Estudiante: Wilmer Joao Correa Guevara
# Nombre del Docente: Lilian Marlene Aman Ramos

import random

# Función principal del juego, la base de todo
def jugar_piedra_papel_tijera():
    # Encabezado del juego, aqui se encuentra el titulo del juego (RNF2: Interfaz clara)
    print("=" * 50)
    print("BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA")
    print("=" * 50)
    
    # (RF1: Ingreso de nombre) Solicitamos el nombre del jugador
    nombre_jugador = input("\nIngresa tu nombre: ")
    
    # (RF7: Instrucciones) Aqui mostramos las instrucciones si el jugador lo desea
    # Nota: Añadimos f antes de las comillas en el print para poder insertar variables o expresiones directamente dentro de la cadena (que en este caso es el nombre_jugador)
    print(f"\n¡Hola {nombre_jugador}!")
    print("\n¿Sabes cómo jugar este juego?")
    # .lower lo usamos para convertir todas las letras mayusculas en minusculas
    sabe_jugar = input("Responde 'si' o 'no': ").lower()
    
    # Debido a que el emoji de piedra no funciona, he escogido figuras (cuadrado, equis y circulo) para representar el papel, la tijera y la piedra
    if sabe_jugar != 'si':
        print("\n--- INSTRUCCIONES DEL JUEGO ---")
        print("1. Piedra vence a Tijera (la rompe) 🔴 > ❌")
        print("2. Papel vence a Piedra (la envuelve) 🟥 > 🔴")
        print("3. Tijera vence a Papel (lo corta) ❌ > 🟥")
        print("4. Si ambos (jugador y computadora) eligen lo mismo, es EMPATE")
        print("-" * 40)
    
    # (RF8: Confirmaciones) Confirmación antes de iniciar el juego
    print("\n¿Quieres iniciar el juego?")
    iniciar = input("Responde 'si' o 'no': ").lower()
    
    if iniciar != 'si':
        print("\n¡Hasta pronto! Vuelve cuando quieras jugar.")
        return
    
    # (RF5: Estadisticas) Inicializamos las estadísticas del jugador
    partidas_ganadas = 0
    partidas_perdidas = 0
    partidas_empatadas = 0
    
    # Diccionario para convertir números en nombres (RNF6: Mantenibilidad)
    opciones = {1: "Piedra 🔴", 2: "Papel 🟥", 3: "Tijera ❌"}
    
    # (RF6: Múltiples partidas) Bucle principal, esto nos permite múltiples partidas si vamos a seguir jugando
    while True:
        print("\n" + "=" * 50)
        print("NUEVA RONDA")
        print("=" * 50)
        
        # (RF2: Generación aleatoria) La computadora elige al azar (distribución uniforme)
        # (RNF5: Uniformidad aleatoria) random.randint garantiza uniformidad estadística
        computadora_eleccion = random.randint(1, 3)
        
        # Aqui mostramos las opciones al jugador (RNF2: Interfaz clara)
        print("\nOpciones:")
        print("1 - Piedra 🔴")
        print("2 - Papel 🟥")
        print("3 - Tijera ❌")
        
        # (RF3: Validación de entradas) Validar la entrada del jugador
        # (RNF3: Mensajes de error) Mensajes de error claros y descriptivos
        while True:
            try:
                jugador_eleccion = int(input(f"\n{nombre_jugador}, elige tu opción (1, 2 o 3): "))
                if jugador_eleccion in [1, 2, 3]:
                    break
                else:
                    # RNF3: Mensaje de error específico
                    print("🚫 ¡Tu opción es inválida! Por favor elige 1, 2 o 3.")
            except ValueError:
                # RNF3: Mensaje de error para tipo incorrecto
                print("🚫 ¡Tu entrada es inválida! Debes ingresar un número (1, 2 o 3).")
        
        # Mostrar las elecciones (RNF4: Retroalimentación inmediata)
        print(f"\n{nombre_jugador} eligió: {opciones[jugador_eleccion]}")
        print(f"Computadora eligió: {opciones[computadora_eleccion]}")
        
        # RF4: Determinar el ganador (100% cobertura de reglas)
        # Implementación de determinar_ganador inline
        if jugador_eleccion == computadora_eleccion:
            # EMPATE - ambos eligieron lo mismo
            print("\n🤝 ¡Empate!")
            partidas_empatadas += 1
            
        elif (jugador_eleccion == 1 and computadora_eleccion == 3) or \
             (jugador_eleccion == 2 and computadora_eleccion == 1) or \
             (jugador_eleccion == 3 and computadora_eleccion == 2):
            # JUGADOR GANA - combinaciones ganadoras
            # Piedra > Tijera, Papel > Piedra, Tijera > Papel
            print("\n🎉 ¡Has ganado!")
            partidas_ganadas += 1
            
        else:
            # COMPUTADORA GANA - resto de combinaciones
            print("\n😞 ¡Has perdido!")
            partidas_perdidas += 1
        
        # RF5: Mostrar estadísticas actualizadas (RNF4: Retroalimentación en tiempo real)
        print("\n------------- ESTADÍSTICAS -------------")
        print(f"Partidas ganadas:    {partidas_ganadas}")
        print(f"Partidas perdidas:   {partidas_perdidas}")
        print(f"Partidas empatadas:  {partidas_empatadas}")
        print(f"Total de partidas:   {partidas_ganadas + partidas_perdidas + partidas_empatadas}")
        print("-" * 40)
        
        # RF8: Confirmación antes de continuar o terminar
        volver_jugar = input("\n¿Quieres volver a jugar? (si/no): ").lower()
        
        if volver_jugar != 'si':
            # Mostrar pantalla final
            print("\n" + "=" * 50)
            print("FIN DEL JUEGO")
            print("=" * 50)
            print(f"\n¡Gracias por jugar, {nombre_jugador}!")
            print("\n--- ESTADÍSTICAS FINALES ---")
            print(f"Partidas ganadas:    {partidas_ganadas}")
            print(f"Partidas perdidas:   {partidas_perdidas}")
            print(f"Partidas empatadas:  {partidas_empatadas}")
            print(f"Total de partidas:   {partidas_ganadas + partidas_perdidas + partidas_empatadas}")
            
            # Cálculo de porcentaje de victorias (estadística adicional)
            total = partidas_ganadas + partidas_perdidas + partidas_empatadas
            if total > 0:
                porcentaje_victorias = (partidas_ganadas / total) * 100
                # .1f nos sirve para aproximar decimales 
                print(f"Porcentaje de victorias: {porcentaje_victorias:.1f}%")
            
            print("\n¡Hasta pronto!")
            break

# Punto de entrada del programa en caso de que se ejecute directamente del archivo.py y no desde un IDE
if __name__ == "__main__":
    jugar_piedra_papel_tijera()