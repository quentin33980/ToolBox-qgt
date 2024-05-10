# ToolBox-qgt

## 🎯 Objectifs 🎯 

L'objectif de la ToolBox QGT est de rechercher et d'exploiter différentes vulnérabilités en utilisant les <strong>CVE-2021-42013</strong> et la <strong>CVE-2024-23897</strong>. Une seconde fonctionnalité de la toolbox sera le scan d'un réseau ainsi que de l'énumération des repertoires possiblements présents sur un serveur web.


## 💻 Gestion de Projet 💻 
#### Schéma réseau 
![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152884/5eb9589d-2349-4e0b-ba8a-4d80d380bfac)


#### 🚀Diagramme de Gantt🚀 
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
La toolbox propose de 6 programmes différents 



![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152877/3a11397f-92bf-4b70-a1e1-4f91a8802de7)


### <strong>🛠️Installation du Jenkins🛠️</strong> <br> 

L'option n°1 permet d'installer un service Jenkins 2.441 sur un docker. Une page Firefox ou le navigateur par défaut devrait s'ouvrir directement sur la page ci-dessous. 

![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152877/8428d758-fbd1-47de-a0a1-5c679aa77887)

🔥ATTENTION🔥

Si la page ne s'ouvre pas automatiquement (souvent quand le navigateur est déjà ouvert), il faudra aller dans votre navigateur pour rechercher l'ip '127.0.0.1:8080'. Si la page ne fonctionne pas, un temps de 80 secondes est imposé pour permettre au serveur de bien démarrer. Une machine suffisament puissante devrait le faire en moins de 80 secondes. Si ce n'est pas le cas, il faudra modifier le fichier JenkinsInstall.py sur les dernières lignes :

```bash 
time.sleep(TEMPS_A_MODIFIER_EN_SECONDE)
```
### <strong>🔍Exploitation du Jenkins🔍</strong> <br> 

L'option n°2 permet d'exploiter le service Jenkins 2.441. Il utilise la CVE-2024-23897 permettant de récupérer le mot de passe de l'administrateur en téléchargeant le fichier 'jenkins-cli.jar' depuis le serveur Jenkins. Ce dernier est mis dans une commande java qui sortira une erreur verbeuse nous indiquant le mot de passe administrateur.Le mot de passe sera également noté dans un fichier nommé 'mdpADMIN'.<strong> Il suffira de copier coller le mot de passe (utilisateur 'admin') sur le navigateur </strong>.  Une page Firefox ou le navigateur par défaut devrait s'ouvrir directement sur la page ci-dessous.

## Première connexion 

![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152877/8428d758-fbd1-47de-a0a1-5c679aa77887)

## Après la première connexion déjà établie  

![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152877/59e47258-2bb9-4f4c-b587-82bc2ee14809)

🔥ATTENTION🔥

Si la page ne s'ouvre pas automatiquement (souvent quand le navigateur est déjà ouvert), il faudra aller dans votre navigateur pour rechercher l'ip '172.17.0.2:80'.

### <strong>📡Scan du réseau📡 : </strong> <br> 

L'option n°3 utilise l'outil scapy ce qui permet de rendre le scan du réseau depuis l'ip automatiquement récupérer où nous sommes connecté. Une fois les ip récupérées, un rapport est généré dans un dossier respectif 'ip-results', en .csv puis converti en .pdf. En plus de cela, il propose de faire un scan plus développé en s'appuyant sur l'outil Nmap pour en faire un rapport, une page par Ip, également produit dans le dossier.


### 🗂️ Enumération répertoires web 🗂️

L'option n°4, énumération des répertoires web permettra à l'utilisateur d'effectuer automatiquement un balayage des répertoires présents sur un serveur web. Cette fonction générera en sortie un fichier CSV et un fichier PDF, offrant ainsi une optimisation du temps lors de l'inspection d'un site web.

