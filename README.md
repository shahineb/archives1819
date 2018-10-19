
# Continuous and Discrete Optimization
OMA Labs 2018-2019

### Table of contents:
+ **[1. Optimisation continue et optimisation approchée](#1-partie1)**
+ **[2. Optimisation discrète et optimisation multiobjectif](#2-partie2&3)**


# 1. Optimisation continue et optimisation approchée
## 1.1. Optimisation sans contraintes
### 1.1.1. Méthode du gradient

__a)__

__b)__

__c)__

### 1.1.2. Méthode BFGS


## 1.2. Optimisation sous contraintes
### 1.2.1. Optimisation à l'aide de routines
### 1.2.2. Optimisation sous contraintes et pénalisation

__1)__

__2)__
### 1.2.3. Méthodes duales pour l'optimisation sous contraintes

__1)__

__2)__

## 1.3. Optimisation non convexe - Recuit simulé


__a)__

__b)__

__c)__

## 1.4. Application à la synthèse à réponse impulsionnelle infinie

---


# 2. Optimisation discrète et optimisation multiobjectif

## 2.1. Rangement d'objets

__1) Comment traduire mathématiquement que la boîte <img src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode?" align=middle width=5.642109000000004pt height=21.602129999999985pt/> contient
un objet et un seul et que l’objet <img src="svgs/36b5afebdba34564d884d347484ac0c7.svg?invert_in_darkmode" align=middle width=7.681657500000003pt height=21.602129999999985pt/> se trouve dans une boîte et une seule ?__

On note <img src="svgs/abbcbca79ee28519cba4772bd0a1ad1b.svg?invert_in_darkmode" align=middle width=61.98324pt height=22.381919999999983pt/> la relation _"l'objet <img src="svgs/36b5afebdba34564d884d347484ac0c7.svg?invert_in_darkmode" align=middle width=7.681657500000003pt height=21.602129999999985pt/> est dans la boite <img src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109000000004pt height=21.602129999999985pt/>"_

Alors,


<p align="center"><img src="svgs/4b75f1d5109bc9b1052537c05008abe3.svg?invert_in_darkmode" align=middle width=260.6802pt height=38.878454999999995pt/></p>

Et de même,

<p align="center"><img src="svgs/5568d17bb6b4fabf83a6eb17220e45a4.svg?invert_in_darkmode" align=middle width=262.7229pt height=36.649305pt/></p>


__2) Formulation du PLNE et mise en oeuvre de sa résolution__

Le problème de programmation linéaire en nombre entiers s’écrit :

<p align="center"><img src="svgs/d21f066eb1078e469bd0272d704de616.svg?invert_in_darkmode" align=middle width=341.92455pt height=44.605934999999995pt/></p>

_Résultat : 15.3776_

![Problème initial, résultat : 15.3776](docs/img/2_1_2.png)



__3) Objet 1 à gauche directe de l'Objet 2__

On formule cette nouvelle contrainte par :

<p align="center"><img src="svgs/23ccc350706539e9f8ec864629d4a395.svg?invert_in_darkmode" align=middle width=226.5912pt height=16.97751pt/></p>

De plus, cette contrainte impose également que la relation <img src="svgs/f37e1a7b2d67db52f1e7ba2228a7f538.svg?invert_in_darkmode" align=middle width=65.89341pt height=22.381919999999983pt/> est impossible car <img src="svgs/adae461c37eccd2f2a6ed21ebf2c5d08.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/> ne peut alors être droite de <img src="svgs/34d65c1be59469e9f98d95ef3afd2f55.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>.

