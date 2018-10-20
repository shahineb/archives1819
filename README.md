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

__1) Comment traduire mathématiquement que la boîte <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png?invert_in_darkmode" align="middle" width="5.663225699999989pt" height="21.68300969999999pt"/> contient
un objet et un seul et que l’objet <img alt="$j$" src="svgs/36b5afebdba34564d884d347484ac0c7.png?invert_in_darkmode" align="middle" width="7.710416999999989pt" height="21.68300969999999pt"/> se trouve dans une boîte et une seule ?__

On note <img alt="$O_{j}\rightarrow B_{i}$" src="svgs/abbcbca79ee28519cba4772bd0a1ad1b.png?invert_in_darkmode" align="middle" width="62.155344899999996pt" height="22.465723500000017pt"/> la relation _"l'objet <img alt="$j$" src="svgs/36b5afebdba34564d884d347484ac0c7.png?invert_in_darkmode" align="middle" width="7.710416999999989pt" height="21.68300969999999pt"/> est dans la boite <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png?invert_in_darkmode" align="middle" width="5.663225699999989pt" height="21.68300969999999pt"/>"_

Alors,


<p align="center"><img alt="$$\forall i\enspace \exists!j\enspace / \enspace O_{j}\rightarrow B_{i} \Leftrightarrow \forall i\; \sum_{j}x_{i,j} = 1$$" src="svgs/4b75f1d5109bc9b1052537c05008abe3.png?invert_in_darkmode" align="middle" width="261.22799999999995pt" height="38.89287435pt"/></p>

Et de même,

<p align="center"><img alt="$$\forall j\enspace \exists!i\enspace / \enspace O_{j}\rightarrow B_{i} \Leftrightarrow \forall j\; \sum_{i}x_{i,j} = 1$$" src="svgs/5568d17bb6b4fabf83a6eb17220e45a4.png?invert_in_darkmode" align="middle" width="263.27519129999996pt" height="36.6554298pt"/></p>


__2) Formulation du PLNE et mise en oeuvre de sa résolution__

Le problème de programmation linéaire en nombre entiers s’écrit :

<p align="center"><img alt="$$ (\mathcal{P}) : \underset{x}{\min}\sum_{i,j}x_{i,j}\|O_{j}-B_{i}\|\quad \text{s.c}\enspace&#10;\begin{matrix}\forall i\; \sum_{j}x_{i,j} = 1\\&#10;\forall j\; \sum_{i}x_{i,j} = 1&#10;\end{matrix}&#10;$$" src="svgs/d21f066eb1078e469bd0272d704de616.png?invert_in_darkmode" align="middle" width="342.44261865pt" height="44.61437145pt"/></p>

_Résultat : 15.3776_

![Problème initial, résultat : 15.3776](docs/img/2_1_2.png)



__3) Objet 1 à gauche directe de l'Objet 2__

On formule cette nouvelle contrainte par :

<p align="center"><img alt="$$\forall i\in [\![2,n-1]\!] \enspace x_{i,1}-x_{i+1,2} = 0$$" src="svgs/23ccc350706539e9f8ec864629d4a395.png?invert_in_darkmode" align="middle" width="227.1147516pt" height="17.031940199999998pt"/></p>

De plus, cette contrainte impose également que la relation <img alt="$O_{1}\rightarrow B_{n}$" src="svgs/f37e1a7b2d67db52f1e7ba2228a7f538.png?invert_in_darkmode" align="middle" width="66.07852514999999pt" height="22.465723500000017pt"/> est impossible car <img alt="$O_{2}$" src="svgs/adae461c37eccd2f2a6ed21ebf2c5d08.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/> ne peut alors être droite de <img alt="$O_{1}$" src="svgs/34d65c1be59469e9f98d95ef3afd2f55.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>.

