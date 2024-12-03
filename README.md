# Blender Python Development Template

This repository provides a template environment for developing Python scripts and addons for Blender with modern development tools and practices. It includes preconfigured debugging support, package management, and code reloading capabilities.

## Overview

The template consists of two primary components:

1. **pyproject.toml**: Defines the project's dependencies and configuration using Poetry for package management
2. **Stub File**: A Python script that handles common development challenges when working with Blender's Python environment, including:
   - Package code reloading
   - Virtual environment path management
   - Blender UI reloading
   - Logging configuration
   - Remote debugging setup

## Getting Started

### Setting Up Your Own Project

1. Create a new directory for your project
2. Copy the `pyproject.toml` and stub file from this template
3. Modify the following elements to match your project:

### Virtual Environment Setup

1. Navigate to your project directory
2. Initialize Poetry:
```bash
poetry install
```

3. Note the virtual environment path created by Poetry (you'll need this for the stub file)

#### Package Name Changes
The template uses "btest" as the default package name. To use your own package name:

1. Update the package name in the stub file:
```python
PACKAGE_NAME = "your_package_name"
```

2. Update the main function import in the stub file:
```python
from your_package_name.main import main
```

3. Update the virtual environment path:
```python
VENV_PATH = '/path/to/your/virtualenv/'
```

## Usage

1. Place your main package code in your project directory
2. Update the stub file with your package's virtual environment path
3. Load the stub file in Blender's text editor
4. Run the script to initialize the development environment

## Troubleshooting

- If modules aren't reloading, verify your package name is correctly set in the stub file
- If the virtual environment isn't found, check the VENV_PATH in the stub file
- For debugging issues, ensure no other process is using port 5678


