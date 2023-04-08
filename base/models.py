from django.db import models
from django.db.models.fields import EmailField
from django.http.request import validate_host

class Couleur(models.Model):
    code_clr=models.CharField(max_length=2)
    nom=models.CharField(max_length=10)

    def __str__(self):
        return self.nom

class Taille(models.Model):
    code_Taille=models.CharField(max_length=3)
    nom=models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Collection(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Famille(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Style(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class TVA(models.Model):
    Taux=models.FloatField()

    def __str__(self):
        return str(self.Taux)+"%"
    
class Categorie_fr(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Depot(models.Model):
    Libelle=models.CharField(max_length=20)
    qte=models.IntegerField(default=0)

    def __str__(self):
        return self.Libelle

class Magasin(models.Model):
    Libelle=models.CharField(max_length=20)
    qte=models.IntegerField(default=0)
    Adresse=models.CharField(max_length=100)
    Tel=models.CharField(max_length=20)
    Fax=models.CharField(max_length=20)
    Email=models.EmailField()

    def __str__(self):
        return self.Libelle

class Client(models.Model):
    nom=models.CharField(max_length=20)
    Adresse=models.CharField(max_length=100)
    Ville=models.CharField(max_length=20)
    Pays=models.CharField(max_length=20)
    Tel=models.CharField(max_length=20)
    Fax=models.CharField(max_length=20)
    Email=models.EmailField()

    def __str__(self):
        return self.nom

class Societe(models.Model):
    Raison_sociale=models.CharField(max_length=100)
    Ice=models.CharField(max_length=15)
    Adresse=models.CharField(max_length=100)
    Ville=models.CharField(max_length=20)
    Pays=models.CharField(max_length=20)
    Tel=models.CharField(max_length=20)
    Fax=models.CharField(max_length=20)
    Email=models.EmailField()

    def __str__(self):
        return self.Raison_sociale

class Fournisseur(models.Model):
    Raison_sociale=models.CharField(max_length=100)
    Adresse=models.CharField(max_length=100)
    Ville=models.CharField(max_length=20)
    Pays=models.CharField(max_length=20)
    Tel=models.CharField(max_length=20)
    Fax=models.CharField(max_length=20)
    Email=models.EmailField()
    categorie=models.ForeignKey(Categorie_fr, on_delete=models.CASCADE)
    page_accueil=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.Raison_sociale

class Produit(models.Model):
    Nom=models.CharField(max_length=50)
    Collection=models.ForeignKey(Collection, on_delete=models.CASCADE,blank=True,null=True)
    Famille=models.ForeignKey(Famille, on_delete=models.CASCADE,blank=True,null=True)
    Style=models.ForeignKey(Style, on_delete=models.CASCADE,blank=True,null=True)
    Tva=models.ForeignKey(TVA, on_delete=models.CASCADE) 
    Code_Produit=models.CharField(max_length=60)
    Code_Barre=models.BigIntegerField(default=3250000000000)
    Designation=models.CharField(max_length=20)
    Libelle_Ticket=models.CharField(max_length=20)
    Prix_Untaire=models.FloatField()
    Prix_HT=models.FloatField()
    Prix_TTC=models.FloatField()

    def __str__(self):
        return self.Code_Produit

class contenir_clr(models.Model):
    prdt=models.ForeignKey(Produit,on_delete=models.CASCADE)
    clr=models.ForeignKey(Couleur,on_delete=models.CASCADE)

class contenir_taille(models.Model):
    prdt=models.ForeignKey(Produit,on_delete=models.CASCADE)
    taille=models.ForeignKey(Taille,on_delete=models.CASCADE)

class Association_Mag_Depot(models.Model):
    depot=models.ForeignKey(Depot,on_delete=models.CASCADE)
    magasin=models.ForeignKey(Magasin,on_delete=models.CASCADE)

class Reception(models.Model):
    fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    depot=models.ForeignKey(Depot,on_delete=models.CASCADE)
    ref_recep=models.CharField(max_length=20)
    date=models.DateField()

class ligne_recep(models.Model):
    prdt=models.ForeignKey(Produit,on_delete=models.CASCADE)
    reception=models.ForeignKey(Reception,on_delete=models.CASCADE)
    date=models.DateField()
    qte=models.IntegerField()

class stockagePrdtDepot(models.Model):
    depot=models.ForeignKey(Depot,on_delete=models.CASCADE)
    prdt=models.ForeignKey(Produit,on_delete=models.CASCADE)
    qte=models.IntegerField()

class Livraison(models.Model):
    depot=models.ForeignKey(Depot,on_delete=models.CASCADE)
    ref_Livr=models.CharField(max_length=20)
    date=models.DateField()

class ligne_livr(models.Model):
    livr=models.ForeignKey(Livraison,on_delete=models.CASCADE)
    prdt=models.ForeignKey(Produit,on_delete=models.CASCADE)
    date=models.DateField()
    qte=models.IntegerField()

class reception_clt(models.Model):
    livr=models.ForeignKey(Livraison,on_delete=models.CASCADE)
    clt=models.ForeignKey(Client,on_delete=models.CASCADE)

class reception_magasin(models.Model):
    livr=models.ForeignKey(Livraison,on_delete=models.CASCADE)
    mag=models.ForeignKey(Magasin,on_delete=models.CASCADE)