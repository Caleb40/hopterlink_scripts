import os
import random
import time

import requests
from faker import Faker
from faker.providers.phone_number import Provider


class CustomPhoneNumberProvider(Provider):
    def nigeria_phone_number(self):
        return f"0{self.random_element(['702', '703', '704', '705', '706', '707', '708', '709'])}{self.random_number(digits=6)}"


# Initialize Faker and add the custom provider
fake = Faker()

fake.add_provider(CustomPhoneNumberProvider)

# Categories Data
categories = [
    {
        "name": "Home Services",
        "description": "Various home services including plumbing, electrical, and more.",
        "icon": "Home",
    },
    {
        "name": "Automotive Services",
        "description": "Automotive services including car repair, car wash, and more.",
        "icon": "Car",
    },
    {
        "name": "Health and Wellness",
        "description": "Health and wellness services including personal trainers, nutritionists, and more.",
        "icon": "HeartPulse",
    },
    {
        "name": "Beauty and Personal Care",
        "description": "Beauty and personal care services including hair stylists, makeup artists, and more.",
        "icon": "View",
    },
    {
        "name": "Education and Tutoring",
        "description": "Education and tutoring services including academic tutors, language instructors, and more.",
        "icon": "GraduationCap",
    },
    {
        "name": "Event Services",
        "description": "Event services including event planners, caterers, and more.",
        "icon": "PartyPopper",
    },
    {
        "name": "Business Services",
        "description": "Business services including accountants, bookkeepers, and more.",
        "icon": "Handshake",
    },
    {
        "name": "Home Improvement and Renovation",
        "description": "Home improvement and renovation services including general contractors, interior designers, and more.",
        "icon": "PaintRoller",
    },
    {
        "name": "Real Estate Services",
        "description": "Real estate services including real estate agents, property managers, and more.",
        "icon": "Caravan",
    },
    {
        "name": "Technology and Gadgets",
        "description": "Technology and gadgets services including computer repair, smartphone repair, and more.",
        "icon": "Cpu",
    },
    {
        "name": "Transportation and Moving",
        "description": "Transportation and moving services including movers, delivery services, and more.",
        "icon": "Truck"
    },
    {
        "name": "Pet Services",
        "description": "Pet services including pet grooming, pet sitting, and more.",
        "icon": "Dog",
    },
    {
        "name": "Fitness and Recreation",
        "description": "Fitness and recreation services including yoga instructors, pilates instructors, and more.",
        "icon": "Dumbbell",
    },
    {
        "name": "Crafts and DIY",
        "description": "Crafts and DIY services including tailors, furniture makers, and more.",
        "icon": "Brush",
    },
    {
        "name": "Writing and Content Creation",
        "description": "Writing and content creation services including freelance writers, copywriters, and more.",
        "icon": "PenTool",
    },
    {
        "name": "Consulting and Coaching",
        "description": "Consulting and coaching services including business consultants, life coaches, and more.",
        "icon": "Lightbulb",
    },
    {
        "name": "Financial Services",
        "description": "Financial services including tax preparers, financial planners, and more.",
        "icon": "Landmark",
    },
    {
        "name": "Childcare and Education",
        "description": "Childcare and education services including nannies, babysitters, and more.",
        "icon": "Baby",
    },
    {
        "name": "Specialty Services",
        "description": "Specialty services including personal assistants, concierge services, and more.",
        "icon": "Gem",
    },
    {
        "name": "Creative Services",
        "description": "Creative services including graphic designers, illustrators, and more.",
        "icon": "Palette",
    },
]

