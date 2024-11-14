# Define the Item class
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value to weight ratio

# Function to solve the fractional knapsack problem
def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.ratio, reverse=True)

    total_value = 0  # Total value of the knapsack
    for item in items:
        if capacity == 0:
            break

        if item.weight <= capacity:
            # Take the whole item if it fits
            total_value += item.value
            capacity -= item.weight
        else:
            # Take the fraction of the item that fits
            total_value += item.value * (capacity / item.weight)
            capacity = 0  # Knapsack is full

    return total_value

# Example usage
if __name__ == "__main__":
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    capacity = 50
    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in Knapsack = {max_value:.2f}")
