# RepoToAI

This script reads every code file from a specified directory and paste them in the terminal, allowing to copy it into an AI.

## Usage

### 1. Using predefined environments

```
python script.py 1 (environment) <folder_path>
```

#### Available environments:

1. Web Development
2. Java Development
3. Python Development
4. .NET Development
5. C++ Development
6. DevOps & Configuration (Docker, YAML, JSON)
7. Infrastructure as Code (Terraform, HCL)
8. Documentation (Markdown, reStructuredText)
9. Scripting (Shell, Batch, PowerShell)
10. iOS Development (Swift)
11. Android Development (Kotlin)
12. Go Development
13. Ruby Development
14. CI/CD Configuration

Environments contains a predefined list of file extensions and excluded folders.

### 2. Using custom file extensions

```
python script.py 2 <folder_path>
```

The script will prompt you to enter the desired file extensions (comma-separated) and folders to exclude.

**Example:**

.py,.java,.html

node_modules,venv

## License

This project is licensed under the MIT License.
