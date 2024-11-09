import os
import fnmatch

def read_file(file_path, exclude_patterns):
    # FIX: usar la funcion adecuada para el regex de filepath con pattern
    if any(pattern in file_path for pattern in exclude_patterns):
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(200)  # Leer solo los primeros 200 caracteres
        return content
    except Exception as e:
        print(f"No se pudo leer el archivo {file_path}: {e}")
        return 'Este archivo no se puede leer como texto'
    
def analyze_project_files(generic_patterns):
    # Analizar los archivos del proyecto para obtener sus nombres y contenido
    project_files = {}
    for root, _, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root, file)
            # Leer el archivo usando la función read_file
            content = read_file(file_path, generic_patterns)
            if content is not None:
                project_files[file_path] = content
    print(f"Tamaño de la lista project_files: {len(project_files)}")
    print(project_files.keys())
    return project_files
