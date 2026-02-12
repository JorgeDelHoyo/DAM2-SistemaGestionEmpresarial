from odoo import _, api, fields, models

# --- CLASE A (Padre 1) ---
class Negocio(models.Model):
    _name = 'prueba1.negocio' # Tabla propia
    _description = 'Clase Negocio'

    rubro = fields.Char(string='Sector/Rubro')
    cif = fields.Char(string='CIF')

# --- CLASE B (Padre 2) ---
class Estructura(models.Model):
    _name = 'prueba1.estructura'
    _description = 'Clase Estructura'

    metros = fields.Float(string='Metros Cuadrados')
    direccion = fields.Char(string='Direccion Fisica')

# -- HERENCIA TIPO 2: HERENCIA MÚLTIPLE ---
# La Empresa "chupa" los campos de Negocio y Estructura.
# Al crear una Empresa, tienes todos los campos juntos en la tabla 'prueba1_empresa'.
class Empresa(models.Model):
    _name = 'prueba1.empresa'
    _inherit = ['prueba1.negocio','prueba1.estructura'] # < -- Lista de padres
    _description = 'Empresa (Hereda de Negocio y Estructura)'

    name = fields.Char(string='Nombre Empresa', required=True)

    alumno_ids = fields.One2many('prueba1.hijo', 'empresa_id', string='Alumnos')