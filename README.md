# Paper A1: JOSIF | Record Linkage

## 📌 Overview

> This implementation is focused around using Record Linkage to unite SIM and SINASC databases.  

This repository is based on our paper:  
**"Proposal For Linkage Between Health Information Systems SIM And SINASC"**   
Authors: Morsoleto, R. et al.  
Presented and accept at: [JOSIF](https://josif.ifsuldeminas.edu.br/ojs/index.php/anais/index) 2025, accessible [here](https://josif.ifsuldeminas.edu.br/ojs/index.php/anais/article/view/2528)

## 🚀 Setup

Requirements are described [here](pyproject.toml), and can be 
installed using the command:

```bash
poetry install
```

## ⚙ Run
Due to the size of the files ``DN.parquet.gzip`` and ``DO.parquet.gzip``, they weren't included in the repository and may need to be manually loaded on to the project's ``data/input`` folder. 
- The folder structure will be created during runtime for convenience.

```bash
python __main__.py
```

## 🔮 Structure

````mermaid
flowchart LR
    a[Pre-processing] --> b[Linkage]
````
- **Pre-processing**: Responsible to handle raw data, removing
duplicates and adding an index
- **Record Linkage**: Blocks rows using ``DTNASC`` and ``CODMUNRES`` columns, then compares each pair's ``PESO``, ``PARTO``, ``GRAVIDEZ``, ``SEMAGESTAC`` and ``ESCMAE`` columns. Only pairs that feature the same value for all 7 columns become part of the new database


## ✨ Dataset

The dataset used corresponds to the interval 2012 to 2022. Both are available through the following links: [SINASC](https://github.com/GOPAD-Datasus/DB_SINASC) and [SIM](https://github.com/GOPAD-Datasus/DB_SIM)

## 📝 License
[LGNU](LICENSE) | © GOPAD 2025