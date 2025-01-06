# README
## 1. Preparar code space
- Ir a extensiones  e instalar python y jupyter
- Crear el archivo gitignore con 
```bash 
echo -e ".venv\n.env > .gitignore
```
- Crear el entorno virtual y activarlo
```bash
python -m venv .venv 
source .venv/bin/activate
```
- Instalar librerias de python para trabajar con jupyter, pandas, y matplotlib
```bash
python -m pip install ipykernel nbformat pandas seaborn 
```
- Crear carpetas de trabajo
```bash
mkdir notebooks src app docs
mkdir -p data/{raw,baking,final}
```
- Editar un archivo
```bash
touch mitexto.txt
nano mitexto.txt
```