# SubcCategories Data
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
    "Event Services": [
        "Event Planners",
        "Caterers",
        "Photographers",
        "Videographers",
        "DJs and Musicians",
        "Florists",
        "Rental Services",
    ],
    "Business Services": [
        "Accountants",
        "Bookkeepers",
        "Financial Advisors",
        "Legal Services",
        "Marketing Consultants",
        "Graphic Designers",
        "Web Developers",
        "IT Support",
    ],
    "Home Improvement and Renovation": [
        "General Contractors",
        "Interior Designers",
        "Painters",
        "Flooring Specialists",
        "Kitchen and Bath Remodelers",
        "Window and Door Installers",
    ],
    "Real Estate Services": [
        "Real Estate Agents",
        "Property Managers",
        "Home Inspectors",
        "Real Estate Photographers",
        "Appraisers",
    ],
    "Technology and Gadgets": [
        "Computer Repair",
        "Smartphone Repair",
        "Home Theater Installation",
        "Smart Home Setup",
        "IT Networking",
    ],
    "Transportation and Moving": [
        "Movers",
        "Delivery Services",
        "Logistics Services",
        "Bike Couriers",
    ],
    "Pet Services": [
        "Pet Grooming",
        "Pet Sitting",
        "Dog Walking",
        "Veterinary Services",
        "Pet Training",
    ],
    "Fitness and Recreation": [
        "Yoga Instructors",
        "Pilates Instructors",
        "Sports Coaches",
        "Martial Arts Instructors",
    ],
    "Crafts and DIY": [
        "Tailors and Seamstresses",
        "Furniture Makers",
        "Custom Artisans",
    ],
    "Writing and Content Creation": [
        "Freelance Writers",
        "Copywriters",
        "Editors",
        "Translators",
        "Social Media Managers",
    ],
    "Consulting and Coaching": [
        "Business Consultants",
        "Life Coaches",
        "Career Coaches",
        "Health Coaches",
    ],
    "Financial Services": ["Tax Preparers", "Financial Planners", "Insurance Brokers"],
    "Childcare and Education": [
        "Nannies",
        "Babysitters",
        "Childcare Centers",
        "Early Childhood Educators",
    ],
    "Specialty Services": [
        "Personal Assistants",
        "Concierge Services",
        "Elderly Care Providers",
        "Errand Services",
    ],
    "Creative Services": [
        "Graphic Designers",
        "Illustrators",
        "Videographers",
        "Content Creators",
    ],
}

