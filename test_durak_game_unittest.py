import unittest
from Durak_game import Durak
Durak_class = Durak


# Проверяем поцедуры класса Durak
class Test_Durak_game_unittest (unittest.TestCase):

    def setUp (self):
        print('start')

    def tearDown (self):
        print('done')

    # Проверка Первый блок процедур
    def test_Blok_1(self):
        self.assertEqual(len(Durak_class.vydat_carty_iz_colody(6,[])),2)
        self.assertEqual(Durak_class.what_rang('туз'), 9)

     # Проверка Второй блок процедур
    def test_Blok_2(self):
        self.assertEqual(Durak_class.what_card(9), 'Туз')
        self.assertEqual(Durak_class.what_mast(1), 'Пики')

     # Проверка Третий блок процедур
    def test_Blok_3(self):
        elem_rang = [6,1]
        rang_card_list = []
        rang_card_list.append(elem_rang)
        self.assertEqual(Durak_class.converter_rang_in_name(rang_card_list),[['Валет', 'Пики']])
        self.assertEqual(len(Durak_class.what_trump([])), 3)

    # Проверка Четвуртый блок процедур
    def test_Blok_4(self):
        self.assertEqual(len(Durak_class.razbor_str_card('валет пики')),3)
        self.assertEqual(Durak_class.ho_iz_stronger('валет пики','Дама пики',1),True)

    # Проверка Пятый блок процедур
    def test_Blok_5(self):
        self.assertEqual(Durak_class.end_game_sign([], []), True)





















