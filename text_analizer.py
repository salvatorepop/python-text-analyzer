import re

def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"[^\w\s]","",texto)
    return  texto.strip()

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo,"r",encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print('Archivo no encontrado')
        return ""

def main():
    nombre_texto = input('Introduce el nombre del archivo: ')
    contenido = leer_archivo(nombre_texto)

    if not contenido:
        return

    texto_limpio = limpiar_texto(contenido)
    palabras = texto_limpio.split()
    lineas = texto_limpio.split('\n')


    print(f"El texto tiene {len(palabras)} palabras")
    print(f'El texto tiene {len(texto_limpio)} caracteres')
    print(f'Contiene {len(lineas)} lineas')

if __name__ == "__main__":
    main()