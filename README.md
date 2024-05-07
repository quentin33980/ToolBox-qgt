# ToolBox-qgt

## 🎯Objectifs 

L'objectif de la toolbox qgt est de rechercher et d'exploiter différentes vulnérabilités en utilisant les <strong>CVE-2021-42013</strong> et la <strong>2024-23897</strong>. Une seconde fonctionnalité de la toolbox sera le scan d'un réseau ainsi que de l'énumération des repertoires possiblement présent sur un serveur web.

## ℹ️ Présentation 
La toolbox est consitué de 4 programmes différents 
<ol>
  <li>Scan du réseau</li>
  <li>Enumération repertoire web </li>
  <li>CVE-2024-23897</li>
  <li>CVE-2021-42013 </li>
</ol>

<strong>Scan du réseau : </strong> <br> explication

<strong>Enumération repertoire web : </strong> <br> explication

<strong>CVE-2024-23897 : </strong> <br> explication

<strong>CVE-2021-42013 : </strong> <br>explication 

## ⚙️Prérequis
Installation sur une machine Linux, préferé une machine Kali ou parrot

Mises à jours de la distribution Linux 

```bash
sudo apt update && sudo apt upgrade
```

Le programme est fonctionnant en python 3, plusieurs libraries sont à installé pour faire fonctionné le programme 

### Installation python et pip

```bash
sudo apt install python3 
sudo apt install python3-pip
```

### Installation librairies 

```pip
sudo pip install argparse && pip install requests && pip install python-nmap
```

### 📂 Création repertoire 
Création d'un répertoire toolbox-qgt
```bash
mkdir Toolbox-qgt 
cd Toolbox-qgt
```
### ⬇️ Téléchargement de la ToolBox 
```bash
wget https://github.com/quentin33980/ToolBox-qgt.git
```

