# HakiRecord 
### A Secure Digital Occurrence Book for Police Stations

The website is live at [HakiRecord Digital OB](https://shann404.github.io/Portfolio-Hackathon-PLP/)


HakiRecord is a **secure, transparent, and tamper-proof Digital Occurrence Book (DOB)** designed to replace manual, paper-based occurrence books used in police stations.  
The system improves **accountability, efficiency, and data integrity** in law enforcement record management through audit trails, role-based access control, and real-time data handling.

---

## Objectives
- Digitize occurrence book records for real-time entry and retrieval  
- Improve transparency and accountability through audit trails  
- Secure sensitive data using authentication and role-based access control  
- Enable reporting and analytics for informed decision-making  

---

## Core Features
- Secure authentication with admin-controlled officer accounts  
- Digital statement recording using structured forms  
- Automatic OB number generation  
- Secure evidence upload and case association  
- Immutable audit trail logging all system actions  
- Crime analysis dashboard with charts and trends  
- Officer shift allocation module  
- SMS notifications via Africa’s Talking API  

---

## Tech Stack

### Backend
- Django (Python)
- SQLite3 (development & prototype)

### Frontend
- HTML5  
- CSS3  
- JavaScript  
- Bootstrap  

### Tools & Services
- Git & GitHub  
- Africa’s Talking (SMS API)  
- Postman  
- Django Test Framework  

---

## System Architecture
HakiRecord follows a **three-tier architecture**:
1. **Presentation Layer** – Web interface (HTML, CSS, JavaScript, Bootstrap)  
2. **Application Layer** – Django (business logic, authentication, validation)  
3. **Data Layer** – SQLite3 (users, cases, evidence, audit logs)  

This design ensures scalability, maintainability, and security.

---

## Non-Functional Requirements
- **Security:** Encrypted passwords, CSRF protection, RBAC  
- **Reliability:** Stable performance under concurrent access  
- **Usability:** Simple and intuitive interface  
- **Auditability:** Permanent logs of all actions  
- **Scalability:** Modular and extensible architecture  

---

## Testing
- Unit testing (models, views, forms)  
- Integration testing (case handling, evidence management)  
- System testing (end-to-end workflows)  
- Security testing (authentication, access control, CSRF protection)  

---


##  Installation & Setup

### Prerequisites
- Python 3.9+
- Git
- Virtual environment tool (venv or virtualenv)

### Steps
1. Clone the repository
   git clone https://github.com/Shann404/HakiRecord.git

2. Navigate into the project directory
   
   cd HakiRecord

4. Create and activate a virtual environment
   
   python -m venv venv
   
   source venv/bin/activate   # On Windows: venv\Scripts\activate

6. Install dependencies
   
   pip install -r requirements.txt

7. Apply database migrations
   
   python manage.py migrate

8. Create a superuser (optional)
   
   python manage.py createsuperuser

9. Run the development server
   
   python manage.py runserver

10. Open in browser
    
    http://127.0.0.1:8000/


