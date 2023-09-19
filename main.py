# De euclidische deling van twee veeltermen
# Dit programma is gemaakt door:
# Mathias Van Nuland, 2023

# Voorstelling van een veelterm:
# Een veelterm wordt voorgesteld als een lijst van coëfficiënten,
# waarbij de hoogste graad vooraan staat.
# Bijvoorbeeld: 2x^3 + 3x^2 + 4x + 5 wordt voorgesteld als [2, 3, 4, 5]

# Vraag de gebruiker om de coëfficiënten van het deeltal (A) in te geven
graad = int(input("Geef de graad van A in: "))
A = []
for i in range(graad + 1):
    A.append(int(input("Geef de coëfficiënt van x^" + str(graad - i) + " in: ")))

print("De coëfficiënten van A zijn: ", A)
print("=" * 30)

# Vraag de gebruiker om de coëfficiënten van de deler (D) in te geven
graad = int(input("Geef de graad van D in: "))
D = []
for i in range(graad + 1):
    D.append(int(input("Geef de coëfficiënt van x^" + str(graad - i) + " in: ")))

print("De coëfficiënten van D zijn: ", D)
print("=" * 30)

# Algoritme
R = A
Q = []
while len(R) >= len(D):
    Q.append(R[0] / D[0])

    # T = []
    # for i, d in enumerate(D):
    #     buffer = Q[-1] * d
    #     T.append(R[i] - buffer)
    T = [R[i] - Q[-1] * D[i] for i in range(len(D))]

    R = T + R[len(T) :]
    R.pop(0)

# Print coëfficiënten van R en Q
print("De coëfficiënten van R zijn:", R)
print("De coëfficiënten van Q zijn:", Q)
