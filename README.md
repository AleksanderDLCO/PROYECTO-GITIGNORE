# Auto-Generación de gitignore

## Contenido
- Introducción
- Prerrequisitos
- Uso

## Introducción
Los archivos .gitignore se actualizan de manera manual y, en caso de que el desarrollador use una extensión, en base a reglas duras. 

Cuando un desarrollador genera un archivo de tipo texto o pdf que utiliza para tomar notas o como un apoyo, tiene que agregarlo al .gitignore o excluirlo explícitamente de los commits.

Es por esta razón que se desarrolla la PoC, para integrarse en el flujo de git antes de ```git add```.

![WhatsApp Image 2024-11-09 at 5 12 28 PM](https://github.com/user-attachments/assets/8d8e231d-f358-445c-a6b7-bbc28bb42963)

## Prerrequisitos

- Debes tener una ```api key``` de la plataforma de OpenAI.
- Crea un archivo ```.env``` en la raíz del proyecto con contenido ```OPENAI_API_KEY={YOUR_KEY}```
- Python 3.12 para utilizar el proyecto.

## Uso
En la raíz del proyecto ejecuta el comando ```python -m my_module```. Esto ejectua el archivo ```__main__.py``` y genera un archivo en ```./.gitignore```.

