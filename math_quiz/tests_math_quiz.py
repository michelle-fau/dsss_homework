import unittest
from math_quiz import generate_random_int, generate_random_operator, create_math_problem


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        """
        Test if generate_random_operator returns one of the valid operators
        """
        valid_operators = ['+', '-', '*']
        result = generate_random_operator()
        self.assertIn(result, valid_operators, "The operator should be one of '+', '-', or '*'.")


    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                # TODO add more test cases here
                (9, 4, '-', '9 - 4', 5),  # Subtraction test case
                (4, 7, '*', '4 * 7', 28),  # Multiplication test case
                (0, 3, '+', '0 + 3', 3),  # Edge case with zero
                (3, 0, '*', '3 * 0', 0),  # Multiplication by zero
                (-3, 7, '+', '-3 + 7', 4),  # Negative number addition
                (-2, -3, '*', '-2 * -3', 6)  # Multiplication with negatives
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                problem, answer = create_math_problem(num1, num2, operator)
                self.assertEqual(problem, expected_problem,
                                 f"Expected problem string to be '{expected_problem}' but got '{problem}'")
                self.assertEqual(answer, expected_answer,
                                 f"Expected answer to be '{expected_answer}' but got '{answer}'")

if __name__ == "__main__":
    unittest.main()