unique_names = {
    "Plumbing": ["PipeMasters", "FlowFixers", "AquaPipe Solutions"],
    "Electrical": ["WattWizards", "CurrentCare", "BrightSpark Electric"],
    "HVAC": ["AirComfort Pros", "ClimateMasters", "TempControl Experts"],
    "Carpentry": ["WoodWorks Creations", "Carpenter's Choice", "TimberCraft Solutions"],
    "Roofing": ["TopShield Roofing", "PeakRoof Services", "Skyline Roofing"],
    "Landscaping": ["GreenScape Designs", "Nature's Touch", "EcoLandscapes"],
    "Cleaning Services": ["SparkleClean", "PristineCleaners", "FreshStart Cleaning"],
    "Pest Control": ["BugBusters", "PestFree Solutions", "CritterControl"],
    "Car Repair": ["AutoFix Garage", "ProMechanics", "RepairMasters"],
    "Car Wash and Detailing": [
        "ShineAuto",
        "DetailPro Services",
        "CleanRide Detailing",
    ],
    "Towing Services": ["TowMasters", "RescueTowing", "FastTow Solutions"],
    "Tire Services": ["TirePros", "QuickTire", "TreadMasters"],
    "Auto Body Repair": ["BodyFixers", "ProAutoBody", "EliteCollision"],
    "Car Rental": ["RentRide", "AutoHire", "CarGo Rentals"],
    "Personal Trainers": ["FitLife Coaching", "ProFit Trainers", "PeakPerformance"],
    "Nutritionists": ["HealthWise Nutrition", "NutriGuide", "BalancedBites"],
    "Physical Therapists": ["RehabMasters", "PhysioCare", "MoveWell Therapy"],
    "Massage Therapists": ["RelaxRestore", "BodyHarmony", "WellnessTouch"],
    "Chiropractors": ["SpineCare", "ChiroHealth", "AlignWell Chiropractic"],
    "Mental Health Counselors": [
        "MindCare",
        "WellnessCounseling",
        "ThriveMental Health",
    ],
    "Acupuncturists": ["AcupunctureBalance", "NeedleHealing", "Acupoint Wellness"],
    "Hair Stylists": ["GlamourCuts Salon", "StyleStudio", "ChicHair Boutique"],
    "Makeup Artists": ["GlamGoddess Makeup", "RadiantBeauty Artistry", "FlawlessFaces"],
    "Nail Technicians": ["PolishPerfection", "NailArtistry", "GlamNails"],
    "Estheticians": ["SkinGlow Spa", "RadiantSkin", "PureBeauty"],
    "Barber Services": ["SharpCuts", "GroomingLounge", "BarberElite"],
    "Spa Services": ["TranquilSpa", "BlissfulRetreat", "HarmonySpa"],
    "Academic Tutors": ["SmartStudy", "TutorExperts", "LearnWell Tutors"],
    "Language Instructors": ["LinguaMasters", "LanguagePro", "FluentTutors"],
    "Music Teachers": ["MelodyMasters", "TuneTutors", "HarmonyLessons"],
    "Art Instructors": ["CreativeCanvas", "ArtisticMentors", "InspireArt"],
    "Test Preparation Tutors": ["PrepExperts", "ScoreHigh Tutors", "TestMasters"],
    "Skill Development": ["SkillBoosters", "ProSkill Development", "MasterSkills"],
    "Event Planners": ["EventCraft", "DreamEvents", "PerfectOccasions"],
    "Caterers": ["GourmetCatering", "TastefulEvents", "CuisineMasters"],
    "Photographers": ["CaptureMoments", "PicturePerfect", "ProShots Photography"],
    "Videographers": ["MotionMedia", "VisualStory", "FilmWorks"],
    "DJs and Musicians": ["SoundMasters", "RhythmPro", "BeatMix DJs"],
    "Florists": ["BloomingDesigns", "FloralElegance", "PetalPros"],
    "Rental Services": ["PartyRentals", "EventEssentials", "RentPro Services"],
    "Accountants": ["BalanceBooks", "ProAccounting", "AccurateAccounts"],
    "Bookkeepers": ["BookkeepingPros", "LedgerMasters", "ClearBooks"],
    "Financial Advisors": ["WealthWise", "FinancePro", "FutureFinance"],
    "Legal Services": ["LawMasters", "JusticeServed", "LegalPro"],
    "Marketing Consultants": ["MarketGurus", "BrandMasters", "ProMarketing"],
    "Graphic Designers": ["DesignGurus", "VisualMasters", "CreativeDesigns"],
    "Web Developers": ["WebCraft", "DigitalMasters", "CodeGenius"],
    "IT Support": ["TechAssist", "ITExperts", "TechSupportPros"],
    "General Contractors": ["BuildMasters", "ConstructPro", "EliteBuilders"],
    "Interior Designers": ["DesignGenius", "InteriorMasters", "HomeStyling"],
    "Painters": ["PaintPros", "ColorMasters", "ProPainters"],
    "Flooring Specialists": ["FloorCraft", "FlooringMasters", "EliteFloors"],
    "Kitchen and Bath Remodelers": ["RemodelMasters", "KitchenPro", "BathExperts"],
    "Window and Door Installers": ["WindowPro", "DoorMasters", "InstallExperts"],
    "Real Estate Agents": ["HomeFinders", "ProRealty", "EliteAgents"],
    "Property Managers": ["PropertyMasters", "EstatePro", "ManageRealty"],
    "Home Inspectors": ["InspectPros", "HomeCheck", "ProInspect"],
    "Real Estate Photographers": ["EstatePhotos", "HomeShots", "RealtyImages"],
    "Appraisers": ["ValueMasters", "ProAppraise", "EliteValuation"],
    "Computer Repair": ["TechFixers", "CompuCare", "PCPro Repair"],
    "Smartphone Repair": ["PhoneFixers", "MobileCare", "GadgetRepair"],
    "Home Theater Installation": ["TheaterPros", "HomeCinema", "EntertainmentInstall"],
    "Smart Home Setup": ["SmartLiving", "HomeAutomation", "SmartHome Experts"],
    "IT Networking": ["NetMasters", "TechNetwork", "ProNetworking"],
    "Movers": ["MovePros", "QuickMove", "EliteMovers"],
    "Delivery Services": ["DeliverMasters", "QuickDeliver", "ShipPro"],
    "Logistics Services": ["LogisticsPro", "FreightMasters", "CargoExperts"],
    "Bike Couriers": ["BikeDelivery", "CycleCourier", "BikeExpress"],
    "Pet Grooming": ["GroomMasters", "PetBeauty", "FurryFriends Grooming"],
    "Pet Sitting": ["PetSitters", "FurryCare", "PetWatch"],
    "Dog Walking": ["WalkMasters", "PawPals", "DogWalkPros"],
    "Veterinary Services": ["VetCare", "PetHealth", "VetMasters"],
    "Pet Training": ["TrainMasters", "PawAcademy", "ProPet Training"],
    "Yoga Instructors": ["YogaPros", "ZenYoga", "BalanceYoga"],
    "Pilates Instructors": ["PilatesMasters", "CorePilates", "FitPilates"],
    "Sports Coaches": ["CoachPros", "EliteCoaches", "ProAthlete"],
    "Martial Arts Instructors": ["MartialMasters", "FightPros", "CombatTraining"],
    "Tailors and Seamstresses": ["TailorMasters", "SewingPros", "FitTailors"],
    "Furniture Makers": ["FurnitureCraft", "WoodMasters", "CustomCreations"],
    "Custom Artisans": ["ArtisanCraft", "ProArtisans", "HandmadeMasters"],
    "Freelance Writers": ["WriteMasters", "ProWriters", "EliteWords"],
    "Copywriters": ["CopyCraft", "ProCopy", "CopyGenius"],
    "Editors": ["EditPros", "WordMasters", "ProEditors"],
    "Translators": ["TranslateMasters", "ProLinguists", "LanguageExperts"],
    "Social Media Managers": ["SocialMasters", "MediaPro", "SocialGurus"],
    "Business Consultants": ["BizConsult", "ProConsult", "ExpertAdvice"],
    "Life Coaches": ["LifeMasters", "CoachPro", "PersonalGrowth"],
    "Career Coaches": ["CareerMasters", "JobCoach", "CareerPros"],
    "Health Coaches": ["HealthMasters", "WellnessCoach", "FitLife"],
    "Tax Preparers": ["TaxPros", "ReturnMasters", "ProTaxPrep"],
    "Financial Planners": ["FinanceMasters", "WealthPlanning", "MoneyGurus"],
    "Insurance Brokers": ["InsurePros", "PolicyMasters", "CoverageGenius"],
    "Nannies": ["NannyMasters", "CarePro", "EliteNannies"],
    "Babysitters": ["SittersPro", "BabyCare", "KidWatch"],
    "Childcare Centers": ["KidMasters", "ChildCarePro", "KidZone"],
    "Early Childhood Educators": ["EarlyEdu", "ChildLearn", "ProEarlyEd"],
    "Personal Assistants": ["AssistPros", "TaskMasters", "PersonalHelp"],
    "Concierge Services": ["ConciergePros", "VIPServices", "LuxuryConcierge"],
    "Elderly Care Providers": ["ElderCarePros", "SeniorAssist", "GoldenCare"],
    "Errand Services": ["ErrandMasters", "TaskRunners", "QuickErrands"],
    "Graphic Designers": ["DesignGurus", "VisualMasters", "CreativeDesigns"],
    "Illustrators": ["ArtMasters", "IllustrationPros", "CreativeSketches"],
    "Videographers": ["FilmMasters", "VideoPros", "VisualStory"],
    "Content Creators": ["MythBusters", "Veritasium", "VSauce"],
}

