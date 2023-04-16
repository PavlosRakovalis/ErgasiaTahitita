
perimetroskonoy = [0.0 , 0.11, 0.149 , 0.183 , 0.211 , 0.235 , 0.252 ]
emvadonkonoy = []
emvadoneleytherisepiphaneias= []
for i in range(0,7):
    
    emvadonkonoy.append(((perimetroskonoy[i]/(2*3.1415926535897))**2)*3.1415926535897)
    emvadonsolina = (0.05**2)*3.1415926535897
    emvadoneleytherisepiphaneias.append(emvadonsolina-emvadonkonoy[i])
    print(emvadonsolina)

print(emvadoneleytherisepiphaneias)
