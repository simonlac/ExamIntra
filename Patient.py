####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen intra patient
###  Nom: Simon Lacaille
###  Description du fichier: classe pour les patient
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
###  https://fr.acervolima.com/serialiser-et-deserialiser-le-json-complexe-en-python/
####################################################################################

import json

class Patient:
    """
    Classe patient

    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################
    def __init__(self,p_noPatient = "",p_nom = "", p_prenom = "",p_date_Naiss = "",p_courriel = "",p_nb_Visite = 0, p_commentaire = "",p_montant = 0):
     """
         méthode constructeur avec paramètre de défaut
         définie les différents attributs de les patients
    """
     self.__no_patient= p_noPatient
     self.__nom = p_nom
     self.__prenom = p_prenom
     self.__dateNaiss = p_date_Naiss
     self.__courriel = p_courriel
     self.__nb_visite = p_nb_Visite
     self.commentaire = p_commentaire
     self.__montant = p_montant

 ##################################################
 ####   Propriétés, accesseurs et mutateurs    ####
 ####                                          ####
 ##################################################

#propriété de numéro de patient
    def _get_no_patient(self):
     """
      Accès à l'attribut privée du numéro de patient
     """
     return self.__no_patient
    def _set_no_patient(self,p_no_patient):
        """
        mutateur de __no_patient
        """
        if p_no_patient.isnumeric() :
          self.__no_patient = p_no_patient
        chaine_no_patient = p_no_patient
        if chaine_no_patient == 7:
            chaine_no_patient = True
            print(chaine_no_patient , "is Ok")
        elif chaine_no_patient != 7:
            chaine_no_patient = False
            print(chaine_no_patient , "is not Ok")


    no_patient = property(_get_no_patient,_set_no_patient)

    # propriété du nom du patient
    def _get_nom(self):
        """
        Accès à l'attribut privée __nom
        """
        return self.__nom
    def _set_nom(self,p_nom):
        """
        mutateur de __nom
        """
        if p_nom.isalpha():
            self.__nom = p_nom
        chaine_nom =p_nom
        if chaine_nom <= 30:
         chaine_nom = True
         print(chaine_nom , "is Ok")
        elif chaine_nom > 30:
         chaine_nom = False
         print(chaine_nom, "is not Ok")


    nom = property(_get_nom,_set_nom)

    # propriété du prénom du patient
    def _get_prenom(self):
        """
        Accès à l'attribut privée __prenom
        """
        return self.__prenom

    def _set_prenom(self, p_prenom):
        """
        mutateur de __prenom
        """
        if p_prenom.isalpha():
            self.__prenom = p_prenom
        chaine_prenom = p_prenom
        if chaine_prenom <= 30:
            chaine_prenom = True
            print(chaine_prenom , "is Ok")
        elif chaine_prenom > 30:
            chaine_prenom = False
            print(chaine_prenom , "is not Ok")

    prenom = property(_get_prenom, _set_prenom)

    #propriété dateNaiss
    def _get_date_Naiss(self):
        """
        accès à l'attribut privé __dateNaiss
        """
        return self.__dateNaiss

    def _set_date_Naiss(self,p_date_Naiss):
        """
        mutateur de __dateNaiss
        """
        if self.calculer_age(p_date_Naiss) >= 0:
            self.__dateNaiss = p_date_Naiss


    DateNaiss = property(_get_date_Naiss,_set_date_Naiss)

    def _get_courriel(self,p_prenom,p_nom,):
        """
        accès à l'attribut privé courriel
        """
        self.__courriel = p_prenom, p_nom, "@CabinetMedical.ca"
        p_courriel = self.__courriel
        return p_courriel

    def _get_nb_visite(self):
        """
        accès attribut nb visite
        """
        return self.__nb_visite

    def _set_nb_visite(self,p_nb_Visite: int):
        """
        mutateur du nombre de visite
        """
        if self.__nb_visite >= 0:
            self.__nb_visite =p_nb_Visite

    nb_visite = property(_get_nb_visite, _set_nb_visite)

    def _get_montant(self):
        """
        accès attribut montant
        """
        return self.__montant

    def _set_montant(self, p_montant: int):
        """
        mutateur du montant
        """
        if self.__montant >= 0:
            self.__montant = p_montant

    Montant = property(_get_montant, _set_montant)

    ############################################
         #####  MÉTHODES SPÉCIALES  #####
    ############################################

    def __str__(self):
        """
        méthode proffesionnel d'affichage
        """
        chaine_affichage_patient = " "*60+"\n"+"*"*60+"\n\n"+"   Le numéro du patient : "+self.no_patient+"\n"+\
                 "   Le nom du patient : "+self.nom+"\n"+\
                "   Le prénom du patient : "+self.prenom+"\n"+ \
                 "   Le courriel du patient : " + self.__courriel + "\n" + \
                "   La date de naissance du patient : "+str(self.DateNaiss.year())+"-" \
                 +str(self.DateNaiss.month())+"-"+ str(self.DateNaiss.day())+"\n" \
                 "   Le commentaire du médecin: " + self.commentaire+ "\n" + "\n"+"*"*60
        return chaine_affichage_patient


    #fonction pour calculer l'âge
    def calculer_age(self, p_date_Naiss):
        """
           calcule âge
           :: return : retourne l'âge
        """
        import datetime
        journee = datetime.date.today()
        return journee.year - p_date_Naiss.year() - (
                    (journee.month, journee.day) < (p_date_Naiss.month(), p_date_Naiss.day()))

    #fonction pour calculer le coût total
    def calculer_total(self,p_montant,p_nb_Visite):
        """
          calcul âge
          ::return : cout total
        """
        cout_total = p_montant * p_nb_Visite
        return cout_total


    def serialiser(self, p_noPatient,p_nom,p_prenom,json):
        """
           Méthode sérialiser
           ::param  : Le nom du fichier
           :: return : retourne confirmation fichier ouvert si le fichier est ouvert et les informations y sont écrites,
                       erreur d'écriture s'il y a erreur d'écriture et ne fonctionne pas s'il y a erreur d'ouverture

        """
        self.__dict__["_Etudiant__date_naiss"]=str(self.DateNaiss.year())+"-"+str(self.DateNaiss.month())+"-"\
                                               +str(self.DateNaiss.day())

        try:
            with open(p_noPatient,p_nom,p_prenom,json , "w") as fichier:
                try:
                    json.dump(self.__dict__, fichier)
                    return "confirmation fichier ouvert"
                except:
                    return "erreur d'écriture"
        except:
            return "ne fonctionne pas"

    def deserialiser(self, p_noPatient,p_nom,p_prenom,json):
        """
           Méthode desérialiser
           ::param  : Le nom du fichier
           return l'objet de Json
        """
        self.__dict__["_Etudiant__date_naiss"]=str(self.DateNaiss.year())+"-"+str(self.DateNaiss.month())+"-"\
                                               +str(self.DateNaiss.day())
        objet_json = Patient(p_noPatient,p_nom,p_prenom,json.loads(json.data))
        return objet_json