from odoo import models, fields

# Clase libro (Muchos libros pueden tener el mismo autor)
class Libro(models.Model):
    _name= 'biblioteca.libro'
    _description = 'Modelo para almacenar libros'
    
    # --- CAMPOS (Columnas de la tabla) ---

    #name es especial : es lo que se ve cuando buscas el libro en otra pantalla
    name = fields.Char(string="Titulo del libro", required=True)

    # Campo de texto largo
    descripcion = fields.Text(string="Sinopsis")

    # Campo numerico (precio)
    precio = fields.Float(string="Precio")

    # Campo boolean (CheckBox)
    activo = fields.Boolean(string="Disponible", default=True)

    # Campo de seleccion (lista desplegable)
    genero = fields.Selection([
        ('novela', 'Novela'),
        ('tecnico', 'Tecnico'),
        ('poesia', 'Poesia')
    ], string='Genero')


    # Relacion directa : Muchos libros tienen el mismo autor
    autor_id = fields.Many2one('biblioteca.autor', string='Autor')
    # Relacion directa: Muchos libros pueden tener una editorial
    editorial_id = fields.Many2one('biblioteca.editorial', string='Editorial')
    # Relacion Many2Many para guardar pares
    etiqueta_id = fields.Many2many('biblioteca.etiqueta', string='Etiquetas')


# Clase autor (Un autor puede tener varios libros)
class Autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'Modelo para almacenar Autores'

    name = fields.Char(string="Nombre autor", required=True)
    nacionalidad = fields.Char(string="Nacionalidad")

    # Relacion inversa: Ver los libros de este autor
    libro_ids = fields.One2many('biblioteca.libro', 'autor_id', string='Libros Escritos')
    
# Clase socio 
class Socio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio de la biblioteca'

    name = fields.Char(string="Nombre y Apellidos", required=True)
    telefono = fields.Char(string="Telefono")
    dni = fields.Char(string="DNI")

# Clase Prestamo (Un prestamo necesita un socio y un libro)
class Prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Modelo para gestionar prestamos'
    
    fecha_inicio = fields.Date(string="Fecha prestamo", default=fields.Date.today)
    fecha_fin = fields.Date(string="Fecha devolucion")

    # Relaciones
    libro_id = fields.Many2one('biblioteca.libro', string='Libro prestado',required=True)
    socio_id = fields.Many2one('biblioteca.socio', string='Socio', required=True)

# Clase Editorial
class Editorial(models.Model):
    _name = 'biblioteca.editorial'
    _description = 'Editorial de libros'

    name = fields.Char(string="Nombre de la editotrial", required=True)
    pais = fields.Char(string="Pais de origen")
    website = fields.Char(string="Sitio web")

class Etiqueta(models.Model):
    _name = 'biblioteca.etiqueta'
    _description = 'Etiquetas para clasificar libros'

    name = fields.Char(string="Nombre de la etiqueta", required=True)
    color = fields.Integer(string="Color")