# Title: Fermat's Last Theorem Near Misses Search Program
# Program file name: fermat_near_misses.py
# External files required for this program: N/A
# External files created by this program: N/A
# Programmers: Harish Reddy, Manoj Kumar Boppudi
# Email address: harishreddy1077@gmail.com, manojkumarboppudi@lewisu.edu
# Course Number: [Course Number]
# Section Number: [Section Number]
# Student ID : L30082842, L30081082
# Date: 29th July 2023
#
# Description: This program allows an interactive user to search for "near misses" of Fermat's Last Theorem in the
# form x^n + y^n <> z^n, where x, y, z, n, and k are positive integers. The program prompts the user to enter the
# values of n (the power) and k (the limit for x and y). It systematically searches for combinations of x, y,
# and z that are close to satisfying the equation. The program calculates the relative miss for each combination and
# outputs the smallest relative miss encountered. The user can examine the output on the screen.
#
# Resources Used:
# https://www.britannica.com/science/Fermats-last-theorem
# https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem
# https://mathworld.wolfram.com/FermatsLastTheorem.html

# Function to calculate the relative miss
def calculate_relative_miss(x, y, z, n):
    """
    Calculates the near miss and relative miss for a given x, y, z, and n.

    Args:
        x (int): Value of x.
        y (int): Value of y.
        z (int): Value of z.
        n (int): Power value.

    Returns:
        float: Near miss.
        float: Relative miss.
    """
    # Calculate (x^n + y^n)
    total = x ** n + y ** n

    # Calculate (z^n) and ((z + 1)^n)
    z_n = z ** n
    z_plus_one_n = (z + 1) ** n

    # Calculate the absolute misses
    miss_1 = total - z_n
    miss_2 = z_plus_one_n - total
    near_miss = abs(min(miss_1, miss_2))

    # Calculate the relative miss
    relative_miss = abs(min(miss_1, miss_2)) / total

    return near_miss, relative_miss


# Declaration for n, the power value
n = int(input("Enter the value of n which is greater than 2 and less than 12: "))  # User input for n

# Declaration for k, the limit value
k = int(input("Enter the value of k which is greater than 10: "))  # User input for k

# Printing empty line to have better view of results
print("\n")

# Initialize variables for holding different values
smallest_relative_miss = float('inf')  # Initialize with infinite value
best_x, best_y, best_z = 0, 0, 0

# Loop through all possible combinations of x, y, and z
for x in range(10, k + 1):  # Loop for x from 10 to k
    for y in range(10, k + 1):  # Loop for y from 10 to k
        for z in range(1, k+1):  # Loop for z from 1 to k
            # Calculate the relative miss for the current combination of x, y, and z
            # based on the power value n
            near_miss, relative_miss = calculate_relative_miss(x, y, z, n)

            # Check if the relative miss is smaller than the current smallest relative miss
            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z, best_n = x, y, z, n

                # Print the current best combination, current smallest near miss value and current smallest relative miss
                print(f"Combination of values                   : x={best_x}, y={best_y}, z={best_z}, n={best_n}")
                print(f"Current Smallest Near Miss Value        : {format(near_miss, '.6f')}")
                print(f"Current Smallest Relative Miss          : {format(smallest_relative_miss, '.20f')}")
                print("\n************************************************************************\n")

# To exit from the console
input('Press ENTER to exit')
