# THIS IS THE BEST AND SMARTEST CODE I HAVE CREATED MUWAHAHAHAHAHA
# Import necessary libraries
import sys
# Ensure sortedcontainers library is installed: pip install sortedcontainers
# SortedList for best efficiency of O(n log n)
# If using only standard libraries see heapq below - (O(n^2 log n) worst-case)
from sortedcontainers import SortedList


def minimum_cost_of_pies():
    # Use sys.stdin.readline for potentially faster input reading
    try:
        n = int(sys.stdin.readline())
    except ValueError:
        print("Error: Invalid input for n.")
        return

    # Handle potential empty input line for prices
    price_line = sys.stdin.readline().split()
    if not price_line and n > 0:
        # According to constraints, n >= 1, so prices should exist
        print(f"Error: Missing price input for n = {n}")
        return
    elif n == 0:
        # If n can be 0 based on adjusted constraints
        print(0)
        return

    try:
        prices = list(map(int, price_line))
        # Verify correct number of prices were read
        if len(prices) != n:
            print(f"Error: Expected {n} prices, but got {len(prices)}.")
            return
    except ValueError:
        print("Error: Invalid price value found.")
        return

    # Sort prices descending (most expensive first)
    prices.sort(reverse=True)

    total_cost = 0
    # Use SortedList to store the prices of pies we HAVE PAID FOR.
    # It automatically maintains sorted order (ascending by default) and allows
    # efficient (O(log n)) searching, adding, and deleting.
    # This acts as our "credit tracker". Each price P in the SortedList represents
    # one available credit that can be used for a future pie costing < P.
    paid_prices = SortedList()

    # Iterate through pies from most expensive to least expensive
    for current_price in prices:
        # --- Find the best credit to use ---
        # We want the SMALLEST paid price P_paid such that P_paid > current_price.
        # 'bisect_right(val)' finds the index 'idx' where 'val' would be inserted
        # to maintain order. All elements sl[idx:] are > val (because the list
        # doesn't have duplicates strictly equal to val at or after this point
        # unless val itself exists there).
        # Therefore, sl[idx] (if it exists) is the smallest element strictly greater than current_price.
        idx = paid_prices.bisect_right(current_price)

        # --- Decide whether to pay or take free ---
        if idx < len(paid_prices):
            # A suitable credit exists. The element at paid_prices[idx] is the
            # smallest paid price P_paid that is strictly greater than current_price.
            # Take 'current_price' pie for free.
            # Use the credit by removing the corresponding paid price from SortedList.
            # .pop(idx) removes the element at that index efficiently (O(log n)).
            paid_prices.pop(idx)
        else:
            # No suitable credit found (no paid pie > current_price is available in the list).
            # Must pay for 'current_price'.
            total_cost += current_price
            # Add 'current_price' to SortedList, generating a new credit source.
            # .add(value) inserts efficiently (O(log n)).
            paid_prices.add(current_price)

    # Python's standard integers handle arbitrary size, so total_cost is fine.
    print(total_cost)


# Run the minimum cost of pies function
if __name__ == "__main__":
    minimum_cost_of_pies()