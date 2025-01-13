# Navigate to the directory containing the virtual environment
cd ".."

# Activate the virtual environment
.\\virtual_envs\D497_Project_1_venv\Scripts\Activate.ps1

# 
cd "WGU_D497_Project_1"

# Launch VSCode
code .

# Launch Jupyterlab
python -m jupyterlab --ip 192.168.86.70 --port 8888 --notebook-dir=.

