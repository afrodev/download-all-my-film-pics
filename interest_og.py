from typing import Union, Literal

class FutureValueCalculator:
    """
    Class to calculate the future value of an investment using simple or compound interest.
    """
    def __init__(self, investment: float, interest_rate: float, years: int, interest_type: Literal["simple", "compound"]):
        """
        Initializes the calculator with investment parameters.
        """
        self.investment = investment
        self.interest_rate = interest_rate
        self.years = years
        self.interest_type = interest_type

    def calculate_future_value(self) -> float:
        """
        Calculates the future value of the investment.
        """
        rate = self.interest_rate / 100  # Convert percentage to decimal
        if self.interest_type == "simple":
            return self.investment * (1 + rate * self.years)
        elif self.interest_type == "compound":
            return self.investment * (1 + rate) ** self.years
        else:
            raise ValueError("Invalid interest type. Use 'simple' or 'compound'.")

class UserInput:
    """
    Class to handle user input and validate the data.
    """
    @staticmethod
    def get_numeric_input(prompt: str, min_value: float = None, max_value: float = None) -> Union[float, int]:
        """
        Requests a numeric value from the user and handles input errors.
        """
        while True:
            try:
                value = float(input(prompt))
                if min_value is not None and value < min_value:
                    print(f"Error: The value must be greater than or equal to {min_value}. Please try again.")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Error: The value must be less than or equal to {max_value}. Please try again.")
                    continue
                return value
            except ValueError:
                print("Error: You must enter a numeric value. Please try again.")

    @staticmethod
    def get_user_input() -> tuple:
        """
        Gets the user's input for investment, interest rate, years, and interest type.
        """
        investment = UserInput.get_numeric_input("Enter the investment amount: ", min_value=0)
        interest_rate = UserInput.get_numeric_input("Enter the annual interest rate (%): ", min_value=0)
        years = int(UserInput.get_numeric_input("Enter the number of years: ", min_value=1))
        while True:
            interest_type = input("Do you want to calculate 'simple' or 'compound' interest?: ").strip().lower()
            if interest_type in ["simple", "compound"]:
                break
            print("Error: Invalid interest type. Use 'simple' or 'compound'.")
        return investment, interest_rate, years, interest_type

def main():
    """
    Main function that performs the future value calculation using the classical formula.
    """
    print("Welcome to the Future Value Calculator (Classical Formula).\n")
    while True:
        try:
            # Get user input
            investment, interest_rate, years, interest_type = UserInput.get_user_input()
            # Create an instance of the calculator
            calculator = FutureValueCalculator(investment, interest_rate, years, interest_type)
            # Calculate future value
            future_value = calculator.calculate_future_value()
            # Display results
            print(f"\nThe future value of your investment with {interest_type} interest will be: ${future_value:.2f}")
            # Ask if the user wants to perform another calculation
            continue_calculating = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
            if continue_calculating != 'y':
                print("\nThank you for using the Future Value Calculator. Goodbye!")
                break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.\n")

# Entry point of the program
if __name__ == "__main__":
    main()