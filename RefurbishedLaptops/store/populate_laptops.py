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
    ]

    for laptop_data in laptops:
        Laptop.objects.create(**laptop_data)
    print("Sample laptops added.")
