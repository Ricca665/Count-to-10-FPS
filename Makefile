ifeq ($(OS),Windows_NT)
    DELETE := cmd /C rd /s /q
else
    DELETE := rm -rf
endif

clean:
	@$(DELETE) dist build
	@$(DELETE) *.spec

game:
	@pyinstaller --onefile --windowed --icon="icon.ico" main.py --name="game.exe" --clean
	@$(DELETE) *.spec

libraries:
	@python -m pip install pipreqs pyinstaller --break-system-packages
	@pipreqs . --force
	@python -m pip install -r requirements.txt --break-system-packages
