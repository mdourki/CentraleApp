import collections
from django.shortcuts import redirect, render   
from django.views import View # view relation with templates
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib import messages
import datetime
from CentraleApp.utils import render_to_pdf
import xlwt
from tablib import Dataset
from django.db.models import Sum

@login_required(login_url='login')
def homeView(request):
    if request.method == 'GET':
        return render(request,"home.html")

class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("home")
        form = LoginForm()
        return render(request,"login.html",{'form': form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request,'Disabled account')
            else:
                messages.info(request,'Invalid login')
        return redirect("home")

class LogOutView(View):
    def get(self,request):
        logout(request)
        return redirect("login")

class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,"signup.html",{'form': form})
    def post(self,request):
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
        
            if password1.isnumeric():
                messages.error(request, 'Le mot de passe ne doit pas être un numéro.')   
                return  redirect("signup") 

            if len(password1) < 8:
                messages.error(request, 'Vous devez avoir au moins 8 caractères dans votre mot de passe.')   
                return  redirect("signup") 

            if password1 != password2:
                messages.error(request, 'Les deux mots de passe doivent être pareilles.')   
                return  redirect("signup") 
            
            

        return redirect("signup")

""""""""""""""""""""""""
"""Couleur"""
""""""""""""""""""""""""
@login_required(login_url='login')
def CouleursListView(request):
    if request.method == 'GET':
        couleurs=Couleur.objects.all()
        return render(request,"ListCouleurs.html",{'couleurs':couleurs})

