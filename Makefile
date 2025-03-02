DELETE := rm
clean:
	@$(DELETE) dist build
	@$(DELETE) dist build

game:
	@pyinstaller --onefile --windowed --icon="icon.ico" main.py --name="game.exe" --clean
	@$(DELETE) *.spec

libraries:
	@python -m pip install pipreqs pyinstaller --break-system-packages
	@pipreqs . --force
	@python -m pip install -r requirements.txt --break-system-packages