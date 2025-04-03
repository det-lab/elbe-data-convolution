import sympy as sm

sig0, sig, E, x = sm.symbols("φ σ E x")

fFunc = sm.exp(-E**2/(2*sig0**2))/(sm.root(2*sm.pi,2)*sig0)

print(fFunc)