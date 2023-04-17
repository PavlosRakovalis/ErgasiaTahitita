import pandas as pd 
import matplotlib.pyplot as plt




perimetroskonoy = [0.0 , 0.11, 0.149 , 0.183 , 0.211 , 0.235 , 0.252 ]
emvadonkonoy = []
emvadoneleytherisepiphaneias= []
for i in range(0,7):
    
    emvadonkonoy.append(((perimetroskonoy[i]/(2*3.1415926535897))**2)*3.1415926535897)
    emvadonsolina = (0.05**2)*3.1415926535897
    emvadoneleytherisepiphaneias.append(emvadonsolina-emvadonkonoy[i])
    print(emvadonsolina)

print(emvadoneleytherisepiphaneias)



for i in range(1,4):



    DataFrame1 = pd.read_excel('Εργασία Ταχύτητα.xlsx', sheet_name= 'ThesiLeitoyrgias'+str(i))
    print(DataFrame1)

    DP = DataFrame1.loc[10,range(0,7)]
    ParohiMazas = DataFrame1.loc[12,range(0,7)]
    print(DP)
    print(ParohiMazas)

    plt.plot(ParohiMazas, DP, label='Κατάσταση'+ ' ' + str(i))
    plt.title("Αύξηση της Πίεσης Συναρτήση της παροχής")
    plt.xlabel("Παροχή Μάζας Αέρα (Kg/sec)")
    plt.ylabel("'Αυξηση Πίεσης (Pa)")
    plt.style.use("ggplot")
    ax = plt.gca()

i = 4
DataFrame1 = pd.read_excel('Εργασία Ταχύτητα.xlsx', sheet_name= 'ThesiLeitoyrgias'+str(i))
print(DataFrame1)

DP = DataFrame1.loc[10,range(0,7)]
ParohiMazas = DataFrame1.loc[12,range(0,7)]
print(DP)
print(ParohiMazas)


plt.plot(ParohiMazas, DP, label='Κατάσταση'+ ' ' + str(i)+ ' (μονο ένας ανεμιστήρας)')
plt.title("Αύξηση της Πίεσης Συναρτήση της παροχής")
plt.xlabel("Παροχή Μάζας Αέρα (Kg/sec)")
plt.ylabel("'Αυξηση Πίεσης (Pa)")
plt.style.use("ggplot")
ax = plt.gca()
plt.legend()
plt.show()

 



for i in range(1,4):

    DataFrame1 = pd.read_excel('Εργασία Ταχύτητα.xlsx', sheet_name= 'ThesiLeitoyrgias'+ str(i))
    print(DataFrame1)


    EpiphaneiaEksodoy = DataFrame1.loc[9,range(0,7)]
    DP = DataFrame1.loc[10,range(0,7)]
    print(EpiphaneiaEksodoy)
    plt.plot(EpiphaneiaEksodoy,DP, label='Κατάσταση'+ ' ' + str(i))
    plt.title("Αύξηση της Πίεσης Συναρτήση της επιφάνειας εξόδου")
    plt.xlabel("Επιφάνεια Εξόδου (m^2)")
    plt.ylabel("'Αυξηση Πίεσης (Pa)")
    plt.style.use("ggplot")
    ax = plt.gca()
    
i = 4

DataFrame1 = pd.read_excel('Εργασία Ταχύτητα.xlsx', sheet_name= 'ThesiLeitoyrgias'+ str(i))
print(DataFrame1)

EpiphaneiaEksodoy = DataFrame1.loc[9,range(0,7)]
DP = DataFrame1.loc[10,range(0,7)]
print(EpiphaneiaEksodoy)
plt.plot(EpiphaneiaEksodoy,DP, label='Κατάσταση'+ ' ' + str(i)+ '(μονο ένας ανεμιστήρας)')
plt.title("Αύξηση της Πίεσης Συναρτήση της επιφάνειας εξόδου")
plt.xlabel("Επιφάνεια Εξόδου (m^2)")
plt.ylabel("'Αυξηση Πίεσης (Pa)")
plt.style.use("ggplot")
ax = plt.gca()
plt.legend()
plt.show()

#Vriskw toys vathmoys apodosis gia tis protes treis periptvseis 


VathmosApodosis = [[0 for i in range(7)]for i in range(4)]
MegistiApodosi = [0,0,0,0]
for a in range (1,4):
    DataFrame1 = pd.read_excel('Εργασία Ταχύτητα.xlsx', sheet_name= 'ThesiLeitoyrgias'+ str(a))
    for b in range(0,7): 
        VathmosApodosis[a-1][b]= (DataFrame1.loc[10,b]* DataFrame1.loc[12,b])/(((DataFrame1.loc[5,0])**2)/7.89 )
    MegistiApodosi[a-1]= max(VathmosApodosis[a-1])
        

#Vriskw ton vathmo apodosis gia tin tetarti periptosi opoy mono enas anemistiras einai anoiktos 

DataFrame1 = pd.read_excel('Εργασία Ταχύτητα.xlsx', sheet_name= 'ThesiLeitoyrgias'+ str(4))
VathmosApodosis[3] = (DataFrame1.loc[10,range(0,7)]* DataFrame1.loc[12,range(0,7)])/(((DataFrame1.loc[5,0])**2)/15.78 )
MegistiApodosi[3] = max(VathmosApodosis[3])

print('Vathmos apodosis = ' , VathmosApodosis)
print('megisti = ' , MegistiApodosi)

#creating the RPM list

rpm = [0,0,0,0]
for i in range(1,5):
    DataFrame1 = pd.read_excel('Εργασία Ταχύτητα.xlsx', sheet_name= 'ThesiLeitoyrgias'+ str(i))
    rpm[i-1] = DataFrame1.loc[5,4]
print('rpm = ', rpm)

for i in range(1,5):
    if i == 4:
        plt.scatter(rpm[i-1],MegistiApodosi[i-1], label='Περιπτωση '+str(i) + '(μόνο ένας ανεμιστήρας)')
    else:
        plt.scatter(rpm[i-1],MegistiApodosi[i-1], label='Περιπτωση '+str(i))
    plt.title("Μέγιστος βαθμός απόδοσης του στροβίλοκινητήρα συναρτήση των στροφών λειτουργίας")
    plt.xlabel("Στροφές λειτουργίας Ανεμιστήρων")
    plt.ylabel("'Βαθμός απόδοσης")
    plt.style.use("ggplot")
    ax = plt.gca()  


plt.legend()
plt.show()




for i in range(1,5):

    DataFrame1 = pd.read_excel('Εργασία Ταχύτητα.xlsx', sheet_name= 'ThesiLeitoyrgias'+ str(i))
    print(DataFrame1)


    EpiphaneiaEksodoy = DataFrame1.loc[9,range(0,7)]
    
    
    plt.plot(EpiphaneiaEksodoy,VathmosApodosis[i-1], label='Κατάσταση'+ ' ' + str(i))
    plt.title("Απόδοση της στροβιλομήχανής συναρτήση της επιφάνειας εξόδου")
    plt.xlabel("Επιφάνεια Εξόδου (m^2)")
    plt.ylabel("Απόδοση Στροβιλομηχανής")
    plt.style.use("ggplot")
    ax = plt.gca()

plt.legend()
plt.show()    

 sdfasjlka

sdfssdfsdf
sdfdsfsdf

sfds