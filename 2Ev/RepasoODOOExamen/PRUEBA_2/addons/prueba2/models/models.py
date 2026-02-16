from odoo import _, api, fields, models
from datetime import date
from odoo.exceptions import ValidationError


# ==========================================
# 1. MODELO EMPRESA (Base para la relación)
# ==========================================
class Empresa(models.Model):
    _name = 'prueba2.empresa'
    _description = 'Empresa propia'

    name = fields.Char(string='Nombre empresa', required=True)
    direccion = fields.Char(string='Dirección')

# ==========================================
# TIPO 2: HERENCIA DE PROTOTIPO (EXTENSION)
# Modificamos 'prueba2.empresa' sin crear tabla nueva.
# (Simulamos que ampliamos el modelo anterior)
# ==========================================
class EmpresaExtension(models.Model):
    _inherit = 'prueba2.empresa' # SIN _name modifica el anterior
    _description = 'EmpresaExtension'

    sector = fields.Selection([
        ('it', 'Informática'),
        ('finanzas', 'Finanzas')
    ], string='sector')

    # Relacion One2Many alumno
    alumno_ids = fields.One2many('prueba2.alumno', 'empresa_id', string='Alumnos')

# ==========================================
# CLASE BASE PERSONA
# ==========================================
class Persona(models.Model):
    _name = 'prueba2.persona'
    _description = 'Clase Base Persona'
    
    name = fields.Char(string='Nombre completo', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    edad = fields.Integer(compute='_compute_edad', string='edad')
    
    estado_vital = fields.Selection([
        ('nino', 'Niño/Estudiante'),
        ('trabajador','Trabajador'),
        ('jubilado','Jubilado')
    ], string='Etapa vital', compute='_compute_estado', store=True)
    
    @api.depends('edad')
    def _compute_estado(self):
        for b in self:
            if b.edad < 18:
                b.estado_vital = 'nino'
            elif b.edad < 65:
                b.estado_vital = 'trabajador'
            else:
                b.estado_vital = 'jubilado'

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for a in self:
            if a.fecha_nacimiento:
                a.edad = date.today().year - a.fecha_nacimiento.year
            else:
                a.edad = 0
    
    @api.constrains('edad')
    def _check_edad(self):
        for c in self:
            if c.edad < 0:
                raise ValidationError("LA EDAD NO PUEDE SER NEGATIVA")

# ==========================================
# TIPO 1: HERENCIA DE CLASE (Class Inheritance)
# Crea tabla nueva 'prueba2_alumno' copiando campos de Persona
# ==========================================
class Alumno(models.Model):
    _name = 'prueba2.alumno'
    _inherit = 'prueba2.persona' # Hereda campos y lógica de Persona
    _description = 'Alumno'

    curso = fields.Char(string='Ciclo formativo')
    nota_media = fields.Float(string='Nota Media')
    
    empresa_id = fields.Many2one('prueba2.empresa', string='Empresa asignada')

# ==========================================
# TIPO 3: HERENCIA POR DELEGACIÓN (Delegation)
# El Sindicalista 'tiene' un Alumno dentro.
# ==========================================
class Sindicalista(models.Model):
    _name = 'prueba2.sindicalista'
    _inherits = {'prueba2.alumno': 'alumno_id'} # Delegación
    _description = 'Sindicalista'

    alumno_id = fields.Many2one('prueba2.alumno', required=True)
    sindicato = fields.Char(string='Sindicato', required=True)
    antiguedad_sindical = fields.Integer(string='Años en Sindicato')