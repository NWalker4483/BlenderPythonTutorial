# Blender Python Development Template
This repository provides a template environment for developing Python scripts and addons for Blender with modern development tools and practices. 



































































# Ignore this for now
poetry build
poetry export -f requirements.txt --output requirements.txt
poetry run pip download -r requirements.txt -d ./wheels