On impose donc <img alt="$x_{n,1}=0$" src="svgs/08a06d4f7e729d98a29261ba8f2281a2.png?invert_in_darkmode" align="middle" width="58.936417649999996pt" height="21.18721440000001pt"/> (il s'ensuit par les contraintes précédentes que <img alt="$x_{1,2}=0$" src="svgs/56f615e86281fb60ac61e214546a5f0e.png?invert_in_darkmode" align="middle" width="57.36293969999999pt" height="21.18721440000001pt"/>)



_Résultat : 15.5651_

![Objet 1 à gauche directe de l'Objet 2, résultat : 15.5651](docs/img/2_1_3.png)


__4) Objet 3 à droite de l'Objet 4__

Montrons que <img alt="$x_{i,3}+x_{i+k,4}\leq 1,\;\forall i,\;\forall k&gt;0 \Leftrightarrow O_{3}$" src="svgs/a80d286aef460bc0fe5c2b7ad9e21c2c.png?invert_in_darkmode" align="middle" width="249.7805244pt" height="22.831056599999986pt"/> à droite de <img alt="$O_{4}$" src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>

<img alt="$(\Rightarrow)$" src="svgs/1370b00fa8877d46fcf781d09a5e08e2.png?invert_in_darkmode" align="middle" width="29.223836399999986pt" height="24.65753399999998pt"/>
> Raisonnons par l'absurde et supposons <img alt="$O_{3}$" src="svgs/7200108c03e178d4c4466653cdf8f26f.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/> à gauche de <img alt="$O_{4}$" src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>

> Notons <img alt="$i_{3}$" src="svgs/e56b421022e3ffb4d421ce22baaa7e08.png?invert_in_darkmode" align="middle" width="12.21577334999999pt" height="21.68300969999999pt"/> l'indice de la boite contenant <img alt="$O_{3}$" src="svgs/7200108c03e178d4c4466653cdf8f26f.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>.
> Alors, la boite contenant <img alt="$O_{4}$" src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/> étant à droite de <img alt="$B_{i_{3}}$" src="svgs/303897b4e1a47af4defcc51e45779705.png?invert_in_darkmode" align="middle" width="22.71324989999999pt" height="22.465723500000017pt"/>, <img alt="$\exists k&gt;0 \enspace / O_{4}\rightarrow B_{i_{3}+k}$" src="svgs/d9380ada4d24996fad0a79ffb522b516.png?invert_in_darkmode" align="middle" width="151.15945514999999pt" height="24.65753399999998pt"/>

> <img alt="$\Rightarrow x_{i_{3},3} = 1$" src="svgs/2af9cae67bec90a141417e413741bb4c.png?invert_in_darkmode" align="middle" width="82.88139254999999pt" height="21.18721440000001pt"/> et <img alt="$x_{i_{3}+k,4}=1$" src="svgs/5310f005e046b1cc932e914bdaab8c6a.png?invert_in_darkmode" align="middle" width="79.23428535pt" height="21.18721440000001pt"/>

> <img alt="$\Rightarrow x_{i_{3},3} + x_{i_{3}+k,4} &gt; 1$" src="svgs/979c2ffeccd797e76e4376d405cfaa8d.png?invert_in_darkmode" align="middle" width="152.07002909999997pt" height="21.18721440000001pt"/> ce qui est impossible

<img alt="$(\Leftarrow)$" src="svgs/1d461727c14b94ed6121c32c2c8fd5c7.png?invert_in_darkmode" align="middle" width="29.223836399999986pt" height="24.65753399999998pt"/>

> Notons <img alt="$i_{3}$" src="svgs/e56b421022e3ffb4d421ce22baaa7e08.png?invert_in_darkmode" align="middle" width="12.21577334999999pt" height="21.68300969999999pt"/> l'indice de la boite contenant <img alt="$O_{3}$" src="svgs/7200108c03e178d4c4466653cdf8f26f.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>

> Comme <img alt="$O_{4}$" src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/> à gauche de <img alt="$O_{3}$" src="svgs/7200108c03e178d4c4466653cdf8f26f.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>, <img alt="$\forall k&gt;0, \; x_{i_{3}+k,4}=0$" src="svgs/0b94198dcd80a5e4ee0426b480475687.png?invert_in_darkmode" align="middle" width="139.45091819999996pt" height="22.831056599999986pt"/>

> <img alt="$\Rightarrow x_{i_{3},3} + x_{i_{3}+k,4} \leq 1$" src="svgs/5f0a939ed05cd88cfe4c4bb59febb82f.png?invert_in_darkmode" align="middle" width="152.07002909999997pt" height="21.18721440000001pt"/>


On remarque que cette contrainte peut se réécrire de façon plus succinte selon :

<p align="center"><img alt="$$ \forall i\in[\![1,n-1]\!], \; x_{i,3} + \sum_{k=i+1}^{n}x_{k,4} \leq 1$$" src="svgs/8e5c214272cc9c7d618aaed293ccfbf4.png?invert_in_darkmode" align="middle" width="258.1306365pt" height="46.64398859999999pt"/></p>

En effet, pour un <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png?invert_in_darkmode" align="middle" width="5.663225699999989pt" height="21.68300969999999pt"/> donné, si <img alt="$O_{3}\rightarrow B_{i}$" src="svgs/9c70c6238426e1f7d0f018954aa6f96c.png?invert_in_darkmode" align="middle" width="62.60340074999999pt" height="22.465723500000017pt"/> et que <img alt="$O_{3}$" src="svgs/7200108c03e178d4c4466653cdf8f26f.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/> à droite de <img alt="$O_{4}$" src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>, alors toutes les boites d'indice supérieur ne peuvent contenir <img alt="$O_{4}$" src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>, c'est à dire <img alt="$\forall k\in[\![i+1,n]\!], \; x_{k,4}=0$" src="svgs/1d50c001aae1f38d6d717cdd8d6b540b.png?invert_in_darkmode" align="middle" width="172.17931829999998pt" height="24.65753399999998pt"/>.

Cette contrainte englobe également les cas limite :

- Si <img alt="$i=1$" src="svgs/081b3265e50f611c00daeffa91931873.png?invert_in_darkmode" align="middle" width="35.80006649999999pt" height="21.68300969999999pt"/>, <img alt="$O_{4}$" src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/> ne peut être dans <img alt="$B_{1}$" src="svgs/494612520069717fc403261788919db4.png?invert_in_darkmode" align="middle" width="19.021198349999988pt" height="22.465723500000017pt"/> aussi selon les contraintes précédentes et la nouvelle contrainte lui interdit d'être à droite de <img alt="$O_{3}$" src="svgs/7200108c03e178d4c4466653cdf8f26f.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>, c'est donc un cas impossible

- So <img alt="$i=n$" src="svgs/2f7f06a413f6ed1e257667af4a69af85.png?invert_in_darkmode" align="middle" width="37.44773339999999pt" height="21.68300969999999pt"/>, <img alt="$O_{4}$" src="svgs/e6c6c2828933ea424bec1e4cdb4a3f14.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/> ne peut être dans <img alt="$B_{n}$" src="svgs/bf3d4d562192561e15a41a7769787f8f.png?invert_in_darkmode" align="middle" width="20.594674649999988pt" height="22.465723500000017pt"/> aussi selon les contraintes précédentes et est donc nécessairement à gauche de <img alt="$O_{3}$" src="svgs/7200108c03e178d4c4466653cdf8f26f.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>


_Résultat : 15.9014_

![Objet 3 à droite de l'Objet 4, résultat :  15.9014](docs/img/2_1_4.png)



__5) Objet 7 à côté de l'Objet 9__

Il suffit ici de symétriser la contrainte énoncée à la question 3 pour autoriser d'être à droite ou à gauche

<p align="center"><img alt="$$\forall i\in [\![1,n-1]\!] \enspace x_{i,7}-x_{i+1,9} = 0 \quad\text{ou}\quad x_{i+1,7}-x_{i,9} = 0 $$" src="svgs/04a860bfcc203075ad6aa6ac4e7721f9.png?invert_in_darkmode" align="middle" width="394.86397995pt" height="17.031940199999998pt"/></p>

<p align="center"><img alt="$$\Rightarrow \forall i\in [\![1,n-1]\!] \enspace (x_{i,7}-x_{i+1,9})(x_{i+1,7}-x_{i,9}) = 0 $$" src="svgs/649e8b1f3e225f3c0b95d01dc4941580.png?invert_in_darkmode" align="middle" width="361.07409524999997pt" height="17.031940199999998pt"/></p>

Le problème d'optimisation n'est alors plus linéaire.

Une façon de contourner ce problème consiste à résoudre le problème en imposant <img alt="$O_{7}$" src="svgs/75226beeadce388a6c1d10b6cdca2931.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/> à gauche de <img alt="$O_{9}$" src="svgs/e917a22ab6b3c5ab8af20345eaa9235b.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>, puis celui imposant <img alt="$O_{7}$" src="svgs/75226beeadce388a6c1d10b6cdca2931.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/> à droite de <img alt="$O_{9}$" src="svgs/e917a22ab6b3c5ab8af20345eaa9235b.png?invert_in_darkmode" align="middle" width="19.09133654999999pt" height="22.465723500000017pt"/>, et de garder la solution minimisant la distance totale

_Résultat : 15.9048_

![Objet 7 à côté de l'Objet 9, résultat : 15.9048](docs/img/2_1_5.png)


__6) Unicité de la solution__

On remarque que les objets 13 et 14 sont symétriques par rapport à l'axe des abscisses. Donc en principe, échanger leurs attributions mutuelles ne devrait pas impacter la distance.

En imposant la contrainte <img alt="$x_{4,13}=1$" src="svgs/8310d1a1ad983b3e17788169c2dbb3a6.png?invert_in_darkmode" align="middle" width="63.91548239999999pt" height="21.18721440000001pt"/> on retrouve la meme distance que précédemment, il n'y a donc pas unicité de la solution. -->



## 2.2. Communication entre espions

__1) Modélisation du problème et démarche de résolution__

