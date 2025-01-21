# Navigate to the directory containing the virtual environment
cd ".."

# Activate the virtual environment
.\\virtual_envs\D497_Project_1_venv\Scripts\Activate.ps1

# Change Directories.
cd "WGU_D497_Project_1"

# Launch a new powershell window and run the Launch Virtual Environment Script and keep window open. 
Start-Process powershell -ArgumentList "-NoExit", "-File", "launchvenv.ps1"

# Launch VSCode
code .

# Launch Jupyterlab
python -m jupyterlab --ip 192.168.86.70 --port 8888 --notebook-dir=.