Lors du lancement de la partie d'énumération, l'utilisateur sera invité à fournir trois paramètres : <br>
**1.** Adresse IP du serveur à scanner : Correspondant à l'adresse du serveur à balayer, récupérée lors de la phase de scan du réseau. <br>
**2.** Port du serveur : Correspondant au port du serveur à scanner, également récupéré lors de la phase de scan du réseau.<br>
**3.** Chemin de la wordlist à utiliser : L'utilisateur a la possibilité de choisir des wordlists personnalisées en fonction de ses besoins, ou bien d'utiliser directement celles présentes sur la machine Kali.<br>
Une fois le scan réaliser l'utilisateur retrouveras les résultats dans le dossier **"Résultats Enummération".**

### <strong>🛠️Installation d'Apache🛠️</strong> <br> 

L'option n°5 permet d'installer un service Apache 2.4.50 sur un docker. Une page Firefox ou le navigateur par défaut devrait s'ouvrir directement sur la page ci-dessous. 

![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152877/32018a64-85c7-4662-a9de-56d24b4e70a8)

🔥ATTENTION🔥

Si la page ne s'ouvre pas automatiquement (souvent quand le navigateur est déjà ouvert), il faudra aller dans votre navigateur pour rechercher l'ip '172.17.0.2:80'. Si la page ne fonctionne pas, il faudra faire la commande suivante : 

```bash
sudo docker ps
```
![image](https://github.com/quentin33980/ToolBox-qgt/assets/129152877/7fce846f-cfcb-4284-8a02-ac4505fe7eef)

Récupérer TOUT les containers ID pour le mettre dans la commande suivante : 

```bash
sudo docker stop CONTAINER_NAME CONTAINER_NAME2
```
### 🔒Vous pourrez à nouveau faire l'installation d'Apache via la Toolbox.🔒 

Si le problème est une erreur de port déjà utilisé, il faut faire un kill du processus pour relance le nc après : 

```bash
sudo lsof -i :4444
sudo kill -9 NUMERO_DU_PID_UTILISE
```

### <strong>🔍Exploitation d'Apache🔍</strong> <br> 

L'option n°6 permet d'utiliser la CVE-2021-42013.py sur le service Apache 2.4.50 (fonctionne également sur la 2.4.49). Cette CVE nous permet d'obtenir un revershell du serveur. <strong> Il faut bien penser à ouvrir un second terminal pour utiliser la commande d'écoute netcat sur le port 4444</strong> : 

```bash
nc -lvp 4444
```

![Vidéo-sans-titre-‐-Réalisée-avec-Clipchamp](https://github.com/quentin33980/ToolBox-qgt/assets/129152877/50e5834e-36f5-4830-b190-c6617d336cf7)


### <strong> 💣 Quitter 💣</strong> <br> 

L'option n°7 sert à quitter l'outil <strong>proprement</strong>  pour pouvoir repartir sur une machine vierge. 


## ⚙️Prérequis⚙️

⚔️AVOIR UNE CONNEXION INTERNET SUR LA MACHINE QUI HEBERGERA LA TOOLBOX⚔️

Le développement de l'outil étant réalisé sur une base de Kali Linux, il est conseillé à l'utilisateur de lancer l'installation sur cette distribution pour éviter toutes erreurs de composants. La toolbox ne fonctionnera pas sur une machine dans un container (docker) ! <br>
Mises à jours de la distribution Linux 

```bash
sudo apt update && sudo apt upgrade -y
```

Le programme est utilisable en python 3, plusieurs libraries sont à installer pour faire fonctionner le programme 

### 🛠️ Installation python et pip 🛠️

```bash
sudo apt install python3 -y
sudo apt install python3-pip -y
```

### 🛠️ Installation de Git 🛠️
```bash
sudo apt install git -y 
```
### 🛠️ Installation de nmap 🛠️
```bash
sudo apt install nmap
```
### ⬇️ Téléchargement de la ToolBox ⬇️ 
```bash
git clone https://github.com/quentin33980/ToolBox-qgt.git
```
```bash
cd ToolBox-qgt
```


### 📚 Installation librairies 📚

```pip
sudo pip install -r requirements.txt
```
### 💣 Utilisation de la ToolBox 💣 

```bash
sudo su
```
```bash
sudo python3 toolbox.py
```





### 🗑️ Désinstallation de docker 🗑️

```bash
sudo apt autoremove docker-compose
```