On pose <img alt="$G = [\![1,n]\!]$" src="svgs/49c9a74e46ac8b7e0b5bd5300d312601.png?invert_in_darkmode" align="middle" width="73.01982104999999pt" height="24.65753399999998pt"/> l'ensemble des espions et <img alt="$E=\bigcup_{i\in G}\{(i,s), s\in S_{i}\}$" src="svgs/7efbed337f1c17335e00c00d6f0617cc.png?invert_in_darkmode" align="middle" width="173.81789865pt" height="24.657735299999988pt"/> les voies de communications entre les espions.

L'objectif étant de minimiser la probabilité d'interception, on peut réexprimer le problème comme la maximisation de la probabilité de non-interception.

Notons <img alt="$K_{ij} = \{$" src="svgs/d80ca50b4de8870df29718e3988cbccb.png?invert_in_darkmode" align="middle" width="55.67533454999998pt" height="24.65753399999998pt"/>interception de la commmunication entre <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png?invert_in_darkmode" align="middle" width="5.663225699999989pt" height="21.68300969999999pt"/> et <img alt="$j\}$" src="svgs/d595347ad95e72821ac625f8ec1a3e66.png?invert_in_darkmode" align="middle" width="15.92962799999999pt" height="24.65753399999998pt"/>, alors:


