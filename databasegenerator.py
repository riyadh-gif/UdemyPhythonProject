import os
from faker import Faker #pip install faker

# Inisialisasi Faker
fake = Faker()

# Nama file SQL output
output_file = "fake_data.sql"

# Fungsi untuk membuat data SQL insert
def generate_sql_insert(num_records=1000):
    sql_insert = "INSERT INTO users (first_name, last_name, email, address, city, country, phone_number) VALUES\n"
    values = []
    for _ in range(num_records):
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        email = fake.email().replace("'", "''")
        address = fake.address().replace("\n", " ").replace("'", "''")
        city = fake.city().replace("'", "''")
        country = fake.country().replace("'", "''")
        phone_number = fake.phone_number().replace("'", "''")
        values.append(f"('{first_name}', '{last_name}', '{email}', '{address}', '{city}', '{country}', '{phone_number}')")
    sql_insert += ",\n".join(values) + ";\n"
    return sql_insert

# Membuka file output dan menulis data
with open(output_file, 'w') as f:
    file_size = 0
    target_size = 5 * 1024 * 1024 * 1024  # 5 GB in bytes
    record_count = 1000  # Jumlah record per insert

    while file_size < target_size:
        sql_data = generate_sql_insert(record_count)
        f.write(sql_data)
        f.flush()  # Memastikan data tertulis ke file
        file_size = os.path.getsize(output_file)
        print(f"Current file size: {file_size / (1024 * 1024):.2f} MB")

print(f"File SQL sebesar {file_size / (1024 * 1024 * 1024):.2f} GB telah dihasilkan.")
