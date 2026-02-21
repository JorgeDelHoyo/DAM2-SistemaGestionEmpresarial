from odoo.tests import TransactionCase, tagged
from odoo.exceptions import ValidationError
from datetime import date

@tagged('test_local', '-at_install', 'post_install')
class TestHospital(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestHospital, cls).setUpClass()

        # Odoo crea el Workplace, el SleepPlace y el Hospital todo de golpe
        cls.hospital = cls.env['examen_hospital.hospital'].create({
            'name': 'Hospital La Paz', # Se guarda en Workplace
            'cantidad': 2,             # Se guarda en SleepPlace
        })

        # Ingresamos al primer paciente (¡Le añadimos fecha de nacimiento!)
        cls.paciente1 = cls.env['examen_hospital.paciente'].create({
            'name': 'Juan Pérez',
            'hospital_id': cls.hospital.id,
            'fecha_nacimiento': date(1990, 1, 1) # Mayor de 0 años
        })
    
    def test_delegacion_multiple_y_compute(self):
        """Verifica que lee datos delegados y calcula las camas"""
        self.assertEqual(self.hospital.name, 'Hospital La Paz', "El nombre del hospital no se ha guardado correctamente")
        self.assertEqual(self.hospital.cantidad, 2, "La cantidad de camas no se ha guardado correctamente")
        self.assertEqual(self.hospital.camas_libres, 1, "El cálculo de camas libres es incorrecto")
    
    def test_restriccion_capacidad(self):
        """Verifica que salte el error si superamos el limite de camas"""
        self.env['examen_hospital.paciente'].create({
            'name': 'María Gómez',
            'hospital_id': self.hospital.id,
            'fecha_nacimiento': date(1992, 5, 15) # Mayor de 0 años
        })
        
        with self.assertRaises(ValidationError, msg="Debería haber saltado un error de capacidad"):
            self.env['examen_hospital.paciente'].create({
                'name': 'Carlos López',
                'hospital_id': self.hospital.id,
                'fecha_nacimiento': date(1985, 10, 20) # Mayor de 0 años
            })

    def test_alta_masiva(self):
        """Comprueba que la acción vacía el hospital correctamente"""
        self.hospital.action_alta_masiva()
        self.assertEqual(len(self.hospital.paciente_ids), 0, "Debería haber dado de alta a todos los pacientes")
        self.assertEqual(self.hospital.camas_libres, 2, "Debería haber 2 camas libres")