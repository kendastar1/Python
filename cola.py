Nombre2 = ["Andres","juan","alvaro"]
def Nombres():
  print(Nombre2)
  del Nombre2[0]
def Insertar():
  Nombres()
  Nombre2.insert(2,("Smith"))
  print(Nombre2)
  Nombre2.insert(3,("Stefanny"))
  print(Nombre2)
  del Nombre2[0]
  Nombre2.insert(4,"alba")
  print(Nombre2)
  del Nombre2[0]
  del Nombre2[0]
  Nombre2.insert(2,"juliana")
  print(Nombre2)
  Nombre2.insert(3,"karina")
  print(Nombre2)
Insertar()
  
   

