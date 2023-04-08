from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('home/', views.homeView, name='home'),
    #Couleur
    path('couleurs/', views.CouleursListView, name='couleurs'),
    path('couleurs/add', views.CouleurAddView, name='couleurNew'),
    path('couleurs/<int:idp>/update', views.CouleurUpdateView,name="couleurUpdate"),
    path('couleurs/<int:idp>/delete', views.CouleurDeleteView,name="couleurDelete"),
    path('couleurs/export',views.ExportCouleursExcel,name="exportCouleurs"),
    #Taille
    path('tailles/', views.TailleListView, name='tailles'),
    path('tailles/add', views.TailleAddView, name='tailleNew'),
    path('tailles/<int:idp>/update', views.TailleUpdateView,name="tailleUpdate"),
    path('tailles/<int:idp>/delete', views.TailleDeleteView,name="tailleDelete"),
    path('tailles/export',views.ExportTaillesExcel,name="exportTailles"),
    #Collection
    path('collections/', views.CollectionListView, name='collections'),
    path('collections/add', views.CollectionAddView, name='collectionNew'),
    path('collections/<int:idp>/update', views.CollectionUpdateView,name="collectionUpdate"),
    path('collections/<int:idp>/delete', views.CollectionDeleteView,name="collectionDelete"),
    path('collections/export',views.ExportCollectionsExcel,name="exportCollections"),
    #Famille
    path('familles/',views.FamilleListView,name="familles"),
    path('familles/Ajout',views.FamilleAddView,name="newFamille"),
    path('familles/<int:idp>/update', views.FamilleUpdateView,name="familleUpdate"),
    path('familles/<int:idp>/delete', views.FamilleDeleteView,name="familleDelete"),
    path('familles/export',views.ExportFamillesExcel,name="exportFamilles"),
    #Style
    path('styles/',views.StyleListView,name="styles"),
    path('styles/Ajout',views.StyleAddView,name="newStyle"),
    path('styles/<int:idp>/update', views.StyleUpdateView,name="styleUpdate"),
    path('styles/<int:idp>/delete', views.StyleDeleteView,name="styleDelete"),
    path('styles/export',views.ExportStylesExcel,name="exportStyles"),
    #TVA
    path('tvas/',views.TVAListView,name="tvas"),
    path('tvas/Ajout',views.TVAAddView,name="newTVA"),
    path('tvas/<int:idp>/update', views.TVAUpdateView,name="tvaUpdate"),
    path('tvas/<int:idp>/delete', views.TVADeleteView,name="tvaDelete"),
    path('tvas/export',views.ExportTVAExcel,name="exportTVA"),
    #Catégorie_Fr
    path('categories/',views.CategoryListView,name="categories"), 
    path('categories/Ajout',views.CategoryAddView,name="newCategorie"),
    path('categories/<int:idp>/update', views.CategoryUpdateView,name="categorieUpdate"),
    path('categories/<int:idp>/delete', views.CategoryDeleteView,name="categorieDelete"),
    path('categories/export',views.ExportCategoriesFrExcel,name="exportCategories"),
    #Societe
    path('societes/',views.SocieteListView,name="societes"),
    path('societes/Ajout',views.SocieteAddView,name="newSociete"),
    path('societes/<int:idp>/update', views.SocieteUpdateView,name="societeUpdate"),
    path('societes/<int:idp>/delete', views.SocieteDeleteView,name="societeDelete"),
    path('societes/export',views.ExportSocietesExcel,name="exportSocietes"),
    #Depot
    path('depots/',views.DepotListView,name="depots"),
    path('depots/Ajout',views.DepotAddView,name="newDepot"),
    path('depots/<int:idp>/update', views.DepotUpdateView,name="depotUpdate"),
    path('depots/<int:idp>/delete', views.DepotDeleteView,name="depotDelete"),
    path('depots/export',views.ExportDepotsExcel,name="exportDepots"),
    #Magasin
    path('magasins/',views.MagasinListView,name="magasins"),
    path('magasins/Ajout',views.MagasinAddView,name="newMagasin"),
    path('magasins/<int:idp>/update', views.MagasinUpdateView,name="magasinUpdate"),
    path('magasins/<int:idp>/delete', views.MagasinDeleteView,name="magasinDelete"),
    path('magasins/export',views.ExportMagasinsExcel,name="exportMagasins"),
    #Clients
    path('clients/',views.ClientListView,name="clients"),
    path('clients/Ajout',views.ClientAddView,name="newClient"),
    path('clients/<int:idp>/update', views.ClientUpdateView,name="clientUpdate"),
    path('clients/<int:idp>/delete', views.ClientDeleteView,name="clientDelete"),
    path('clients/export',views.ExportClientsExcel,name="exportClients"),
    #Fournisseur
    path('fournisseurs/',views.FournisseurListView,name="fournisseurs"),
    path('fournisseurs/Ajout',views.FournisseurAddView,name="newFournisseur"),
    path('fournisseurs/<int:idp>/update', views.FournisseurUpdateView,name="fournisseurUpdate"),
    path('fournisseurs/<int:idp>/delete', views.FournisseurDeleteView,name="fournisseurDelete"),
    path('fournisseurs/export',views.ExportFournisseursExcel,name="exportFournisseurs"),
    #Produit
    path('produits/',views.ProduitListView,name="produits"),
    path('produits/Ajout',views.ProduitAddView,name="newProduit"),
    path('produits/<int:idp>/delete', views.ProduitDeleteView,name="produitDelete"),
    path('produits/export',views.ExportProduitsExcel,name="exportProduits"),
    #Association magasin avec dépot
    path('association/magasin&depot',views.Association_Mag_Depot_View,name="associationMgasinDepot"),
    #Réception
    path('receptions/',views.ReceptionListView,name="receptions"),
    path('receptions/Ajout',views.ReceptionView,name="newReception"),
    path('reception/<int:idp>/Bon_Reception', views.ReceptionDetailsView,name="recepDetails"),
    #Livraison
    path('livraisons/',views.LivraisonListView,name="livraisons"),
    path('livraisonType/<int:idp>/',views.LivraisonTypeView,name="livraisonType"),

    path('livraisonClt/<int:idp>/',views.LivraisonCltDepotView,name="CltLiv"),
    path('livraisonClt/Qte/<int:prdt_id>/<int:depot_id>/<int:qte_max>/',views.ChooseCltQteView,name="cltChooseQte"),
    path('livraisonClt/<int:prdt_id>/<int:depot_id>/<int:qte>/',views.LivraisonCltAddView,name="newLivraisonClt"),
    
    path('livraisonMag/<int:idp>/',views.LivraisonMagDepotView,name="MagLiv"),
    path('livraisonMag/Qte/<int:prdt_id>/<int:depot_id>/<int:qte_max>/',views.ChooseMagQteView,name="magChooseQte"),
    path('livraisonMag/<int:prdt_id>/<int:depot_id>/<int:qte>/',views.LivraisonMagAddView,name="newLivraisonMag"),
    
    path('livraisons/<int:idp>/Bon_Livraison', views.LivraisonDetailsView,name="livrDetails"),
]
