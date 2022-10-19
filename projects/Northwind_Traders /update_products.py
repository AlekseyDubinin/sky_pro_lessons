import json

with open('suppliers.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

count = 1
with open('update_table_products.sql', 'w', encoding='utf-8') as file:
    for d in data:
        d['id'] = count
        prod = [i.replace("'", "''") for i in d['products']]
        update_table = f"""
        UPDATE products 
        SET id_suppliers = {d['id']} 
        WHERE product_name in ('{"', '".join(prod)}');\n
        """
        file.write(update_table)
        count += 1
