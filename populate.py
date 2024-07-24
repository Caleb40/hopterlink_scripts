import os
import random

import requests
from faker import Faker

BASE_URL = "http://localhost:8000/api"

cookies = {
    "sessionid": "xljvaakh7h170alzzo15our705pewkjn",
    "hopterlink-refresh-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjA0ODcxMSwiaWF0IjoxNzIxNjE2NzExLCJqdGkiOiJmMjk4OWE4Mzg4MDk0Nzg2YTA3N2QzYThmYjQxOTU3MSIsInVzZXJfaWQiOjF9.smPx5mwUkelmPWPjrfZDFzPVUZY7X6p-A0oVEWJR5V0",
    "hopterlink-auth-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxNzAzMTExLCJpYXQiOjE3MjE2MTY3MTEsImp0aSI6IjY0YzJkNDVlNDRlYzRlMTNhZWYwNGVmYjU0MmZiYzhhIiwidXNlcl9pZCI6MX0.xP-9b3_OhEothpfUSfNso9CO_OWdkFXnVjq81CZzIcU",
    "csrftoken": "KK9CHqQBxlRELW86q9gPvTq831khJNVl",
}

categories = [
    {
        "name": "Home Services",
        "description": "Various home services including plumbing, electrical, and more.",
    },
    {
        "name": "Automotive Services",
        "description": "Automotive services including car repair, car wash, and more.",
    },
    {
        "name": "Health and Wellness",
        "description": "Health and wellness services including personal trainers, nutritionists, and more.",
    },
    {
        "name": "Beauty and Personal Care",
        "description": "Beauty and personal care services including hair stylists, makeup artists, and more.",
    },
    {
        "name": "Education and Tutoring",
        "description": "Education and tutoring services including academic tutors, language instructors, and more.",
    },
    # {
    #     "name": "Event Services",
    #     "description": "Event services including event planners, caterers, and more.",
    # },
    # {
    #     "name": "Business Services",
    #     "description": "Business services including accountants, bookkeepers, and more.",
    # },
    # {
    #     "name": "Home Improvement and Renovation",
    #     "description": "Home improvement and renovation services including general contractors, interior designers, and more.",
    # },
    # {
    #     "name": "Real Estate Services",
    #     "description": "Real estate services including real estate agents, property managers, and more.",
    # },
    # {
    #     "name": "Technology and Gadgets",
    #     "description": "Technology and gadgets services including computer repair, smartphone repair, and more.",
    # },
    # {
    #     "name": "Transportation and Moving",
    #     "description": "Transportation and moving services including movers, delivery services, and more.",
    # },
    # {
    #     "name": "Pet Services",
    #     "description": "Pet services including pet grooming, pet sitting, and more.",
    # },
    # {
    #     "name": "Fitness and Recreation",
    #     "description": "Fitness and recreation services including yoga instructors, pilates instructors, and more.",
    # },
    # {
    #     "name": "Crafts and DIY",
    #     "description": "Crafts and DIY services including tailors, furniture makers, and more.",
    # },
    # {
    #     "name": "Writing and Content Creation",
    #     "description": "Writing and content creation services including freelance writers, copywriters, and more.",
    # },
    # {
    #     "name": "Consulting and Coaching",
    #     "description": "Consulting and coaching services including business consultants, life coaches, and more.",
    # },
    # {
    #     "name": "Financial Services",
    #     "description": "Financial services including tax preparers, financial planners, and more.",
    # },
    # {
    #     "name": "Childcare and Education",
    #     "description": "Childcare and education services including nannies, babysitters, and more.",
    # },
    # {
    #     "name": "Specialty Services",
    #     "description": "Specialty services including personal assistants, concierge services, and more.",
    # },
    # {
    #     "name": "Creative Services",
    #     "description": "Creative services including graphic designers, illustrators, and more.",
    # },
]

