# Proyecto CI/CD con Python, GitHub y Streamlit

Este repositorio es un tutorial paso a paso para crear un proyecto Python desde cero, usar Git y GitHub, crear ramas y Pull Requests, configurar CI con GitHub Actions y desplegar una app simple con Streamlit.

## Requisitos

- Python 3.10+ (usamos Python 3.12)
- Git
- VS Code
- WSL (si estás en Windows) o terminal Linux

## Estructura final del proyecto

```
ci_cd/
+- .github/
¦  +- workflows/
¦     +- ci.yml
+- src/
¦  +- __init__.py
¦  +- app.py
+- tests/
¦  +- conftest.py
¦  +- test_app.py
+- streamlit_app.py
+- requirements.txt
+- .gitignore
+- README.md
```

## Paso 1: Crear carpeta del proyecto y abrir VS Code

```bash
mkdir ci_cd
cd ci_cd
code .
```

- `mkdir` crea la carpeta.
- `cd` entra a la carpeta.
- `code .` abre VS Code en esa carpeta.

## Paso 2: Crear entorno virtual (WSL/Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- `venv` crea un entorno aislado.
- `source` lo activa (verás `(.venv)` en la terminal).

Si te da error con `ensurepip`, instala el soporte:

```bash
sudo apt update
sudo apt install -y python3-venv
```

## Paso 3: Crear carpetas y archivos base

```bash
mkdir -p src tests
```

Crea `src/app.py`:

```python
def suma(a, b):
    return a + b
```

Crea `tests/test_app.py`:

```python
from src.app import suma

def test_suma():
    assert suma(2, 3) == 5
```

Crea `tests/conftest.py` para que pytest encuentre `src`:

```python
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
```

Instala pytest y ejecuta pruebas:

```bash
pip install pytest
pytest
```

## Paso 4: Inicializar Git y hacer primer commit

Inicializa Git:

```bash
git init
```

Crea `.gitignore`:

```
.venv/
__pycache__/
*.pyc
.pytest_cache/
```

Configura tu usuario (solo una vez en tu máquina):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

Primer commit:

```bash
git add .
git commit -m "Inicio del proyecto con prueba"
```

## Paso 5: Crear repo en GitHub y conectar

En GitHub crea un repo nuevo (vacío) llamado `ci_cd`.

Conecta el repo local:

```bash
git branch -M main
git remote add origin https://github.com/TU_USUARIO/ci_cd.git
git push -u origin main
```

## Paso 6: Crear rama y Pull Request

Crea una rama nueva:

```bash
git checkout -b feature/saludo
```

Agrega la función `saludo` en `src/app.py`:

```python
def saludo(nombre):
    return f"Hola, {nombre}!"
```

Agrega el test en `tests/test_app.py`:

```python
from src.app import suma, saludo

def test_suma():
    assert suma(2, 3) == 5

def test_saludo():
    assert saludo("Sergio") == "Hola, Sergio!"
```

Corre pruebas:

```bash
pytest
```

Commit y push:

```bash
git add .
git commit -m "Agrega funcion saludo y prueba"
git push -u origin feature/saludo
```

En GitHub crea el Pull Request y haz merge a `main`.

## Paso 7: Configurar CI con GitHub Actions

Crea `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del repo
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install pytest

      - name: Ejecutar tests
        run: pytest
```

Commit y push:

```bash
git add .github/workflows/ci.yml
git commit -m "Agrega CI con pytest en GitHub Actions"
git push
```

Revisa la pestaña **Actions** en GitHub para ver el pipeline en verde.

## Paso 8: Deploy simple con Streamlit

Crea `streamlit_app.py` en la raíz:

```python
import streamlit as st
from src.app import suma, saludo

st.title("Mi app con CI/CD")
st.write("Probando funciones desde src/app.py")

a = st.number_input("A", value=2)
b = st.number_input("B", value=3)
st.write("Suma:", suma(a, b))

nombre = st.text_input("Tu nombre", value="Sergio")
st.write(saludo(nombre))
```

Crea `requirements.txt`:

```
streamlit
```

Commit y push:

```bash
git add streamlit_app.py requirements.txt
git commit -m "Agrega app Streamlit para deploy"
git push
```

En Streamlit Community Cloud (share.streamlit.io):

- Repository: `TU_USUARIO/ci_cd`
- Branch: `main`
- Main file path: `streamlit_app.py`
- App URL: un subdominio simple (solo letras, números y guiones)

## Notas importantes

- Los tests deben ir en la carpeta `tests/`.
- `tests/conftest.py` es necesario para que Python encuentre `src`.
- `requirements.txt` es necesario para que Streamlit instale dependencias.
- El workflow de GitHub Actions se dispara automáticamente en cada push y PR a `main`.

---

Si quieres, puedo agregar badges de CI en el README o explicar cómo proteger la rama `main` para exigir que el CI pase antes del merge.