On impose donc <img src="svgs/08a06d4f7e729d98a29261ba8f2281a2.svg?invert_in_darkmode" align=middle width=58.82283pt height=21.10812pt/> (il s'ensuit par les contraintes précédentes que <img src="svgs/56f615e86281fb60ac61e214546a5f0e.svg?invert_in_darkmode" align=middle width=57.249390000000005pt height=21.10812pt/>)



_Résultat : 15.5651_

![Objet 1 à gauche directe de l'Objet 2, résultat : 15.5651](docs/img/2_1_3.png)


__4) Objet 3 à droite de l'Objet 4__

Montrons que <img src="svgs/a80d286aef460bc0fe5c2b7ad9e21c2c.svg?invert_in_darkmode" align=middle width=249.21814499999996pt height=22.745910000000016pt/> à droite de <img src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>

<img src="svgs/1370b00fa8877d46fcf781d09a5e08e2.svg?invert_in_darkmode" align=middle width=29.114745000000003pt height=24.56552999999997pt/>
> Raisonnons par l'absurde et supposons <img src="svgs/7200108c03e178d4c4466653cdf8f26f.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/> à gauche de <img src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>

> Notons <img src="svgs/e56b421022e3ffb4d421ce22baaa7e08.svg?invert_in_darkmode" align=middle width=12.170235000000002pt height=21.602129999999985pt/> l'indice de la boite contenant <img src="svgs/7200108c03e178d4c4466653cdf8f26f.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>.
> Alors, la boite contenant <img src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/> étant à droite de <img src="svgs/303897b4e1a47af4defcc51e45779705.svg?invert_in_darkmode" align=middle width=22.62843pt height=22.381919999999983pt/>, <img src="svgs/d9380ada4d24996fad0a79ffb522b516.svg?invert_in_darkmode" align=middle width=150.74713500000001pt height=24.56552999999997pt/>

> <img src="svgs/2af9cae67bec90a141417e413741bb4c.svg?invert_in_darkmode" align=middle width=82.706415pt height=21.10812pt/> et <img src="svgs/5310f005e046b1cc932e914bdaab8c6a.svg?invert_in_darkmode" align=middle width=79.1208pt height=21.10812pt/>

> <img src="svgs/979c2ffeccd797e76e4376d405cfaa8d.svg?invert_in_darkmode" align=middle width=151.81221pt height=21.10812pt/> ce qui est impossible

<img src="svgs/1d461727c14b94ed6121c32c2c8fd5c7.svg?invert_in_darkmode" align=middle width=29.114745000000003pt height=24.56552999999997pt/>

> Notons <img src="svgs/e56b421022e3ffb4d421ce22baaa7e08.svg?invert_in_darkmode" align=middle width=12.170235000000002pt height=21.602129999999985pt/> l'indice de la boite contenant <img src="svgs/7200108c03e178d4c4466653cdf8f26f.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>

> Comme <img src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/> à gauche de <img src="svgs/7200108c03e178d4c4466653cdf8f26f.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>, <img src="svgs/0b94198dcd80a5e4ee0426b480475687.svg?invert_in_darkmode" align=middle width=139.17585pt height=22.745910000000016pt/>

> <img src="svgs/5f0a939ed05cd88cfe4c4bb59febb82f.svg?invert_in_darkmode" align=middle width=151.81221pt height=21.10812pt/>


On remarque que cette contrainte peut se réécrire de façon plus succinte selon :

<p align="center"><img src="svgs/8e5c214272cc9c7d618aaed293ccfbf4.svg?invert_in_darkmode" align=middle width=257.58975pt height=46.620419999999996pt/></p>

En effet, pour un <img src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109000000004pt height=21.602129999999985pt/> donné, si <img src="svgs/9c70c6238426e1f7d0f018954aa6f96c.svg?invert_in_darkmode" align=middle width=62.431214999999995pt height=22.381919999999983pt/> et que <img src="svgs/7200108c03e178d4c4466653cdf8f26f.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/> à droite de <img src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>, alors toutes les boites d'indice supérieur ne peuvent contenir <img src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>, c'est à dire <img src="svgs/1d50c001aae1f38d6d717cdd8d6b540b.svg?invert_in_darkmode" align=middle width=171.719295pt height=24.56552999999997pt/>.

Cette contrainte englobe également les cas limite :

- Si <img src="svgs/081b3265e50f611c00daeffa91931873.svg?invert_in_darkmode" align=middle width=35.700555pt height=21.602129999999985pt/>, <img src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/> ne peut être dans <img src="svgs/494612520069717fc403261788919db4.svg?invert_in_darkmode" align=middle width=18.950250000000004pt height=22.381919999999983pt/> aussi selon les contraintes précédentes et la nouvelle contrainte lui interdit d'être à droite de <img src="svgs/7200108c03e178d4c4466653cdf8f26f.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>, c'est donc un cas impossible

- So <img src="svgs/2f7f06a413f6ed1e257667af4a69af85.svg?invert_in_darkmode" align=middle width=37.341975000000005pt height=21.602129999999985pt/>, <img src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/> ne peut être dans <img src="svgs/bf3d4d562192561e15a41a7769787f8f.svg?invert_in_darkmode" align=middle width=20.517750000000003pt height=22.381919999999983pt/> aussi selon les contraintes précédentes et est donc nécessairement à gauche de <img src="svgs/7200108c03e178d4c4466653cdf8f26f.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>


_Résultat : 15.9014_

![Objet 3 à droite de l'Objet 4, résultat :  15.9014](docs/img/2_1_4.png)



__5) Objet 7 à côté de l'Objet 9__

Il suffit ici de symétriser la contrainte énoncée à la question 3 pour autoriser d'être à droite ou à gauche

<p align="center"><img src="svgs/04a860bfcc203075ad6aa6ac4e7721f9.svg?invert_in_darkmode" align=middle width=394.14374999999995pt height=16.97751pt/></p>

<p align="center"><img src="svgs/649e8b1f3e225f3c0b95d01dc4941580.svg?invert_in_darkmode" align=middle width=360.27585pt height=16.97751pt/></p>

Le problème d'optimisation n'est alors plus linéaire.

Une façon de contourner ce problème consiste à résoudre le problème en imposant <img src="svgs/75226beeadce388a6c1d10b6cdca2931.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/> à gauche de <img src="svgs/e917a22ab6b3c5ab8af20345eaa9235b.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>, puis celui imposant <img src="svgs/75226beeadce388a6c1d10b6cdca2931.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/> à droite de <img src="svgs/e917a22ab6b3c5ab8af20345eaa9235b.svg?invert_in_darkmode" align=middle width=19.020045pt height=22.381919999999983pt/>, et de garder la solution minimisant la distance totale

_Résultat : 15.9048_

![Objet 7 à côté de l'Objet 9, résultat : 15.9048](docs/img/2_1_5.png)


__6) Unicité de la solution__

On remarque que les objets 13 et 14 sont symétriques par rapport à l'axe des abscisses. Donc en principe, échanger leurs attributions mutuelles ne devrait pas impacter la distance.

En imposant la contrainte <img src="svgs/8310d1a1ad983b3e17788169c2dbb3a6.svg?invert_in_darkmode" align=middle width=63.802035000000004pt height=21.10812pt/> on retrouve la meme distance que précédemment, il n'y a donc pas unicité de la solution. -->



## 2.2. Communication entre espions

__1) Modélisation du problème et démarche de résolution__

