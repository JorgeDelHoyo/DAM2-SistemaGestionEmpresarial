from odoo import models, fields

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