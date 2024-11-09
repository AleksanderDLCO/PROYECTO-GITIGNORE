def generate_gitignore_file(generic_patterns, specific_patterns):
    # Combinar patrones genéricos y específicos y escribir en .gitignore
    with open('.gitignore', 'w') as f:
        for pattern in generic_patterns + ['# Archivos auto-generados'] + specific_patterns:
            f.write(pattern + '\n')