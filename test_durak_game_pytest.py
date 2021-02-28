import Durak_game as Durak_game
Durak_class = Durak_game.Durak

# Проверяем поцедуры класса Durak_class
class Test_Durak_game_pytest (Durak_class):

    def setup (self):
        print('start')

    def teardown (self):
        print('done')

    # Проверка Первый блок процедур
    def test_Blok_1(self):
        assert len(Test_Durak_game_pytest.vydat_carty_iz_colody(6,[]))==2
        assert Test_Durak_game_pytest.what_rang('туз')==9
        assert Test_Durak_game_pytest.what_card(9) == 'Туз'
        assert Test_Durak_game_pytest.what_mast(1) == 'Пики'

    # Проверка Второй блок процедур
    def test_Blok_2(self):

        elem_rang = [6,1]
        rang_card_list = []
        rang_card_list.append(elem_rang)
        assert Test_Durak_game_pytest.converter_rang_in_name(rang_card_list) ==  [['Валет', 'Пики']]
        assert len(Test_Durak_game_pytest.what_trump([]))==3
        assert len(Test_Durak_game_pytest.razbor_str_card('валет пики')) == 3
        assert Test_Durak_game_pytest.ho_iz_stronger('валет пики','Дама пики',1) == True

    # Проверка Третий блок процедур
    def test_Blok_3(self):
        assert Test_Durak_game_pytest.end_game_sign([], []) == True




















