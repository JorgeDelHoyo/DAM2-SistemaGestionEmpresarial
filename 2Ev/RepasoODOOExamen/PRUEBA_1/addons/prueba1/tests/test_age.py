from odoo.exceptions import ValidationError
from odoo.test.common import TransactionCase
from datetime import date, timedelta

class TestAge(TransactionCase):

    def setUp(self):
        super(TestAge, self).setUp()
        self.student = self.env['prueba1.student']

    def test_01_age_computation(self):
        """Calcula la edad al guardar"""
        born_2000 = date(2000,1,1)
        student = self.student.create({
            'name': 'Alumno Test',
            'birth_date': born_2000
        })
        # Calculamos la edad esperada dinámicamente
        expected_age = date.today().year-2000-(date.today().month, date.today().day < (1,1))
        self.assertEqual(student.age, expected_age)

    def test_02_future_error(self):
        """Falla si nace en el futuro"""
        future = date.today() + timedelta(days=10)
        with self.assertRaises(ValidationError):
            self.student.create({
                'name':'Marty McFly',
                'birth_date': future
            })