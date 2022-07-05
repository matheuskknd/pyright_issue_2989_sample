# Setup after download

Just run the following commands before trying to reproduce the [issue](https://github.com/microsoft/pylance-release/issues/2989):

```bash
git submodule init
git submodule update --recursive
```

Then, one of the following depending on your terminal interpreter:

Bash

```bash
python3 -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```

CMD

```bash
python3 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

Power Shell

```powershell
python3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