On pose <img src="svgs/49c9a74e46ac8b7e0b5bd5300d312601.svg?invert_in_darkmode" align=middle width=72.77094pt height=24.56552999999997pt/> l'ensemble des espions et <img src="svgs/7efbed337f1c17335e00c00d6f0617cc.svg?invert_in_darkmode" align=middle width=173.423745pt height=24.65792999999999pt/> les voies de communications entre les espions.

L'objectif étant de minimiser la probabilité d'interception, on peut réexprimer le problème comme la maximisation de la probabilité de non-interception.

Notons <img src="svgs/d80ca50b4de8870df29718e3988cbccb.svg?invert_in_darkmode" align=middle width=55.544774999999994pt height=24.56552999999997pt/>interception de la commmunication entre <img src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109000000004pt height=21.602129999999985pt/> et <img src="svgs/d595347ad95e72821ac625f8ec1a3e66.svg?invert_in_darkmode" align=middle width=15.873660000000003pt height=24.56552999999997pt/>, alors:


<p align="center"><img src="svgs/67750a54fe1e7f426b5c5b9dd496c86f.svg?invert_in_darkmode" align=middle width=671.2431pt height=59.068185pt/></p>

En pondérant les arrêtes de notre graphe par l'application symétrique <img src="svgs/fba88a9534f2b7913327a0109cf57334.svg?invert_in_darkmode" align=middle width=233.52994499999997pt height=24.56552999999997pt/>, le problème revient alors à résoudre un problème d'arbre recouvrant minimum sur <img src="svgs/772bbf713526861cc8775bf01d17a7ac.svg?invert_in_darkmode" align=middle width=65.39544pt height=24.56552999999997pt/>,

