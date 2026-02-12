from odoo import _, api, fields, models
from odoo.exceptions import ValidationError # Necesario para excepciones
from datetime import date #Necesario para calcular la edad


# ==========================================
#  CLASE PADRE (BASE)
# ==========================================
class Persona(models.Model):
    _name = 'prueba1.persona'
    _description = 'Clase Base Persona'
    
    name = fields.Char(string='Nombre completo', required=True, help="El nombre es obligatorio")
    dni = fields.Char(string='DNI', size=9)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')

    rol = fields.Selection([
        ('hijo', 'Alumno'),
        ('trabajador', 'Trabajador'),
        ('jubilado', 'Jubilado'),
        ('sindicalista', 'Sindicalista'),
    ], string='Rol', default='hijo', required=True)

    empresa_id = fields.Many2one('prueba1.empresa', string='Empresa')

    # CAMPO CALCULADO (Store guarda el dato en la BBDD)
    edad = fields.Integer(compute='_compute_edad', string='Edad', store=True)
    
    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for record in self:
            if record.fecha_nacimiento:
                hoy = date.today()
                nac = record.fecha_nacimiento

                record.edad = hoy.year - nac.year - ((hoy.month,hoy.day) < (nac.month, nac.day))
            else:
                record.edad = 0

    # Comprueba que la edad es válida
    @api.constrains('edad')
    def _check_edad_logica(self):
        for record in self:
            if record.edad < 0 :
                raise ValidationError("LA EDAD NO PUEDE SER NEGATIVA!!")
            
            if record.edad > 120:
                raise ValidationError("Nadie vive tanto... Revisa la fecha")

    # Comprueba que el DNI tenga longitude 9
    @api.constrains('dni')
    def _check_dni_format(self):
        for record in self:
            if record.dni and len(record.dni) != 9:
                raise ValidationError("EL DNI DEBE TENER 9 CARACTERES")


# ==========================================
#  HERENCIA TIPO 1: PROTOTIPO (Class Inheritance)
# ==========================================
# Creamos 'examen.hijo'. COPIA todo de Persona pero en SU PROPIA TABLA.
# Es independiente de Persona. (Equivalente al 'Worker' de tu profe).
class Hijo(models.Model):
    _name = 'prueba1.hijo'
    _inherit = 'prueba1.persona'
    _description = 'Hijo (Hereda de persona)'
    
    curso = fields.Char(string='Curso escolar')
    nota_media = fields.Float(string='Nota Media')

    # Relación con Empresa (Muchos Hijos -> 1 Empresa)
    empresa_id = fields.Many2one('prueba1.empresa', string='Colegio/Empresa')


class Trabajador(models.Model):
    _name = 'prueba1.trabajador'
    _inherit = 'prueba1.persona'
    _description = 'Trabajador'

    puesto = fields.Char(string='Puesto de Trabajo')
    salario = fields.Float(string='Salario Mensual')


# ==========================================
#  HERENCIA TIPO 3: DELEGACIÓN (Delegation)
# ==========================================
# El Sindicalista NO copia. TIENE una persona dentro (Link).
# (Equivalente al 'Omnivore' de tu profe).
class Sindicalista(models.Model):
    _name = 'prueba1.sindicalista'
    # Diccionario {'Modelo Padre': 'Campo FK'}
    _inherits = {'prueba1.persona': 'persona_id'}
    _description = 'Sindicalista (Delega en persona)'
    
    # Este campo conecta las dos tablas
    persona_id = fields.Many2one('prueba1.persona', string='Persona', required=True)

    # Campos solo del Sindicalista
    sindicato = fields.Char(string='Nombre sindicato')
    cuota = fields.Float(string='Cuota mensual')