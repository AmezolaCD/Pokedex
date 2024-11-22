import requests
import os
import json
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def obtener_datos_pokemon(nombre_pokemon):
    """
    Obtiene los datos de un Pokémon desde la API de PokeAPI o del archivo local si ya existe.
    
    Args:
        nombre_pokemon (str): Nombre del Pokémon a buscar.
    
    Returns:
        dict: Información del Pokémon si existe, de lo contrario None.
    """
    carpeta = "pokedex"
    archivo_local = os.path.join(carpeta, f"{nombre_pokemon.lower()}.json")
    
    # Verificar si ya tenemos el Pokémon guardado localmente
    if os.path.exists(archivo_local):
        print(Fore.YELLOW + f"⚡ Cargando datos de {nombre_pokemon} desde archivo local...")
        with open(archivo_local, "r", encoding="utf-8") as f:
            return json.load(f)
    
    # Si no está guardado, realizar la solicitud a la API
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    try:
        print(Fore.CYAN + f"🔍 Buscando datos de {nombre_pokemon} en la API...")
        respuesta = requests.get(url, timeout=10)  # Tiempo límite de espera
        respuesta.raise_for_status()  # Lanza excepción si la respuesta no es 2xx
        datos_pokemon = respuesta.json()
        guardar_pokemon_en_json(datos_pokemon, carpeta)  # Guardar para uso futuro
        return datos_pokemon
    except requests.exceptions.HTTPError:
        print(Fore.RED + f"❌ El Pokémon '{nombre_pokemon}' no existe en la Pokédex.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"❌ Error al conectarse a la API: {e}")
    return None

def guardar_pokemon_en_json(datos_pokemon, carpeta="pokedex"):
    """
    Guarda los datos esenciales del Pokémon en un archivo JSON.
    
    Args:
        datos_pokemon (dict): Información completa del Pokémon.
        carpeta (str): Nombre de la carpeta donde se guardará el archivo.
    """
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    # Filtrar datos esenciales
    datos_essenciales = {
        "name": datos_pokemon["name"],
        "weight": datos_pokemon["weight"] / 10,  # Convertir a kilogramos
        "height": datos_pokemon["height"] / 10,  # Convertir a metros
        "types": [tipo["type"]["name"] for tipo in datos_pokemon["types"]],
        "abilities": [habilidad["ability"]["name"] for habilidad in datos_pokemon["abilities"]],
        "image": datos_pokemon["sprites"]["front_default"]
    }
    
    nombre_pokemon = datos_pokemon["name"]
    archivo = os.path.join(carpeta, f"{nombre_pokemon.lower()}.json")
    
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos_essenciales, f, indent=4, ensure_ascii=False)
        print(Fore.GREEN + f"✅ Los datos de '{nombre_pokemon}' se guardaron en {archivo}.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar los datos: {e}")

def mostrar_informacion_pokemon(datos_pokemon):
    """
    Muestra la información principal de un Pokémon en un formato visual mejorado.
    
    Args:
        datos_pokemon (dict): Información del Pokémon.
    """
    nombre = datos_pokemon["name"].capitalize()
    peso = datos_pokemon["weight"] / 10  # Convertir de decagramos a kilogramos
    altura = datos_pokemon["height"] / 10  # Convertir de decímetros a metros
    tipos = [tipo["type"]["name"].capitalize() for tipo in datos_pokemon["types"]]
    habilidades = [habilidad["ability"]["name"].capitalize() for habilidad in datos_pokemon["abilities"]]
    imagen = datos_pokemon["sprites"]["front_default"]

    print(Fore.MAGENTA + f"\n--- Información de {nombre} ---")
    print(Fore.YELLOW + f"Nombre: {nombre}")
    print(Fore.YELLOW + f"Peso: {peso} kg")
    print(Fore.YELLOW + f"Altura: {altura} m")
    print(Fore.YELLOW + f"Tipos: {', '.join(tipos)}")
    print(Fore.YELLOW + f"Habilidades: {', '.join(habilidades)}")
    if imagen:
        print(Fore.YELLOW + f"Imagen: {imagen}")
        print(Fore.CYAN + "\nPuedes copiar este enlace para ver la imagen:")
        print(imagen)
    else:
        print(Fore.RED + "❌ Imagen no disponible para este Pokémon.")

def main():
    """
    Función principal para interactuar con el usuario.
    """
    print(Fore.LIGHTBLUE_EX + "🌟 Bienvenido a la Pokédex Avanzada 🌟")
    
    while True:
        nombre_pokemon = input(Fore.LIGHTBLUE_EX + "\n🔍 Introduce el nombre de un Pokémon (o 'salir' para terminar): ").strip()
        if nombre_pokemon.lower() == "salir":
            print(Fore.LIGHTGREEN_EX + "👋 ¡Gracias por usar la Pokédex! ¡Hasta pronto!")
            break
        
        # Validar entrada del usuario
        if not nombre_pokemon.isalpha():
            print(Fore.RED + "❌ El nombre del Pokémon debe contener solo letras. Inténtalo nuevamente.")
            continue
        
        # Obtener datos y manejar si existe o no
        datos_pokemon = obtener_datos_pokemon(nombre_pokemon)
        if datos_pokemon:
            mostrar_informacion_pokemon(datos_pokemon)

if __name__ == "__main__":
    main()

