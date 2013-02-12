import unittest


class CenterStringTest(unittest.TestCase):
    def test_center(self):
        """Unittest for string.center()"""
        print 'Basic functionality'
        test_cases = [('1', '  1  '),
                      ('12', '  12 '),
                      #in oddnumberof additions, center
                      #prefers to add from the left
                      #('12', ' 12  '),
                      #center doesn't cut the string
                      #('123456', '12345'),
                      #('1234567', '23456'),
                      (' ', '     '),
                      ('  1', '   1 '),
                      ('', '     ')]
        for string, expected in test_cases:
            # When
            output = string.center(5)
            # Then
            self.assertEqual(output, expected)
        print 'Filling with specific characters'
        test_cases_var = [('1', '!!1!!'),
                          ('12', '!!12!'),
                          (' ', '!! !!'),
                          ('  1', '!  1!'),
                          ('', '!!!!!')]
        for string, expected in test_cases_var:
            # When
            output = string.center(5, '!')
            # Then
            self.assertEqual(output, expected)
        test_cases_var_2 = [('1', 'qq1qq'),
                            ('12', 'qq12q'),
                            (' ', 'qq qq'),
                            ('  1', 'q  1q'),
                            ('', 'qqqqq')]
        for string, expected in test_cases_var_2:
            # When
            output = string.center(5, 'q')
            # Then
            self.assertEqual(output, expected)
        test_cases_var_3 = [('1', '22122'),
                            ('12', '22122'),
                            (' ', '22 22'),
                            ('  1', '2  12'),
                            ('', '22222')]
        for string, expected in test_cases_var_3:
            # When
            output = string.center(5, '2')
            # Then
            self.assertEqual(output, expected)
        print 'Test for Type Errors'
        string = 'sfgf'
        with self.assertRaises(TypeError):
            string.center(5, '')
        with self.assertRaises(TypeError):
            string.center(5, '1234')
        with self.assertRaises(TypeError):
            string.center('a')


if __name__ == '__main__':
        unittest.main()
