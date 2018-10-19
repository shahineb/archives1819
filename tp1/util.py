import numpy as np

import time

from scipy.optimize import minimize

A_up = np.hstack([np.diag([1]*5), np.zeros((5,5))])

A_down = np.hstack([np.zeros((5,5)), np.diag([-1]*5)])

A = np.concatenate([A_up, A_down])

b = np.concatenate([np.zeros(5), np.ones(5)])


# Definition des constante A, B et S

def definition_constantes():

    B = np.matrix('-1.0; 2.0; -3.5; 1.2; 1.5')

    A = np.matrix([[ 1.0, -1.0, 2.0, -0.9, 2.1],

                   [ 1.25, 2.0, 0.5, 1.2, -0.5],

                   [ -3.0, 2.3, 0.5, 1.3, -2.5],

                   [ -2.2, 2.3, 1.5, 0.5, 1.45],

                   [ -1.2, 3.0, -0.5, 0.75, -1.5]])



    S = A*np.transpose(A)

    return A, B, S



def f1(U,B,S):

    n=U.shape[0]

    U=np.matrix(U)

    U.shape=(n,1)

    fU = np.transpose(U) * S * U - np.transpose(B) * U;

    return float(fU)





def df1(U,B,S):

    n=U.shape[0]

    U=np.matrix(U)

    U.shape=(n,1)

    dfU = 2 * S * U - B

    dfU = np.array(dfU)

    dfU.shape=(n,)

    return dfU





def f2(U,S):

    n=U.shape[0]

    U=np.matrix(U)

    U.shape=(n,1)

    fU = np.transpose(U) * S * U + np.transpose(U) * np.exp(U);

    return float(fU)





def df2(U,S):

    foo = 2*np.matmul(S,U)

    bar = np.exp(U) + np.array(U)*np.exp(U)

    output = foo + bar

    return output





def L1_U(U, B, S, lambda_):

    fU = f1(U,B,S)

    n = U.shape[0]

    U_2 = np.concatenate([U,U])

    gU = np.matmul(A, U_2) + b

    return f1(U,B,S) + np.inner(lambda_, gU)



def dL1_U(U, B, S, lambda_):

    n = U.shape[0]

    U_2 = np.concatenate([U,U])

    gU = np.matmul(A, U_2) + b

    return gU



def L1_lambda(lambda_, B, S, U):

    fU = f1(U,B,S)

    n = U.shape[0]

    U_2 = np.concatenate([U,U])

    gU = np.matmul(A, U_2) + b

    return f1(U,B,S) + np.inner(lambda_, gU)



def dL1_lambda(lambda_, B, S, U):

    n = U.shape[0]

    U_2 = np.concatenate([U,U])

    gU = np.matmul(A, U_2) + b

    return gU


def gradient_rho_constant(fun, fun_der, U0, rho, tol,args):

# Fonction permettant de minimiser la fonction f(U) par rapport au vecteur U

# Méthode : gradient à pas fixe

# INPUTS :

# - han_f   : handle vers la fonction à minimiser

# - han_df  : handle vers le gradient de la fonction à minimiser

# - U0      : vecteur initial

# - rho     : paramètre gérant l'amplitude des déplacement

# - tol     : tolérance pour définir le critère d'arrêt

# OUTPUT :

# - GradResults : structure décrivant la solution





    itermax=10000  # nombre maximal d'itérations

    xn=U0

    f=fun(xn,*args) # point initial de l'algorithme

    it=0         # compteur pour les itérations

    f_calls=0    # compteur pour les appels a la fonction de cout

    converged = False;



    while (~converged & (it < itermax)):

        it=it+1

        dfx=fun_der(xn,*args)       # valeur courante de la fonction à minimiser

        xnp1=xn-rho*dfx             # nouveau point courant (x_{n+1})

        fnp1=fun(xnp1,*args)

        f_calls += 1

        if abs(fnp1-f)<tol:

            converged = True

        xn=xnp1; f=fnp1;           # xnp1 : nouveau point courant



    GradResults = {

            'initial_x':U0,

            'minimum':xnp1,

            'f_minimum':fnp1,

            'iterations':it,

            'converged':converged,

            'calls':f_calls

            }

    return GradResults


