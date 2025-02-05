# WGU_D497_Project_1
 
## Instructions:

There are two methods to setup and run the project. 

1. Automated - Powershell. 

To perform the automated setup and launch method, please run the "LaunchVenvAndLabServer" powershell file from within the "WGU_D497_Project_1" folder to setup and launch the project. 

The powershell file will perform the following: 
- Update PIP if necessary
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
    NOTE: If launching the server does not launch the "order_of_operations_landing_page.ipynb" notebook. Please navigate to the Notebook directory, and open the "order_of_operations_landing_page" notebook.


2. Manually - Command Line Interface. 

To perform the manual setup and launch of the project. Please follow the steps below: 

1. Starting from this folder, the "D497" parent directory. Hold the shift key and right click in the window space.
2. This will open an exanded context menu, please locate and select "Open PowerShell Window Here". 
3. A new PowerShell instance should open with the prompt flashing waiting for input, the command line navigation path reading something similar to "PS ...\D497>" 
    (NOTE: In the example above, the '...' would be replaced with your system's navigation path to this current folder, an example: "C:\Users\Udacity_Windows_Station_1\Desktop\D497>")

4. We will begin by making sure Python's package installer manager, PIP is fully updated. Please type in the following command to the PowerShell prompt: 
    ```
        python -m pip install --upgrade pip
    ```

5. Verify and press the enter key to perform an upgrade on PIP. Whether or not an update is performed, the prompt will check and install if necesary. 

6. On the new the PowerShell prompt line, we will now install a virtual environment python package using the following command:
    ```
        python -m pip install virtualenv"
    ```
    
5. Once you have input this, please hit enter to begin the install of the Virtual Environment package using Python's built in Package Installer/Manager, PIP.

6. Once the install has completed, we will now create a new python virtual environment to install our package dependencies to. The virtual environment files will be saved into the "virtaul_envs" folder located in this directory, "D497". To setup the new virtual envirnoment please enter the following into the PowerShell Prompt: 
    ```
        python -m venv virtual_envs/D497_Project_1_venv
    ```

    NOTE: If virtual_envs folder does not exist for some reason, you can easily create the subfolder by running the following command in the PowerShell instance
        ```
            New-Item -ItemType Directory -Force -Path virtual_envs" and hit enter to create it
        ```

7. Verify the command and press enter to begin creating the new virtual envirnoment. 
8. Next,  we will now activate the virtual environment we just created by typing the following into the PowerShell prompt: 
    ```
        .\\virtual_envs\D497_Project_1_venv\Scripts\Activate.ps1
    ```

9. Verify and press enter to run the command, activating the virtual environment. 

If successful, you should now see the name of the newly created virtual envirnment in paranthesis and different color font (typically green) before the previous prompt path (PS: C:\....\D497>)

10. Now that we are inside the virtual environment, we will now install the project dependencies using the following command line:
    ```
        python -m pip install -r requirements.txt
    ```

11. Press enter to run the command and begin the package installation. Please verify that all the packages installed correctly, and troubleshoot any failed installs. 
12. Once the package requirements have been installed, we will now navigated into the project's core directory, using the command: 
    ``` 
        cd "WGU_D497_Project_1"
    ```

13. Verify the entry and press the enter key to perform the directory change. You should received a fresh prompt line, but the working directory path (The path between the PS and ">" ) should now have the main project folder on the ends, "PS C:\....\D497\WGU_D497_Project_1>"

14. From here, we will now need to install the custom python package that I created for use with this project. The custom package is a collection of python scripts that have been modified and grouped into a folder so that they can be turned into a local package using the "SetupTools" python package. To begin this install, please input the following command:
    ```
        python -m pip install -e .
    ```
15. Verify and press enter to install the package into the machine's Python packages list. 
16. Next we will run be manually running my "folder_manager.py" script that is inside my custom package. To perform an initialization of the project's "folder_paths.json" file to the system. Please input the following command into the prompt:
    ``` 
        python ./d497_helpers/folder_manager.py
    ```
17. Verify and press enter. You should see a python output on the screen and if necessary you can check the data directory, /data/, to see if the folders_path.json file was created. 
18. Finally, we can now launch JupyterLab server and load the project's landing page notebook, "Order of Operations - Landing Page". To make the use easier, please use the following command to launch the server. This command should launch the server to the correct notebook, as well as set the project's working directory to the current location. 
    ```
        python -m jupyterlab notebooks/order_of_operations_landing.ipynb --notebook-dir=.
    ``` 

    > NOTE: If for some reason the server does not launch to the correct notebook, please navigate to the "notebooks" directory and open the landing page, "order_of_operations_landing_page.ipynb" notebook file. 


