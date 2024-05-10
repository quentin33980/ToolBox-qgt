# ToolBox-qgt

## 🎯 Objectifs 🎯 

L'objectif de la toolbox qgt est de rechercher et d'exploiter différentes vulnérabilités en utilisant les <strong>CVE-2021-42013</strong> et la <strong>CVE-2024-23897</strong>. Une seconde fonctionnalité de la toolbox sera le scan d'un réseau ainsi que de l'énumération des repertoires possiblement présent sur un serveur web.


##💻 Gestion de Projet 💻 
#### Schéma réseau 
![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152884/5eb9589d-2349-4e0b-ba8a-4d80d380bfac)


####🚀Diagramme de Gantt🚀
![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152884/663b917f-9fbf-407c-be8f-bf8e87909bd2)


Le projet s'est composé de neuf grandes parties : <br>

1. **Planification** : Élaboration d'une stratégie et d'un calendrier pour le développement. <br>
2. **Choix des outils développés** : Sélection des outils à concevoir pour répondre aux besoins du projet. <br>
3. **Recherche de CVE** : Identification des vulnérabilités courantes et pertinentes à prendre en compte.<br>
4. **Analyse de la faille** : Étude approfondie des vulnérabilités détectées pour comprendre leurs implications. <br>
5. **Recherche de POC** : Recherche de Preuves de Concept pour valider les vulnérabilités identifiées. <br>
6. **Développement de la toolBox** : Création des outils nécessaires pour exploiter les failles découvertes. <br>
7. **Test et débogage** : Évaluation et correction des erreurs et des bogues dans les outils développés. <br>
8. **Documentation** : Rédaction de documents expliquant l'utilisation et le fonctionnement des outils.<br>
9. **Révision finale** : Dernière vérification de l'ensemble du projet avant sa livraison ou sa publication. <br>





## ℹ️ Présentation ℹ️ 
La toolbox est consitué de 6 programmes différents 

METTRE CAPTURE D ECRAN DE LA TOOLBOX ET SUPPRIMER LE RESTE
<ol>
  <li>Installation de Jenkins</li>
  <li>Installation d'Apache</li>
  <li>Exploitation du Jenkins</li>
  <li>Exploitation d'Apache</li>
  <li>Scan réseau</li>
  <li>Enumération de répertoire web</li>
</ol>

<strong>🛠️Installation du Jenkins🛠️</strong> <br> explication

<strong>🛠️Installation d'Apache🛠️</strong> <br> explication

<strong>🔍Exploitation du Jenkins🔍</strong> <br> explication

<strong>🔍Exploitation d'Apache🔍</strong> <br> explication

<strong>📡Scan du réseau📡 : </strong> <br> explication


### 🗂️ Enumération répertoires web 🗂️
L'option d'énumération des répertoires web permettra à l'utilisateur d'effectuer automatiquement un balayage des répertoires présents sur un serveur web. Cette fonction générera en sortie un fichier CSV et un fichier PDF, offrant ainsi une optimisation du temps lors de l'inspection d'un site web.

Lors du lancement de la partie d'énumération, l'utilisateur sera invité à fournir trois paramètres : <br>
**1.** Adresse IP du serveur à scanner : Correspondant à l'adresse du serveur à balayer, récupérée lors de la phase de scan du réseau. <br>
**2.** Port du serveur : Correspondant au port du serveur à scanner, également récupéré lors de la phase de scan du réseau.<br>
**3.** Chemin de la wordlist à utiliser : L'utilisateur a la possibilité de choisir des wordlists personnalisées en fonction de ses besoins, ou bien d'utiliser directement celles présentes sur la machine Kali.<br>
Une fois le scan réaliser l'utilisateur retrouveras les résultats dans le dossier **"Résultats Enummération".**


## ⚙️Prérequis⚙️
Le développement de l'outil étant réalisé sur une base de Kali Linux, il est conseillé à l'utilisateur de lancer l'installation sur cette distribution pour éviter toutes erreurs de composants. <br>
Mises à jours de la distribution Linux 

```bash
sudo apt update && sudo apt upgrade
```

Le programme est fonctionnant en python 3, plusieurs libraries sont à installé pour faire fonctionné le programme 

### 🛠️ Installation python et pip 🛠️

```bash
sudo apt install python3 -y
sudo apt install python3-pip -y
```

### 📚 Installation librairies 📚

```pip
sudo pip install argparse && pip install requests && pip install python-nmap && pip install reportlab
```





###⬇️ Téléchargement de la ToolBox ⬇️ 
```bash
git clone https://github.com/quentin33980/ToolBox-qgt.git
```
```bash
cd ToolBox-qgt
```



###🐋 Installation Docker 🐋
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
###✅ Verification du fonctionnement de docker ✅
```bash
sudo systemctl status docker
```
###🗑️ Désinstallation de docker 🗑️

```bash
sudo apt autoremove docker-compose
```









