# Continuous and Discrete Optimization
OMA Labs 2018-2019

### Table of contents:
+ **[1. Optimisation continue et optimisation approchée](#1-partie1)**
+ **[2. Optimisation discrète et optimisation multiobjectif](#2-partie2&3)**


## 1. Optimisation continue et optimisation approchée
### 1.1. Optimisation sans contraintes
#### 1.1.1. Méthode du gradient

__a)__

__b)__

__c)__

#### 1.1.2. Méthode BFGS


### 1.2. Optimisation sous contraintes
#### 1.2.1. Optimisation à l'aide de routines
#### 1.2.2. Optimisation sous contraintes et pénalisation
__1)__

__2)__
#### 1.2.3. Méthodes duales pour l'optimisation sous contraintes
__1)__

__2)__
### 1.3. Optimisation non convexe - Recuit simulé

__a)__

__b)__

__c)__

### 1.4. Application à la synthèse à réponse impulsionnelle infinie

---


## 2. Optimisation discrète et optimisation multiobjectif

### 2.1. Rangement d'objets

__1) Comment traduire mathématiquement que la boîte $i$ contient
un objet et un seul et que l’objet $j$ se trouve dans une boîte et une seule ?__

On note $O_{j}\rightarrow B_{i}$ la relation _"l'objet $j$ est dans la boite $i$"_

Alors,

$$\forall i\enspace \exists!j\enspace / \enspace O_{j}\rightarrow B_{i} \Leftrightarrow \forall i\; \sum_{j}x_{i,j} = 1$$

Et de même,

$$\forall j\enspace \exists!i\enspace / \enspace O_{j}\rightarrow B_{i} \Leftrightarrow \forall j\; \sum_{i}x_{i,j} = 1$$
