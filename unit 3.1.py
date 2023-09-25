def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
product_list = input("Enter a list of products (separated by commas): ").split(",")
target = input("Enter the target product: ")

indices = linear_search_product(product_list, target)
if indices:
    print("Target product found at indices:", indices)
else:
    print("Target product not found.")