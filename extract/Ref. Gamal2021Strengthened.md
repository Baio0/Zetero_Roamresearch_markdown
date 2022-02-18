- Title: Strengthened Cutset Upper Bounds on the Capacity of the Relay Channel and Applications
- Author(s): [[Au. Gamal, Abbas El]], [[Au. Gohari, Amin]], [[Au. Nair, Chandra]]
- Year: 2021
- [Local Library](zotero://select/library/items/ZFCXJH5T)
- [Pdf link](zotero://open-pdf/library/items/UX7XQPNU)
- Type: journal article
- Publication: arXiv:2101.11139 [cs, math]
- 
- Reading Note: 
- 
- **Theorem 6** ([[Ref. Wu2019Capacity]]). 
    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FResearch_Collection%2FicTKIjrvi7.png?alt=media&token=0293715f-718a-4b44-b8b2-fa8159fa6e5e)
    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FResearch_Collection%2Fv86ZW18CUn.png?alt=media&token=be853c01-e7b3-4e00-8685-b7fed5afc892)
    - 
    - For convenience, we set $$\mathbb{E}[\|X\|^2]=S=1$$. 
$$R\leq \frac{1}{2} \ln2+\sup_{\theta:\sin^2\theta\in[\frac{1}{1+S_{23}},1]}\min\{C_0+\ln\sin\theta, \min_{\omega\in(\frac{\pi}{2}-\theta,\frac{\pi}{2}]}h_\theta(\omega)\},$$ where
$$h_\theta(\omega)=\frac{1}{2}\ln(\frac{2(1-\cos\omega)(2-\frac{1}{2}(1-\cos\omega
))\sin^2\theta}{(\sin^2\theta-\cos^2\omega)})=\frac{1}{2}\frac{\sin^2\theta(3-2\cos \omega-\cos^2\omega)}{\sin^2\theta-\cos^2\omega}$$.
    - Remark 1: $$S_{23}=e^{2C_0}-1$$
    - Remark 2: Relation of notations, $$C',C_0,\theta,\omega$$. 
        - $$\frac{1}{2}\ln \frac{1}{\sin^2\theta}=C'=I(Z;U|X)=I(\bar{Z};U|X)\leq C_0=\frac{1}{2}\ln(S_{23}+1)$$
$$r=I(Y;\bar{Z}|U,X)=\frac{1}{2}\ln\frac{\sin^2\theta}{\sin^2\theta-\cos^2\omega}$$
    - Now we simplify this upper bound. 
        - As $$\theta$$ increases, $$C_0+\sin\theta$$ increase and $$\min_\omega h_\theta(\omega)$$  decreases in $$\theta$$, then the optimal $$\theta_*$$ is the one that the two value mathes (if it exists). 
        - Consider $$\theta_*$$ such that 
$$\sin^2\theta_*=(1+\frac{S_{23}}{2S_{23}+1})\frac{1}{1+S_{23}},\\
\cos \omega_*=\frac{2+\cos^2\theta_*-\cos\theta_*\sqrt{8+\cos^2\theta_*}}{2}$$. 
One can verify that $$\omega_*$$ is the optimal $$\omega$$ and $$\theta_*$$makes the two terms equal.  
It becomes $$\frac{1}{2}\ln(2+\frac{2S_{23}}{2S_{23}+1})$$. 
- __Proof__.
    - We have
$$\begin{aligned}
nR&=H(M|Y)\leq I(M;Y^n,U_n)+n \epsilon\\
&=I(X^n;Y^n,U_n)+n\epsilon\\
&\leq  I(X^n;Y^n)+I(X^n;U_n|Y^n)\end{aligned}$$
    - Formulation 1 (Do not need $$X-\bar{Z}-U$$):
$$\begin{aligned}
&I(X;U|Y)=h(U|Y)-h(U|X)\\
&=I(Z;U|Y)-I(Z;U|X)\\
&=I(Z;U|Y)-C'
\end{aligned}$$
        - For first term in min, we have: $$I(Z;U|Y)\leq C_0$$. 
        - For the second, 
            - Choose any $$\bar{Z}$$ such that 
                - $$h(\bar{Z}|X)\ge \frac{1}{2}\ln 2\pi e$$
                - $$I(\bar{Z};U|X)\leq I(Z;U|X)=C'$$
            - Remark:
                - Such a $$\bar{Z}$$ exists. 
                - Since $$h(U|Z)\ge h(U|Y,\bar{Z})$$, then $$I(Z;U|Y)\leq I(\bar{Z};U|Y)$$.
            - We have 
$$\begin{aligned}
I(Z;U|Y)&\leq I(\bar{Z};U|Y)\\
&\leq_{(2)} h(\bar{Z}|Y)-h(\bar{Z}|Y,U,X)\\
&=h(\bar{Z}|Y)-h(\bar{Z}|X)+I(\bar{Z};Y,U|X)\\
&=h(\bar{Z}|Y)-h(\bar{Z}|X)+I(\bar{Z};U|X)+I(\bar{Z};Y|U,X)\\
&\leq h(\bar{Z}|Y)-\frac{1}{2}\ln(2\pi e)+C'+r
\end{aligned}$$
            - By new OT, $$\mathbb{E}[\bar{Z}Y]\ge 1+\cos\omega,$$ thus 
$$h(\bar{Z}|Y)=h(\bar{Z}-\frac{\mathbb{E}[\bar{Z}Y]}{\mathbb{E}[Y^2]}Y|Y)\leq \frac{1}{2}\ln 2\pi e(2-\frac{(1+\cos\omega)^2}{2})=\frac{1}{2}\ln(2\pi e \frac{3-2\cos\omega-\cos^2\omega}{2})$$.
Then we complete the proof. $$\square$$ 
    - Formulation 2 (Do not introduce $$Z$$)
        - We have
