# Blender Python Development Template
This repository provides a template environment for developing Python scripts and addons for Blender with modern development tools and practices. 










poetry export -f requirements.txt --output requirements.txt

pip download -r requirements.txt -d ./wheels

blender --command extension build