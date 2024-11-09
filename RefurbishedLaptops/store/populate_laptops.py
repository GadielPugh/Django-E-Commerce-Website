from store.models import Laptop

def populate_laptops():
    laptops = [
        {
            "manufacturer": "Dell",
            "processor_type": "Intel Core i5",
            "ram_size": 8,
            "storage_type": "SSD",
            "storage_size": 256,
            "usb_ports": 3,
            "sale_price": 799.99,
            "name": "Dell Inspiron",
            "description": "A reliable laptop for everyday use.",
            "photo": ""  
        },
        {
            "manufacturer": "Dell",
            "processor_type": "Intel Core i5",
            "ram_size": 8,
            "storage_type": "SSD",
            "storage_size": 256,
            "usb_ports": 3,
            "sale_price": 799.99,
            "name": "Dell Inspiron",
            "description": "A reliable laptop for everyday use.",
            "photo": ""  
        },
            {
            "manufacturer": "Apple",
            "processor_type": "Apple M1",
            "ram_size": 8,
            "storage_type": "SSD",
            "storage_size": 256,
            "usb_ports": 2,
            "sale_price": 999.99,
            "name": "MacBook Air",
            "description": "The ultra-portable laptop with Apple's M1 chip, perfect for everyday tasks and light creative work.",
            "photo": "https://example.com/macbook_air.jpg"
        },
        {
            "manufacturer": "HP",
            "processor_type": "Intel Core i7",
            "ram_size": 16,
            "storage_type": "SSD",
            "storage_size": 512,
            "usb_ports": 3,
            "sale_price": 1199.99,
            "name": "HP Envy 13",
            "description": "A powerful 13-inch laptop with an Intel Core i7 processor, ideal for productivity and media consumption.",
            "photo": "https://example.com/hp_envy_13.jpg"
        },
        {
            "manufacturer": "Lenovo",
            "processor_type": "Intel Core i5",
            "ram_size": 8,
            "storage_type": "HDD",
            "storage_size": 1,
            "usb_ports": 4,
            "sale_price": 649.99,
            "name": "Lenovo ThinkPad E15",
            "description": "A durable business laptop with a 15.6-inch screen, designed for professionals who need reliability.",
            "photo": "https://example.com/lenovo_thinkpad_e15.jpg"
        },
        {
            "manufacturer": "Asus",
            "processor_type": "AMD Ryzen 7",
            "ram_size": 16,
            "storage_type": "SSD",
            "storage_size": 512,
            "usb_ports": 4,
            "sale_price": 1399.99,
            "name": "Asus ROG Zephyrus G14",
            "description": "A high-performance gaming laptop with AMD Ryzen 7 processor and NVIDIA GeForce GTX 1660 Ti.",
            "photo": "https://example.com/asus_rog_zephyrus_g14.jpg"
        },
        {
            "manufacturer": "Microsoft",
            "processor_type": "Intel Core i5",
            "ram_size": 8,
            "storage_type": "SSD",
            "storage_size": 128,
            "usb_ports": 2,
            "sale_price": 899.99,
            "name": "Microsoft Surface Laptop 4",
            "description": "A sleek, lightweight laptop with a high-resolution display and long battery life, ideal for students and professionals.",
            "photo": "https://example.com/surface_laptop_4.jpg"
        },
        {
            "manufacturer": "Acer",
            "processor_type": "Intel Core i5",
            "ram_size": 8,
            "storage_type": "SSD",
            "storage_size": 256,
            "usb_ports": 3,
            "sale_price": 749.99,
            "name": "Acer Aspire 5",
            "description": "A budget-friendly laptop with a solid performance for work and entertainment, offering excellent value for money.",
            "photo": "https://example.com/acer_aspire_5.jpg"
        },
    ]

    for laptop_data in laptops:
        Laptop.objects.create(**laptop_data)
    print("Sample laptops added.")
