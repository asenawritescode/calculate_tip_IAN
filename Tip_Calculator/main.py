# IAN Interview question.

# Steven needs a very simple tip calculator for whenever he goes to eat in a restaurant. In his country, it's usual to tip 15% if the bill value is between 50 and 300. If the value is different, the tip is 20%.
# Your tasks:   
# 1. Calculate the tip, depending on the bill value. Create a variable called tip for this. 
# 2. Print a string to the console containing the bill value, the tip, and the final value (bill + tip).
# Take the bill values as: 275, 40, and 430


# Constants
TIP_RANGE_BELOW = 0.15
TIP_RANGE_ABOVE = 0.20

def calculate_tip (amount):
    """
    Calculate the tip based on the amount provided.

    Parameters:
    amount (float): The amount of the bill.

    Returns:
    str: A string containing the tip, bill, and total value.
    """
    
    try:
        amount = float(amount)
            
        # Initial values
        tip = 0
        total = 0
        
        # find the tip band
        if amount > 50 and amount < 300:
            tip = amount * TIP_RANGE_BELOW
        elif amount >= 300:
            tip = amount * TIP_RANGE_ABOVE
        else:
            tip = 0

        total = amount + tip
        
        # return result
        return f"Your bill is {amount}, your tip is {tip}, and your total value is {total}"
    except ValueError:
        raise ValueError("Please provide a valid amount")
    except Exception as e :
        print("An unexpected error has occured : ", e )


# Test Cases
# 275, 40, and 430



def main():
    test_cases = [275, 40, 430]

    for test_case in test_cases:
        print(f"Tip for {test_case}")
        print(calculate_tip(test_case) + "\n")

if __name__ == "__main__":
    main()