<p align="center"><img alt="$$\underset{E'\subset E}{\max}\mathbb{P}\left(\bigcap_{(i,j)\in E'} \overline{K_{ij}}\right) \Leftrightarrow \underset{E'\subset E}{\max}\prod_{(i,j)\in E'} (1-p_{ij}) \Leftrightarrow \underset{E'\subset E}{\min}\sum_{(i,j)\in E'} -\log(1-p_{ij}) \quad\text{avec } E' \text{ connexe}$$" src="svgs/67750a54fe1e7f426b5c5b9dd496c86f.png?invert_in_darkmode" align="middle" width="672.0232728pt" height="59.1786591pt"/></p>

En pondérant les arrêtes de notre graphe par l'application symétrique <img alt="$w=(i,j)\in E\longmapsto -\log(1-p_{ij})$" src="svgs/fba88a9534f2b7913327a0109cf57334.png?invert_in_darkmode" align="middle" width="234.08480534999995pt" height="24.65753399999998pt"/>, le problème revient alors à résoudre un problème d'arbre recouvrant minimum sur <img alt="$(G,E,w)$" src="svgs/772bbf713526861cc8775bf01d17a7ac.png?invert_in_darkmode" align="middle" width="65.6148669pt" height="24.65753399999998pt"/>,

<p align="center"><img alt="$$ i.e.\quad (\mathcal{P}) : \text{Trouver } (G,E') \enspace\text{  tq  }\enspace \begin{matrix}\sum_{e'\in E'}w(e') \text{ est min}\\&#10;(G,E') \text{ connexe}&#10;\end{matrix}$$" src="svgs/e9377497c7e473e2d0ba1866a0d00b92.png?invert_in_darkmode" align="middle" width="384.05422439999995pt" height="36.1936806pt"/></p>

