import json

with open('suppliers.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('table_suppliers.sql', 'w', encoding='utf-8') as file:
    creat_table = """
CREATE TABLE IF NOT EXISTS suppliers (
    id smallint PRIMARY KEY,
    company_name character varying(40) NOT NULL,
    contact_name character varying(30),
    contact_title character varying(30),
    country character varying(15),
    city character varying(15),
    postal_code character varying(10),
    region character varying(15),
    address character varying(60),
    phone character varying(100),
    fax character varying(100),
    homepage character varying(100)
);


"""
    file.write(creat_table)

    count = 1
    for d in data:
        suppliers = f"""INSERT INTO suppliers VALUES ({count}, '{d["company_name"].replace("'", " ")}', '{d["contact"].split(",")[0]}', '{d["contact"].split(",")[1]}', '{d["address"].split(";")[0]}', '{d["address"].split(';')[1]}', '{d["address"].split(";")[2]}', '{d["address"].split(";")[3]}', '{d["address"].split(";")[4].replace("'", " ")}', '{d["phone"]}', '{d["fax"]}', '{d["homepage"].replace("'", " ")}');\n"""
        file.write(suppliers)
        count += 1



