from odoo import _, api, fields, models

# ---------------------------------------------------------
# 1. HERENCIA PROTOTIPO (Class Inheritance)
# Escenario: Persona -> Hijo
# ---------------------------------------------------------

class Persona(models.Model):
    _name = 'prueba1.persona'
    _description = 'Modelo base Persona'

    name = fields.Char(string='Nombre Completo', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    direccion = fields.Text(string='Direccion')

class Hijo(models.Model):
    _name = 'prueba1.hijo'
    _inherit = 'prueba1.persona' # <-- HERENCIA PROTOTIPO (Copia campos de Persona)
    _description = 'Modelo Hijo (Alumno)'

    # Campos del Hijo
    colegio = fields.Char(string='Colegio')
    curso = fields.Selection([
        ('primaria', 'Primaria'),
        ('secundaria','Secundaria')
    ], string='Curso')

    #RELACION MANY2ONE: Muchos hijos pertenecen a una empresa
    empresa_id = fields.Many2one('prueba1.empresa', string='Empresa de Prácticas')

# ---------------------------------------------------------
# 2. HERENCIA MÚLTIPLE (Mixins)
# Escenario: Negocio + Estructura -> Empresa
# ---------------------------------------------------------

class Negocio(models.Model):
    _name = 'prueba1.negocio'
    _description = 'Mixin de Negocio'

    rubro = fields.Char(string='Rubro/Sector', help='Ej: Tecnológico, Alimentación')
    cif = fields.Char(string='cif')

class Estructura(models.Model):
    _name = 'prueba1.estructura'
    _description = 'Mixin de Estructura Física'

    ubicacion = fields.Char(string='Ubicacion de la Sede')
    metros_cuadrados = fields.Float(string='Metros Cuadrados')

class Empresa(models.Model):
    _name = 'prueba1.empresa'
    _inherit = ['prueba1.negocio', 'prueba1.estructura'] # <-- HERENCIA MÚLTIPLE
    _description = 'Modelo empresa'

    name = fields.Char(string='Nombre de la empresa', required=True)

    # RELACIÓN ONE2MANY: Una empresa tiene muchos alumnos (hijos) asignados
    # Es la inversa del campo 'empresa_id' en el modelo 'prueba1.hijo'
    hijo_ids = fields.One2many('prueba1.hijo', 'empresa_id', string='Alumnos Asignados')