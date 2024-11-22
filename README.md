# Pokedex
Pokédex en Python

Este proyecto consiste en una Pokédex interactiva creada con Python, que utiliza la API pública PokeAPI para buscar información de cualquier Pokémon. Al introducir el nombre de un Pokémon, el programa muestra su información básica, como peso, altura, tipos, habilidades y una imagen. Además, guarda los datos en un archivo JSON para que puedan reutilizarse sin necesidad de consultar la API nuevamente.

 Explicación del código

El programa está dividido en varias partes clave para hacerlo más organizado y fácil de entender:

1. *Consulta a la API*: 
   Se utiliza la biblioteca `requests` para enviar solicitudes a PokeAPI. Si el Pokémon existe, la API devuelve su información; si no, el programa muestra un mensaje de error.

2. *Procesamiento de datos*:
   Los datos obtenidos de la API se filtran para mostrar solo la información relevante, como el peso, la altura, los tipos y las habilidades.

3. *Guardado en archivos JSON*:
   Los datos de cada Pokémon se guardan en la carpeta `pokedex/` en un archivo JSON individual. Si se vuelve a buscar el mismo Pokémon, el programa utiliza este archivo en lugar de consultar la API nuevamente.

4. *Interfaz en la terminal*:
   Se mejoró la experiencia visual en la terminal usando `colorama`, con colores para destacar mensajes importantes (errores, información encontrada, etc.).

5. *Estructura modular*:
   El programa está dividido en funciones que se encargan de tareas específicas:
   - `buscar_pokemon(nombre)`: Consulta la API o el archivo local.
   - `guardar_pokemon(datos)`: Guarda los datos en un archivo JSON.
   - `mostrar_datos(datos)`: Presenta la información del Pokémon en la terminal.

    Lo que aprendí

Durante este proyecto aprendí a trabajar con APIs usando la biblioteca `requests`, a manejar errores relacionados con respuestas HTTP, y a guardar información en formato JSON. También mejoré mi capacidad para estructurar código de forma modular y aprendí a implementar características como el manejo de datos en modo offline.

  Mejoras futuras

- Agregar soporte para buscar Pokémon por su número o ID.
- Crear una interfaz gráfica para mejorar la experiencia del usuario.
- Implementar una opción para comparar estadísticas entre dos Pokémon.