subcategories = {
    "Home Services": [
        "Plumbing",
        "Electrical",
        "HVAC",
        "Carpentry",
        "Roofing",
        "Landscaping",
        "Cleaning Services",
        "Pest Control",
    ],
    "Automotive Services": [
        "Car Repair",
        "Car Wash and Detailing",
        "Towing Services",
        "Tire Services",
        "Auto Body Repair",
        "Car Rental",
    ],
    "Health and Wellness": [
        "Personal Trainers",
        "Nutritionists",
        "Physical Therapists",
        "Massage Therapists",
        "Chiropractors",
        "Mental Health Counselors",
        "Acupuncturists",
    ],
    "Beauty and Personal Care": [
        "Hair Stylists",
        "Makeup Artists",
        "Nail Technicians",
        "Estheticians",
        "Barber Services",
        "Spa Services",
    ],
    "Education and Tutoring": [
        "Academic Tutors",
        "Language Instructors",
        "Music Teachers",
        "Art Instructors",
        "Test Preparation Tutors",
        "Skill Development",
    ],
    # "Event Services": [
    #     "Event Planners",
    #     "Caterers",
    #     "Photographers",
    #     "Videographers",
    #     "DJs and Musicians",
    #     "Florists",
    #     "Rental Services",
    # ],
    # "Business Services": [
    #     "Accountants",
    #     "Bookkeepers",
    #     "Financial Advisors",
    #     "Legal Services",
    #     "Marketing Consultants",
    #     "Graphic Designers",
    #     "Web Developers",
    #     "IT Support",
    # ],
    # "Home Improvement and Renovation": [
    #     "General Contractors",
    #     "Interior Designers",
    #     "Painters",
    #     "Flooring Specialists",
    #     "Kitchen and Bath Remodelers",
    #     "Window and Door Installers",
    # ],
    # "Real Estate Services": [
    #     "Real Estate Agents",
    #     "Property Managers",
    #     "Home Inspectors",
    #     "Real Estate Photographers",
    #     "Appraisers",
    # ],
    # "Technology and Gadgets": [
    #     "Computer Repair",
    #     "Smartphone Repair",
    #     "Home Theater Installation",
    #     "Smart Home Setup",
    #     "IT Networking",
    # ],
    # "Transportation and Moving": [
    #     "Movers",
    #     "Delivery Services",
    #     "Logistics Services",
    #     "Bike Couriers",
    # ],
    # "Pet Services": [
    #     "Pet Grooming",
    #     "Pet Sitting",
    #     "Dog Walking",
    #     "Veterinary Services",
    #     "Pet Training",
    # ],
    # "Fitness and Recreation": [
    #     "Yoga Instructors",
    #     "Pilates Instructors",
    #     "Sports Coaches",
    #     "Martial Arts Instructors",
    # ],
    # "Crafts and DIY": [
    #     "Tailors and Seamstresses",
    #     "Furniture Makers",
    #     "Custom Artisans",
    # ],
    # "Writing and Content Creation": [
    #     "Freelance Writers",
    #     "Copywriters",
    #     "Editors",
    #     "Translators",
    #     "Social Media Managers",
    # ],
    # "Consulting and Coaching": [
    #     "Business Consultants",
    #     "Life Coaches",
    #     "Career Coaches",
    #     "Health Coaches",
    # ],
    # "Financial Services": ["Tax Preparers", "Financial Planners", "Insurance Brokers"],
    # "Childcare and Education": [
    #     "Nannies",
    #     "Babysitters",
    #     "Childcare Centers",
    #     "Early Childhood Educators",
    # ],
    # "Specialty Services": [
    #     "Personal Assistants",
    #     "Concierge Services",
    #     "Elderly Care Providers",
    #     "Errand Services",
    # ],
    # "Creative Services": [
    #     "Graphic Designers",
    #     "Illustrators",
    #     "Videographers",
    #     "Content Creators",
    # ],
}


def create_category(name, description):
    print(f"Creating category: {name}")
    response = requests.post(
        f"{BASE_URL}/categories/",
        json={"name": name, "description": description},
        cookies=cookies,
    )
    if response.status_code == 201:
        print(f"Category {name} created successfully.")
        return response.json()["id"]
    else:
        print(f"Failed to create category {name}: {response.content}")
        return None


def create_subcategory(category_id, name):
    print(f"Creating subcategory: {name}")
    response = requests.post(
        f"{BASE_URL}/categories/{category_id}/subcategories/",
        json={"name": name, "category": category_id},
        cookies=cookies,
    )
    if response.status_code != 201:
        print(f"Failed to create subcategory {name}: {response.content}")
    return response.json()["id"]


def create_business(
        email,
        business_name,
        location,
        description,
        website,
        business_phone_1,
        min_delivery_time_in_days,
        max_delivery_time_in_days,
        industry,
        industry_subcategory,
        images_folder="images_compressed/"
):
    print(f"Creating business: {business_name}")
    image_files = random.sample(os.listdir(images_folder), random.randint(2, 5))
    files = [("uploaded_images", open(os.path.join(images_folder, img), 'rb')) for img in image_files]
    response = requests.post(
        f"{BASE_URL}/businesses/",
        files=files,
        data={
            "email": email,
            "business_name": business_name,
            "location": location,
            "description": description,
            "website": website,
            "business_phone_1": business_phone_1,
            "min_delivery_time_in_days": min_delivery_time_in_days,
            "max_delivery_time_in_days": max_delivery_time_in_days,
            "industry": industry,
            "industry_subcategory": industry_subcategory,
        },
        cookies=cookies,
    )
    for file in files:
        file[1].close()
    if response.status_code != 201:
        print(f"Failed to create business {business_name}: {response.content}")
    else:
        print(f"Business {business_name} created successfully.")


def populate_businesses():
    fake = Faker()
    for category in categories:
        category_name = category["name"]
        category_id = create_category(category_name, category["description"])
        if category_id:
            for subcategory in subcategories.get(category_name, []):
                subcategory_id = create_subcategory(category_id, subcategory)
                for _ in range(4):  # Create 4 businesses per subcategory
                    email = fake.email()
                    business_name = fake.company()
                    location = fake.address()
                    description = fake.catch_phrase()
                    website = fake.url()
                    business_phone_1 = fake.phone_number()
                    min_delivery_time_in_days = fake.random_int(min=1, max=5)
                    max_delivery_time_in_days = fake.random_int(min=6, max=15)
                    create_business(
                        email,
                        business_name,
                        location,
                        description,
                        website,
                        business_phone_1,
                        min_delivery_time_in_days,
                        max_delivery_time_in_days,
                        category_id,
                        subcategory_id,
                    )


if __name__ == "__main__":
    print("Starting population of businesses.")
    populate_businesses()
    print("Finished population of businesses.")
