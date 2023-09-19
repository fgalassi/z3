# Let's play with Z3 and Jupyter

## Create and activate a python virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
echo ".venv/" >> .gitignore # or add to .git/info/exclude
```

## Install deps: ipykernel, z3-solver
```bash
pip install ipykernel
pip install z3-solver
```

## Create and play with a Jupyter notebook
E.g. in VSCode select the .venv interpeter and launch command "Create: New Jupyter Notebook"
