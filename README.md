# Flask Web Calculator

Simple Flask web calculator using GET parameters.

## How to run

1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
2. Install dependencies:
    ```powershell
    pip install -r requirements.txt
   
3. Run the application:
    ```powershell
    python appFlask.py

4. Example request:
 ```bash
    http://127.0.0.1:5000/calculate?op=sum&arg1=2&arg2=5
```