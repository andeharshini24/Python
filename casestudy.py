class ProductApp:
 def __init__(self):
  self.products = {}
 def add_product(self, pid, name, category, price):
   if pid in self.products:
    print(f"Product with PId {pid} already exists!")
   else:
    self.products[pid] = {'name': name, 'category': category, 'price': price}
    print(f"Product {name} added successfully.")
    
 def update_product(self, pid, name=None, category=None, price=None):
  if pid in self.products:
   if name:
    self.products[pid]['name'] = name
   if category:
    self.products[pid]['category'] = category
   if price:
    self.products[pid]['price'] = price
   print(f"Product {pid} updated successfully.")
  else:
   print(f"Product with PId {pid} not found.")

 def delete_product(self, pid):
  if pid in self.products:
   del self.products[pid]
   print(f"Product with PId {pid} deleted successfully.")
  else:
   print(f"Product with PId {pid} not found.")

 def get_product_by_pid(self, pid):
  if pid in self.products:
   return self.products[pid]
  else:
   return f"Product with PId {pid} not found."
  
 def get_all_products(self):
  return self.products if self.products else "No products available."
 
 def get_products_by_category(self, category):
  products_in_category = {pid: product for pid, product in self.products.items() if product['category'] == category}
  return products_in_category if products_in_category else f"No products found in category {category}."
 
 def get_products_between_prices(self, min_price, max_price):
  products_in_price_range = {pid: product for pid, product in self.products.items() if min_price <=product['price'] <= max_price}
  return products_in_price_range if products_in_price_range else f"No products found between prices {min_price} and {max_price}."
 
 
def main():
 app = ProductApp()
 while True:
  print("\nProduct App Menu:")
  print("1. Add Product")
  print("2. Update Product")
  print("3. Delete Product")
  print("4. Get Product by PId")
  print("5. Get All Products")
  print("6. Get Products by Category")
  print("7. Get Products between Prices")
  print("8. Exit")
  
  choice = input("Enter your choice (1-8): ")
  if choice == '1':
   pid = int(input("Enter Product ID: "))
   name = input("Enter Product Name: ")
   category = input("Enter Product Category: ")
   price = float(input("Enter Product Price: "))
   app.add_product(pid, name, category, price)
   
  elif choice == '2':
   pid = int(input("Enter Product ID to update: "))
   name = input("Enter new Product Name (leave empty if no change): ")
   category = input("Enter new Product Category (leave empty if no change): ")
   price = input("Enter new Product Price (leave empty if no change): ")
   app.update_product(pid, name if name else None, category if category else None, float(price) if price else None)

  elif choice == '3':
   pid = int(input("Enter Product ID to delete: "))
   app.delete_product(pid)

  elif choice == '4':
   pid = int(input("Enter Product ID to retrieve: "))
   product = app.get_product_by_pid(pid)
   print(product)

  elif choice == '5':
   products = app.get_all_products()
   print(products)
 
  elif choice == '6':
   category = input("Enter Product Category to search: ")
   products = app.get_products_by_category(category)
   print(products)
 
  elif choice == '7':
   min_price = float(input("Enter minimum price: "))
   max_price = float(input("Enter maximum price: "))
   products = app.get_products_between_prices(min_price, max_price)
   print(products)

  elif choice == '8':
   print("Exiting the app.")
   break
  
  else:
   print("Invalid choice! Please try again.")
if __name__ == "__main__":
 main()