# ToolBox-qgt

## 🎯Objectifs 

L'objectif de la toolbox qgt est de rechercher et d'exploiter différentes vulnérabilités en utilisant les <strong>CVE-2021-42013</strong> et la <strong>CVE-2024-23897</strong>. Une seconde fonctionnalité de la toolbox sera le scan d'un réseau ainsi que de l'énumération des repertoires possiblement présent sur un serveur web.


## Gestion de Projet 
#### Schéma réseau 
![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152884/5eb9589d-2349-4e0b-ba8a-4d80d380bfac)


#### Diagramme de Gantt
![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152884/663b917f-9fbf-407c-be8f-bf8e87909bd2)


## ℹ️ Présentation 
La toolbox est consitué de 4 programmes différents 
<ol>
  <li>Scan du réseau</li>
  <li>Enumération repertoire web </li>
  <li>CVE-2024-23897</li>
  <li>CVE-2021-42013 </li>
</ol>

<strong>Scan du réseau : </strong> <br> explication

<strong>Enumération repertoire web : </strong> <br> permet à l'utilisateur de lancer une exploration des répertoires sur un serveur web. L'outil scanne automatiquement les répertoires en fonction de la liste de mots choisie et renvoie les résultats sous forme d'un fichier CSV.

<strong>CVE-2024-23897 : </strong> <br> Ce choix permet d'utiliser un exploit pfonctionnant sur le service <strong>Jenkin version 2.441 </strong>.


<strong>CVE-2021-42013 : </strong> <br>explication 

## ⚙️Prérequis
Installation sur une machine Linux, préferé une machine Kali ou parrot

Mises à jours de la distribution Linux 

```bash
sudo apt update && sudo apt upgrade
```

Le programme est fonctionnant en python 3, plusieurs libraries sont à installé pour faire fonctionné le programme 

###  Installation python et pip

```bash
sudo apt install python3 -y
sudo apt install python3-pip -y
```

### 📚 Installation librairies 

```pip
sudo pip install argparse && pip install requests && pip install python-nmap
```

### 🐋 Installation Docker
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```
```bash
sudo apt update
```
```bash
sudo apt install docker-ce
```

Verification du fonctionnement de docker
```bash
sudo systemctl status docker
```
### 📂 Création repertoire 
Création d'un répertoire toolbox-qgt
```bash
mkdir Toolbox-qgt 
cd Toolbox-qgt
```


### ⬇️ Téléchargement de la ToolBox 
```bash
git clone git@github.com:quentin33980/ToolBox-qgt.git
```
```bash
### 🏴‍☠️ Installation du docker APACHE 
sudo docker build -t apache .
```
```bash
sudo docker run -it apache
```



