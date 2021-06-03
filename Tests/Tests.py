import unittest
from random import random

from Table import Table
from Column import Column
from Row import Row
from Database import Database


class TestDb(unittest.TestCase):

    def setUp(self):
        self.database = Database()

    def test1_table(self):
        base = Database()
        test_table = Table("test1")
        base.add_table(test_table)
        test_table.add_column(Column(int, "ID"))
        test_table.add_column(Column(str, "imię"))
        test_table.add_column(Column(str, "nazwisko"))
        test_table.add_column(Column(float, "wzrost"))

        self.assertEqual("test1", test_table.name)  # test 1 a)
        self.assertEqual(["ID", "imię", "nazwisko", "wzrost"], test_table.get_column_names())  # test 1 b)

        test_table.add_row(Row(["1", "Roch", "Przyłbipięt", "1.50"]))
        self.assertEqual([1, "Roch", "Przyłbipięt", 1.5], test_table.get_rows()[0])  # test 2

        test_table.add_row(Row(["2", "Ziemniaczysław", "Bulwiasty", "1.91"]))
        self.assertEqual([2, "Ziemniaczysław", "Bulwiasty", 1.91], test_table.get_rows()[1])  # test 3

        self.assertRaises(ValueError, test_table.add_row, Row(["cztery", "bla", "bla", "-90"]))  # test 4

        self.assertRaises(ValueError, test_table.add_row, Row(["3.14", "pi", "ludolfina", "314e-2"]))  # test 5

        # test 6
        # test 7

    def test2_table(self):
        base = Database()
        test_table2 = Table("test2")
        base.add_table(test_table2)
        test_table2.add_column(Column(str, "reserved"))
        test_table2.add_column(Column(int, "kolor"))

        self.assertEqual("test2", test_table2.name)  # test 8
        self.assertEqual(["reserved", "kolor"], test_table2.get_column_names())  # test 9

        test_table2.add_row(Row(["", "1337"]))
        self.assertEqual(["", 1337], test_table2.get_rows()[0])  # test 9

        self.assertRaises(ValueError, test_table2.add_row, Row(["bla", "1939b"]))  # test 10

        # test 11

    def test3_wrong_table(self):
        base = Database()
        test_table3 = Table("")
        base.add_table(test_table3)
        self.assertEqual([], base.get_tables_names())  # test 12

        test_table4 = Table(" ")
        base.add_table(test_table4)
        self.assertEqual([], base.get_tables_names())  # test 13

        test_table5 = Table("Cols_check")
        base.add_table(test_table5)
        test_table5.add_column(Column(str, ""))  # test 14
        self.assertEqual([], test_table5.get_column_names())

        test_table5.add_column(Column(str, "   "))  # test 15
        self.assertEqual([], test_table5.get_column_names())

    def test_lambda(self):
        base = Database()
        test_table_lambda = Table("lambda_check")
        base.add_table(test_table_lambda)
        test_table_lambda.add_column(Column(int, "ID"))
        test_table_lambda.add_column(Column(float, "wzrost"))

        test_table_lambda.add_row(Row(["0", "1.1"]))
        test_table_lambda.add_row(Row(["1", "1.9"]))
        test_table_lambda.add_row(Row(["2", "1.7"]))
        test_table_lambda.add_row(Row(["3", "1.2"]))
        self.assertEqual([[3, 1.2]], test_table_lambda.query("lambda row: row['ID'] > 1 and row['wzrost'] < 1.5"))  # test 16