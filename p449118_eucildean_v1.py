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
    print("Using predefined numbers: 270 and 198")

    # Predefined values
    a = 270
    b = 192

    # Calculate and display the GCD
    gcd = euclidean_algorithm(a, b)
    print(f"The GCD of {a} and {b} is: {gcd}")