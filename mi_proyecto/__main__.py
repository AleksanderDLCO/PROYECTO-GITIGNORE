from mi_proyecto.config import load_python_vscode_gitignore
from mi_proyecto.file_analyzer import analyze_project_files
from mi_proyecto.gpt_classifier import classify_files_to_ignore
from mi_proyecto.gitignore_generator import generate_gitignore_file

def main():
    # Cargar patrones de .gitignore específicos para Python y VSCode
    generic_patterns = load_python_vscode_gitignore()

    # Analizar archivos del proyecto
    project_files = analyze_project_files(generic_patterns)

    # Identificar archivos específicos para ignorar usando GPT-4
    specific_patterns = classify_files_to_ignore(project_files)

    # Generar el archivo .gitignore
    generate_gitignore_file(generic_patterns, specific_patterns)
    print(".gitignore generado automáticamente.")

if __name__ == "__main__":
    main()