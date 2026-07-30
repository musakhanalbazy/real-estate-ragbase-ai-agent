"""Knowledge base content for Tanveer Associates.

Contains all company information organized by category.
Each entry becomes a LangChain Document with category metadata.
"""

from typing import Dict, List

from langchain_core.documents import Document
# All company information organized by category
CATEGORIZED_INFO: Dict[str, List[str]] = {
    # ------------------------------------------------------------------
    # 1. COMPANY OVERVIEW & GENERAL INFORMATION
    # ------------------------------------------------------------------
    "Company Overview & General Information": [
        "Tanveer Associates is a leading real estate developer in Islamabad with 27+ high-rise projects and 325+ homes delivered with in-house construction.",
        "Tanveer Associates is a trusted real estate and construction firm with decades of experience, delivering landmark projects through quality, transparency, and integrity.",
        "Tanveer Associates is one of the best real estate developers and consultants in Islamabad, Pakistan.",
        "The company operates in Real Estate Development, Construction, Interior Design & Furnishing, Design & Planning, and Consultation services.",
        "The company's brand color is green (#006034) representing trust, growth, and prosperity in real estate.",
        "The official website is https://tanveerassociates.com.pk/",
        "Tanveer Associates has a strong presence on social media including Facebook, Instagram, YouTube, and LinkedIn.",
        "The company motto focuses on quality construction, transparency, and client satisfaction.",
        "Tanveer Associates operates with in-house construction capabilities through their subsidiary Miusam Construction.",
    ],

    # ------------------------------------------------------------------
    # 2. ABOUT TANVEER ASSOCIATES
    # ------------------------------------------------------------------
    "About Tanveer Associates": [
        "Tanveer Associates is a trusted real estate and construction firm with decades of experience, delivering landmark projects through quality, transparency, and integrity.",
        "The company has completed 27+ high-rise projects across Islamabad and surrounding areas.",
        "Tanveer Associates has delivered 325+ homes to satisfied families and investors.",
        "The company operates with in-house construction, ensuring quality control at every stage of development.",
        "Tanveer Associates brings several decades of experience with projects like Tower 45 Faisal Town, Veranda E-11, Tanveer Villas Faisal Town, Saira Tower E-11, and Areej Tower E-11.",
        "Their dedicated professionals deliver to international quality standards.",
        "The CEO of Tanveer Associates is Sayed Tanveer Hussain Shah.",
        "The company focuses on modern architecture, premium facilities, and creating elevated living experiences.",
    ],

    # ------------------------------------------------------------------
    # 3. CEO & LEADERSHIP
    # ------------------------------------------------------------------
    "CEO & Leadership": [
        "The CEO and Founder of Tanveer Associates is Sayed Tanveer Hussain Shah.",
        "Sayed Tanveer Hussain Shah has led the company through decades of successful real estate development in Islamabad.",
        "Under his leadership, Tanveer Associates has grown to become one of Islamabad's most trusted real estate developers.",
        "The CEO's vision focuses on delivering quality construction with transparency and integrity.",
    ],

    # ------------------------------------------------------------------
    # 4. MIUSAM CONSTRUCTION (SUBSIDIARY)
    # ------------------------------------------------------------------
    "Miusam Construction (Subsidiary)": [
        "Miusam Construction is the in-house construction arm of Tanveer Associates.",
        "Miusam Construction handles all construction work for Tanveer Associates projects, ensuring quality control from foundation to finishing.",
        "Having an in-house construction company allows Tanveer Associates to maintain strict quality standards and timely delivery.",
        "Miusam Construction has been responsible for building 27+ high-rise projects and 325+ homes.",
        "The subsidiary operates from the same offices as Tanveer Associates in E-11/3, Islamabad.",
        "Miusam Construction's dedicated page can be found at https://tanveerassociates.com.pk/miusam-construction/",
    ],

    # ------------------------------------------------------------------
    # 5. ON-GOING PROJECTS
    # ------------------------------------------------------------------
    "On-Going Projects": [
        "Eaden Heights is an on-going project by Tanveer Associates located in E-11, Islamabad.",
        "Eaden Heights is a high-rise residential and commercial development project.",
        "The NOC for Eaden Heights is approved.",
        "Eaden Heights offers modern living spaces with premium amenities in the heart of Islamabad's E-11 sector.",
        "Eaden Heights project page: https://tanveerassociates.com.pk/project/eaden-hieghts/",
        "Serene Hills is an on-going project by Tanveer Associates.",
        "Serene Hills is a residential development project offering serene living in a peaceful environment.",
        "Serene Hills features modern architecture with a focus on nature-integrated living.",
        "Serene Hills project page: https://tanveerassociates.com.pk/project/serene-hills/",
    ],

    # ------------------------------------------------------------------
    # 6. IN-FINISHING PHASE PROJECTS
    # ------------------------------------------------------------------
    "In-Finishing Phase Projects": [
        "Apollo Towers II is a high-rise residential building currently in the finishing stage.",
        "Apollo Towers II is located in Faisal Town, Islamabad.",
        "The NOC for Apollo Towers II is approved.",
        "Following the success of Apollo I in E-11/4, Tanveer Associates are delighted to launch Apollo Towers II in Faisal Town.",
        "Modern spaces, meticulous service, and a full security system create luxury apartments designed for everyday comfort.",
        "The Apollo Towers II site is near Fateh Jang Interchange, five minutes to Islamabad Airport, with Margalla views.",
        "Apollo Towers II apartments come in 1, 2, and 3 bedroom layouts with light on three sides and efficient plans.",
        "Apollo Builders bring several decades of experience with projects like Tower 45 Faisal Town, Veranda E-11, Tanveer Villas Faisal Town, Saira Tower E-11, and Areej Tower E-11.",
        "Apollo Towers II offers 40% downpayment and 60% installments payment plan.",
        "Apollo Towers II offers 1, 2, and 3 Bedroom Apartments.",
        "Prices and simple installment plan shared on request after verification.",
        "Built to exist in perfect harmony with their surroundings, Apollo Towers II embody the human ideal of living peacefully and pleasurably within the ecology of the natural world.",
        "The Apollo Builders offers a full range of floor plans to suit your needs from 1 to 3 bedroom luxury apartments.",
        "Apollo Towers II amenities include: Swimming Pool, Kids Play Area, Gymnasium, BBQ Area, CCTV Cameras, Rooftop Garden, Power Backup, Lobby, Parking, Elevator, Mosque, and Reception.",
        "Apollo Towers II project page: https://tanveerassociates.com.pk/project/apollo-towers-ii/",
        "Apollo Towers II also has a Faisal Town location page: https://tanveerassociates.com.pk/project/apollo-towers-ii-faisal-town/",
        "Casablanca is a residential project currently in the finishing stage.",
        "Casablanca is located near the Murree Expressway.",
        "The NOC for Casablanca is TMA Approved.",
        "Welcome to Casablanca Premium Apartments, an enchanting residential project crafted by Tanveer Associates, set in the breathtaking hill station of Murree, Pakistan near the Murree Expressway.",
        "This prestigious address blends contemporary architecture, premium facilities, and a serene forest backdrop to create a calm, elevated way of life.",
        "Proximity to Gloria Jeans adds daily convenience and a friendly social stop.",
        "Casablanca stands as a beacon of elegance with bright interiors, generous terraces, and expansive windows that frame valley and pine views.",
        "Residents enjoy a gated environment, attentive on site services, elevators, ample parking, a mosque, a mini park, and nearby essentials.",
        "Studio, one, two, and three bedroom options offer an unparalleled living experience for families and investors.",
        "Casablanca offers 40% downpayment and 60% installments payment plan.",
        "Casablanca offers 1 and 2 Bedroom Apartments.",
        "Breathe pine air, see wide terraces, feel calm rooms, and decide if this hillside home feels like yours.",
        "Wake to crisp pine air on Murree Expressway near Gloria Jeans, with secure hill view apartments, large terraces, easy access, and budget friendly plans.",
        "Casablanca amenities include: Kids Play Area, CCTV Cameras, Parking, Elevator, Mosque, and Mini Park.",
        "Casablanca project page: https://tanveerassociates.com.pk/project/casablanca/",
    ],

    # ------------------------------------------------------------------
    # 7. DELIVERED PROJECTS
    # ------------------------------------------------------------------
    "Delivered Projects": [
        "Apollo Towers I is a delivered high-rise residential project by Tanveer Associates.",
        "Apollo Towers I is located in E-11/4, Islamabad.",
        "Apollo Towers I was the first project in the Apollo Towers series, successfully completed and delivered.",
        "The success of Apollo Towers I led to the launch of Apollo Towers II in Faisal Town.",
        "Apollo Towers I project page: https://tanveerassociates.com.pk/project/apollo-towers-i/",
        "Miusam Mall & Apartments is a delivered mixed-use commercial and residential project.",
        "Miusam Mall & Apartments combines retail shopping spaces with residential apartments.",
        "Miusam Mall & Apartments project page: https://tanveerassociates.com.pk/project/miusam-mall-and-apartments/",
        "The Veranda Residence is a delivered residential project by Tanveer Associates.",
        "The Veranda Residence is located in E-11, Islamabad.",
        "The Veranda Residence features spacious apartments with large verandas and modern amenities.",
        "The Veranda Residence project page: https://tanveerassociates.com.pk/project/the-veranda-residence/",
        "Tanveer Homes is a delivered residential housing project by Tanveer Associates.",
        "Tanveer Homes offers independent houses/villas for families seeking their own homes.",
        "Tanveer Homes project page: https://tanveerassociates.com.pk/project/tanveer-homes/",
        "Prime Tower is a delivered high-rise project by Tanveer Associates.",
        "Prime Tower features commercial and residential spaces in a prime location.",
        "Prime Tower project page: https://tanveerassociates.com.pk/project/prime-tower/",
        "Royal Empire is a delivered project by Tanveer Associates.",
        "Royal Empire features a grand design with premium living spaces.",
        "Royal Empire project page: https://tanveerassociates.com.pk/project/royal-empire/",
        "Miusam Heights is a delivered residential project by Tanveer Associates.",
        "Miusam Heights offers modern apartment living with quality construction.",
        "Miusam Heights project page: https://tanveerassociates.com.pk/project/miusam-heights/",
        "Tower 45 is a delivered project by Tanveer Associates located in Faisal Town.",
        "Tower 45 is one of the landmark projects that established Tanveer Associates' reputation in Faisal Town.",
        "Tower 45 project page: https://tanveerassociates.com.pk/project/tower-45/",
    ],

    # ------------------------------------------------------------------
    # 8. ALL PROJECTS SUMMARY
    # ------------------------------------------------------------------
    "All Projects Summary": [
        "Tanveer Associates has a total of 27+ high-rise projects across Islamabad and surrounding areas.",
        "On-Going Projects: Eaden Heights (E-11, Islamabad) and Serene Hills.",
        "In-Finishing Phase Projects: Apollo Towers II (Faisal Town, Islamabad) and Casablanca (Murree Expressway).",
        "Delivered Projects: Apollo Towers I (E-11/4), Miusam Mall & Apartments, The Veranda Residence (E-11), Tanveer Homes, Prime Tower, Royal Empire, Miusam Heights, and Tower 45 (Faisal Town).",
        "Other notable completed projects mentioned include: Tanveer Villas Faisal Town, Saira Tower E-11, and Areej Tower E-11.",
        "325+ homes have been delivered to satisfied families and investors.",
        "All projects are built by Miusam Construction, the in-house construction arm of Tanveer Associates.",
    ],

    # ------------------------------------------------------------------
    # 9. SERVICES - CONSTRUCTION
    # ------------------------------------------------------------------
    "Services - Construction": [
        "Tanveer Associates offers comprehensive construction services through their subsidiary Miusam Construction.",
        "Construction services page: https://tanveerassociates.com.pk/construction-company-in-islamabad/",
        "Detailed construction services page: https://tanveerassociates.com.pk/construction-services/",
        "The company handles all aspects of construction from foundation to finishing.",
        "In-house construction ensures quality control, timely delivery, and cost efficiency.",
        "Construction services cover residential buildings, commercial complexes, and mixed-use developments.",
        "The company uses modern construction techniques and international quality standards.",
        "27+ high-rise projects have been constructed by the in-house construction team.",
    ],

    # ------------------------------------------------------------------
    # 10. SERVICES - FURNISHING & INTERIOR
    # ------------------------------------------------------------------
    "Services - Furnishing & Interior": [
        "Tanveer Associates provides Furnishing and Interior Design services.",
        "Furnishing & Interior services page: https://tanveerassociates.com.pk/furnishing-and-interior-services/",
        "Interior design services cover residential and commercial spaces.",
        "The company offers complete interior fit-out solutions from concept to completion.",
        "Modern and contemporary interior design styles are offered to match diverse client preferences.",
        "Services include furniture selection, lighting design, color consultation, and space planning.",
    ],

    # ------------------------------------------------------------------
    # 11. SERVICES - DESIGN & PLANNING
    # ------------------------------------------------------------------
    "Services - Design & Planning": [
        "Tanveer Associates offers Design and Planning services for real estate projects.",
        "Design & Planning services page: https://tanveerassociates.com.pk/design-planning/",
        "Design services cover architectural planning, structural design, and project visualization.",
        "The company uses modern design tools and techniques for creating efficient and aesthetically pleasing structures.",
        "Design and planning services are available for both new construction and renovation projects.",
        "The team includes experienced architects and planners who deliver innovative solutions.",
    ],

    # ------------------------------------------------------------------
    # 12. SERVICES - CONSULTATION
    # ------------------------------------------------------------------
    "Services - Consultation": [
        "Tanveer Associates offers real estate consultation services.",
        "Consultation services page: https://tanveerassociates.com.pk/consultation/",
        "Consultation services help clients make informed decisions about real estate investments.",
        "The company provides guidance on property selection, investment opportunities, and market trends.",
        "Free consultation is available through WhatsApp at +92 330 197 9311.",
        "Consultation covers both residential and commercial real estate sectors.",
        "Expert advisors help clients understand payment plans, financing options, and legal requirements.",
    ],

    # ------------------------------------------------------------------
    # 13. COMMUNITIES - FAISAL TOWN PHASE 2
    # ------------------------------------------------------------------
    "Communities - Faisal Town Phase 2": [
        "Faisal Town Phase 2 is one of the communities where Tanveer Associates operates.",
        "Faisal Town Phase 2 page: https://tanveerassociates.com.pk/faisal-town-phase-2/",
        "Faisal Town Phase 2 is a planned residential community in Islamabad.",
        "Tanveer Associates has multiple projects within Faisal Town Phase 2.",
        "Apollo Towers II is one of the flagship projects located in Faisal Town.",
        "Faisal Town Phase 2 is near Fateh Jang Interchange, providing easy access to key locations.",
        "The community is located five minutes from Islamabad International Airport.",
        "Faisal Town Phase 2 offers views of the Margalla Hills.",
    ],

    # ------------------------------------------------------------------
    # 14. COMMUNITIES - FAISAL TOWN PHASE 1
    # ------------------------------------------------------------------
    "Communities - Faisal Town Phase 1": [
        "Faisal Town Phase 1 is an established community where Tanveer Associates has completed projects.",
        "Faisal Town Phase 1 page: https://tanveerassociates.com.pk/faisal-town-phase-1/",
        "Tower 45 is one of the delivered projects in Faisal Town.",
        "Tanveer Villas were also developed by Tanveer Associates in Faisal Town.",
        "Faisal Town Phase 1 is a well-developed residential area in Islamabad.",
    ],

    # ------------------------------------------------------------------
    # 15. COMMUNITIES - FAISAL HILLS
    # ------------------------------------------------------------------
    "Communities - Faisal Hills": [
        "Faisal Hills is one of the communities featured by Tanveer Associates.",
        "Faisal Hills page: https://tanveerassociates.com.pk/faisal-hills/",
        "Faisal Hills is a residential community offering plots and developed properties.",
        "Tanveer Associates provides real estate services and project development in Faisal Hills.",
    ],

    # ------------------------------------------------------------------
    # 16. APOLLO TOWERS II - DETAILED AMENITIES & FEATURES
    # ------------------------------------------------------------------
    "Apollo Towers II - Detailed Amenities & Features": [
        "Swimming Pool - Apollo Towers II features a swimming pool for residents.",
        "Kids Play Area - A dedicated play area for children is provided.",
        "Gymnasium - A fully equipped gym is available for fitness enthusiasts.",
        "BBQ Area - Residents can enjoy outdoor BBQ gatherings.",
        "CCTV Cameras - 24/7 CCTV surveillance ensures security throughout the building.",
        "Rooftop Garden - A beautiful rooftop garden offers a relaxing outdoor space.",
        "Power Backup - Uninterrupted power supply with backup generators.",
        "Lobby - A grand lobby welcomes residents and visitors.",
        "Parking - Ample parking space is provided for residents and their guests.",
        "Elevator - Modern elevators for convenient vertical transportation.",
        "Mosque - An on-site mosque for daily prayers.",
        "Reception - A dedicated reception area for building management and visitor handling.",
        "Full Security System - Comprehensive security measures for peace of mind.",
        "Light on Three Sides - Apartments are designed with natural light from three sides.",
        "Efficient Floor Plans - Well-designed layouts maximize space utilization.",
    ],

    # ------------------------------------------------------------------
    # 17. CASABLANCA - DETAILED AMENITIES & FEATURES
    # ------------------------------------------------------------------
    "Casablanca - Detailed Amenities & Features": [
        "Kids Play Area - A safe play space for children within the Casablanca complex.",
        "CCTV Cameras - Security cameras for round-the-clock surveillance.",
        "Parking - Sufficient parking spaces for residents.",
        "Elevator - Modern elevator service in the building.",
        "Mosque - On-site mosque for residents' convenience.",
        "Mini Park - A green park area within the residential complex.",
        "Gated Environment - Secure gated community with controlled access.",
        "On-Site Services - Attentive on-site management services.",
        "Generous Terraces - Large terraces with valley and pine views.",
        "Expansive Windows - Large windows framing natural scenery.",
        "Bright Interiors - Well-lit interior spaces designed for comfort.",
        "Near Gloria Jeans - Proximity to Gloria Jeans coffee shop for daily convenience.",
        "Forest Backdrop - Serene forest surroundings creating a peaceful environment.",
        "Valley and Pine Views - Stunning views from apartments.",
    ],

    # ------------------------------------------------------------------
    # 18. PAYMENT PLANS & INVESTMENT INFORMATION
    # ------------------------------------------------------------------
    "Payment Plans & Investment Information": [
        "Apollo Towers II offers a 40% downpayment and 60% installments payment structure.",
        "Casablanca offers a 40% downpayment and 60% installments payment structure.",
        "Prices and simple installment plans are shared on request after verification for both Apollo Towers II and Casablanca.",
        "Free consultation is available for investment guidance through WhatsApp at +92 330 197 9311.",
        "Tanveer Associates projects offer opportunities for both families looking for homes and investors seeking returns.",
        "Brochures are available for download on individual project pages.",
        "For price inquiries, clients can use the contact form at https://tanveerassociates.com.pk/contact/",
    ],

    # ------------------------------------------------------------------
    # 19. CONTACT INFORMATION
    # ------------------------------------------------------------------
    "Contact Information": [
        "Office Address: Office # 4, 5, 6, 1st Floor, Askaan Centre, MPCHS, E-11/3, Islamabad, Pakistan.",
        "Phone: +92 51 111 525 525",
        "Phone: +92 330 197 9311",
        "Email: info@tanveerassociates.com.pk",
        "WhatsApp: +92 330 197 9311 (https://wa.me/923301979311)",
        "Google Maps Directions: https://goo.gl/maps/6jeJNMp7k2n6zxqE6",
        "Contact Page: https://tanveerassociates.com.pk/contact/",
        "Clients can get free consultation by reaching out through WhatsApp or the contact form.",
    ],

    # ------------------------------------------------------------------
    # 20. SOCIAL MEDIA LINKS
    # ------------------------------------------------------------------
    "Social Media Links": [
        "Facebook: https://www.facebook.com/TanveerAssociates/",
        "Instagram: https://www.instagram.com/tanveer.associates1/",
        "YouTube: https://www.youtube.com/@tanveerassociates3451",
        "LinkedIn: https://www.linkedin.com/company/tanveer-associates",
    ],

    # ------------------------------------------------------------------
    # 21. WEBSITE NAVIGATION & PAGES STRUCTURE
    # ------------------------------------------------------------------
    "Website Navigation & Pages Structure": [
        "Home page: https://tanveerassociates.com.pk/",
        "About Us page: https://tanveerassociates.com.pk/about-us/",
        "Miusam Construction page: https://tanveerassociates.com.pk/miusam-construction/",
        "Our Team page: https://tanveerassociates.com.pk/our-team/",
        "Contact page: https://tanveerassociates.com.pk/contact/",
        "Our Blogs page: https://tanveerassociates.com.pk/our-blogs/",
        "Our Projects page: https://tanveerassociates.com.pk/our-projects/",
        "On-going Projects: Eaden Heights and Serene Hills.",
        "In-Finishing Phase Projects: Apollo Towers II and Casablanca.",
        "Delivered Projects: Apollo Towers I, Miusam Mall & Apartments, The Veranda Residence, Tanveer Homes, Prime Tower, Royal Empire, Miusam Heights, and Tower 45.",
        "Services menu includes: Construction, Construction Services, Furnishing & Interior, Design & Planning, and Consultation.",
        "Construction Company page: https://tanveerassociates.com.pk/construction-company-in-islamabad/",
        "Construction Services page: https://tanveerassociates.com.pk/construction-services/",
        "Furnishing & Interior page: https://tanveerassociates.com.pk/furnishing-and-interior-services/",
        "Design & Planning page: https://tanveerassociates.com.pk/design-planning/",
        "Consultation page: https://tanveerassociates.com.pk/consultation/",
        "Communities menu includes: Faisal Town Phase 2, Faisal Town Phase 1, and Faisal Hills.",
        "Faisal Town Phase 2 page: https://tanveerassociates.com.pk/faisal-town-phase-2/",
        "Faisal Town Phase 1 page: https://tanveerassociates.com.pk/faisal-town-phase-1/",
        "Faisal Hills page: https://tanveerassociates.com.pk/faisal-hills/",
    ],

    # ------------------------------------------------------------------
    # 22. PROJECT LOCATIONS & AREAS
    # ------------------------------------------------------------------
    "Project Locations & Areas": [
        "E-11 Sector, Islamabad: Eaden Heights, The Veranda Residence, Apollo Towers I (E-11/4), Saira Tower, Areej Tower.",
        "Faisal Town, Islamabad: Apollo Towers II, Tower 45, Tanveer Villas.",
        "Murree Expressway: Casablanca Premium Apartments.",
        "Faisal Town is near Fateh Jang Interchange and five minutes to Islamabad International Airport.",
        "E-11/3, Islamabad: Tanveer Associates Head Office at Askaan Centre, MPCHS.",
        "All projects are located in and around Islamabad, the capital city of Pakistan.",
    ],

    # ------------------------------------------------------------------
    # 23. KEY STATISTICS & NUMBERS
    # ------------------------------------------------------------------
    "Key Statistics & Numbers": [
        "27+ high-rise projects completed or under construction.",
        "325+ homes delivered to families and investors.",
        "Decades of experience in real estate development and construction.",
        "Multiple projects across E-11 sector, Faisal Town, and Murree Expressway.",
        "In-house construction through Miusam Construction subsidiary.",
        "Serving clients with 4 core services: Construction, Furnishing & Interior, Design & Planning, and Consultation.",
        "Operating in 3 major communities: Faisal Town Phase 1, Faisal Town Phase 2, and Faisal Hills.",
    ],

    # ------------------------------------------------------------------
    # 24. APARTMENT TYPES OFFERED
    # ------------------------------------------------------------------
    "Apartment Types Offered": [
        "Apollo Towers II offers 1 Bedroom Apartments.",
        "Apollo Towers II offers 2 Bedroom Apartments.",
        "Apollo Towers II offers 3 Bedroom Apartments.",
        "Casablanca offers Studio Apartments.",
        "Casablanca offers 1 Bedroom Apartments.",
        "Casablanca offers 2 Bedroom Apartments.",
        "Casablanca offers 3 Bedroom Apartments.",
        "Various projects offer different apartment configurations to suit different family sizes and budgets.",
    ],

    # ------------------------------------------------------------------
    # 25. WHY CHOOSE TANVEER ASSOCIATES
    # ------------------------------------------------------------------
    "Why Choose Tanveer Associates": [
        "Decades of experience in real estate development and construction in Islamabad.",
        "27+ high-rise projects completed or under construction.",
        "325+ homes delivered with satisfaction.",
        "In-house construction through Miusam Construction ensures quality control at every stage.",
        "Transparent business practices and integrity in all dealings.",
        "Projects delivered to international quality standards.",
        "Convenient payment plans with 40% downpayment and 60% installment options.",
        "Free consultation available for property investment decisions.",
        "Prime locations in Islamabad's most sought-after areas.",
        "Comprehensive services from design and planning to construction, furnishing, and consultation.",
        "Strong track record with successfully delivered projects like Apollo Towers I, The Veranda Residence, Prime Tower, and Tower 45.",
        "Projects feature modern amenities including swimming pools, gyms, rooftop gardens, mosques, security systems, and more.",
        "Multiple project types available: apartments, villas, homes, commercial spaces, and mixed-use developments.",
    ],

    # ------------------------------------------------------------------
    # 26. NOTABLE PAST PROJECTS MENTIONED
    # ------------------------------------------------------------------
    "Notable Past Projects Mentioned": [
        "Tower 45 Faisal Town - A delivered project that helped establish Tanveer Associates' reputation.",
        "Veranda E-11 (The Veranda Residence) - A delivered residential project in E-11, Islamabad.",
        "Tanveer Villas Faisal Town - Residential villas delivered in Faisal Town.",
        "Saira Tower E-11 - A completed project in E-11 sector, Islamabad.",
        "Areej Tower E-11 - A completed project in E-11 sector, Islamabad.",
        "Apollo Towers I E-11/4 - The first Apollo Towers project, delivered in E-11/4, Islamabad.",
        "Miusam Mall & Apartments - A delivered mixed-use project with retail and residential spaces.",
        "Miusam Heights - A delivered residential project.",
        "Royal Empire - A delivered project with grand design and premium living spaces.",
        "Prime Tower - A delivered high-rise project with commercial and residential spaces.",
    ],

    # ------------------------------------------------------------------
    # 27. PROJECT DEVELOPMENT STAGES
    # ------------------------------------------------------------------
    "Project Development Stages": [
        "On-Going: Projects that are currently under active construction. Examples: Eaden Heights, Serene Hills.",
        "In-Finishing Phase (Finishing Stage): Projects where structural work is complete and interior finishing is in progress. Examples: Apollo Towers II, Casablanca.",
        "Delivered: Projects that have been completed and handed over to owners. Examples: Apollo Towers I, Miusam Mall & Apartments, The Veranda Residence, Tanveer Homes, Prime Tower, Royal Empire, Miusam Heights, Tower 45.",
        "NOC Status 'Approved' means the No Objection Certificate from relevant authorities has been obtained, confirming the project meets all legal and regulatory requirements.",
        "NOC Status 'TMA Approved' means the project has been approved by the Tehsil Municipal Administration.",
    ],

    # ------------------------------------------------------------------
    # 28. COMPANY-SPECIFIC FAQs
    # ------------------------------------------------------------------
    "Company-Specific FAQs": [
        "Q: Where is Tanveer Associates located? A: Office # 4, 5, 6, 1st Floor, Askaan Centre, MPCHS, E-11/3, Islamabad, Pakistan.",
        "Q: How can I contact Tanveer Associates? A: You can call +92 51 111 525 525, +92 330 197 9311, email info@tanveerassociates.com.pk, or WhatsApp +92 330 197 9311.",
        "Q: How many projects has Tanveer Associates completed? A: Tanveer Associates has completed 27+ high-rise projects and delivered 325+ homes.",
        "Q: Who is the CEO of Tanveer Associates? A: The CEO is Sayed Tanveer Hussain Shah.",
        "Q: What services does Tanveer Associates offer? A: Construction, Furnishing & Interior Design, Design & Planning, and Consultation.",
        "Q: Does Tanveer Associates have its own construction company? A: Yes, Miusam Construction is the in-house construction arm of Tanveer Associates.",
        "Q: What are the current on-going projects? A: Eaden Heights and Serene Hills are currently on-going projects.",
        "Q: What projects are in the finishing phase? A: Apollo Towers II (Faisal Town) and Casablanca (Murree Expressway) are in the finishing phase.",
        "Q: What payment plans are available? A: Projects typically offer 40% downpayment and 60% installment plans. Detailed plans are shared on request after verification.",
        "Q: Can I get a free consultation? A: Yes, free consultation is available through WhatsApp at +92 330 197 9311.",
        "Q: What apartment types are available in Apollo Towers II? A: 1, 2, and 3 bedroom apartments are available.",
        "Q: What apartment types are available in Casablanca? A: Studio, 1, 2, and 3 bedroom apartments are available.",
        "Q: Where is Apollo Towers II located? A: Apollo Towers II is located in Faisal Town, Islamabad, near Fateh Jang Interchange, five minutes to Islamabad Airport.",
        "Q: Where is Casablanca located? A: Casablanca is located near Murree Expressway, in the hill station of Murree, Pakistan.",
        "Q: What amenities does Apollo Towers II offer? A: Swimming Pool, Kids Play Area, Gymnasium, BBQ Area, CCTV Cameras, Rooftop Garden, Power Backup, Lobby, Parking, Elevator, Mosque, and Reception.",
        "Q: Are the projects NOC approved? A: Yes, all projects have their NOC (No Objection Certificate) approved from relevant authorities.",
        "Q: How can I download the project brochure? A: Brochures are available for download on individual project pages on the website.",
        "Q: What communities does Tanveer Associates operate in? A: Faisal Town Phase 1, Faisal Town Phase 2, and Faisal Hills.",
        "Q: Can I visit the site? A: Yes, you can contact Tanveer Associates to schedule a site visit.",
        "Q: What is the website of Tanveer Associates? A: https://tanveerassociates.com.pk/",
    ],

    # ------------------------------------------------------------------
    # 29. BLOG & CONTENT
    # ------------------------------------------------------------------
    "Blog & Content": [
        "Tanveer Associates maintains a blog section at https://tanveerassociates.com.pk/our-blogs/",
        "The blog covers topics related to real estate, construction, investment tips, and project updates.",
        "Clients and visitors can stay updated with the latest news and developments through the blog.",
    ],

    # ------------------------------------------------------------------
    # 30. TEAM
    # ------------------------------------------------------------------
    "Team": [
        "The Our Team page can be found at https://tanveerassociates.com.pk/our-team/",
        "Tanveer Associates has a dedicated team of professionals including architects, engineers, project managers, and sales consultants.",
        "The team is led by CEO Sayed Tanveer Hussain Shah.",
        "The company prides itself on its experienced and dedicated professionals who deliver to international quality standards.",
    ],

    # ------------------------------------------------------------------
    # 31. LEAD QUALIFICATION QUESTIONS
    # ------------------------------------------------------------------
    "Lead Qualification Questions": [
        # Conversation flow guidance
        "Step 1: Answer the client's property question in 2-4 sentences using the knowledge base.",
        "Step 2: Ask the budget or financing question before pushing toward a call.",
        "Step 3: Ask only for missing details like name, phone, or email depending on the platform.",
        "Step 4: Ask for a convenient time for a specialist to call or for a site visit.",

        # Contact questions (platform-dependent)
        "On WhatsApp, ask the user for their name only. Do NOT ask for phone number or email on WhatsApp as phone is auto-captured from sender ID.",
        "On Facebook Messenger, ask the user for their name and phone number.",
        "On Web Chat, ask the user for their name, phone number, and email. Email is optional.",

        # Property & Qualification Questions
        "Q: What type of property are you looking for — residential, commercial, or a plot? This helps route the lead to the right specialist team.",
        "Q: Which city or area are you interested in? This helps match the lead to a regional agent.",
        "Q: What is your approximate budget range? This is a core qualification filter.",
        "Q: Will you be paying via bank financing, installment plan, or cash? This filters out unqualified leads early.",
        "Q: Are you looking to buy immediately or within a few months? This helps prioritize hot leads vs nurture leads.",

        # Site visit and call time
        "After collecting lead info, ask: What is a convenient time for our specialist to call you?",
        "If the user says anytime, reply: We will reach you at the earliest.",
        "You can also ask: Would you like to schedule a site visit?",

        # Lead status classification
        "Lead status 'new': Client has just started the conversation.",
        "Lead status 'qualified_ready_for_call': Budget confirmed, name, phone, and preferred call time all collected.",
        "Lead status 'qualified_missing_call_time': Budget confirmed, name and phone collected, but no call time yet.",
        "Lead status 'ready_for_call_missing_contact_details': Budget confirmed, but missing name or phone.",
        "Lead status 'not_interested': Property interest expressed, but budget or financing is unknown.",
    ],
}


def get_company_documents() -> List[Document]:
    """Convert categorized company info into LangChain Documents with metadata."""
    documents: List[Document] = []
    for category, entries in CATEGORIZED_INFO.items():
        for i, text in enumerate(entries):
            documents.append(
                Document(
                    page_content=text.strip(),
                    metadata={"source": "company_knowledge_base", "category": category, "index": i},
                )
            )
    return documents