$$\begin{aligned}
&I(X;U|Y)=h(U|Y)-h(U|X)\\
&\leq_{(3)} I(\bar{Z};U|Y)-I(\bar{Z};U|X)
\end{aligned}$$
        - where $$\bar{Z}$$ satisfies: 
            - $$X-\bar{Z}-U$$
            - $$I(\bar{Z};U|Y)\leq C_0$$ (Note, $$I(Z;U|Y)\leq I(\bar{Z};U|Y), C_0$$)
            - $$h(\bar{Z}|X)\ge \frac{1}{2}\ln(2\pi e)$$.
        - Remark:
            - Such $$\bar{Z}$$ exists. 
            - $$C':=I(\bar{Z};U|X)$$ (Note, $$C':=I(\bar{Z};U|X)\leq I(\bar{Z};U|Y)\leq C_0$$)
        - First term in the mean is trivial by assumption. 
        - For second term, we have 
$$
\begin{aligned}
I(\bar{Z};U|Y)&\leq_{(2)} h(\bar{Z}|Y)-h(\bar{Z}|Y,U,X)\\
&=h(\bar{Z}|Y)-h(\bar{Z}|X)+I(\bar{Z};Y,U|X)\\
&=h(\bar{Z}|Y)-h(\bar{Z}|X)+I(\bar{Z};U|X)+I(\bar{Z};Y|U,X)\\
&\leq h(\bar{Z}|Y)-\frac{1}{2}\ln(2\pi e)+C'+r
\end{aligned}
$$
        - 
-  .**Proposition 5**
$$R\leq \frac{1}{2}\ln(2+\frac{2S_{23}}{2S_{23}+1})$$. It is implied by the following proposition. 
- 
- **Proposition 4** For product rely channel ($$p_{y_1,y_r|x}=p_{y_1|x}p_{y_r|x}$$), the achievabe rate satisfies
$$R\leq I(X;Y_1,Y_r)-I(V;Y_1|Y_r)-I(X;Y_r|V,Y_1)\\=I(X;Y_r)+I(X;Y_1|V)-I(X;Y_r|V)$$.
for some $$p(x)p(y_1,y_r|x)p(v|x,y_r)$$  satisfying $$I(V;Y_r)-I(V;Y_1)\leq C_0$$.
    - Notation: $$Y_1=X+W_1, Y_r=X+W_r$$, $$\sigma^2(W_1)=N_1, \sigma^2(W_r)=N_r$$.  
    - $$p(y_1,y_r|x)$$ is determined in Gaussian Rely problem. 
    - My understanding:
    - $$Y_1-X-Y_r$$ is a Markov chain (set up of the channel) and  $$Y-(X,Y_r)-V$$ is a Markov chain.  
    - $$V$$ is generalization of rely $$U$$. 
    - Remark 1: why it suffices to consider joint Gaussian? 
- __Proof__ of Proposition 5 from Proposition 4.
It suffices to consider Gaussian random variables in proposition 4. 
$$p(y_1y_r|x)=\mathcal{N}(0,1)^2$$.
We need $$K_{X,Y_r|V}=\begin{bmatrix} K_1 &\rho\sqrt{K_1K_2}\\
\rho\sqrt{K_1K_2} &K_2
\end{bmatrix}\preceq \begin{bmatrix}
1 & 1\\
1 & 2
\end{bmatrix}$$. 
The right handside is $$K(X,Y_r)$$ when $$X=\mathcal{N}(0,1)$$. 
(It follows from the fact that conditional covariance is less than equal to covariance matrix.)
The problem in proposition 4 becomes: 
$$I(V;Y_r)-I(V;Y_1)=\frac{1}{2}\ln\frac{2}{K_1+1}\leq C_0$$. 
$$I(X;Y_1,Y_r)-I(V;Y_1|Y_r)-I(X;Y_r|V,Y_1)=\frac{1}{2}\ln(2)+\frac{1}{2}\ln(K_1+1)+\frac{1}{2}\ln(1-\rho^2)$$. 
To maximize it over all possible $$K_1\leq 1,K_2\leq 2,\rho\in[-1,1]$$, we get the result $$\frac{1}{2}\ln(2+\frac{2S_{23}}{2S_{23}+1})$$. 
- **Lemma 7**. For the (maximum) problem in proposition 4, it suffices to consider joint Gaussian. 
    - __Proof__: 
Consider problem 
$$\max I(X;Y_r)+I(X;Y_{1,\epsilon}|V)-I(X;Y_{r,\epsilon}|V)-\epsilon h(Y_{1,\epsilon}|V)$$
Subject to $$I(V;Y_{r,\epsilon}-I(V;Y_{1,\epsilon}))\leq C_0$$
$$Y_{1,\epsilon}=[Y_1,\epsilon Z_r+W]^T,Y_{r,\epsilon}=[Y_r,\epsilon Z_r+W]^T$$
wher $$W\sim\mathcal{N}(0,1)$$ is independent. (Do not know what is $$Z_r$$ here, I guess it is $$W_r$$.)
Let $$\epsilon\to 0$$, the problem becomes 
$$ I(X;Y_r)+I(X;Y_1|V)-I(X;Y_r|V)$$
$$I(X;Y_1,Y_r)-I(V;Y_1|Y_r)-I(X;Y_r|V,Y_1)\\
=I(X;Y_r)+I(X;Y_1|Y_r)-I(V;Y_1|Y_r)-I(X;Y_r|V,Y_1)\\
=I(X;Y_r)+I(X;Y_1|Y_r)+$$
- [[Res. Conjecture of Ref. Gamal2021Strengthened]]
