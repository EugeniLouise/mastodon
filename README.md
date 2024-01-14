# Summaritzador de toots de mastodon

Aquest software utilitza la xarxa social Mastodon (https://mastodon.social/home) per a llegir toots (com tweets de X) i fer recomptes en excel interessants.

## Resultats

Aquest software, després de cada execució guardarà en un directori adient, dos fitxers .csv.
* Fitxer històric amb totes les dades que s'han recollit en la història de les execucions del programa. Cada fila es un toot i en cada columna posarem totes les dades que aquí s'hi recullen. Els toots tene la estructura detallada aquí https://docs.joinmastodon.org/entities/Status/.
* Fitxer resumit on posarem el recompte total de toots que hem rebut de cada idioma diferent, i el nom d'usuari de l'ultim usuari que ha 'tootejat' en aquest idioma. El fitxer consta de les columnes: idioma, total_toots, ultim_usuari
És important que després de cada execució es guardin els estats dels arxius de forma persistent fins a la pòxima execució.

## Bones pràctiques

Imprescindible conèixer i fer un ús adequat dels seguents conceptes. Necessito que quan m'ho ensenyis em diguis per a què serveixen cadascun d'ells.
* Fitxer .gitignore
* Fitxer requirements.txt
* Utilització dels conceptes de classes adequats. He fet algunes classes d'exemple. cal crear-ne més. Cada classe va al seu arxiu. Els arxius no poden tenir més de 50 línies.
* Utilització d'una nomenclatura de variables adequada. les variables van en minúscula, les calsses en CamelCase.
* Realització d'almenys un unit test fent servir la llibreria pytest. Veure test dummy d'exemple que t'he deixat. buscar per internet.
* Utilització dels objectes de domini (dins del directori domain) que crequis oportuns. Recorda: un objecte de domini el pot entendre algú no-tècnic que sàpiga què és Twitter/Mastodon.
* Utilització de use cases per a la modificació d'objectes de domini. Qui sap, potser agrupar toots????
* Utilització d'una classe Proxy per a parlar amb Mastodon
* Utilització d'una classe Repository per a la interacció amb els excels. Aquesta te la deixo més lliure.
* Emmagatzematge de les credencials en un fitxer de credencials separat. Pot ser un fitxer .py amb les variables i au, pero han d'estar recollidetes en un lloc.
* Utilització d'una classe Controller/Service/Orchestrator per a orquestrar la resta de classes.
  
> [!CAUTION]
> Molt de ojo amb el chatGPT, és traicioner. Segurament sigui capaç de fer-te l'exercici però et demanaré el perquè de la ubicació de cada línia de codi en cada arxiu.
