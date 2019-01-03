
# coding: utf-8

# ## 先算一个小素数表

# In[215]:


MAX_PRIME=100
primes=[]
i=2
while i<MAX_PRIME:
    for prime in primes:
        if i%prime==0:
            break
    else:
        primes.append(i)
    i+=1


# ## 输入参数

# In[216]:


def ext_euclid(a, b):
     if b == 0:
         return 1, 0, a
     else:
         x, y, q = ext_euclid(b, a % b) # q = gcd(a, b) = gcd(b, a%b)
         x, y = y, (x - (a // b) * y)
         return x, y, q


# In[217]:


def exp_mod(x,p,m):
    y=1
    x=x%m
    for _ in range(p):
        y=y*x%m
    return y


# In[218]:


template="""
p={p},q={q},e={e},M={M}
1)p={p},q={q}
2)n=pq={p}*{q}={n}
3)ϕ(n)=(p-1)(q-1)={phi}
4)选择e使其与ϕ(n)互素且小于ϕ(n)，这里选择e={e}
5)确定d使得de=1(mod {phi}),且d<{phi}
  有扩展欧几里得定理，可得
  {d}*{e}+{phi}*x=1(mod 20)
  d={d}

公钥PU=(e,n)=({e},{n})
私钥PR=(d,n)=({d},{n})

加密:
C=M^e(mod n)={C}

解密：
M=C^d(mod n)={M}
"""


# In[219]:


print(template.format(**globals()))


# In[220]:


def rsa(p,q,e,M):
    n=p*q
    phi=(p-1)*(q-1)
    _,d,x=ext_euclid(phi,e)
    if d<0:
        d=d+phi
    C=exp_mod(M,e,n)
    M=exp_mod(C,d,n)
    print(template.format(**locals()))


# In[221]:


rsa(5,11,3,9)


# In[222]:


rsa(7,11,17,8)


# In[223]:


rsa(11,13,11,7)


# In[224]:


rsa(17,31,7,2)