Des algorithmes polynomiaux de type Kruskal et Prim permettent de résoudre le problème de façon exacte.

__2) Résultat__

![Arbre recouvrant minimum](docs/img/2_2.png)

La probabilité d'interception est donnée par :

<p align="center"><img alt="$$ \mathbb{P}(interception) = 1-\mathbb{P}(\overline{interception}) = \mathbb{P}\left(\bigcap_{(i,j)\in E'} \overline{K_{ij}}\right) = \prod_{(i,j)\in E'}\mathbb{P}(\overline{K_{ij}}) = \prod_{(i,j)\in E'}(1-p_{ij})$$" src="svgs/beb0f8fea72d63441399d09fed289104.png?invert_in_darkmode" align="middle" width="668.0231679pt" height="59.1786591pt"/></p>

Où <img alt="$E'$" src="svgs/7f081d1835e90a8884079517a9963dde.png?invert_in_darkmode" align="middle" width="16.87213934999999pt" height="24.7161288pt"/> est la solution obtenu par l'algorithme de Kruskal

On obtient <img alt="$\mathbb{P}(interception) = 0.5809$" src="svgs/f1b20e5b8fe1bc239dd4c8b4110b9da3.png?invert_in_darkmode" align="middle" width="179.87707484999999pt" height="24.65753399999998pt"/>


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

<p align="center"><img alt="$$ \underset{(a,b)}{\min} : \lambda*p(a,b)+d(a,b) $$" src="svgs/19a546de7fe0ea01ebd49d8be64a2b02.png?invert_in_darkmode" align="middle" width="174.79807125pt" height="26.5753257pt"/></p>

On fait varier <img alt="$\lambda$" src="svgs/fd8be73b54f5436a5cd2e73ba9b6bfa9.png?invert_in_darkmode" align="middle" width="9.58908224999999pt" height="22.831056599999986pt"/> sur un intervalle afin de donner à chaque itération plus de poids à l'une des 2 fonctions que l'on cherche à minimiser et on résout plusieurs fois le problème de minimisation précédent.

On notera que le problème de minimisation sous contraintes se fera en utilisant une méthode de type quasi Newton (SLSQP) dans laquelle on définira des bornes et des contraintes. Aussi, comme les solutions obtenus dépendent de notre point d'initialisation, on définira à chaque itération un x0 différent que l'on générera de manière random.