BASE_URL = "https://hopterlink.up.railway.app"
BUSINESSES_PER_SUBCATEGORY = 3


def format_eta(eta_seconds):
    hours = eta_seconds // 3600
    minutes = (eta_seconds % 3600) // 60
    seconds = eta_seconds % 60
    return f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"


def authenticate_admin():
    url = f"{BASE_URL}/auth/login/"
    email = "calebseyi123@gmail.com"
    password = "mnb111"
    response = requests.post(url, data={"email": email, "password": password})
    if response.status_code == 200:
        return response.cookies
    else:
        print("Failed to authenticate admin:", response.text)
        return None


def create_user_and_authenticate():
    url = f"{BASE_URL}/auth/registration/"
    email = fake.email()
    password1 = "p@55w0rd"
    password2 = "p@55w0rd"
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.nigeria_phone_number()

    response = requests.post(
        url=url,
        data={
            "email": email,
            "password1": password1,
            "password2": password2,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
        },
    )

    if response.status_code != 201:
        print("Error while creating user:", response.text)
        return None

    user = response.json()["user"]

    login = requests.post(
        f"{BASE_URL}/auth/login/",
        data={"email": user.get("email"), "password": password1},
    )

    if login.status_code != 200:
        print("Error while logging in:", login.text)
        return None

    return login.cookies


