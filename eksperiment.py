import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# observationer = pd.read_excel("KDI2018vest.xlsx", sheet_name="Observationer")
det_hele = pd.read_excel("KDI2018vest.xlsx", sheet_name=None)

print(80*"-")
print(det_hele.keys())   # Navnene på alle ark i mappen
print(80*"-")
print(det_hele["Beregning"].head())
print(80*"-")
print(det_hele["Observationer"].head())
print(80*"-")
nogle_punktnavne = det_hele["Observationer"]["Fra"].head()
print(nogle_punktnavne)
print(80*"-")
nogle_højdeforskelle = det_hele["Observationer"]["dH"].head()
print(nogle_højdeforskelle)
print(80*"-")
plt.plot(nogle_højdeforskelle)
plt.show()

