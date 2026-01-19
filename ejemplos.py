class Persona:
    def __init__(self,nombre,apellido,saludo,email):
        self.nombre = nombre
        self.apellido = apellido
        self.saludo = saludo
        self.email = email
        print("Hola esto es un objeto de clase persona")
    
    def __repr__(self):
        return f"Nombre:{self.nombre},Apellido:{self.apellido},Saludo:{self.saludo},Email:{self.email}"
    
objPersona = Persona("Jose","Perez","Hello","j@email.com")
