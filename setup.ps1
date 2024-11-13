
mkdir config, handlers, utils, logs


New-Item -Name "bot.py" -ItemType File
New-Item -Name "requirements.txt" -ItemType File
New-Item -Name ".env" -ItemType File
New-Item -Name "README.md" -ItemType File


New-Item -Path "config" -Name "config.py" -ItemType File


New-Item -Path "handlers" -Name "__init__.py" -ItemType File
New-Item -Path "handlers" -Name "start_handler.py" -ItemType File
New-Item -Path "handlers" -Name "help_handler.py" -ItemType File
New-Item -Path "handlers" -Name "photo_handler.py" -ItemType File
New-Item -Path "utils" -Name "__init__.py" -ItemType File
New-Item -Path "utils" -Name "imgbb.py" -ItemType File
New-Item -Path "logs" -Name "bot.log" -ItemType File
