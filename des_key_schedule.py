# Fitimi i 16 subkey per secilin round te algoritmit DES

# Ky eshte kodi gjeneral per implementimin e nje PBox
# n paraqet numrin e input bitave
# P eshte nje liste qe permban m integera
# Integerat ne P jane ne mes te 1 dhe n
# Input parametri x eshte nje integer n-bitesh
# Outputi y eshte nje integer m-bitesh
def pbox(x, P, n):
    y = 0
    for i in P:
        y <<= 1
        y ^= (x >> (n-i)) & 1
    return y

