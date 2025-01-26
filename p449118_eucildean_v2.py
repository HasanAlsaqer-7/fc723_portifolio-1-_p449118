def euclidean_algorithm(a, b):
    """
    This function calculates the GCD of two positive integers using the Euclidean Algorithm.
    Parameters:
        a (int): The first positive integer.
        b (int): The second positive integer.
    Returns:
        int: The GCD of the two integers.
    """
    while b != 0:  # Continue until the remainder becomes zero
        print(f"Calculating: A = {a}, B = {b}")  # Show current values
        a, b = b, a % b  # Update A and B using the remainder
    print(f"Final GCD: {a}")  # Display the final GCD
    return a


if __name__ == "__main__":
    try:
        print("Welcome to the Euclidean Algorithm GCD Calculator!")

        # Prompt the user for the first number
        a = int(input("Enter the first positive integer (A): "))
        # Prompt the user for the second number
        b = int(input("Enter the second positive integer (B): "))

        # Ensure both numbers are positive
        if a <= 0 or b <= 0:
            raise ValueError("Both numbers must be positive integers.")

        # Calculate and display the GCD
        gcd = euclidean_algorithm(a, b)
        print(f"The GCD of {a} and {b} is: {gcd}")

    except ValueError as e:
        print(f"Error: {e}")