def gradient_rho_adaptatif(fun, fun_der, U0, rho, tol,args):

# Fonction permettant de minimiser la fonction f(U) par rapport au vecteur U

# Méthode : gradient à pas fixe

# INPUTS :

# - han_f   : handle vers la fonction à minimiser

# - han_df  : handle vers le gradient de la fonction à minimiser

# - U0      : vecteur initial

# - rho     : valeur initiale du paramètre gérant l'amplitude des déplacement

# - tol     : tolérance pour définir le critère d'arrêt

# OUTPUT :

# - GradResults : structure décrivant la solution





    itermax=10000  # nombre maximal d'itérations

    xn=U0

    f=fun(xn,*args) # point initial de l'algorithme

    it=0         # compteur pour les itérations

    f_calls=0    # compteur pour les appels a la fonction de cout

    converged = False;



    while (~converged & (it < itermax)):

        it=it+1

        dfx=fun_der(xn,*args)       # valeur courante de la fonction à minimiser

        xnp1=xn-rho*dfx             # nouveau point courant (x_{n+1})

        fnp1=fun(xnp1,*args)

        f_calls += 1

        if fnp1 < f :
            
            if abs(fnp1-f)<tol:
                converged = True
                
            xn, f = xnp1, fnp1
            rho *= 2
        else :
            rho /= 2


    GradResults = {

            'initial_x':U0,

            'minimum':xnp1,

            'f_minimum':fnp1,

            'iterations':it,

            'converged':converged,

            'calls':f_calls
        
            }

    return GradResults


def beta_1(X):

    z = np.sum(np.maximum(X-1, 0)**2 + (np.maximum(-X,0))**2)

    return z


def f1penal(U,B,S,epsilon):

    z=f1(U,B,S)+beta_1(U)/epsilon

    return float(z)


def f2penal(U,S,epsilon):

    output = f2(U,S) + beta_1(U)/epsilon

    return output

def projection(X):

    # projection de X sur R+^n

    proj_X = np.maximum(X,0)

    return proj_X

def H0(nu):

    if nu >=0 and nu<=0.1:

        return 1

    elif nu>=0.15 and nu<=0.5:

        return 0

    else:

        return None



def H(nu, h, n):

    cos_vec = np.cos(2*np.pi*nu*np.arange(n))

    H_nu = np.inner(h, cos_vec)

    return H_nu



def J(h, nu_1_p, n):

    delta_max = 0

    for nuj in nu_1_p:

        H_nu = H(nuj, h, n)

        delta_max = max(delta_max, np.abs(H_nu-H0(nuj)))

    return delta_max


def uzawa(fun, gradient_L, x0,lambda_0, rho, tol):

    itermax=10000  # nombre maximal d'itérations

    xnm1=x0

    lambda_n=lambda_0
    
    it=0         # compteur pour les itérations

    f_calls=0    # compteur pour les appels a la fonction de cout

    converged = False;

    while (~converged & (it < itermax)):

        it=it+1

        problem=minimize(fun=L1_U,x0=x0,args=(B,S,lambda_n),method='BFGS',tol=1e-6)
        
        xn=problem['x']

        f_calls += problem['nfev']
        
        if abs(f1(xn,B,S)-f1(xnm1,B,S))<tol:

            converged = True

        else:
            grad=gradient_L(xn)
            lambda_np1=projection(lambda_n+rho_0*grad)
            lambda_n=lambda_np1 
            xnm1=xn

    GradResults = {

            'initial_x':x0,

            'minimum':xn,

            'iterations':it,

            'converged':converged,

            'calls':f_calls,
        
            'fmin': f1(xn,B,S)

            }

    return GradResults
