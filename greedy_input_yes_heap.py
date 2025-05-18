import heapq
import sys

def solve():
    # Use sys.stdin.readline for potentially faster input reading
    n = int(sys.stdin.readline())
    # Handle potential empty input line for prices
    price_line = sys.stdin.readline().split()
    if not price_line:
         # Or handle as an error depending on problem constraints if n > 0
        prices = []
    else:
        prices = list(map(int, price_line))

    # Sort prices descending (most expensive first)
    prices.sort(reverse=True)

    total_cost = 0
    # This min-heap stores the prices of pies we HAVE PAID FOR.
    # It acts as our "credit tracker". Each price P in the heap represents
    # one available credit that can be used for a future pie costing < P.
    paid_prices_heap = []

    # Iterate through pies from most expensive to least expensive
    for current_price in prices:
        temp_popped = []
        found_credit_source_price = -1 # Value of the paid pie whose credit we used

        # --- Find the best credit to use ---
        # We want the SMALLEST paid price P_paid such that P_paid > current_price.
        # This is inefficient with heapq, involving potentially many pops/pushes.

        # 1. Pop elements from heap that are too small (<= current_price)
        while paid_prices_heap and paid_prices_heap[0] <= current_price:
            # Temporarily store popped elements that can't be used for this current_price
            temp_popped.append(heapq.heappop(paid_prices_heap))

        # 2. Check if a valid credit source exists now
        if paid_prices_heap:
            # The smallest element remaining in the heap (paid_prices_heap[0])
            # is now the smallest P_paid > current_price. This is the best credit to use.
            found_credit_source_price = heapq.heappop(paid_prices_heap) # Use the credit (remove from heap)

        # 3. Restore the elements that were popped but not used
        for val in temp_popped:
            heapq.heappush(paid_prices_heap, val)

        # --- Decide whether to pay or take free ---
        if found_credit_source_price != -1:
            # Successfully found and used a credit from a paid pie costing 'found_credit_source_price'.
            # Take 'current_price' pie for free.
            # Cost doesn't increase, and a credit was consumed (already popped).
            pass
        else:
            # No suitable credit found (no paid pie > current_price is available).
            # Must pay for 'current_price'.
            total_cost += current_price
            # Add 'current_price' to the heap, generating a new credit source for future, cheaper pies.
            heapq.heappush(paid_prices_heap, current_price)

    print(total_cost)

solve()