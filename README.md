# DOCUMENATION DU LOGICIEL LerniLingvo

## Installation
* Installez python3.12
* Installez Visual Studio Code
* Allez sur le site : github https://github.com/lernilingvo/alpha.1
* choisissez une langue (japonais)
* Cliquez sur Code (icone verte)
* cliquez sur HTTPS puis Download ZIP
* Décompressez l’archive

## Tester l’installation de visual Studio Code et de python
### 1. ouvrir un terminal pouvant afficher des caractères japonais :
* Pour ouvrir vs code, double-cliquez sur wConsole.bat
* Pour ouvrir le terminal, dans le menu choisissez : ```view``` puis ```terminal```
* Pour vérifier que vous êtes bien dans le bon dossier tapez la commande : ```ls```
* dans la liste vous devez voir reload.py et ludi.py

### 2. contrôler que python est bien installé : 
* dans ce même terminal tapez la commande : ```python```
* puis  ```>>>exit()```

## Utilisation
### 1. ouvrir un terminal pouvant afficher des caractères japonais :
* double-cliquer sur wConsole.bat

### 2. initialiser des données à partir des fichiers de paramétrage
* chargez la base de données  : \
 ```python reload.py reset```

### 3. réviser le vocabulaire
* exécuter le programme : \
 ```python ludi.py```
* pour quitter le programme taper : ```$```

### ATTENTION :
* vous pouvez utilisez un terminal, mais les caractères japonais ne seront pas lisible.

## Information sur le paramétrage
* le fichier de paramétrage est lerni/lerni/data/config/lerni.param.json
* Vous pouvez ajouter des fichiers dans la liste : "csvs"
 * le type 	"word_list" ne contient qu’un mot par ligne
 * le type "word_translation" contient un numéro;un mot japonais;une,ou,plusieurs,traduction,séparée,par,des,virules;un champ vide;  
* Pour l’instant quand vous recharger les données, tout est effacé, puis deux fichiers sont chargés :
 * J.m1.csv qui contient quelques mots en japonais avec leur traduction
 * ex.ja.csv qui contient la liste des mots demandés par le logiciel

## Créer ou modifier des leçons
* Vous pouvez soit créer plus de fichier soit modifier les fichiers présents.
* Pour commencer, vous pouvez compléter le fichier JFG.m1.csv qui peut servir de sauvegarde des traductions.
* Ensuite, vous pouvez ajouter des lignes complètes dans le fichier de traduction utilisé par le logiciel
* Et surtout, vous pouvez supprimer ou ajouter des mots dans ex.ja.csv