_Résultat : 2.4975 s_

__Comparaison__ :

Qualité de l'estimation: [Méthode Gloutonne : Très bonne estimation, Méthode Sophistiquée: Bonne estimation]

Nombre d'évaluations des objectifs: [Méthode Gloutonne: 200000, Méthode Sophistiquée: 10000]

Temps d'éxecution: [Méthode Gloutonne améliorée: 13.7s, Méthode Sophistiquée: 2.5s]




## 2.4 Approvisionnement d'un chantier

__1) Modélisation du problème__

Notons <img alt="$\textbf{a}=(a_{t})_{1\leq t\leq N}$" src="svgs/1d46a3ce28e29f73e1777a65b8fe7a18.png?invert_in_darkmode" align="middle" width="102.08186009999997pt" height="24.65753399999998pt"/> et <img alt="$\textbf{r}=(r_{t})_{1\leq t\leq N}$" src="svgs/ff91e8bb12b00da31150cade0965163e.png?invert_in_darkmode" align="middle" width="99.40498424999998pt" height="24.65753399999998pt"/> les vecteurs designant respectivement le nombre de machine à ajouter et retirer au temps <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.png?invert_in_darkmode" align="middle" width="5.936097749999991pt" height="20.221802699999984pt"/>.

Chaque semaine, l'entreprise paye donc <img alt="$a_{t}p^{\text{init}}$" src="svgs/b701859a37d007db10f655e5e551581a.png?invert_in_darkmode" align="middle" width="42.58770779999999pt" height="27.410192700000007pt"/> de frais de mise en service et <img alt="$r_{t}p^{\text{fin}}$" src="svgs/f93fbfd1b8621aeeb7b7d08eb819a74f.png?invert_in_darkmode" align="middle" width="36.17784719999999pt" height="27.91243950000002pt"/> de frais de restitution.

De plus, en prenant la somme sur les semaines passées des ajouts moins les retraits, on obtient le nombre de machines actuellement louées. On en déduit que l'entreprise paye également chaque semaine <img alt="$\left(\sum_{i=0}^{t}a_{i}-r_{i}\right)p^{\text{loc}}$" src="svgs/21e76ce9855c2f91783694b988ab330f.png?invert_in_darkmode" align="middle" width="136.46786174999997pt" height="37.80850590000001pt"/> de frais de location.

On peut ainsi définir une fonction de frais dépensé sur la durée du chantier par :

<p align="center"><img alt="$$J(\textbf{a},\textbf{r}) = \sum_{t=0}^{N}\left[a_{t}p^{\text{init}}+r_{t}p^{\text{fin}}+\sum_{i=0}^{t}(a_{i}-r_{i})p^{\text{loc}}\right]$$" src="svgs/7b0a0fc5641ad9d09c9fcb9e6825adff.png?invert_in_darkmode" align="middle" width="345.1711527pt" height="49.315569599999996pt"/></p>

De plus, on doit vérifier les contraintes suivantes :

- Aucun retour de machine possible la première semaine <img alt="$\Rightarrow r_{1}=0$" src="svgs/ec25bccde6f0320a1d0cf9720df62596.png?invert_in_darkmode" align="middle" width="65.93212229999999pt" height="21.18721440000001pt"/>
- Le nombre de machine louée sur une semaine donnée doit toujours être supérieur au nombre de machines requises <img alt="$\Rightarrow \forall t\in [\![1,N]\!],\enspace \sum_{i=0}^{t}a_{i}-r_{i} \geq d_{t}$" src="svgs/e5d5dccd3b925cf136748c5e9484e3d1.png?invert_in_darkmode" align="middle" width="239.78954835pt" height="30.685221600000023pt"/>
- Tout est rendu et rien n'est ajouté lors de la dernière semaine <img alt="$\Rightarrow \sum_{i=0}^{N}a_{i}-r_{i} = 0$" src="svgs/9811d0c3ff756e6e5d196b51515d355a.png?invert_in_darkmode" align="middle" width="140.49161775pt" height="32.256008400000006pt"/>