<p align="center"><img src="svgs/e9377497c7e473e2d0ba1866a0d00b92.svg?invert_in_darkmode" align=middle width=383.40554999999995pt height=36.154469999999996pt/></p>

Des algorithmes polynomiaux de type Kruskal et Prim permettent de résoudre le problème de façon exacte.

__2) Résultat__

![Arbre recouvrant minimum](docs/img/2_2.png)

La probabilité d'interception est donnée par :

<p align="center"><img src="svgs/beb0f8fea72d63441399d09fed289104.svg?invert_in_darkmode" align=middle width=666.97125pt height=59.068185pt/></p>

Où <img src="svgs/7f081d1835e90a8884079517a9963dde.svg?invert_in_darkmode" align=middle width=16.812675000000002pt height=24.668490000000013pt/> est la solution obtenu par l'algorithme de Kruskal

On obtient <img src="svgs/f1b20e5b8fe1bc239dd4c8b4110b9da3.svg?invert_in_darkmode" align=middle width=179.24164499999998pt height=24.56552999999997pt/>


## 2.3 Dimensionnement d'une poutre

__1) Méthode gloutonne__

Dans ce problème, il sera question d'optimisation multi-objectif puisque l'on cherche à minimiser à la fois le poids et la deflexion de la poutre sous certaines contraintes.

Les fonctions qui donnent le poids et la deflexion de la poutre, étant faciles à évaluer, nous pouvons utiliser la méthode gloutonne (gourmande) dans laquelle il sera question de générer 100000 points qui réalisent les contraintes physiques imposées et de tracer un front de Pareto.

La recherche des points Pareto Optimales se fait en 2 étapes:

- Pour chaque point généré, on stocke sous forme de liste l'ensemble des points situés en bas et à gauche de lui (ayant un poids et une deflexion inférieurs à lui)

- Si cette liste est vide, alors ce point est pareto-optimal. Dans le cas contraire, ce point n'est pas retenu

_Résultat : 13.7482 s_

![Front de pareto méthode gloutonne](docs/img/2_3.png)


__2) Méthode plus sophistiquée__

On transforme ici notre problème en problème mono-objectif:

<p align="center"><img src="svgs/19a546de7fe0ea01ebd49d8be64a2b02.svg?invert_in_darkmode" align=middle width=174.35715pt height=26.518469999999997pt/></p>

On fait varier <img src="svgs/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode" align=middle width=9.553335pt height=22.745910000000016pt/> sur un intervalle afin de donner à chaque itération plus de poids à l'une des 2 fonctions que l'on cherche à minimiser et on résout plusieurs fois le problème de minimisation précédent.

On notera que le problème de minimisation sous contraintes se fera en utilisant une méthode de type quasi Newton (SLSQP) dans laquelle on définira des bornes et des contraintes. Aussi, comme les solutions obtenus dépendent de notre point d'initialisation, on définira à chaque itération un x0 différent que l'on générera de manière random.

_Résultat : 2.4975 s_

__Comparaison__ :

Qualité de l'estimation: [Méthode Gloutonne : Très bonne estimation, Méthode Sophistiquée: Bonne estimation]

Nombre d'évaluations des objectifs: [Méthode Gloutonne: 200000, Méthode Sophistiquée: 10000]

Temps d'éxecution: [Méthode Gloutonne améliorée: 13.7s, Méthode Sophistiquée: 2.5s]




## 2.4 Approvisionnement d'un chantier

__1) Modélisation du problème__

Notons <img src="svgs/1d46a3ce28e29f73e1777a65b8fe7a18.svg?invert_in_darkmode" align=middle width=101.790645pt height=24.56552999999997pt/> et <img src="svgs/ff91e8bb12b00da31150cade0965163e.svg?invert_in_darkmode" align=middle width=99.11846999999999pt height=24.56552999999997pt/> les vecteurs designant respectivement le nombre de machine à ajouter et retirer au temps <img src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg?invert_in_darkmode" align=middle width=5.9139630000000025pt height=20.14650000000001pt/>.

