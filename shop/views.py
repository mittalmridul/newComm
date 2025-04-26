from django.shortcuts import render

def home_view(request):
    products = [
        {
            "id": 1,
            "name": "Premium Wireless Headphones",
            "price": "$49.99",
            "image": "https://picsum.photos/seed/p1/400/300",
            "description": "High-quality wireless headphones with noise cancellation and 20-hour battery life.",
            "category": "Electronics",
            "rating": "4.5",
            "stock": "In Stock",
            "specs": ["Bluetooth 5.0", "Active Noise Cancellation", "20hr Battery"]
        },
        {
            "id": 2,
            "name": "Smart Fitness Watch",
            "price": "$79.99",
            "image": "https://picsum.photos/seed/p2/400/300",
            "description": "Track your fitness goals with this advanced smartwatch. Features heart rate monitoring and sleep tracking.",
            "category": "Wearables",
            "rating": "4.8",
            "stock": "Only 3 left",
            "specs": ["Heart Rate Monitor", "Sleep Tracking", "Water Resistant"]
        },
        {
            "id": 3,
            "name": "Portable Power Bank",
            "price": "$29.99",
            "image": "https://picsum.photos/seed/p3/400/300",
            "description": "10000mAh portable charger with fast charging capability. Perfect for travel.",
            "category": "Accessories",
            "rating": "4.3",
            "stock": "In Stock",
            "specs": ["10000mAh", "Fast Charging", "Dual USB Ports"]
        },
        {
            "id": 4,
            "name": "Wireless Mouse",
            "price": "$19.99",
            "image": "https://picsum.photos/seed/p4/400/300",
            "description": "Ergonomic wireless mouse with adjustable DPI and silent clicks.",
            "category": "Accessories",
            "rating": "4.6",
            "stock": "In Stock",
            "specs": ["Ergonomic", "Adjustable DPI", "Silent Clicks"]
        },
        {
            "id": 5,
            "name": "Bluetooth Speaker",
            "price": "$39.99",
            "image": "https://picsum.photos/seed/p5/400/300",
            "description": "Portable Bluetooth speaker with deep bass and 12-hour playtime.",
            "category": "Electronics",
            "rating": "4.7",
            "stock": "Only 2 left",
            "specs": ["Deep Bass", "12hr Playtime", "Water Resistant"]
        },
        {
            "id": 6,
            "name": "Smart LED Bulb",
            "price": "$14.99",
            "image": "https://picsum.photos/seed/p6/400/300",
            "description": "Color-changing smart bulb compatible with Alexa and Google Home.",
            "category": "Home",
            "rating": "4.2",
            "stock": "In Stock",
            "specs": ["Color Changing", "Voice Control", "Energy Efficient"]
        },
        {
            "id": 7,
            "name": "USB-C Charging Cable",
            "price": "$9.99",
            "image": "https://picsum.photos/seed/p7/400/300",
            "description": "Durable USB-C cable for fast charging and data transfer.",
            "category": "Accessories",
            "rating": "4.4",
            "stock": "In Stock",
            "specs": ["Fast Charging", "Durable", "1.5m Length"]
        },
        {
            "id": 8,
            "name": "Noise Cancelling Earbuds",
            "price": "$59.99",
            "image": "https://picsum.photos/seed/p8/400/300",
            "description": "Compact earbuds with active noise cancellation and touch controls.",
            "category": "Electronics",
            "rating": "4.6",
            "stock": "Only 5 left",
            "specs": ["Active Noise Cancellation", "Touch Controls", "Compact Design"]
        },
        {
            "id": 9,
            "name": "Fitness Tracker Band",
            "price": "$24.99",
            "image": "https://picsum.photos/seed/p9/400/300",
            "description": "Lightweight fitness band with step and calorie tracking.",
            "category": "Wearables",
            "rating": "4.1",
            "stock": "In Stock",
            "specs": ["Step Tracking", "Calorie Tracking", "Water Resistant"]
        },
        {
            "id": 10,
            "name": "Laptop Stand",
            "price": "$34.99",
            "image": "https://picsum.photos/seed/p10/400/300",
            "description": "Adjustable laptop stand for better ergonomics and cooling.",
            "category": "Accessories",
            "rating": "4.5",
            "stock": "In Stock",
            "specs": ["Adjustable", "Portable", "Aluminum"]
        },
        {
            "id": 11,
            "name": "Wireless Charger Pad",
            "price": "$22.99",
            "image": "https://picsum.photos/seed/p11/400/300",
            "description": "Qi-certified wireless charging pad for smartphones.",
            "category": "Electronics",
            "rating": "4.3",
            "stock": "In Stock",
            "specs": ["Qi Certified", "Fast Charging", "Slim Design"]
        },
        {
            "id": 12,
            "name": "Smart Plug",
            "price": "$17.99",
            "image": "https://picsum.photos/seed/p12/400/300",
            "description": "WiFi smart plug for remote control of home appliances.",
            "category": "Home",
            "rating": "4.4",
            "stock": "In Stock",
            "specs": ["WiFi Control", "Voice Assistant Compatible", "Energy Monitoring"]
        },
        {
            "id": 13,
            "name": "Gaming Keyboard",
            "price": "$69.99",
            "image": "https://picsum.photos/seed/p13/400/300",
            "description": "Mechanical gaming keyboard with RGB lighting.",
            "category": "Electronics",
            "rating": "4.7",
            "stock": "Only 1 left",
            "specs": ["Mechanical", "RGB Lighting", "Anti-Ghosting"]
        },
        {
            "id": 14,
            "name": "4K Action Camera",
            "price": "$99.99",
            "image": "https://picsum.photos/seed/p14/400/300",
            "description": "Waterproof 4K action camera with wide-angle lens.",
            "category": "Electronics",
            "rating": "4.5",
            "stock": "In Stock",
            "specs": ["4K Video", "Waterproof", "Wide Angle"]
        },
        {
            "id": 15,
            "name": "Mini Projector",
            "price": "$89.99",
            "image": "https://picsum.photos/seed/p15/400/300",
            "description": "Portable mini projector for home entertainment.",
            "category": "Electronics",
            "rating": "4.2",
            "stock": "In Stock",
            "specs": ["Portable", "HD Ready", "Built-in Speaker"]
        },
    ]
    return render(request, "home.html", {
        "products": products,
        "paginator_count": len(products),
    })

def contact_view(request):
    return render(request, "contact.html")
