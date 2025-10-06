# Piedra_Papel_o_Tijeras
Trabajo correspondiente a Logica de Programación, en este caso he escogido la aplicación de Piedra, Papel o Tijera.

BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA

─────INSTRUCCIONES DEL JUEGO─────

1. Piedra vence a Tijera (la rompe)                

2. Papel vence a Piedra (la envuelve)              

3. Tijera vence a Papel (lo corta)                 

4. Si ambos eligen lo mismo, es EMPATE             


Opciones:

  [1] - Piedra 🔴
  
  [2] - Papel 🟥
  
  [3] - Tijera ❌

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
- Chi-cuadrado test confirma uniformidad (p-value > 0.05)

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

   - Funciona perfectamente como ejecutable como en un IDE (Visual Studio Code)
──────────────────────────────────────────────────────
