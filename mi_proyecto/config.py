import openai
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_python_vscode_gitignore():
    # Plantilla de .gitignore para proyectos de Python y VSCode
    return [
        "# Byte-compiled / optimized / DLL files",
        "__pycache__/",
        "*.py[cod]",
        "*$py.class",

        "# C extensions",
        "*.so",

        "# Distribution / packaging",
        ".Python",
        "build/",
        "develop-eggs/",
        "dist/",
        "downloads/",
        "eggs/",
        ".eggs/",
        "lib/",
        "lib64/",
        "parts/",
        "sdist/",
        "var/",
        "wheels/",
        "share/python-wheels/",
        "*.egg-info/",
        ".installed.cfg",
        "*.egg",
        "MANIFEST",

        "# PyInstaller",
        "*.manifest",
        "*.spec",

        "# Installer logs",
        "pip-log.txt",
        "pip-delete-this-directory.txt",

        "# Unit test / coverage reports",
        "htmlcov/",
        ".tox/",
        ".nox/",
        ".coverage",
        ".coverage.*",
        ".cache",
        "nosetests.xml",
        "coverage.xml",
        "*.cover",
        "*.py,cover",
        ".hypothesis/",

        "# Jupyter Notebook",
        ".ipynb_checkpoints",

        "# VSCode",
        ".vscode/",
        "*.code-workspace",

        "# Environments",
        ".env",
        ".venv",
        "env/",
        "venv/",
        "ENV/",
        "env.bak/",
        "venv.bak/",

        "# Spyder project settings",
        ".spyderproject",
        ".spyproject",

        "# Rope project settings",
        ".ropeproject",

        "# mkdocs documentation",
        "/site",

        "# mypy",
        ".mypy_cache/",
        ".dmypy.json",
        "dmypy.json",

        "# Pyre type checker",
        ".pyre/",

        "# pytype static type analyzer",
        ".pytype/",

        "# Celery stuff",
        "celerybeat-schedule",
        "celerybeat.pid",

        "# SageMath parsed files",
        "*.sage.py",

        "# Encrypted keys",
        "*.pem",
        "*.key",

        "# dotenv environment variables file",
        ".env",

        "# IDE-specific",
        ".idea/"
    ]