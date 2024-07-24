import requests
from faker import Faker

base_url = "http://localhost:8000"

# Updated list of unique business names related to categories and subcategories
business_names = [
    "Home Solutions Plumbing", "Electric Fixes", "HVAC Experts", "Carpentry Craft", "Roof Masters", "Green Landscaping",
    "Clean Sweep Services", "Pest Busters",
    "Speedy Auto Repair", "Detailing Dynamics", "Tow Truck Pros", "Tire Techs", "Body Shop Wizards", "Rental Ride Hub",
    "Wellness Trainers", "Nutrition Now", "Therapy Haven", "Massage Magic", "Chiro Care", "Mental Health Hub",
    "Acupuncture Experts",
    "Hair Design Studio", "Makeup Magic", "Nail Artistry", "Skin Care Studio", "Barber Zone", "Spa Retreat",
    "Top Tutors", "Language Learners", "Music Masters", "Artistic Instructors", "Test Prep Gurus", "Skill Builders",
    "Event Planners", "Catering Excellence", "Photo Studio", "Video Visionaries", "DJ Beats", "Floral Creations",
    "Event Rentals",
    "Accounting Ace", "Bookkeeping Bliss", "Finance Wizards", "Legal Experts", "Marketing Masterminds", "Design Studio",
    "Web Wizards", "IT Support Solutions",
    "Contractor Crew", "Interior Innovations", "Painter Pros", "Flooring Experts", "Remodel Masters",
    "Window Installations",
    "Real Estate Advisors", "Property Managers", "Inspection Experts", "Photo Real Estate", "Appraisal Authority",
    "Tech Repair Center", "Smartphone Fix", "Home Theater Hub", "Smart Home Solutions", "Network Experts",
    "Moving Masters", "Delivery Express", "Logistics Leaders", "Bike Couriers",
    "Pet Grooming Lounge", "Pet Sitting Services", "Dog Walkers", "Vet Clinic", "Pet Training Academy",
    "Yoga Wellness", "Pilates Precision", "Sports Coaching Hub", "Martial Arts Academy",
    "Tailoring Trends", "Custom Furniture Studio", "Artisan Creations",
    "Freelance Writers Hub", "Copywriting Pros", "Editing Experts", "Translation Services", "Social Media Wizards",
    "Consulting Solutions", "Life Coaching Center", "Career Coaching Hub", "Health Coaching",
    "Tax Prep Experts", "Financial Planning Hub", "Insurance Solutions",
    "Nanny Network", "Babysitting Services", "Childcare Centers", "Early Education Experts",
    "Personal Assistant Hub", "Concierge Services", "Elder Care Solutions", "Errand Running Services",
    "Graphic Design Studio", "Illustration Experts", "Video Production Hub", "Content Creation Agency",
]


def create_users():
    faker = Faker()
    Faker.seed(0)

    with open('log.txt', "a") as f:
        for i, business_name in enumerate(business_names, start=1):
            print(f"Creating user for business: {business_name} ({i}/{len(business_names)})")
            email = faker.email()
            first_name = faker.first_name()
            last_name = faker.last_name()
            phone = f"080{faker.random_int(min=10000000, max=99999999)}"

            payload = {
                "email": email,
                "password1": "p@55w0rd",
                "password2": "p@55w0rd",
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
            }

            try:
                response = requests.post(f"{base_url}/auth/registration/", data=payload)
                response.raise_for_status()  # Raise HTTPError for bad responses

                if response.status_code == 201:
                    f.write(f"User for {business_name} created successfully.\n")
                    print(f"User for {business_name} created successfully.")
                else:
                    f.write(f"Failed to create user for {business_name}: {response.status_code}, {response.text}\n")
                    print(f"Failed to create user for {business_name}: {response.status_code}")

            except requests.RequestException as e:
                f.write(f"Error occurred for {business_name}: {e}\n")
                print(f"Error occurred for {business_name}: {e}")


if __name__ == "__main__":
    create_users()
