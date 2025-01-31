# WGU_D497_Project_1
 
Please run the "LaunchVenvAndLabServer" powershell file from within the "WGU_D497_Project_1" folder to setup and launch the project. 

The powershell file will perform the following: 
- Install VirtualEnvironment Python Package
- Navigate to this project's parent directory
- Create the Virtual Environment directory, if it does not exist
- Create a Python Virtual Environment.
- Perform the PIP install requirements to install all needed modules/packages. 
- Activate the Virtual Environment
- Navigate back into the project directory
- Install the local package "d497_helpers"
- Run my "folder_manager.py" script to setup the "folder_paths.json" config file. 
- Launch a new powershell window for this virtual environment
- Launch VS Code if installed and configured
- Obtain the computer's local IPv4 Address
- Launch a JupyterLab Server, starting on the "order_of_operations_landing_page.ipynb" notebook.

- If launching the server does not launch the "order_of_operations_landing_page.ipynb" notebook. Please navigate to the Notebook directory, and open the "order_of_operations_landing_page" notebook.


Manually:

- From the D497 Parent directory
- Hold Shift and Right-click 
- Select "Open PowerShell Window Here" in the context menu
- You should have a new powershell window here, with the command line reading something similar to "PS ...\D497>" (the '...' would contain the folder's path on your system instead, example: "C:\Users\Udacity_Windows_Station_1\Desktop\D497>")

- In the command line, type: "python -m pip install virtualenv" (without quotes)
- Hit Enter to install Python Virtual Environment package. 
- Next we will create the Python Virtual Environment for this project inside the virtual_envs folder.
    NOTE: If virtual_envs folder does not exist for some reason, type: 
        "New-Item -ItemType Directory -Force -Path virtual_envs" and hit enter to create it

- Type: "python -m venv virtual_envs/D497_Project_1_venv"
- Hit Enter to create the new python virtual environment.

- Now we will activate the virtual environment with the following command line: 
    ".\\virtual_envs\D497_Project_1_venv\Scripts\Activate.ps1"

- Next we will install the python dependencies for this project with the following command line:
"python -m pip install -r requirements.txt"

- Hit enter to install the requirements. 
- Once done, we will now navigated into the project's core directory, using the command: 'cd "WGU_D497_Project_1"'  (Include the double quotes, not the single quotes.)
- Hit enter to change directories. 

- Now your command line should be almost the same as before, but now with the directory we navigated to on the end, such as this: "PS ... \D497\WGU_D497_Project_1>"

Here we will install the custom package I created for this project. Use the following command: "python -m pip install -e ." (without the double quotes)

Next we will run my folder_manager.py script to create the required folder_paths.json config file. 
    "python ./d497_helpers/folder_manager.py" 

Finally we can run the jupyterlab instance. 
python -m jupyterlab notebooks/order_of_operations_landing.ipynb --notebook-dir=.

