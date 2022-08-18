#Condiciones anidadas ELIF

sensorNivelAgua = int(input("Digite el nivel de agua actual"))
if(sensorNivelAgua>=0 and sensorNivelAgua<20):
    print(f'Peligro el nilvel {sensorNivelAgua} es pegriloso')
elif(sensorNivelAgua>=20 and sensorNivelAgua<400):
     print(f'Hidroituango funcionando OK {sensorNivelAgua}')
elif(sensorNivelAgua>=400):
     print(f'Peligro el nilvel {sensorNivelAgua} es pegriloso')  
else:
    print("El nivel del agua no es valido")        
