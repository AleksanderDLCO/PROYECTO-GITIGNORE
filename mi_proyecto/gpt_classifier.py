from openai import OpenAI

client = OpenAI()

def classify_files_to_ignore(files):
    # Utilizar GPT-4 para clasificar los archivos a ignorar
    ignore_patterns = []
    for file_path, content in files.items():
        response = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente que ayuda a clasificar archivos para un .gitignore de un proyecto de Python con VSCode. Usualmente archivos como pdf o txt deberian ir en el gitignore porque son documentación temporal"},
            {"role": "user", "content": f"¿Debería el siguiente archivo ser ignorado en un archivo .gitignore para un proyecto de Python con VSCode? Archivo: {file_path}\nContenido:\n{content}\nResponde con 'Sí' o 'No'."}
        ],
        max_tokens = 5)
        print('-------------------------')
        print(response.choices[0].message.content)
        decision = response.choices[0].message.content.strip()
        if decision.lower() == 'sí':
            print(file_path)
            ignore_patterns.append(file_path)
    return ignore_patterns