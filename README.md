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

#### 4. Running the Script on Linux
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

#### 5. Environment Variables (`ping.env`)
Place the `ping.env` file in the same directory as the script or the compiled executable. The file should look like this:

```env
DNS=8.8.4.4
GATEWAY=192.168.0.1
EXTRA=1.1.1.1
```

- **Defaults**:
  - `DNS` → Defaults to `8.8.8.8` if not set.
  - `GATEWAY` → Defaults to `192.168.1.1` if not set.
  - `EXTRA` → Skipped if not set.

---

### Commands Summary

#### For Windows:
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pyinstaller --onefile ping_script.py
```

#### For Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python ping_script.py
```

#### Running the Executable on Windows:
```cmd
ping_script.exe
```

---

### Requirements File Example (`requirements.txt`)
Ensure the dependencies used in your project are listed. For this script, it might look like this:

```
ping3
python-dotenv
```
