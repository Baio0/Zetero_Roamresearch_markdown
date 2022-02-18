- Author: [[Yikun Bai]]
- Date Finished [[February 17th, 2022]]
- Related Reference: 
    - [[Ref. Villani2003Topics]]
    - [[Ref. Villani2009Optimal]]
    - [[Ref. Thorpe2018Introduction]]
- Optimal transport studies the most cost effective way to move mass from one place to another place with pre described shapes. 
![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FResearch_Collection%2Fe7YN95Hvqw.png?alt=media&token=25e767d8-bf24-4e86-95d0-1d7fa6610bf9)
- To define an OT problem, we need the following concepts: 
    - $$X,Y$$ are two sets, in most of the literatures, they are assumed to be [[Polish Space]]s (e.g. $$\mathbb{R}^n$$). 
(Rigorously, the original OT only needs the sets to be measurable spaces. But to discuss some related concepts, ([[Wasserstein distance]], [[Kantorovich Duality Theorem]], etc), we need the space to be a Polish space). 
    - Cost function $$c: X\times Y\to \mathbb{R}$$ tells how much it costs to transport one unit of mass from location $$x$$ to location $$y$$. It is natural to assume $$c\ge 0$$ and is measurable.
    - Finite radon Measures $$\mu\in \mathcal{P}(X),\nu\in \mathcal{P}(Y)$$ describe the pre-described shapes. The two measures should have same total mass (transportation do not create/destroy mass). In generally, they are normalized to be two probability measures. 
    - Transference plan $$\pi$$ is a coupling of $$(\mu,\nu)$$, denoted as $$\pi\in\Pi(X\times Y)$$, which means $$\pi$$ satisfies the following equivalent statements  
        - $$\int_Y d\pi(x,y)=d\mu(x), \forall x$$ and $$\int_X d\pi(x,y)=d\nu(y), \forall y$$ 
        - $$\pi(A\times Y)=\mu(A),\pi(X\times B)=\nu(B)$$ for all measurable set $$A,B$  (It's a more rigorously statement)
        - $$\int_{X\times Y}[\phi(x)+\psi(y)]d\pi(x,y)=\int_X \phi(x)d\mu(x)+\int_Y\psi (y)d\nu(y)$$ for all functions $$\phi,\psi$$ in a suitable class, for example, in $$L^1(d\mu)\times L^1(d\nu)$$, or equivalently $$L^\infty(d\mu)\times L^\infty(d\nu)$$. 
        - If $$(X,Y)\sim \pi$$, then $$\text{Law}(X)=\mu, \text{Law}(Y)=\nu$$.
- [[Kantorovich's optimal transportation problem]]: 
$$\min_{\pi\in\Pi(\mu,\nu)} I(\pi):=\int_{X\times Y}c(x,y)d\pi(x,y)$$

- [[Monge problem]] 
$$\min_T I(T)=\int_X c(x,T(x))d\mu(x)=\mathbb{E}[c(U,T(U))]$$ such that $$\text{Law}(U)=\mu,\text{Law}(V)=\nu$$. 
    - Monge's problem requires that no mass be split. (Each x should be associated a unit destination $$y$$.
    - One can write Monge's problem in the style of Kantorovich's formulation by assuming
$$d\pi(x,y)=d\pi_T(x,y):=d\mu(x)\delta[y=T(x)]$$ for some mapping $$T$$. 
        - Sometime $$\pi_T$$ is called the coupling induced by $$T$$. 
        - When $$c$$ is a measurable function, we can write  
$$\int_{X\times Y}c(x,y)d\pi_T(x,y)=\int_Xc(x,T(x))d\mu(x)$$. 
- What is the condition $$T$$ should satisfy such that $$\pi_T\in\Pi(\mu,\nu)$$? It induces a concept called [[pushforward measure]]
We say $$\nu$$ is the [[pushforward measure]] or image measure of $$\mu$$ under $$T$$, (or we say $$T$$ transports $$\mu$$ onto $$\nu$$), denoted as $$\nu=T_\# \mu$$, if the following equivalent statements hold: 
    - $$\nu(B)=\mu[T^{-1}(B)]$$ for all measurable set $$B\subset Y$$. 
    - $$\int_X \psi\circ Td\mu=\int_Y d\nu$$ for all $$\psi \in L^1(d\nu)$$ or equivalently all positive $$\psi$$, or equivalently, all $$\psi \in L^\infty(d\nu)$$.
    - let $$X$$ be a realization of $$\mu$$, (i.e. $$X\sim \mu$$), then $$T(X)\sim \nu$$. 
    - Say $$\mu$$ admits a density, i.e. $$d\mu=f dL$$ for some function $$f$$, we can compute the density of $$\nu$$ by 
$$d\nu(y) =\int_{T(x)=y}d\mu=\int_{T(x)=y}f dx$$
- Example 1: $$T:x\mapsto x^2$$, $$\mu=\mathcal{N}(0,1)$$, $$\nu=\chi^2(1)$$. Then we say $$\nu$$ is push forward measure of $$\mu$$ under $$T$$.
