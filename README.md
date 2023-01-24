## Objectif
Ce TP a pour objectif d'apprendre à utiliser les classes. 
Ici, nous créons une classe Animal possédant des attributs et des méthodes. 
Une classe Human héritera des attributs de cette classe (classe supèrieure), qui ne seront donc pas à redéfinir (éviter la répétition de code) ainsi que de ses méthodes, étant la sous-classe 
d'Animal.

## Utilisation du Script
child=self.add_children(child_name,child_age) permet de créer un objet enfant. L'objet courant, self, devra donc être le parent souhaité de l'enfant et ajoutera aux attributs destinés aux 
informations sur ses potentiels enfants, l'objet child et son nom. L'objet enfant quant à lui ajoutera aux attributs destinés aux informations sur sa potentielle mère l'objet self et son nom.

L'utilisation de remove_children(child,child_name)est similaire, seuls les arguments à rentrer sont différents.

Le résultat d'un ajout ou d'une supression d'un enfant sera visible sur toutes les générations.  

 