def create_category(name, description, icon, admin_cookies):
    print(f"Creating category: {name}")
    response = requests.post(
        f"{BASE_URL}/api/categories/",
        json={"name": name, "description": description, "icon": icon},
        cookies=admin_cookies,
    )
    if response.status_code == 201:
        print(f"Category {name} created successfully.")
        return response.json()["id"]
    else:
        print(f"Failed to create category {name}: {response.content}")
        return None


def create_subcategory(category_id, name, admin_cookies):
    print(f"Creating subcategory: {name}")
    response = requests.post(
        f"{BASE_URL}/api/categories/{category_id}/subcategories/",
        json={"name": name, "category": category_id},
        cookies=admin_cookies,
    )
    if response.status_code != 201:
        print(f"Failed to create subcategory {name}: {response.content}")
        return None
    return response.json()


def create_business(
    cookies,
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
    images_folder="images_compressed/",
):
    print(f"Creating business: {business_name}")
    image_files = random.sample(os.listdir(images_folder), random.randint(2, 5))
    files = [
        ("uploaded_images", open(os.path.join(images_folder, img), "rb"))
        for img in image_files
    ]
    response = requests.post(
        f"{BASE_URL}/api/businesses/",
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


def main():
    admin_cookies = authenticate_admin()
    if not admin_cookies:
        print("Failed to authenticate admin.")
        return

    total_businesses = sum(
        len(subcategories[category["name"]]) * BUSINESSES_PER_SUBCATEGORY
        for category in categories
    )
    businesses_created = 0
    start_time = time.time()

    for category in categories:
        category_name = category["name"]
        category_id = create_category(
            category_name, category["description"], category["icon"], admin_cookies
        )
        if category_id:
            for subcategory in subcategories.get(category_name, []):
                subcategory_json = create_subcategory(
                    category_id, subcategory, admin_cookies
                )
                if subcategory_json["id"]:
                    for _ in range(BUSINESSES_PER_SUBCATEGORY):
                        user_cookies = create_user_and_authenticate()
                        if not user_cookies:
                            print("Failed to create user and authenticate.")
                            return
                        email = fake.email()
                        business_name = random.choices(
                            unique_names.get(subcategory_json["name"], [fake.company()])
                        )[0]
                        location = fake.address()
                        description = fake.catch_phrase()
                        website = fake.url()
                        business_phone_1 = fake.nigeria_phone_number()
                        min_delivery_time_in_days = fake.random_int(min=1, max=5)
                        max_delivery_time_in_days = fake.random_int(min=6, max=15)

                        business_start_time = time.time()
                        create_business(
                            user_cookies,
                            email,
                            business_name,
                            location,
                            description,
                            website,
                            business_phone_1,
                            min_delivery_time_in_days,
                            max_delivery_time_in_days,
                            category_id,
                            subcategory_json["id"],
                        )
                        business_end_time = time.time()
                        businesses_created += 1
                        elapsed_time = business_end_time - business_start_time
                        avg_time_per_business = (
                            business_end_time - start_time
                        ) / businesses_created
                        businesses_left = total_businesses - businesses_created
                        eta = avg_time_per_business * businesses_left

                        print(
                            f"Business {business_name} creation time: {format_eta(elapsed_time)}"
                        )
                        print(
                            f"Average time per business: {format_eta(avg_time_per_business)}"
                        )
                        print(f"Businesses left: {businesses_left}")
                        print(f"Estimated time to complete: {format_eta(eta)}")

        else:
            continue


if __name__ == "__main__":
    main()
