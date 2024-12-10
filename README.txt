- Requires
Python.3.11
pip

-- Build Instructions -- 
Open terminal in the root directory,
run: 
pip install -r requirements.txt

For windows, run:
pyinstaller --onefile --add-data "Dependencies;Dependencies" Flock.py

For mac/linux, run:
pyinstaller --onefile --add-data "Dependencies:Dependencies" Flock.py

The final executable will be in the 'dist' folder
