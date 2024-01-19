nombre = "Ever"
apellido = "Lugo"
Edad = 18
peso = 87

print(type(nombre))
print(type(Edad))
print(type(peso))

edad_en_string = str(Edad)
print(f"""la edad anterior era {type(Edad)}
      la edad parseada es de tipo
      {type(edad_en_string)}""")