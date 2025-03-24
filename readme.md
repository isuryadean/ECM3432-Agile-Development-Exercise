# Council Complaint Management System

A Django-based web application that allows members of the public to submit complaints to the local council, and enables staff to log in, review, verify, and manage these complaints using an admin dashboard and workflow.

---

## Features

###  Public Interface
- Submit complaints via a web form
- Select category and subcategory of issue
- Use current location or select it on an interactive **OpenStreetMap** map (Leaflet.js)
- Auto-fill location address via reverse geocoding
- All complaints stored in a **SQLite** database

###  Staff Portal
- Staff login via secure form (`is_staff=True`)
- Staff dashboard to:
  - View submitted complaints
  - Expand complaint rows to see details
  - **Verify** issues (move to Active Issues)
  - **Dismiss** issues (delete from DB)
- View list of **Active (Verified) Issues**
- Protected views (non-staff users cannot access staff pages)

###  Admin Panel
- Access and manage all models (`Complaint`, `ActiveIssue`) via Django admin
- Only accessible to superusers or staff via `/admin/`

---

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/council-complaint-system.git
cd council-complaint-system
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional but useful)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Visit:
- `http://127.0.0.1:8000/` – Public complaint form  
- `http://127.0.0.1:8000/staff/login/` – Staff login  
- `http://127.0.0.1:8000/admin/` – Django Admin panel

---

##  Models Overview

### `Complaint`
| Field | Description |
|-------|-------------|
| name | Name of complainant |
| email | Contact email |
| category | Top-level complaint category |
| subcategory | Subcategory of issue |
| complaint_text | Complaint description |
| location | Address string |
| latitude / longitude | Coordinates |
| created_at | Timestamp of submission |

### `ActiveIssue`
| Field | Description |
|-------|-------------|
| complaint | Reference to original complaint |
| verified_by | Staff user who verified it |
| verified_at | Timestamp of verification |

---

##  Authentication & Permissions

- **Staff Users**: `is_staff=True`, can log in to dashboard and verify/dismiss complaints.
- **Superusers**: Full admin panel access.
- **Public users**: No login required; can submit complaints anonymously.

---

##  Running Tests

Run unit tests for complaint workflows:

```bash
python manage.py test
```

Covers:
- Complaint creation
- Staff login and dashboard access
- Verifying & dismissing complaints
- Access restrictions

---

##  Technologies Used

- **Python 3 / Django**
- **SQLite** (default database)
- **Leaflet.js** + OpenStreetMap for location
- **Bootstrap 5** for styling
- **Django Admin** for back-office access
- **CSRF protection**, form validation, access control

---

##  Future Improvements

- [ ] Add complaint filtering by category/date/status
- [ ] Attach images/screenshots to complaints
- [ ] Add status history to complaints
- [ ] Enable email notifications for complaint updates
- [ ] Use PostGIS or GeoDjango for advanced mapping

---

