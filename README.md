### **Setup Instructions**

#### 1. Create a Virtual Environment
A virtual environment isolates dependencies for this project.

**Windows:**
```cmd
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
venv\Scripts\activate
Set-ExecutionPolicy Restricted
```

**Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

#### 2. Install Dependencies
Install the required libraries using `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

#### 3. Compile the Script into an Executable for Windows
To compile the Python script into an executable:

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Compile the Script**:
   ```bash
   pyinstaller --onefile ping.py
   ```

3. **Locate the Executable**:
   The compiled executable will be available in the `dist` directory as `ping_script.exe`.

---

#### 4. Modify the `ping.env.example` File
Before installing the script as a service, you need to modify the `ping.env.example` file to configure the environment variables.

1. Open the `dist/ping.env.example` file in a text editor.
   
2. Set the appropriate values for the environment variables:

   ```env
   DNS=8.8.4.4         # Set your DNS server (defaults to 8.8.8.8 if not set)
   GATEWAY=192.168.0.1 # Set your gateway IP (defaults to 192.168.1.1 if not set)
   EXTRA=1.1.1.1      # Set an additional server IP or leave blank to skip
   ```

3. Save the modified file as `ping.env` in the same directory as the executable (`dist/ping_script.exe`).

---

#### 5. Running the Script on Linux
To run the script directly on Linux:

1. Ensure the environment is active:
   ```bash
   source venv/bin/activate
   ```

2. Run the script:
   ```bash
   python ping_script.py
   ```

---

#### 6. Running the Script as a Windows Service with NSSM

To run the compiled executable (`ping_script.exe`) as a service on Windows using **NSSM**:

1. **Download and Install NSSM**:
   - Go to the [NSSM official website](https://nssm.cc/download) to download the appropriate version for your system (32-bit or 64-bit).
   - Extract and place the `nssm.exe` file in a directory of your choice, or add it to your system’s `PATH`.

2. **Install the Service**:
   Open a Command Prompt with administrative privileges and run the following command to install the service:

   ```cmd
   nssm install tridz-ping "C:\path\to\ping_script.exe"
   ```

   Replace `"C:\path\to\ping_script.exe"` with the actual path to your `ping_script.exe` file.

3. **Configure the Service**:
   - In the NSSM configuration window, set the **Environment Variables** by clicking on the **Environment** tab.
   - Add the `ping.env` file as a **variable** to the environment (if the script needs environment variables set).
     - For example:
       - **Variable Name**: `ping.env`
       - **Value**: `C:\path\to\ping.env`
   - Optionally, configure other parameters like the **Output Log** to capture script logs.

4. **Start the Service**:
   To start the service, run:

   ```cmd
   nssm start tridz-ping
   ```

5. **Stop the Service**:
   To stop the service, run:

   ```cmd
   nssm stop tridz-ping
   ```

6. **Uninstall the Service**:
   To remove the service, run:

   ```cmd
   nssm remove tridz-ping
   ```

---

### Requirements File Example (`requirements.txt`)
Ensure the dependencies used in your project are listed. For this script, it might look like this:

```
ping3
python-dotenv
```