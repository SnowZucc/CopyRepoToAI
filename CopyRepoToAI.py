import os
import sys

def clear_terminal():
    """Efface le terminal en fonction du système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Début du script...")

def read_files_from_folder(folder_path, exclude_folders=None, extensions=[]):
    if not os.path.exists(folder_path):
        print(f"Le dossier {folder_path} n'existe pas.")
        return

    files_to_print = []
    exclude_folders = exclude_folders or []

    for root, dirs, files in os.walk(folder_path):
        if any(excluded in root for excluded in exclude_folders):
            continue

        for file in files:
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                files_to_print.append(file_path)
    
    clear_terminal()
    
    for file in files_to_print:
        print(f"\nChemin du fichier: {file}")
        try:
            with open(file, 'r', encoding='utf-8') as f:
                print(f"\nContenu de {file}:")
                print(f.read())
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier {file}: {e}")

    print("\nListe des fichiers à imprimer:")
    for file in files_to_print:
        print(file)

def get_environment_settings(environment):
    settings = {
        "1": {"extensions": [".html", ".css", ".js", ".jsx", ".ts", ".tsx", ".vue", ".php", ".scss", ".sass", "Dockerfile", ".yml", ".yaml", ".toml"], "exclude_folders": ["node_modules"]},
        "2": {"extensions": [".java", ".fxml", ".properties", ".xml", "Dockerfile", ".yml", ".yaml"], "exclude_folders": ["target"]},
        "3": {"extensions": [".py", "Dockerfile", ".yml", ".yaml"], "exclude_folders": ["__pycache__"]},
        "4": {"extensions": [".cs", ".config", ".sln", ".csproj", "Dockerfile", ".yml", ".yaml"], "exclude_folders": ["bin"]},
        "5": {"extensions": [".cpp", ".h", ".hpp", ".c", ".cc", "Dockerfile", ".yml", ".yaml"], "exclude_folders": ["build"]},
        "6": {"extensions": ["Dockerfile", ".yml", ".yaml", ".toml", ".env", ".sh"], "exclude_folders": []},
        "7": {"extensions": [".tf", ".tfvars", ".hcl", "Dockerfile", ".yml", ".yaml"], "exclude_folders": []},
        "8": {"extensions": [".md", ".rst", ".txt", ".yml", ".yaml"], "exclude_folders": []},
        "9": {"extensions": [".sh", ".bat", ".ps1", ".cmd", "Dockerfile", ".yml", ".yaml"], "exclude_folders": []},
        "10": {"extensions": [".swift", ".plist", "Dockerfile", ".yml", ".yaml"], "exclude_folders": ["DerivedData"]},
        "11": {"extensions": [".kt", ".kts", "Dockerfile", ".yml", ".yaml"], "exclude_folders": ["build"]},
        "12": {"extensions": [".go", "Dockerfile", ".yml", ".yaml"], "exclude_folders": ["bin"]},
        "13": {"extensions": [".rb", ".gemspec", "Gemfile", "Dockerfile", ".yml", ".yaml"], "exclude_folders": ["vendor"]},
        "14": {"extensions": [".xml", ".cfg", ".ini", "Jenkinsfile", "Dockerfile", ".yml", ".yaml"], "exclude_folders": []}
    }
    return settings.get(environment, None)

if len(sys.argv) == 4:
    mode = sys.argv[1].strip().lower()
    environment = sys.argv[2].strip()
    folder_path = sys.argv[3].strip()
    
    if mode == "1":
        settings = get_environment_settings(environment)
        if settings:
            clear_terminal()
            read_files_from_folder(folder_path, settings["exclude_folders"], settings["extensions"])
        else:
            print("Numéro d'environnement invalide.")
    else:
        print("Mode inconnu. Utilisez 1 pour sélectionner un environnement.")
elif len(sys.argv) == 3:
    mode = sys.argv[1].strip().lower()
    folder_path = sys.argv[2].strip()
else:
    clear_terminal()
    mode = input("Voulez-vous choisir par thème (1) ou par liste de langages (2) ?: ").strip()
    folder_path = input("Entrez le chemin du dossier: ").strip()

if mode == "1":
    print("Choisissez un environnement:")
    print("1 - Web Development")
    print("2 - Java Development")
    print("3 - Python Development")
    print("4 - .NET Development")
    print("5 - C++ Development")
    print("6 - DevOps & Configuration (Docker, YAML, JSON)")
    print("7 - Infrastructure as Code (Terraform, HCL)")
    print("8 - Documentation (Markdown, reStructuredText)")
    print("9 - Scripting (Shell, Batch, PowerShell)")
    print("10 - iOS Development (Swift)")
    print("11 - Android Development (Kotlin)")
    print("12 - Go Development")
    print("13 - Ruby Development")
    print("14 - CI/CD Configuration")
    environment = input("Entrez le numéro correspondant: ").strip()
    settings = get_environment_settings(environment)
elif mode == "2":
    extensions_input = input("Entrez les extensions de fichiers à rechercher (séparées par des virgules, ex: .py,.java,.html): ").strip()
    exclude_folders_input = input("Entrez les dossiers à exclure (séparés par des virgules, laissez vide si aucun): ").strip()
    extensions = [ext.strip() for ext in extensions_input.split(",")]
    exclude_folders = [folder.strip() for folder in exclude_folders_input.split(",")] if exclude_folders_input else []
    
    clear_terminal()
    read_files_from_folder(folder_path, exclude_folders, extensions)
    exit()
else:
    print("Option non reconnue. Veuillez choisir 1 ou 2.")
    exit()

if settings:
    clear_terminal()
    read_files_from_folder(folder_path, settings["exclude_folders"], settings["extensions"])
else:
    print("Paramètres non reconnus. Veuillez vérifier votre sélection.")
