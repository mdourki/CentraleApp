from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput,label="Mot de passe")

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name' ,'last_name' , 'email', 'password1', 'password2']
        labels= {
            "username":"Nom d'utilisateur",
            "first_name":"Nom",
            "last_name":"Prénom",
            "email":"Adresse email",
            "password1":"Mot de passe",
            "password2":"Confirmation du mot de passe",
        }

class CouleurForm(forms.ModelForm):
    class Meta:
        model=Couleur
        fields = "__all__"
        labels={
            "code_clr":"Code du couleur",
            "nom":"Nom du couleur",
        }
            
class TailleForm(forms.ModelForm):
    class Meta:
        model=Taille
        fields = "__all__"
        labels={
            "code_Taille":"Code de la taille",
            "nom":"Nom du taille",
        }

class CollectionForm(forms.ModelForm):
    class Meta:
        model=Collection
        fields = "__all__"
        labels={
            "nom":"Nom de collection ",
        }

class FamilleForm(forms.ModelForm):
    class Meta:
        model = Famille
        fields = "__all__"
        labels = {
            "nom":"Nom de famille",
        }

class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = "__all__"
        labels = {
            "nom":"Nom du style",
        }

class TVAForm(forms.ModelForm):
    class Meta:
        model = TVA
        fields = "__all__" 
        labels = {
            "taux":"Taux",
        }

class CategorieFrForm(forms.ModelForm):
    class Meta:
        model = Categorie_fr
        fields = "__all__"
        labels = {
            "nom":"Nom",
        }

class DepotForm(forms.ModelForm):
    class Meta:
        model = Depot
        fields = "__all__" 
        labels = {
            "Libelle":"Libelle",
            "qte":"Quantité en stock",
        }

class MagasinForm(forms.ModelForm):
    class Meta:
        model = Magasin
        fields = "__all__" 
        labels = {
            "Libelle":"Libelle",
            "qte":"Quantité en stock",
            "Adresse":"Adresse",
            "Tel":"N° tel",
            "Fax":"FAX",
            "Email":"Email",
        }

class SocieteForm(forms.ModelForm):
    class Meta:
        model = Societe
        fields = "__all__" 
        labels = {
            "Raison_sociale":"Raison sociale",
            "Ice":"ICE",
            "Adresse":"Adresse",
            "Ville":"Ville",
            "Pays":"Pays",
            "Tel":"N° tel",
            "Fax":"FAX",
            "Email":"Email",
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__" 
        labels = {
            "nom":"Nom",
            "Adresse":"Adresse",
            "Ville":"Ville",
            "Pays":"Pays",
            "Tel":"N° tel",
            "Fax":"FAX",
            "Email":"Email",
        }

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__" 
        labels = {
            "Raison_sociale":"Raison sociale",
            "Adresse":"Adresse",
            "Ville":"Ville",
            "Pays":"Pays",
            "Tel":"N° tel",
            "Fax":"FAX",
            "Email":"Email",
            "categorie":"Catégorie",
            "page_accueil":"Page d'accueil",
        }

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['Nom',
        'Collection',
        'Famille',
        'Style',
        'Tva',
        'Designation',
        'Prix_Untaire',
        'Prix_TTC',
        ]

        labels = {
            "Nom":"Nom",
            "Famille":"Famille",
            "Collection":"Collection",
            "Designation":"Désignation",
            "Style":"Style",
            "Prix_Untaire":"Prix unitaire",
            "Tva":"TVA",
            "Prix_TTC":"Prix TTC",
        }

class AssociationMagDepotForm(forms.ModelForm):
    class Meta:
        model = Association_Mag_Depot
        fields = "__all__" 
        
class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = [
            'fournisseur',
            'ref_recep',
        ]
        labels = {
            "fournisseur":"Fournisseur",
            "ref_recep":"Réferense du réception",
            "date":"Date",
        }

class stockagePrdtDepotForm(forms.ModelForm):
    class Meta:
        model = stockagePrdtDepot
        fields = "__all__"
        labels = {
            "depot":"Depot",
            "prdt":"Produit",
            "qte":"Quantité",
        }

class LivraisonForm(forms.ModelForm):
    class Meta:
        model = Livraison
        fields = [
            'ref_Livr',
            'depot',
        ]
        labels = {
            "ref_Livr":"Réferense du livraison",
        }

class ligneLivraisonForm(forms.ModelForm):
    class Meta:
        model = ligne_livr
        fields = [
            'qte',
        ]
        labels = {
            "qte":"Quantité",
        }

class receptCltForm(forms.ModelForm):
    class Meta:
        model = reception_clt
        fields = [
            'clt',
        ]
        labels = {
            "clt":"Client",
        }

class receptMagForm(forms.ModelForm):
    class Meta:
        model = reception_magasin
        fields = [
            'mag',
        ]
        labels = {
            "mag":"Magasin",
        }

