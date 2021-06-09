import unittest

from Logic.Table import Table
from Logic.Column import Column
from Logic.Row import Row
from Logic.Database import Database
from Exceptions.Exceptions import UnableToCastException
from Exceptions.Exceptions import WrongNameException


class TestDb(unittest.TestCase):

    def setUp(self):
        self.database = Database()

    def test1_table(self):
        ######
        # 1. Utworzenie tabeli "test1" z kolumnami liczbową "ID"(typ int),
        # dwoma tekstowymi "imię" oraz "nazwisko" oraz liczbową "wzrost"(typ float).
        base = Database()
        test_table = Table("test1")
        base.add_table(test_table)
        test_table.add_column(Column(int, "ID"))
        test_table.add_column(Column(str, "imię"))
        test_table.add_column(Column(str, "nazwisko"))
        test_table.add_column(Column(float, "wzrost"))

        self.assertEqual("test1", test_table.name)  # test 1 a)
        self.assertEqual(["ID", "imię", "nazwisko", "wzrost"], test_table.get_column_names())  # test 1 b)
        ######
        # 2. Dodanie wiersza do tabeli "test1" z danymi "1", "Roch", "Przyłbipięt", "1.50" - oczekiwane powodzenie.
        test_table.add_row(Row(["1", "Roch", "Przyłbipięt", "1.50"]))
        self.assertEqual([1, "Roch", "Przyłbipięt", 1.5], test_table.get_rows()[0])  # test 2

        ######
        # 3. Dodanie wiersza do tabeli "test1" z danymi "2", "Ziemniaczysław", "Bulwiasty",
        # "1.91" - oczekiwane powodzenie.
        test_table.add_row(Row(["2", "Ziemniaczysław", "Bulwiasty", "1.91"]))
        self.assertEqual([2, "Ziemniaczysław", "Bulwiasty", 1.91], test_table.get_rows()[1])  # test 3

        #######
        # 4. Dodanie wiersza do tabeli "test1" z danymi "cztery", "bla", "bla", "-90"
        # - oczekiwane niepowodzenie(dane tekstowe w polu liczbowym).
        self.assertRaises(UnableToCastException, test_table.add_row, Row(["cztery", "bla", "bla", "-90"]))  # test 4

        #######
        # 5. Dodanie wiersza do tabeli "test1" z danymi "3.14", "pi", "ludolfina", "314e-2"
        # - oczekiwane niepowodzenie (liczba rzeczywista w kolumnie z liczbą całkowitą).
        self.assertRaises(UnableToCastException, test_table.add_row,
                          Row(["3.14", "pi", "ludolfina", "314e-2"]))  # test 5

        #######
        # 6. Wyświetlenie zawartości tabeli "test1".
        result_table = base.get_active("test1")
        self.assertEqual([[1, 'Roch', 'Przyłbipięt', 1.5],
                          [2, 'Ziemniaczysław', 'Bulwiasty', 1.91]],
                         result_table.get_rows())  # test 7

        #######
        # 7. Dodanie trzech kolejnych wierszy do tabeli “test1” i usunięcie dwóch wierszy z niej
        # (pierwszego i środkowego), w obu przypadkach najpierw anulowanie operacji, a
        # potem jej akceptacja.
        add_row1 = Row(["3", "Jan", "Ciekawy", "1.40"])
        add_row2 = Row(["4", "Paweł", "Ciekawszy", "1.60"])
        add_row3 = Row(["5", "Karol", "Najciekawszy", "1.70"])
        test_table.add_row(add_row1)
        test_table.add_row(add_row2)
        test_table.add_row(add_row3)

        test_table.remove_row(add_row1)
        test_table.remove_row(add_row2)

        print(test_table.get_rows())
        self.assertEqual([[1, 'Roch', 'Przyłbipięt', 1.5],
                          [2, 'Ziemniaczysław', 'Bulwiasty', 1.91],
                          [5, 'Karol', 'Najciekawszy', 1.7]],
                         test_table.get_rows())  # test 7
        ########

    def test2_table(self):
        ########
        # 8. Utworzenie tabeli "test2" z kolumnami “reserved" typu string oraz "kolor" typu liczba
        # całkowita.
        base = Database()
        test_table2 = Table("test2")
        base.add_table(test_table2)
        test_table2.add_column(Column(str, "reserved"))
        test_table2.add_column(Column(int, "kolor"))

        self.assertEqual("test2", test_table2.name)  # test 8
        self.assertEqual(["reserved", "kolor"], test_table2.get_column_names())  # test 8

        #########
        # 9. Dodanie wiersza do tabeli “test2” z danymi (puste pole), “1337” - oczekiwane
        # powodzenie.
        test_table2.add_row(Row(["", "1337"]))
        self.assertEqual(["", 1337], test_table2.get_rows()[0])  # test 9

        #########
        # 10. Dodanie wiersza do tabeli "test2" z danymi “bla”, “1939b" - oczekiwane
        # niepowodzenie (tekst w polu typu liczba całkowita).
        self.assertRaises(UnableToCastException, test_table2.add_row, Row(["bla", "1939b"]))  # test 10

        #########
        # 11. Usunięcie tabeli “test2”, najpierw anulowanie operacji, a potem jej akceptacja.
        base.remove_table(test_table2)
        self.assertEqual([], base.get_tables_names())  # test 11

        #########
    def test3_wrong_table(self):
        #########
        # 12. Próba utworzenia tabeli bez nazwy - oczekiwane niepowodzenie.
        base = Database()
        test_table3 = Table("")
        self.assertRaises(WrongNameException, base.add_table, test_table3)  # test 12

        ########
        # 13. Próba utworzenia tabeli o nazwie " " (spacja) - oczekiwane niepowodzenie.
        test_table4 = Table(" ")
        self.assertRaises(WrongNameException, base.add_table, test_table4)  # test 13

        ########
        # 14. Próba utworzenia tabeli z kolumną bez nazwy - oczekiwane niepowodzenie.

        test_table5 = Table("Cols_check")
        base.add_table(test_table5)
        self.assertRaises(WrongNameException, test_table5.add_column, Column(str, ""))  # test 14

        ########
        # 15. Próba utworzenia tabeli z kolumną o nazwie " " (cztery spacje) - oczekiwane
        # niepowodzenie.

        self.assertRaises(WrongNameException, test_table5.add_column, Column(str, "    "))  # test 15

    def test_lambda(self):
        # 16. Wypełnij tabelę "test" danymi testowymi (kolejne wartości "ID", "wzrost" między 1.0 i 2.0),
        # wyszukaj wiersze dla których “wzrost” ma wartość podaną przez prowadzącego oraz
        # “ID” jest liczbą parzystą lub nieparzystą (zależnie od woli prowadzącego).
        base = Database()
        test_table_lambda = Table("lambda_check")
        base.add_table(test_table_lambda)
        test_table_lambda.add_column(Column(int, "ID"))
        test_table_lambda.add_column(Column(float, "wzrost"))

        test_table_lambda.add_row(Row(["0", "1.1"]))
        test_table_lambda.add_row(Row(["1", "1.9"]))
        test_table_lambda.add_row(Row(["2", "1.7"]))
        test_table_lambda.add_row(Row(["3", "1.2"]))
        self.assertEqual([[3, 1.2]],
                         test_table_lambda.query("lambda row: row['ID'] > 1 and row['wzrost'] < 1.5"))  # test 16
