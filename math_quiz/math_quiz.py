import random


def generate_random_int(min_val, max_val):
    """
    Generate a random integer between min_val and max_val

    Args:
        min_val (int): The minimum value of the range
        max_val (int): The maximum value of the range

    Returns:
        int: A random integer within the specified range
    """
    try:
        return random.randint(min_val, max_val)
    except ValueError:
        print("Error: Invalid range provided")
        return None


def generate_random_operator():
    """
    Randomly select a mathematical operator between +, -, or *

    Returns:
        str: A random operator
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(num1, num2, operator):
    """
    Generate a math problem string and calculate the expected answer

    Args:
        num1 (int): The first number
        num2 (int): The second number
        operator (str): The operator ('+', '-', or '*') to use in the problem

    Returns:
        tuple: A tuple containing the problem as a string and the correct answer
    """
    problem = f"{num1} {operator} {num2}"

    # Calculate the correct answer based on the operator
    if operator == '+':
        answer = num1 + num2 # Corrected logic
    elif operator == '-':
        answer = num1 - num2 # Corrected logic
    else:
        answer = num1 * num2

    return problem, answer

def math_quiz():
    """
    Run the math quiz game where the user solves randomly generated math problems
    """
    score = 0
    total_question = 3 # Number of questions in the quiz should be int

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_question):
        # Generate two random integers for the problem
        num1 = generate_random_int(1, 10)
        num2 = generate_random_int(1, 5) # Corrected max_val to an int
        operator = generate_random_operator()

        if num1 is None or num2 is None:
            print("Skipping this question due to an error in number generation.")
            continue

        # Create the math problem and retrieve the correct answer
        problem, correct_answer = create_math_problem(num1, num2, operator) # Corrected variables naming convention
        print(f"\nQuestion: {problem}")

        # Handle invalid user input with try-except
        try:
            user_answer = int(input("Your answer: ")) # Corrected variables naming convention
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        # Check the user's answer
        if user_answer == correct_answer: # Corrected indentation
            print("Correct! You earned a point.")
            score += 1 # Simplify logic
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_question}")

if __name__ == "__main__":
    math_quiz()
