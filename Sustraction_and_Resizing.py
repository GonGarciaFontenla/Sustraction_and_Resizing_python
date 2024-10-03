#https://www.remove.bg/api#sample-code
import requests
import os
import shutil
from PIL import Image

#Explicacion rapida de como usarlo: 
#1. Colocar las imagenes que se quieren procesar en la carpeta "Imagenes/Sin Extraer y Sin procesar"
#2. Colocar la clave de la API en la variable api_key
#3. Correr el programa --> python3 Sustraction_and_Resizing.py
#4. Las imagenes procesadas se guardaran en la carpeta "Imagenes/Procesadas"
#Nota: Si ya esta en png y solo se quiere hacer el resizing, colocar la imagen en la carpeta "Imagenes/Sin procesar"
#Nota 2: Creo que por cuenta creada en la API se pueden hacer 50 peticiones al mes, si se llega al limite, se debe crear otra cuenta de Gmail
#Nota 3: Creo que por razones que solo Microsoft sabe, si estan usando windows en la linea 76 a 78 deben cambiar las '/' por '\'
#Nota 4: Se crea un archivo conteo.txt para saber cuantas veces se utilizo el codigo y poder llevar trakeo de las peticiones restantes

def resizing(f, f_saved, x=70, y=90): # Aca van los valores de x e y para el Resizing
    """
    Realiza el redimensionamiento de las imágenes a XxY pixels.
    """
    for file in os.listdir(f):
        f_img = os.path.join(f, file)
        f_img_save = os.path.join(f_saved, file)
        img = Image.open(f_img)
        img = img.resize((x, y))
        # Cambia la extensión si es .jpg a .png
        f_img_save = f_img_save.replace(".jpg", ".png") if ".jpg" in f_img_save else f_img_save
        img.save(f_img_save)
        shutil.move(os.path.join(f, file), os.path.join('Ya usado y procesado', file))

def extraction(archivo_conteo, api_key):
    """
    Usa la API para remover el fondo de las imágenes y las guarda en otra carpeta.
    """
    # Verificar que las carpetas existan
    if not os.path.exists(f_SE_SP):
        raise FileNotFoundError(f"La carpeta {f_SE_SP} no existe.")
    
    if not os.path.exists('Ya usado y procesado'):
        os.makedirs('Ya usado y procesado')
    
    with open(archivo_conteo, "r") as file0:
        data = int(file0.readline())
        print(f"Usos de la API: {data}")
        
        for file1 in os.listdir(f_SE_SP):
            if data < 50:
                data += 1
                image_path = os.path.join(f_SE_SP, file1)
                
                response = requests.post(
                    'https://api.remove.bg/v1.0/removebg',
                    files={'image_file': open(image_path, 'rb')},
                    data={'size': 'auto'},
                    headers={'X-Api-Key': api_key},
                )
                
                if response.status_code == requests.codes.ok:
                    output_path = os.path.join(f_SP, file1)
                    with open(output_path, 'wb') as out:
                        out.write(response.content)
                else:
                    print(f"Error: {response.status_code}, {response.text}")
                
                with open(archivo_conteo, 'w') as file2:
                    file2.write(str(data))

                shutil.move(image_path, os.path.join('Ya usado y procesado', file1))
            else:
                raise Exception("Se alcanzó el límite de 50 imágenes por mes de la API, usa otra cuenta de Gmail.")

if __name__ == "__main__":
    try:
        api_key = ""  # Coloca aquí tu clave de API

        # Definir rutas
        f_SE_SP = 'Imagenes/Sin Extraer y Sin procesar'
        f_SP = 'Imagenes/Sin procesar'
        f_saved = 'Imagenes/Procesadas'

        # Asegurarse de que las carpetas existen
        if not os.path.exists(f_SE_SP):
            raise FileNotFoundError(f"La carpeta {f_SE_SP} no existe.")
        
        if not os.path.exists(f_SP):
            os.makedirs(f_SP)
        
        if not os.path.exists(f_saved):
            os.makedirs(f_saved)
        
        # Llamar a las funciones
        extraction("conteo.txt", api_key)
        resizing(f_SP, f_saved)

    except Exception as e:
        print(f"Se ha producido un error: {e}")