@login_required(login_url='login')
def CouleurAddView(request):
    if request.method == 'GET':
        form=CouleurForm()
        return render(request,"AddCouleur.html",{'form':form})
    if request.method == 'POST':
        form=CouleurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_clr=request.FILES['myfile']
            imported_data = dataset.load(new_clr.read(),format='xlsx')
            for data in imported_data:
	        	    value = Couleur(
	        		    data[0],
	        		    data[1],
                        data[2],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("couleurs")

@login_required(login_url='login')
def CouleurUpdateView(request,idp):
    if request.method == 'GET':
        couleur=Couleur.objects.get(id=idp)
        form=CouleurForm(instance=couleur)
        return render(request,"AddCouleur.html",{'form':form})
    if request.method == 'POST':
        couleur=Couleur.objects.get(id=idp)
        form=CouleurForm(request.POST,request.FILES,instance=couleur)
        if form.is_valid():
            form.save()
        return  redirect("couleurs")

@login_required(login_url='login')
def CouleurDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerCouleur.html",{})
    if request.method == 'POST':
        couleur=Couleur.objects.get(id=idp)
        couleur.delete()
        return  redirect("couleurs")

""""""""""""""""""""""""
"""Taille"""
""""""""""""""""""""""""
@login_required(login_url='login')
def TailleListView(request):
    if request.method == 'GET':
        tailles=Taille.objects.all()
        return render(request,"ListTailles.html",{'tailles':tailles})

@login_required(login_url='login')
def TailleAddView(request):
    if request.method == 'GET':
        form=TailleForm()
        return render(request,"AddTaille.html",{'form':form})
    if request.method == 'POST':
        form=TailleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_taille=request.FILES['myfile']
            imported_data = dataset.load(new_taille.read(),format='xlsx')
            for data in imported_data:
	        	    value = Taille(
	        		    data[0],
	        		    data[1],
                        data[2],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("tailles")

@login_required(login_url='login')
def TailleUpdateView(request,idp):
    if request.method == 'GET':
        taille=Taille.objects.get(id=idp)
        form=TailleForm(instance=taille)
        return render(request,"AddTaille.html",{'form':form})
    if request.method == 'POST':
        taille=Taille.objects.get(id=idp)
        form=TailleForm(request.POST,request.FILES,instance=taille)
        if form.is_valid():
            form.save()
        return  redirect("tailles") # tailles is url of listtailles

@login_required(login_url='login')
def TailleDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerTaille.html",{})
    if request.method == 'POST':
        taille=Taille.objects.get(id=idp)
        taille.delete()
        return  redirect("tailles")

""""""""""""""""""""""""
"""Collection"""
""""""""""""""""""""""""
@login_required(login_url='login')
def CollectionListView(request):
    if request.method == 'GET':
        collections=Collection.objects.all() #select from Collection *
        return render(request,"ListCollections.html",{'collections':collections})

@login_required(login_url='login')
def CollectionAddView(request):
    if request.method == 'GET':
        form=CollectionForm()
        return render(request,"AddCollection.html",{'form':form})
    if request.method == 'POST':
        form=CollectionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_collection=request.FILES['myfile']
            imported_data = dataset.load(new_collection.read(),format='xlsx')
            for data in imported_data:
	        	    value = Collection(
	        		    data[0],
	        		    data[1],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("collections")

@login_required(login_url='login')
def CollectionUpdateView(request,idp):
    if request.method == 'GET':
        collection=Collection.objects.get(id=idp)
        form=CollectionForm(instance=collection)
        return render(request,"AddCollection.html",{'form':form})
    if request.method == 'POST':
        collection=Collection.objects.get(id=idp)
        form=CollectionForm(request.POST,request.FILES,instance=collection)
        if form.is_valid():
            form.save()
        return  redirect("collections")

@login_required(login_url='login')
def CollectionDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerCollection.html",{})
    if request.method == 'POST':
        collection=Collection.objects.get(id=idp)
        collection.delete()
        return  redirect("collections")

""""""""""""""""""""""""
"""Famille"""
""""""""""""""""""""""""
@login_required(login_url='login')
def FamilleListView(request):
    familles=Famille.objects.all()
    return render(request,"ListFamilles.html",{'familles':familles})

@login_required(login_url='login')
def FamilleAddView(request):
    if request.method == 'GET':
        form=FamilleForm()
        return render(request,"AddFamille.html",{'form':form})
    if request.method == 'POST':
        form=FamilleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_famille=request.FILES['myfile']
            imported_data = dataset.load(new_famille.read(),format='xlsx')
            for data in imported_data:
	        	    value = Famille(
	        		    data[0],
	        		    data[1],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("familles")  

@login_required(login_url='login')
def FamilleUpdateView(request,idp):
    if request.method == 'GET':
        famille=Famille.objects.get(id=idp)
        form=FamilleForm(instance=famille)
        return render(request,"AddFamille.html",{'form':form})
    if request.method == 'POST':
        famille=Famille.objects.get(id=idp)
        form=FamilleForm(request.POST,request.FILES,instance=famille)
        if form.is_valid():
            form.save()
        return  redirect("familles")

@login_required(login_url='login')
def FamilleDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerFamille.html",{})
    if request.method == 'POST':
        famille=Famille.objects.get(id=idp)
        famille.delete()
        return  redirect("familles")  

""""""""""""""""""""""""
"""Style"""
""""""""""""""""""""""""
@login_required(login_url='login')
def StyleListView(request):
    styles=Style.objects.all()
    return render(request,"ListStyles.html",{'styles':styles})

@login_required(login_url='login')
def StyleAddView(request):
    if request.method == 'GET':
        form=StyleForm()
        return render(request,"AddStyle.html",{'form':form})
    if request.method == 'POST':
        form=StyleForm(request.POST,request.FILES)        
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_style=request.FILES['myfile']
            imported_data = dataset.load(new_style.read(),format='xlsx')
            for data in imported_data:
	        	    value = Style(
	        		    data[0],
	        		    data[1],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("styles")    

@login_required(login_url='login')
def StyleUpdateView(request,idp):
    if request.method == 'GET':
        style=Style.objects.get(id=idp)
        form=StyleForm(instance=style)
        return render(request,"AddStyle.html",{'form':form})
    if request.method == 'POST':
        style=Style.objects.get(id=idp)
        form=StyleForm(request.POST,request.FILES,instance=style)
        if form.is_valid():
            form.save()
        return  redirect("styles")

@login_required(login_url='login')
def StyleDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerStyle.html",{})
    if request.method == 'POST':
        style=Style.objects.get(id=idp)
        style.delete()
        return  redirect("styles")

""""""""""""""""""""""""
"""TVA"""
""""""""""""""""""""""""  
@login_required(login_url='login')
def TVAListView(request):
    tvas=TVA.objects.all()
    return render(request,"ListTVA.html",{'tvas':tvas})

@login_required(login_url='login')
def TVAAddView(request):
    if request.method == 'GET':
        form=TVAForm()
        return render(request,"AddTVA.html",{'form':form})
    if request.method == 'POST':
        form=TVAForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_tva=request.FILES['myfile']
            imported_data = dataset.load(new_tva.read(),format='xlsx')
            for data in imported_data:
	        	    value = TVA(
	        		    data[0],
	        		    data[1],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("tvas")

@login_required(login_url='login')
def TVAUpdateView(request,idp):
    if request.method == 'GET':
        tva=TVA.objects.get(id=idp)
        form=TVAForm(instance=tva)
        return render(request,"AddTVA.html",{'form':form})
    if request.method == 'POST':
        tva=TVA.objects.get(id=idp)
        form=TVAForm(request.POST,request.FILES,instance=tva)
        if form.is_valid():
            form.save()
        return  redirect("tvas")

@login_required(login_url='login')
def TVADeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerTVA.html",{})
    if request.method == 'POST':
        tva=TVA.objects.get(id=idp)
        tva.delete()
        return  redirect("tvas")

""""""""""""""""""""""""
"""Catégorie"""
""""""""""""""""""""""""
@login_required(login_url='login')
def CategoryListView(request):
    categories=Categorie_fr.objects.all()
    return render(request,"ListCategories.html",{'categories':categories})

@login_required(login_url='login')
def CategoryAddView(request):
    if request.method == 'GET':
        form=CategorieFrForm()
        return render(request,"AddCategorieFr.html",{'form':form})
    if request.method == 'POST':
        form=CategorieFrForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_category=request.FILES['myfile']
            imported_data = dataset.load(new_category.read(),format='xlsx')
            for data in imported_data:
	        	    value = Categorie_fr(
	        		    data[0],
	        		    data[1],
	        		    )
	        	    value.save()
            """End Import with excel"""
        return redirect("categories")

@login_required(login_url='login')
def CategoryUpdateView(request,idp):
    if request.method == 'GET':
        categorie=Categorie_fr.objects.get(id=idp)
        form=CategorieFrForm(instance=categorie)
        return render(request,"AddCategorieFr.html",{'form':form})
    if request.method == 'POST':
        categorie=Categorie_fr.objects.get(id=idp)
        form=CategorieFrForm(request.POST,request.FILES,instance=categorie)
        if form.is_valid():
            form.save()
        return  redirect("categories")

@login_required(login_url='login')
def CategoryDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerCategorieFr.html",{})
    if request.method == 'POST':
        categorie=Categorie_fr.objects.get(id=idp)
        categorie.delete()
        return  redirect("categories")

""""""""""""""""""""""""
"""Societe"""
""""""""""""""""""""""""
@login_required(login_url='login')
def SocieteListView(request):
    societes=Societe.objects.all()
    return render(request,"ListSocietes.html",{'societes':societes})

@login_required(login_url='login')
def SocieteAddView(request):
    if request.method == 'GET':
        form=SocieteForm()
        return render(request,"AddSociete.html",{'form':form})
    if request.method == 'POST':
        form=SocieteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_societe=request.FILES['myfile']
            imported_data = dataset.load(new_societe.read(),format='xlsx')
            for data in imported_data:
	        	    value = Societe(
	        		    data[0],
	        		    data[1],
                        data[2],
	        		    data[3],
                        data[4],
                        data[5],
	        		    data[6],
                        data[7],
                        data[8],
	        		        )
	        	    value.save()
        """End Import with excel"""
        return redirect("societes")

@login_required(login_url='login')
def SocieteUpdateView(request,idp):
    if request.method == 'GET':
        societe=Societe.objects.get(id=idp)
        form=SocieteForm(instance=societe)
        return render(request,"AddSociete.html",{'form':form})
    if request.method == 'POST':
        societe=Societe.objects.get(id=idp)
        form=SocieteForm(request.POST,request.FILES,instance=societe)
        if form.is_valid():
            form.save()
        return  redirect("societes")

@login_required(login_url='login')
def SocieteDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerSociete.html",{})
    if request.method == 'POST':
        societe=Societe.objects.get(id=idp)
        societe.delete()
        return  redirect("societes")

""""""""""""""""""""""""
"""Depot"""
""""""""""""""""""""""""
@login_required(login_url='login')
def DepotListView(request):
    depots=Depot.objects.all()
    return render(request,"ListDepots.html",{'depots':depots})

@login_required(login_url='login')
def DepotAddView(request):
    if request.method == 'GET':
        form=DepotForm()
        return render(request,"AddDepot.html",{'form':form})
    if request.method == 'POST':
        form=DepotForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_depot=request.FILES['myfile']
            imported_data = dataset.load(new_depot.read(),format='xlsx')
            for data in imported_data:
	        	    value = Depot(
	        		    data[0],
	        		    data[1],
                        data[2],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("depots")   

@login_required(login_url='login')
def DepotUpdateView(request,idp):
    if request.method == 'GET':
        depot=Depot.objects.get(id=idp)
        form=DepotForm(instance=depot)
        return render(request,"AddDepot.html",{'form':form})
    if request.method == 'POST':
        depot=Depot.objects.get(id=idp)
        form=DepotForm(request.POST,request.FILES,instance=depot)
        if form.is_valid():
            form.save()
        return  redirect("depots")

@login_required(login_url='login')
def DepotDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerDepot.html",{})
    if request.method == 'POST':
        depot=Depot.objects.get(id=idp)
        depot.delete()
        return  redirect("depots")

""""""""""""""""""""""""
"""Magasin"""
""""""""""""""""""""""""
@login_required(login_url='login')
def MagasinListView(request):
    magasins=Magasin.objects.all()
    return render(request,"ListMagasins.html",{'magasins':magasins})

@login_required(login_url='login')
def MagasinAddView(request):
    if request.method == 'GET':
        form=MagasinForm()
        return render(request,"AddMagasin.html",{'form':form})
    if request.method == 'POST':
        form=MagasinForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_magasin=request.FILES['myfile']
            imported_data = dataset.load(new_magasin.read(),format='xlsx')
            for data in imported_data:
	        	    value = Magasin(
	        		    data[0],
	        		    data[1],
                        data[2],
	        		    data[3],
                        data[4],
                        data[5],
	        		    data[6],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("magasins")

@login_required(login_url='login')
def MagasinUpdateView(request,idp):
    if request.method == 'GET':
        magasin=Magasin.objects.get(id=idp)
        form=MagasinForm(instance=magasin)
        return render(request,"AddMagasin.html",{'form':form})
    if request.method == 'POST':
        magasin=Magasin.objects.get(id=idp)
        form=MagasinForm(request.POST,request.FILES,instance=magasin)
        if form.is_valid():
            form.save()
        return  redirect("magasins")

@login_required(login_url='login')
def MagasinDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerMagasin.html",{})
    if request.method == 'POST':
        magasin=Magasin.objects.get(id=idp)
        magasin.delete()
        return  redirect("magasins")

""""""""""""""""""""""""
"""Client"""
""""""""""""""""""""""""
@login_required(login_url='login')
def ClientListView(request):
    clients=Client.objects.all()
    return render(request,"ListClients.html",{'clients':clients})

@login_required(login_url='login')
def ClientAddView(request):
    if request.method == 'GET':
        form=ClientForm()
        return render(request,"AddClient.html",{'form':form})
    if request.method == 'POST':
        form=ClientForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_client=request.FILES['myfile']
            imported_data = dataset.load(new_client.read(),format='xlsx')
            for data in imported_data:
	        	    value = Client(
	        		    data[0],
	        		    data[1],
                        data[2],
	        		    data[3],
                        data[4],
                        data[5],
	        		    data[6],
                        data[7],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("clients")

@login_required(login_url='login')
def ClientUpdateView(request,idp):
    if request.method == 'GET':
        client=Client.objects.get(id=idp)
        form=ClientForm(instance=client)
        return render(request,"AddClient.html",{'form':form})
    if request.method == 'POST':
        client=Client.objects.get(id=idp)
        form=ClientForm(request.POST,request.FILES,instance=client)
        if form.is_valid():
            form.save()
        return  redirect("clients")

@login_required(login_url='login')
def ClientDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerClient.html",{})
    if request.method == 'POST':
        client=Client.objects.get(id=idp)
        client.delete()
        return  redirect("clients")

""""""""""""""""""""""""
"""Fournisseur"""
""""""""""""""""""""""""
@login_required(login_url='login')
def FournisseurListView(request):
    fournisseurs=Fournisseur.objects.all()
    return render(request,"ListFournisseurs.html",{'fournisseurs':fournisseurs})

@login_required(login_url='login')
def FournisseurAddView(request):
    if request.method == 'GET':
        form=FournisseurForm()
        return render(request,"AddFournisseur.html",{'form':form})
    if request.method == 'POST':
        form=FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_four=request.FILES['myfile']
            imported_data = dataset.load(new_four.read(),format='xlsx')
            for data in imported_data:
	        	    value = Fournisseur(
	        		    data[0],
	        		    data[1],
                        data[2],
	        		    data[3],
                        data[4],
                        data[5],
	        		    data[6],
                        data[7],
                        data[8],
                        data[9],
	        		    )
	        	    value.save()
        """End Import with excel"""
        return redirect("fournisseurs")

@login_required(login_url='login')
def FournisseurUpdateView(request,idp):
    if request.method == 'GET':
        fournisseur=Fournisseur.objects.get(id=idp)
        form=FournisseurForm(instance=fournisseur)
        return render(request,"AddFournisseur.html",{'form':form})
    if request.method == 'POST':
        fournisseur=Fournisseur.objects.get(id=idp)
        form=FournisseurForm(request.POST,request.FILES,instance=fournisseur)
        if form.is_valid():
            form.save()
        return  redirect("fournisseurs")

@login_required(login_url='login')
def FournisseurDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerFournisseur.html",{})
    if request.method == 'POST':
        fournisseur=Fournisseur.objects.get(id=idp)
        fournisseur.delete()
        return  redirect("fournisseurs")

""""""""""""""""""""""""
"""Produit"""
""""""""""""""""""""""""
@login_required(login_url='login')
def ProduitListView(request):
    produits=Produit.objects.all()
    listQteDepots=[]#liste des quantités des produits dans les dépots
    listQteFournisseurs=[]#liste des quantités des produits reçus d'après les fournisseurs
    #Somme des quantités des produits dans les dépots
    for prdt in produits:
        if stockagePrdtDepot.objects.filter(prdt_id=prdt.id):
            sum=stockagePrdtDepot.objects.filter(prdt_id=prdt.id).aggregate(Sum('qte'))
            listQteDepots.append(sum['qte__sum'])
        else:
            listQteDepots.append(0)
    
    #Somme des quantités des produits reçus d'après les fournisseurs
    for prdt in produits:
        if ligne_recep.objects.filter(prdt_id=prdt.id):
            sum=ligne_recep.objects.filter(prdt_id=prdt.id).aggregate(Sum('qte'))
            listQteFournisseurs.append(sum['qte__sum'])
        else:
            listQteFournisseurs.append(0)

    list_Clrs=contenir_clr.objects.values('clr_id')
    lClrs=[]
    for c in list_Clrs:
        clr_id=c['clr_id']
        clr=Couleur.objects.get(id=clr_id)
        lClrs.append(clr)

    list_Tailles=contenir_taille.objects.values('taille_id')
    lTailles=[]
    for t in list_Tailles:
        taille_id=t['taille_id']
        tai=Taille.objects.get(id=taille_id)
        lTailles.append(tai)

    return render(request,"ListProduits.html",{'produits':produits,'lClrs':lClrs,'lTailles':lTailles,
    'zipped_data':zip(produits,lClrs,lTailles,listQteDepots,listQteFournisseurs)})

@login_required(login_url='login')
def ProduitAddView(request):
    if request.method == 'GET':
        form=ProduitForm()
        couleurs=Couleur.objects.all()
        tailles=Taille.objects.all()
        return render(request,"AddProduit.html",{'form':form,'couleurs':couleurs,'tailles':tailles})
    if request.method == 'POST':
        form=ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            strClrs=request.POST.get('colorsTxt')
            lC=strClrs.split()#liste des couleurs
            strtailles=request.POST.get('taillesTxt')
            lt=strtailles.split()#liste des tailles
            for c in lC:
                for t in lt:                    
                    savePrdt=Produit()
                    clr=Couleur.objects.get(id=c)
                    tai=Taille.objects.get(id=t)
                    savePrdt.Nom=cd['Nom']
                    savePrdt.Code_Produit=str(cd['Nom'])+"-"+str(clr.code_clr)+"-"+str(tai.code_Taille)
                    savePrdt.Famille=cd['Famille']
                    savePrdt.Collection=cd['Collection']
                    savePrdt.Style=cd['Style']
                    savePrdt.Tva=cd['Tva']
                    if Produit.objects.count() > 0:
                        lastPrdt=Produit.objects.last()
                        savePrdt.Code_Barre=lastPrdt.Code_Barre+1
                    else:
                        savePrdt.Code_Barre=3250000000000  
                    savePrdt.Designation=cd['Designation']
                    savePrdt.Libelle_Ticket=cd['Designation'][0:5]
                    savePrdt.Prix_Untaire=cd['Prix_Untaire']
                    savePrdt.Prix_TTC=cd['Prix_TTC']
                    savePrdt.Prix_HT=(cd['Prix_TTC']*100)/(100+cd['Tva'].Taux)
                    savePrdt.save()
                    savePrdtClr=contenir_clr()
                    savePrdtClr.prdt_id=savePrdt.id
                    savePrdtClr.clr_id=c
                    savePrdtClr.save()
                    savePrdtTaille=contenir_taille()
                    savePrdtTaille.prdt_id=savePrdt.id
                    savePrdtTaille.taille_id=t
                    savePrdtTaille.save()
        else:
            """Import with excel"""
            dataset=Dataset()
            new_prdt=request.FILES['myfile']
            imported_data = dataset.load(new_prdt.read(),format='xlsx')
            for data in imported_data:
                    clr=Couleur.objects.get(code_clr=data[10])
                    tai=Taille.objects.get(code_Taille=data[11])
                    tva=TVA.objects.get(Taux=data[5])
                    value=Produit(
                        data[0],
	        		    data[1],
                        data[2],
	        		    data[3],
                        data[4],
                        tva.id,
                        str(data[1])+"-"+str(data[10])+"-"+str(data[11]),
	        		    data[6],
                        data[7],
                        str(data[7])[0:5],
                        data[8],
                        (data[9]*100)/(100+data[5]),
                        data[9],
                        )
                    value.save()
                    savePrdtClr=contenir_clr()
                    savePrdtClr.prdt_id=value.id
                    savePrdtClr.clr_id=clr.id
                    savePrdtClr.save()
                    savePrdtTaille=contenir_taille()
                    savePrdtTaille.prdt_id=value.id
                    savePrdtTaille.taille_id=tai.id
                    savePrdtTaille.save()
        """End Import with excel"""

        return redirect("produits")

@login_required(login_url='login')
def ProduitDeleteView(request,idp):
    if request.method == 'GET':
        return render(request,"SupprimerProduit.html",{})
    if request.method == 'POST':
        if ligne_recep.objects.filter(prdt_id=idp):
            messages.error(request, 'Impossible de supprimer ce produit, car il existe dans une réception.')
            return  redirect("produits")
        suppPrdtClr=contenir_clr.objects.get(prdt_id=idp)
        suppPrdtClr.delete()
        suppPrdtTaille=contenir_taille.objects.get(prdt_id=idp)
        suppPrdtTaille.delete()
        produit=Produit.objects.get(id=idp)
        produit.delete()
        return  redirect("produits")

""""""""""""""""""""""""
"""Association Magasin Dépot"""
""""""""""""""""""""""""
@login_required(login_url='login')
def Association_Mag_Depot_View(request):
    if request.method == 'GET':
        form=AssociationMagDepotForm()
        return render(request,"AssocierMagasinDépot.html",{'form':form})
    if request.method == 'POST':
        form=AssociationMagDepotForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect("home")

""""""""""""""""""""""""
"""Réception"""
""""""""""""""""""""""""
@login_required(login_url='login')
def ReceptionListView(request):
    receptions=Reception.objects.all()
    return render(request,"ListReceptions.html",{'receptions':receptions})

@login_required(login_url='login')
def ReceptionView(request):
    if request.method == 'GET':
        form=ReceptionForm()
        form2=stockagePrdtDepotForm()
        return render(request,"AddReception.html",{'form':form,'form2':form2})
    if request.method == 'POST':
        form=ReceptionForm(request.POST,request.FILES)
        form2=stockagePrdtDepotForm(request.POST,request.FILES)
        if form.is_valid() and form2.is_valid():
            cd=form.cleaned_data
            cd2=form2.cleaned_data
            saveReception=Reception()
            saveReception.fournisseur=cd['fournisseur']
            saveReception.ref_recep=cd['ref_recep']
            saveReception.date=datetime.datetime.now().date()
            saveReception.depot_id=cd2['depot'].id
            saveReception.save()
            saveLigneRecep=ligne_recep()
            cd=form2.cleaned_data
            saveLigneRecep.prdt=cd['prdt']
            saveLigneRecep.reception_id=saveReception.id
            saveLigneRecep.date=datetime.datetime.now().date()
            saveLigneRecep.qte=cd['qte']
            saveLigneRecep.save()
            depot=Depot.objects.get(id=cd['depot'].id)
            depot.qte=depot.qte+cd['qte']
            depot.save()
            if stockagePrdtDepot.objects.filter(depot_id=depot.id,prdt_id=cd['prdt'].id):
                stockPrdtDepot=stockagePrdtDepot.objects.get(depot_id=depot.id,prdt_id=cd['prdt'].id)
                stockPrdtDepot.qte+=cd['qte']
                stockPrdtDepot.save()
            else:
                form2.save()
        return redirect("receptions")

@login_required(login_url='login')
def ReceptionDetailsView(request,idp):
    if request.method == 'GET':
        recep=Reception.objects.get(id=idp)
        fournisseur=Fournisseur.objects.get(id=recep.fournisseur_id)
        ligneRecep=ligne_recep.objects.get(reception_id=idp)
        prdt=Produit.objects.get(id=ligneRecep.prdt_id)
        contenirClr=contenir_clr.objects.get(prdt_id=prdt.id)
        contenirTaille=contenir_taille.objects.get(prdt_id=prdt.id)
        clr=Couleur.objects.get(id=contenirClr.clr_id)
        taille=Taille.objects.get(id=contenirTaille.taille_id)
        qte=ligneRecep.qte
        total=qte*prdt.Prix_Untaire
        societe=Societe.objects.get(id=1)
        date=recep.date
        pdf = render_to_pdf('Bon_Réception.html',{'recep':recep,'fournisseur':fournisseur,'date':date,
        'prdt':prdt,'clr':clr,'taille':taille,'qte':qte,'total':total,'societe':societe})
        return HttpResponse(pdf, content_type='application/pdf')
        return render(request,"Bon_Réception.html",{'recep':recep,'fournisseur':fournisseur,'date':date,
        'prdt':prdt,'depot':depot,'clr':clr,'taille':taille,'qte':qte,'total':total,'societe':societe})

""""""""""""""""""""""""
"""Livraison"""
""""""""""""""""""""""""

@login_required(login_url='login')
def LivraisonListView(request):
    livraisons=Livraison.objects.all()
    return render(request,"ListLivraisons.html",{'livraisons':livraisons})

@login_required(login_url='login')
def LivraisonTypeView(request,idp):
    if request.method == 'GET':
        checkPrdtExist=bool(False)
        stockPrdtDepot=stockagePrdtDepot.objects.all()
        for s in stockPrdtDepot:
            if s.prdt_id==idp and s.qte>0:
                checkPrdtExist=bool(True)
        if checkPrdtExist:
            return render(request,"LivraisonType.html",{'prdt_id':idp})
        messages.error(request, 'Vous devez recevoir ce produit.')   
        return  redirect("produits")      

"""Livraison vers client"""
@login_required(login_url='login')
def LivraisonCltDepotView(request,idp):
    if request.method == 'GET':
        stockPrdtDepot=stockagePrdtDepot.objects.all()
        listDepots=[]
        for s in stockPrdtDepot:
            if s.prdt_id==idp and s.qte>0:
                listDepots.append(s.depot.Libelle)
                
        return render(request,"ChoisirDepotClt.html",{'listDepots':listDepots}) 
    if request.method == 'POST':
        depotTxt=request.POST.get('selectPrdt')#contient le nom du dépot
        depot=Depot.objects.get(Libelle=depotTxt)
        prdt=Produit.objects.get(id=idp)
        if stockagePrdtDepot.objects.filter(prdt_id=prdt.id):
            ligneStockPrdtDepot=stockagePrdtDepot.objects.get(prdt_id=prdt.id,depot_id=depot.id)
            qte_max=ligneStockPrdtDepot.qte
        else:
            qte_max=0

        return redirect('cltChooseQte',prdt_id=prdt.id,depot_id=depot.id,qte_max=qte_max)
        
@login_required(login_url='login')
def ChooseCltQteView(request,prdt_id,depot_id,qte_max):
    if request.method == 'GET':
        return render(request,"ChoisirQuantiteClt.html",{'qte_max':qte_max})
    if request.method == 'POST':
        qte=request.POST.get('qte')
        return redirect('newLivraisonClt',prdt_id=prdt_id,depot_id=depot_id,qte=qte)

@login_required(login_url='login')
def LivraisonCltAddView(request,prdt_id,depot_id,qte):
    if request.method == 'GET':
        clts=Client.objects.all()
        return render(request,"ChoisirClient.html",{'clts':clts})
    if request.method == 'POST':
        cltNom=request.POST.get('selectClt')
        clt=Client.objects.get(nom=cltNom)
        prdt=Produit.objects.get(id=prdt_id)
        depot=Depot.objects.get(id=depot_id)
        depot.qte=depot.qte-qte
        depot.save()
        saveLivraison=Livraison()
        saveLivraison.ref_Livr='Livraison ' + str(prdt.Nom)
        saveLivraison.depot_id=depot_id
        saveLivraison.date=datetime.datetime.now().date()
        saveLivraison.save()
        saveLigneLivr=ligne_livr()
        saveLigneLivr.livr_id=saveLivraison.id
        saveLigneLivr.prdt_id=prdt_id
        saveLigneLivr.date=datetime.datetime.now().date()
        saveLigneLivr.qte=qte
        saveLigneLivr.save()
        saveReceptClt=reception_clt()
        saveReceptClt.clt_id=clt.id
        saveReceptClt.livr_id=saveLivraison.id
        saveReceptClt.save()
        ligneDepotPrdt=stockagePrdtDepot.objects.get(prdt_id=prdt_id,depot_id=depot_id)
        ligneDepotPrdt.qte=ligneDepotPrdt.qte-qte
        ligneDepotPrdt.save()
        return redirect('produits')

"""Livraison vers magasin"""
@login_required(login_url='login')
def LivraisonMagDepotView(request,idp):
    if request.method == 'GET':
        
        stockPrdtDepot=stockagePrdtDepot.objects.all()
        listDepots=[]
        for s in stockPrdtDepot:
            if s.prdt_id==idp and s.qte>0:
                listDepots.append(s.depot.Libelle)
                
        return render(request,"ChoisirDepotMag.html",{'listDepots':listDepots}) 
       
    if request.method == 'POST':
        depotTxt=request.POST.get('selectPrdt')#contient le nom du dépot
        depot=Depot.objects.get(Libelle=depotTxt)
        prdt=Produit.objects.get(id=idp)
        if stockagePrdtDepot.objects.filter(prdt_id=prdt.id):
            ligneStockPrdtDepot=stockagePrdtDepot.objects.get(prdt_id=prdt.id,depot_id=depot.id)
            qte_max=ligneStockPrdtDepot.qte
        else:
            qte_max=0

        return redirect('magChooseQte',prdt_id=prdt.id,depot_id=depot.id,qte_max=qte_max)

@login_required(login_url='login')
def ChooseMagQteView(request,prdt_id,depot_id,qte_max):
    if request.method == 'GET':
        return render(request,"ChoisirQuantiteMag.html",{'qte_max':qte_max})
    if request.method == 'POST':
        qte=request.POST.get('qte')
        return redirect('newLivraisonMag',prdt_id=prdt_id,depot_id=depot_id,qte=qte)

@login_required(login_url='login')
def LivraisonMagAddView(request,prdt_id,depot_id,qte):
    if request.method == 'GET':
        magDepot=Association_Mag_Depot.objects.all()
        listMagasins=[]
        for item in magDepot:
            if item.depot_id==depot_id:
                listMagasins.append(item.magasin.Libelle)
        return render(request,"ChoisirMagasin.html",{'listMagasins':listMagasins})
    if request.method == 'POST':
        magLibelle=request.POST.get('selectMag')
        magasin=Magasin.objects.get(Libelle=magLibelle)
        magasin.qte=magasin.qte+qte
        magasin.save()
        prdt=Produit.objects.get(id=prdt_id)
        depot=Depot.objects.get(id=depot_id)
        depot.qte=depot.qte-qte
        depot.save()
        saveLivraison=Livraison()
        saveLivraison.ref_Livr='Livraison ' + str(prdt.Nom)
        saveLivraison.depot_id=depot_id
        saveLivraison.date=datetime.datetime.now().date()
        saveLivraison.save()
        saveLigneLivr=ligne_livr()
        saveLigneLivr.livr_id=saveLivraison.id
        saveLigneLivr.prdt_id=prdt_id
        saveLigneLivr.date=datetime.datetime.now().date()
        saveLigneLivr.qte=qte
        saveLigneLivr.save()
        saveReceptMag=reception_magasin()
        saveReceptMag.mag_id=magasin.id
        saveReceptMag.livr_id=saveLivraison.id
        saveReceptMag.save()
        ligneDepotPrdt=stockagePrdtDepot.objects.get(prdt_id=prdt_id,depot_id=depot_id)
        ligneDepotPrdt.qte=ligneDepotPrdt.qte-qte
        ligneDepotPrdt.save()
        return redirect('produits')

@login_required(login_url='login')
def LivraisonMagView(request):
    if request.method == 'GET':
        prdts=ligne_recep.objects.values('prdt').distinct()
        listPrdts=[]
        for prdt in prdts:
            listPrdts.append(prdt["prdt"])
        prdtsCode=[]
        for p in listPrdts:
            prdt=Produit.objects.get(id=p)
            prdtsCode.append(prdt.Code_Produit)
        form=LivraisonForm()
        form2=ligneLivraisonForm()
        form3=receptMagForm()
        return render(request,"AddLivraison.html",{'form':form,'form2':form2,'form3':form3,
        'prdtsCode':prdtsCode})
    if request.method == 'POST':
        form=LivraisonForm(request.POST,request.FILES)
        form2=ligneLivraisonForm(request.POST,request.FILES)
        form3=receptMagForm(request.POST,request.FILES)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            cd=form.cleaned_data
            saveLivraison=Livraison()
            saveLivraison.ref_Livr=cd['ref_Livr']
            saveLivraison.date=datetime.datetime.now().date()
            saveLivraison.save()
            saveLigneLivraison=ligne_livr()
            cd=form2.cleaned_data
            prdtCode=request.POST['prdt']
            prdt=Produit.objects.get(Code_Produit=prdtCode)
            saveLigneLivraison.prdt_id=prdt.id
            saveLigneLivraison.livr_id=saveLivraison.id
            saveLigneLivraison.date=datetime.datetime.now().date()
            saveLigneLivraison.qte=cd['qte']
            saveLigneLivraison.save()
            cd=form3.cleaned_data
            saveRecepMag=reception_magasin()
            saveRecepMag.mag=cd['mag']
            saveRecepMag.livr_id=saveLivraison.id
            saveRecepMag.save()
        return redirect("livraisons")

@login_required(login_url='login')
def LivraisonDetailsView(request,idp):
    if request.method == 'GET':
        TypeLivraison=''
        livr=Livraison.objects.get(id=idp)
        ligneLivr=ligne_livr.objects.get(livr_id=idp)
        prdt=Produit.objects.get(id=ligneLivr.prdt_id)
        if reception_clt.objects.filter(livr_id=idp):
            receptClt=reception_clt.objects.get(livr_id=idp)
            recepteur=Client.objects.get(id=receptClt.clt_id)
            TypeLivraison='Client'
        else:
            recptMag=reception_magasin.objects.get(livr_id=idp)
            recepteur=Magasin.objects.get(id=recptMag.mag_id)
        contenirClr=contenir_clr.objects.get(prdt_id=prdt.id)
        contenirTaille=contenir_taille.objects.get(prdt_id=prdt.id)
        clr=Couleur.objects.get(id=contenirClr.clr_id)
        taille=Taille.objects.get(id=contenirTaille.taille_id)
        qte=ligneLivr.qte
        total=qte*prdt.Prix_Untaire
        societe=Societe.objects.get(id=1)
        date=livr.date
        pdf = render_to_pdf('Bon_Livraison.html',{'livr':livr,'recepteur':recepteur,'date':date,
        'prdt':prdt,'clr':clr,'taille':taille,'qte':qte,'total':total,'societe':societe,
        'TypeLivraison':TypeLivraison})
        return HttpResponse(pdf, content_type='application/pdf')
        return render(request,"Bon_Livraison.html",{'livr':livr,'recepteur':recepteur,'date':date,
        'prdt':prdt,'clr':clr,'taille':taille,'qte':qte,'total':total,'societe':societe,
        'TypeLivraison':TypeLivraison})
        


""""""""""""""""""""""""
"""Export to excel"""
""""""""""""""""""""""""
@login_required(login_url='login')
def ExportCouleursExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Couleurs'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Couleurs')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Nom']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Couleur.objects.values_list('code_clr','nom')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportTaillesExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Tailles'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Tailles')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Nom']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Taille.objects.values_list('code_Taille','nom')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportCollectionsExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Collections'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Collections')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Nom']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Collection.objects.values_list('id','nom')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportFamillesExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Familles'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Familles')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Nom']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    rows=Famille.objects.values_list('id','nom')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportStylesExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Styles'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Styles')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Nom']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Style.objects.values_list('id','nom')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportTVAExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=TVA'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('TVA')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Taux']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=TVA.objects.values_list('id','Taux')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportCategoriesFrExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Catégories des fournisseurs'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Catégories des fournisseurs')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Nom']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Categorie_fr.objects.values_list('id','nom')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportSocietesExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Societes'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Societes')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Raison sociale','ICE','Adresse','Ville','Pays','N° tel',
    'FAX','Email']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Societe.objects.values_list('id','Raison_sociale','Ice','Adresse','Ville',
    'Pays','Tel','Fax','Email')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportDepotsExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Dépots'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Dépots')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Libelle','Quantité en stock']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Depot.objects.values_list('id','Libelle','qte')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportMagasinsExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Magasins'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Magasins')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Libelle','Quantité en stock','Adresse','N° tel','FAX','Email']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Magasin.objects.values_list('id','Libelle','qte','Adresse','Tel','Fax','Email')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportClientsExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Clients'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Clients')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Nom','Adresse','Ville','Pays','N° tel',
    'FAX','Email']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Client.objects.values_list('id','nom','Adresse','Ville',
    'Pays','Tel','Fax','Email')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportFournisseursExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Fournisseurs'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Fournisseurs')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Nom','Raison sociale','Adresse','Ville','Pays','N° tel',
    'FAX','Email','Catégorie','Page d\'accueil']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Fournisseur.objects.values_list('id','Raison_sociale','Adresse','Ville',
    'Pays','Tel','Fax','Email','categorie','page_accueil')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

@login_required(login_url='login')
def ExportProduitsExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Produits'+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Produits')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Code','Nom','Collection','Famille','Style','TVA','Code barre','Designation',
    'Libelle Ticket','Prix unitaire','Prix hors taxes','Prix TTC']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows=Produit.objects.values_list('Code_Produit','Nom','Collection','Famille','Style','Tva',
    'Code_Barre','Designation','Libelle_Ticket','Prix_Untaire','Prix_HT','Prix_TTC')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response