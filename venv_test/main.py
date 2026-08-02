import math
from log import log_info, log_warning, log_error

def calculate_square_root(numbers: list) ->None:
    for number in numbers:
        try:
            if number < 0:
                log_warning(f"Cannot calculate square root of negative number: {number}")
                continue
            root = math.sqrt(number)
            log_info(f"The square root of {number} is {root:.2f}")
        except Exception as e:
            log_error(f"An error occurred while calculating square root of {number}: {e}")

if __name__ == "__main__":
    test_numbers = [16, -4, 9, 25, 0, 4, "16"]
    calculate_square_root(test_numbers)