- Upper bound of [[Ref. Wu2019Capacity]] is 
 $$ I(X;Y)+I(\bar{Z};U|Y)-I(\bar{Z};U|X) \text{ bound 1}\\ 
\leq I(X;Y)+\min\{C_0-I(\bar{Z};U|X),h(\bar{Z}|Y)-h(\bar{Z}|X,U,Y)\} \text{ bound 2}$$ for some 
$$P_{\bar{Z},X,U}=P_{Z,X,U}$$ satisfies $$I(\bar{Z};U|X)\leq C_0$$. 
- **Conjecture** 1. The result of [[Ref. Wu2019Capacity]] can be recovered by the following proposition: 
$$\max\text{bound 2}$$.
    - where $$(\bar{Z},U)$$ satisfies:
        - where $$\bar{Z}$$ satisfies: 
            - $$X-\bar{Z}-U$$
            - $$I(\bar{Z};U|Y)\leq C_0$$ (Note, $$I(Z;U|Y)\leq I(\bar{Z};U|Y), C_0$$)
            - $$h(\bar{Z}|X)\ge \frac{1}{2}\ln(2\pi e)$$.
        - Choose any $$\bar{Z}$$ such that 
            - $$h(\bar{Z}|X)\ge \frac{1}{2}\ln 2\pi e$$
            - $$I(\bar{Z};U|X)\leq I(Z;U|X)=C'$$
    - Furthermore, It suffices to consider Joint Gaussian. 
- __Proof__ . 
The object function is upper bounded by the result in [[Ref. Wu2019Capacity]]. 
One can construct such a Gaussian that achieves the result.
    - The result can be achieved by the following Joint Gaussian:
Denote $$X=\frac{1}{2}Z+\sqrt{\frac{1}{2}}W$$, where $$W\perp Z$$
Let $$U=\frac{\cos\theta}{\sqrt{1+\cos^2\theta}}Z+\frac{\sin\theta}{\sqrt{1+\cos^2\theta}}W'$$ (where $$W'\perp W_2, W_1, X,W$$. Additionally, scaling of $$U$$ is not important, so we normalize it. ) 
Then we have $$W_1=Z-X\\=-\cos^2⁡\theta X+\cos\theta \sqrt{1+\cos\theta}⁡ U+\sin\theta W''$$ 
$$W_2=\sqrt{\frac{\cos^2\omega}{\sin^2\theta}}W_{2a}+\sqrt{\frac{\sin^2\theta-\cos^2\omega}{\sin^2\theta}}W_{2b}$$.
So $$\bar{W}_1=-\cos^2⁡\theta X+\cos\theta \sqrt{1+\cos^2\theta}⁡ U+\sin\theta W_{2a}$$.
$$\bar{Z}=\sin^2\theta  X+\cos\theta \sqrt{1+\cos^2\theta}U+\sin\theta W_{2a}$$
    - Verification: 
$$\mathbb{E}[\bar{Z}Y]=1+\cos\omega$$
$$h(\bar{Z}|Y)=\frac{1}{2}\ln2\pi e\frac{3-2\cos\omega-\cos^2\omega}{2}$$
$$I(\bar{Z};Y|X,U)=\frac{1}{2}\ln \frac{\sin^2\theta}{\sin^2\theta-\cos^2\omega}$$
- Conjecture 2, bound 1 can be achieved. (Verified, answer is no).
- __Verify__ 1 of conjecture2. 
    - Note, even it holds, it only holds on optimal $$(\theta^*,\omega^*)$$. 
Since we consider the optimal pair, then the two terms in bound 2 are the same. If bound 1 is achieved by the joint Gaussian. We have bound1 and bound 2 are consistent. That is, step (2) is tight. 
    - That is $$h(\bar{Z}|Y,U)=h(\bar{Z}|Y,U,X)$$.
        - We have $$h(\bar{Z}|Y,U,X)=h(\bar{Z}|U,X)-I(Y;\bar{Z}|U,X)=h(\mathcal{N}(0,\sin^2\theta-\cos^2\omega))$$
        - For the other term, we have 
$$[U,Y,\bar{Z}]\sim \mathcal{N}\left(0,\begin{bmatrix}
1 & \frac{\cos\theta}{\sqrt{1+\cos^2\theta}} & \frac{2\cos\theta}{\sqrt{1+\cos^2\theta}}\\
\frac{\cos\theta}{\sqrt{1+\cos^2\theta}} & 2 & 1+\cos\omega\\ 
\frac{2\cos\theta}{\sqrt{1+\cos^2\theta}} & 1+\cos\omega &2
\end{bmatrix}\right)$$ 
Then given $$Y$$, 
$$\text{Cov}(\bar{Z},U)=\begin{bmatrix}
B & A\\
A & C
\end{bmatrix}$$
where $$A=\frac{2 \cos⁡\theta}{\sqrt{1+\cos^2⁡\theta}}-\frac{1}{2} (1+\cos⁡\omega)\frac{\cos⁡\theta}{\sqrt{1+\cos^2⁡\theta} }$$, 
$$B=2-\frac{1}{2}(1+\cos \omega)^2$$
$$C=1-\frac{1}{2}\frac{\cos^2\theta}{1+\cos^2\theta}$$
and thus $$h(\bar{Z}|Y,U)=h(\mathcal{N}(0, B-A^2/C))$$.
That is to check whether $$B-A^2/C=\sin^2\theta-\cos^2\omega$$
By plug in $$\theta^*, \omega^*$$. We have the two values are not same. 
So bound 1 can not be achieved. 
- __Verify__ 2 of conjecture 2: 
    - We can check whether $$I(\bar{Z};U|Y)=C_0$$. 
    - By numerical experiment, we have $$I(Z;U|Y)< I(\bar{Z},U|Y)<C_0$$. 
- 
- Conclusion: The following problems have same results (and is achieved by joint Gaussian).
    - $$\max I(X;Y,Z)-I(V;Y|Z)-I(X;Y|V,Y)\\=I(X;Z)+I(X;Z|V)-I(X;Z|V)$$.
        - $$Y-X-Z$$
        - $$Y-(X,Z)-V$$ 
        - $$I(V;Z)-I(V;Y)\leq C_0$$.
    - $$\max I(X;Y)+\min\{C_0-I(\bar{Z},U|X), h(\bar{Z}|Y)-h(\bar{Z}|Y,U,X)\}$$
        - where $$\bar{Z}$$ satisfies: 
            - $$X-\bar{Z}-U$$
            - $$I(\bar{Z};U|Y)\leq C_0$$ (Note, $$I(Z;U|Y)\leq I(\bar{Z};U|Y), C_0$$)
            - $$h(\bar{Z}|X)\ge \frac{1}{2}\ln(2\pi e)$$.
        - Choose any $$\bar{Z}$$ such that 
            - $$h(\bar{Z}|X)\ge \frac{1}{2}\ln 2\pi e$$
            - $$I(\bar{Z};U|X)\leq I(Z;U|X)=C'$$
        - 
