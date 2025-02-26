from django.db import models

# Create your models here.

class SubmittedIssue(models.Model):
    CATEGORY_CHOICES = [
        ("infrastructure", "Infrastructure & Maintenance"),
        ("waste", "Waste Management & Recycling"),
        ("safety", "Public Safety & Crime"),
        ("noise", "Noise & Environmental Nuisances"),
        ("traffic", "Parking & Traffic Issues"),
        ("housing", "Housing & Property Concerns"),
        ("transport", "Public Transport Complaints"),
        ("parks", "Green Spaces & Parks"),
        ("water", "Water & Sewage Issues"),
        ("licensing", "Licensing & Regulatory Complaints"),
        ("animals", "Animal-Related Concerns"),
        ("accessibility", "Accessibility & Disability Issues"),
        ("health", "Public Health & Hygiene"),
        ("council", "Council Services & Administration"),
        ("other", "Other"),
    ]

    SUBCATEGORY_CHOICES = {
        "infrastructure": [
            ("potholes", "Potholes and road surface damage"),
            ("street_signs", "Damaged or missing street signs"),
            ("street_lights", "Faulty or non-functioning streetlights"),
            ("pavements", "Broken or dangerous pavements"),
            ("drains", "Blocked or overflowing drains"),
            ("bridges", "Bridge or tunnel damage"),
            ("benches", "Issues with public benches or shelters"),
        ],
        "waste": [
            ("missed_bins", "Missed bin collections"),
            ("public_bins", "Overflowing public bins"),
            ("fly_tipping", "Fly-tipping and illegal dumping"),
            ("recycling", "Lack of recycling facilities"),
            ("hazardous_waste", "Hazardous waste disposal concerns"),
        ],
        "safety": [
            ("vandalism", "Vandalism and graffiti"),
            ("antisocial", "Anti-social behavior"),
            ("drugs", "Drug use or dealing in public areas"),
            ("loitering", "Loitering and public disturbances"),
            ("cctv", "Concerns about CCTV coverage"),
        ],
        "noise": [
            ("parties", "Loud parties or persistent noise complaints"),
            ("industrial", "Industrial or construction noise violations"),
            ("bonfires", "Bonfires and smoke nuisances"),
            ("light_pollution", "Light pollution concerns"),
        ],
        "traffic": [
            ("illegal_parking", "Illegal or obstructive parking"),
            ("abandoned_vehicles", "Abandoned vehicles"),
            ("speeding", "Speeding and reckless driving"),
            ("congestion", "Traffic congestion hotspots"),
            ("road_signs", "Poorly marked or confusing road signage"),
        ],
        "housing": [
            ("unsafe_housing", "Unsafe or unfit council housing conditions"),
            ("mold", "Damp, mold, or structural issues in council homes"),
            ("tenant_disputes", "Tenant disputes involving council properties"),
            ("squatting", "Squatting in abandoned buildings"),
        ],
        "transport": [
            ("service_disruptions", "Bus or train service disruptions"),
            ("bus_shelters", "Inadequate bus stops or shelters"),
            ("unsafe_facilities", "Dirty or unsafe public transport facilities"),
            ("accessibility", "Lack of accessibility for disabled passengers"),
        ],
        "parks": [
            ("overgrown_trees", "Overgrown trees and hedges obstructing pathways"),
            ("poor_maintenance", "Poorly maintained parks or playgrounds"),
            ("damaged_equipment", "Damaged or unsafe playground equipment"),
            ("littering", "Littering and vandalism in parks"),
            ("dog_fouling", "Dog fouling and lack of waste bins"),
        ],
        "water": [
            ("supply_disruptions", "Water supply disruptions"),
            ("leaks", "Leaks or burst pipes"),
            ("flooding", "Flooding concerns"),
            ("sewage", "Sewage overflows and bad odors"),
        ],
        "licensing": [
            ("street_vendors", "Unauthorized street vendors"),
            ("unlicensed_businesses", "Unlicensed or disruptive businesses"),
            ("trading_hours", "Breach of trading hours or alcohol licensing laws"),
            ("hygiene", "Poor hygiene at food establishments"),
        ],
        "animals": [
            ("dangerous_dogs", "Dangerous or aggressive dogs"),
            ("cruelty", "Animal cruelty or neglect"),
            ("stray_animals", "Stray or abandoned animals"),
            ("pest_control", "Insufficient pest control measures"),
        ],
        "accessibility": [
            ("wheelchair_facilities", "Lack of wheelchair-accessible facilities"),
            ("ramps", "Poorly maintained mobility ramps or lifts"),
            ("obstructed_pathways", "Obstructed pathways for visually impaired individuals"),
        ],
        "health": [
            ("pests", "Pest infestations (rats, cockroaches, etc.)"),
            ("hygiene", "Poor hygiene in public spaces or businesses"),
            ("unsafe_conditions", "Unsafe conditions in council-run buildings"),
        ],
        "council": [
            ("customer_service", "Poor customer service from council offices"),
            ("delays", "Delays in processing permits or documents"),
            ("council_tax", "Issues with council tax billing or benefits"),
            ("governance", "Transparency and governance concerns"),
        ],
    }
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=11)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="infrastructure")
    subcategory = models.CharField(max_length=50, blank=True)
    issue_description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)  # Store location as text
    latitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically store submission time 
    validated = models.BooleanField(default=False)

    def __str__(self):
        return f"Complaint by {self.name} - {self.submitted_at}"