Chaque semaine, l'entreprise paye donc <img src="svgs/b701859a37d007db10f655e5e551581a.svg?invert_in_darkmode" align=middle width=42.450210000000006pt height=27.352380000000007pt/> de frais de mise en service et <img src="svgs/f93fbfd1b8621aeeb7b7d08eb819a74f.svg?invert_in_darkmode" align=middle width=36.06438pt height=27.852989999999977pt/> de frais de restitution.

De plus, en prenant la somme sur les semaines passées des ajouts moins les retraits, on obtient le nombre de machines actuellement louées. On en déduit que l'entreprise paye également chaque semaine <img src="svgs/21e76ce9855c2f91783694b988ab330f.svg?invert_in_darkmode" align=middle width=136.37679pt height=37.803480000000015pt/> de frais de location.

On peut ainsi définir une fonction de frais dépensé sur la durée du chantier par :

<p align="center"><img src="svgs/7b0a0fc5641ad9d09c9fcb9e6825adff.svg?invert_in_darkmode" align=middle width=344.58435pt height=49.131389999999996pt/></p>

De plus, on doit vérifier les contraintes suivantes :

- Aucun retour de machine possible la première semaine <img src="svgs/ec25bccde6f0320a1d0cf9720df62596.svg?invert_in_darkmode" align=middle width=65.764545pt height=21.10812pt/>
- Le nombre de machine louée sur une semaine donnée doit toujours être supérieur au nombre de machines requises <img src="svgs/e5d5dccd3b925cf136748c5e9484e3d1.svg?invert_in_darkmode" align=middle width=239.24224499999997pt height=30.632580000000004pt/>
- Tout est rendu et rien n'est ajouté lors de la dernière semaine <img src="svgs/9811d0c3ff756e6e5d196b51515d355a.svg?invert_in_darkmode" align=middle width=140.243895pt height=32.19743999999999pt/>

Finalement, les vecteurs <img src="svgs/f3acd3ad07cbb3204b505285686c149b.svg?invert_in_darkmode" align=middle width=9.155190000000003pt height=14.55728999999999pt/> et <img src="svgs/9f9c14b9a3c7d1e583ad84cde97887bc.svg?invert_in_darkmode" align=middle width=7.756336500000003pt height=14.55728999999999pt/> étant des vecteurs entiers de <img src="svgs/9c742ea8a8c8fb1678103f67da6c65d9.svg?invert_in_darkmode" align=middle width=23.430495pt height=27.598230000000008pt/>, en notant <img src="svgs/669414151348025c7ba90b4fd5de2feb.svg?invert_in_darkmode" align=middle width=68.23113000000001pt height=24.56552999999997pt/>, on peut poser le problème comme le problème de programmation linéaire en nombre entier suivant :

<p align="center"><img src="svgs/78aa7ffa4b5d26be98b80f264a80c04b.svg?invert_in_darkmode" align=middle width=306.17565pt height=58.791975pt/></p>


__2) Résultat__

_Coût optimal = 3304000_

![Besoin en machine vs stratégie optimale](docs/img/2_4.png)


__3) Commentaires__

On remarque que <img src="svgs/579ccd8502942de5185d66404cda4a84.svg?invert_in_darkmode" align=middle width=135.60921pt height=27.852989999999977pt/>. Ainsi, en terme de coût, les 2 process suivants sont équivalents :

<p align="center"><img src="svgs/3470aae5fe01b247f08086348d29f972.svg?invert_in_darkmode" align=middle width=395.97689999999994pt height=40.248285pt/></p>

<p align="center"><img src="svgs/e8a3bc0b904a019379d91c8ab4597b39.svg?invert_in_darkmode" align=middle width=461.16675pt height=40.248285pt/></p>

On en déduit qu'une stratégie optimale intuitive consiste à ne conserver une machine que si sa durée de location n'excède pas 10 semaines, autrement il est plus intéressant de la restituer pour la relouer après.

Cette stratégie est cohérente avec la stratégie optimale observée entre les semaines 77 et 87 durant lesquelles le nombre de machines louées est supérieur au besoin car il coûterait plus cher de les restituer pour les relouer en vue de la semaine 87