Finalement, les vecteurs <img alt="$\textbf{a}$" src="svgs/f3acd3ad07cbb3204b505285686c149b.png?invert_in_darkmode" align="middle" width="9.18943409999999pt" height="14.611878600000017pt"/> et <img alt="$\textbf{r}$" src="svgs/9f9c14b9a3c7d1e583ad84cde97887bc.png?invert_in_darkmode" align="middle" width="7.785368249999991pt" height="14.611878600000017pt"/> étant des vecteurs entiers de <img alt="$\mathbb{N}^{N}$" src="svgs/9c742ea8a8c8fb1678103f67da6c65d9.png?invert_in_darkmode" align="middle" width="23.51834099999999pt" height="27.6567522pt"/>, en notant <img alt="$x = (\textbf{a},\textbf{r})$" src="svgs/669414151348025c7ba90b4fd5de2feb.png?invert_in_darkmode" align="middle" width="68.37871589999999pt" height="24.65753399999998pt"/>, on peut poser le problème comme le problème de programmation linéaire en nombre entier suivant :

<p align="center"><img alt="$$ (\mathcal{P}) : \underset{x\in\mathbb{N}^{2N}}{\min}J(x) \quad \text{s.c}\enspace&#10;\begin{matrix} r_{1}=0 \\&#10;\sum_{i=0}^{t}a_{i}-r_{i} \geq d_{t}\,, \forall t\;\\&#10;\sum_{i=0}^{N}a_{i}-r_{i} = 0&#10;\end{matrix}&#10;$$" src="svgs/78aa7ffa4b5d26be98b80f264a80c04b.png?invert_in_darkmode" align="middle" width="306.6618126pt" height="58.8315387pt"/></p>


__2) Résultat__

_Coût optimal = 3304000_

![Besoin en machine vs stratégie optimale](docs/img/2_4.png)


__3) Commentaires__

On remarque que <img alt="$p^{\text{init}}+p^{\text{fin}} = 10p^{\text{loc}}$" src="svgs/579ccd8502942de5185d66404cda4a84.png?invert_in_darkmode" align="middle" width="135.91898429999998pt" height="27.91243950000002pt"/>. Ainsi, en terme de coût, les 2 process suivants sont équivalents :

<p align="center"><img alt="$$\underbrace{\text{ajout machine}}_{p^{\text{init}}}\longrightarrow\underbrace{\text{location 10 semaines}}_{10p^{\text{loc}}}\longrightarrow\underbrace{\text{restitution}}_{p^{\text{fin}}}$$" src="svgs/3470aae5fe01b247f08086348d29f972.png?invert_in_darkmode" align="middle" width="396.2106555pt" height="40.2993096pt"/></p>

<p align="center"><img alt="$$\underbrace{\text{ajout machine}}_{p^{\text{init}}}\longrightarrow\underbrace{\text{restitution}}_{p^{\text{fin}}}\longrightarrow\underbrace{\text{ajout machine}}_{p^{\text{init}}}\longrightarrow\underbrace{\text{restitution}}_{p^{\text{fin}}}$$" src="svgs/e8a3bc0b904a019379d91c8ab4597b39.png?invert_in_darkmode" align="middle" width="461.4618162pt" height="40.2993096pt"/></p>

On en déduit qu'une stratégie optimale intuitive consiste à ne conserver une machine que si sa durée de location n'excède pas 10 semaines, autrement il est plus intéressant de la restituer pour la relouer après.

Cette stratégie est cohérente avec la stratégie optimale observée entre les semaines 77 et 87 durant lesquelles le nombre de machines louées est supérieur au besoin car il coûterait plus cher de les restituer pour les relouer en vue de la semaine 87
