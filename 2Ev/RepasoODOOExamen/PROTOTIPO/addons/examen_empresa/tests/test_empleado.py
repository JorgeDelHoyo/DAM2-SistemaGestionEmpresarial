from odoo.tests import TransactionCase, tagged
from odoo.exceptions import ValidationError
from datetime import date

@tagged('test_local', '-at_install', 'post_install')
class TestEmpleado(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestEmpleado, cls).setUpClass()

        cls.anyo_actual = date.today().year
    
    def test_compute_email_y_edad(self):
        """Comprueba que los campos calculados funcionan bien"""
        empleado = self.env['examen_empresa.empleado'].create({
            'name':'Ana Sanz',
            'fecha_nacimiento': date(self.anyo_actual - 30,1,1), # Nació hace 30 años
            'puesto': 'Desarrolladora'
        })

        # Comprobar la edad
        self.assertEqual(empleado.edad, 30)

        #Comprobar email
        self.assertEqual(empleado.email, 'ana.sanz@empresa.com')
    
    def test_action_cambiar_puesto(self):
        """Comprueba el método de acción para cambiar el puesto"""
        empleado = self.env['examen_empresa.empleado'].create({
            'name':'Carlos López',
            'fecha_nacimiento': date(self.anyo_actual - 25,1,1), # Nació hace 25 años
            'puesto': 'Analista'
        })

        # Cambiar el puesto
        empleado.action_cambiar_puesto('Consultor')

        # Comprobar que se ha cambiado
        self.assertEqual(empleado.puesto, 'Consultor')
    
    def test_raises_error_edad_minima(self):
        """Comprueba que salta la restricción si el empleado tiene menos de 16 años"""
        with self.assertRaises(ValidationError):
            self.env['examen_empresa.empleado'].create({
                'name':'Joven Empleado',
                'fecha_nacimiento': date(self.anyo_actual - 15,1,1), # Nació hace 10 años
                'puesto': 'Practicante'
            })