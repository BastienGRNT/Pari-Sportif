#Ce programme vise à maximiser ses chances de gagner un pari sportif, cependant il fonctionne uniquement 
#s'il y a trois cotes possibles et que la mise se fait sur seulement deux d'entre elles pour fonctionner.

cote_Equipe_A = float(input("Veuillez renseigner la cote de l'équipe A : "))
cote_Equipe_B = float(input("Veuillez renseigner la cote de l'équipe B : "))

a = range(1, 100)
res=[0,0,0,0,0,0,0]

for mise_Equipe_A in a:
    for mise_Equipe_B in a:
        gain_Equipe_A = mise_Equipe_A * cote_Equipe_A
        gain_Equipe_B = mise_Equipe_B * cote_Equipe_B
        mise_Total = mise_Equipe_A + mise_Equipe_B
        benefice_Equipe_A = gain_Equipe_A - mise_Total
        benefice_Equipe_B = gain_Equipe_B - mise_Total
        if gain_Equipe_A > mise_Total and gain_Equipe_B > mise_Total:
            prov=[gain_Equipe_A, mise_Total, gain_Equipe_B, mise_Equipe_A, mise_Equipe_B, benefice_Equipe_A, benefice_Equipe_B]
            if (prov[5]>res[5] and prov[5]>res[6] and prov[6]>res[5] and prov[6]>res[6]):   
                res=prov


print("")
print(f"BENEFICE SI A GAGNANT : ", res[5])
print(f"BENEFICE SI B GAGNANT : ", res[6])
print("")
print(f"Mise Totale : ", res[1])
print("")
print(f"Mise-A : ", res[3])
print(f"GAIN-A : ", res[0])
print("")
print(f"Mise-B : ", res[4])
print(f"GAIN-B : ", res[2])
