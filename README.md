# Piedra Papel o Tijera
Proyecto final de Lógica de Programación 2 - UIDE

──────────────────────────────────────────────────────

INFORMACIÓN DEL PROYECTO

Estudiante: Wilmer Joao Correa Guevara

Docente: Lilian Marlene Aman Ramos

Materia: Lógica de Programación 2-ECC-1B

Universidad Internacional del Ecuador (UIDE)

Repositorio: [Piedra, Papel o Tijera](https://github.com/ArteJo/Piedra_Papel_o_Tijeras)

──────────────────────────────────────────────────────

REGLAS DEL JUEGO

1. Piedra vence a Tijera (la rompe)                

2. Papel vence a Piedra (la envuelve)              

3. Tijera vence a Papel (lo corta)                 

4. Si ambos eligen lo mismo, es EMPATE             

Opciones:

  [1] - Piedra 🔴
  
  [2] - Papel 🟥
  
  [3] - Tijera ❌
  
──────────────────────────────────────────────────────

INSTALACIÓN

Requisitos Previos:
[Python 3.13](https://www.python.org/downloads/) o superior

Sistema operativo: Windows, macOS, o Linux

──────────────────────────────────────────────────────

Pasos de Instalación:

Clonar el repositorio: 

git clone https://github.com/ArteJo/Piedra_Papel_o_Tijeras.git

Verificar instalación de Python: 

python --version

Ejecutar el programa: Autonomo2.1.py

Nota: No se requieren dependencias externas. Solo usa la biblioteca estándar de Python.

──────────────────────────────────────────────────────

USO

Bienvenida: El juego muestra un mensaje de bienvenida

Ingreso de Nombre: Solicita el nombre del jugador

Instrucciones: Pregunta si conoce las reglas (opcional)

Confirmación: Pregunta si desea iniciar el juego

Juego: Bucle de partidas:

- Computadora genera su elección aleatoriamente
  
- Jugador elige su opción (1, 2 o 3)
  
- El sistema determina el ganador
  
- Muestra estadísticas actualizadas
  
- Pregunta si desea volver a jugar

Despedida: Muestra estadísticas finales y se despide

──────────────────────────────────────────────────────

**REQUISITOS FUNCIONALES (RF):**

RF1: El sistema debe permitir al jugador ingresar su nombre

RF2: El sistema debe generar elecciones aleatorias para la computadora (1-3)

RF3: El sistema debe validar las entradas del jugador (solo 1, 2 o 3)

RF4: El sistema debe determinar el ganador según las reglas del juego

RF5: El sistema debe mantener estadísticas (ganadas, perdidas, empatadas)

RF6: El sistema debe permitir partidas múltiples en una sesión

RF7: El sistema debe mostrar instrucciones si el jugador no sabe jugar

RF8: El sistema debe confirmar antes de iniciar y terminar el juego

**REQUISITOS NO FUNCIONALES (RNF):**

RNF1: Tiempo de respuesta < 1 segundo por jugada

RNF2: Interfaz de texto clara con separadores visuales

RNF3: Mensajes de error descriptivos para entradas inválidas

RNF4: Uso de emojis para mejorar la experiencia visual

RNF5: Distribución uniforme en la generación aleatoria (33.33% cada opción)

RNF6: Código mantenible con comentarios y estructura clara

**JUSTIFICACIÓN ESTADÍSTICA - ALEATORIEDAD:**
- Se utiliza random.randint(1,3) del módulo random de Python
- Genera números pseudoaleatorios con distribución uniforme
- Probabilidad teórica: P(Piedra) = P(Papel) = P(Tijera) = 1/3 ≈ 33.33%
- En 10,000 simulaciones esperamos: ~3,333 de cada opción (±2% variación)

CRITERIOS DE USABILIDAD:

  **MENSAJES DE ERROR CLAROS:**
   - "¡Opción inválida!" para números fuera de rango
   - "¡Entrada inválida!" para caracteres no numéricos
   - Repetición del prompt hasta entrada correcta
     
  **CONTRASTE VISUAL:**
   - Separadores con "=" para secciones principales
   - Separadores con "-" para subsecciones
   - Emojis para resultados (🎉 victoria, 😞 derrota)
   - Espaciado adecuado entre secciones
     
  **RETROALIMENTACIÓN INMEDIATA:**
   - Confirmación de cada elección
   - Resultado visible de cada ronda
   - Estadísticas actualizadas en tiempo real

──────────────────────────────────────────────────────

PROGRAMAS UTILIZADOS PARA EL DESAROLLO

Diagrama de Flujo:
[Raptor Avalonia 0.10.0001](https://raptor.martincarlisle.com/)

Lenguaje de Programación:
[Python 3.13](https://www.python.org/downloads/)

Bibliotecas:
random - Generación de números aleatorios (biblioteca estándar)

Herramientas de Desarrollo:

[Visual Studio Code 1.105.0](https://code.visualstudio.com/download)

[Git for Windows 2.51.1](https://git-scm.com/downloads/win) & [GitHub](https://github.com/)

Entornos de Ejecución:

- Terminal/CMD
- IDE (Visual Studio Code, PyCharm)
- Ejecutable compilado (Autonomo2.1.py)

──────────────────────────────────────────────────────

AGRADECIMIENTOS

A la profesora Lilian Marlene Aman Ramos por su guía y enseñanza en las clases impartidas.
A la Universidad Internacional del Ecuador (UIDE) por la formación académica
A la comunidad de Python, YouTube por la documentación y recursos

