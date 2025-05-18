import heapq
from collections import defaultdict


def minimum_cost_to_acquire_pies(pies):
    if not pies:
        return 0

    # Sort the pies in descending order
    pies.sort(reverse=True)
    print(f"Sorted pies: {pies}")

    # Total cost starts at 0
    total_cost = 0
    # Heap to track the free pies
    min_heap = []
    # Track the last paid value to ensure strict pairing
    last_paid_value = float('inf')
    # Count of each value in the heap
    heap_counts = defaultdict(int)
    # To track the number of free slots we can use
    free_slots_available = 0

    remaining_pies = len(pies)

    for i, pie in enumerate(pies):
        remaining_pies = len(pies) - i - 1

        # Check if we have more free slots than remaining pies
        if free_slots_available > remaining_pies:
            # We must pay for this pie since we can't use all slots
            total_cost += pie
            print(f"Paid for pie {pie} (too many free slots: {free_slots_available} )")
            continue

        # Only add to heap if strictly less than last paid value
        if free_slots_available > 0 and pie < last_paid_value:
            heapq.heappush(min_heap, pie)
            heap_counts[pie] += 1
            print(f"Got pie for free: {pie}")
            free_slots_available -= 1
        else:
            # We must pay for this pie
            total_cost += pie
            last_paid_value = pie
            print(f"Paid for pie: {pie}, total cost now: {total_cost}")
            free_slots_available += 1

        # If the heap exceeds the free slots, remove smallest value
        while len(min_heap) > free_slots_available:
            smallest = heapq.heappop(min_heap)
            heap_counts[smallest] -= 1
            if heap_counts[smallest] == 0:
                del heap_counts[smallest]
            print(f"Removed free pie: {smallest}")

    # After we've iterated through all pies, subtract the sum of our free pies
    total_cost -= sum(min_heap)

    return total_cost


pies = [7, 5, 5, 2, 4, 6, 2, 2, 2, 1]
print(f"Final cost: {minimum_cost_to_acquire_pies(pies)}")