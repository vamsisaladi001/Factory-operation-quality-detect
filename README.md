# Factory Operations & Quality Control System

A full-stack web application designed to manage factory work orders and perform quality inspections. The system helps track production progress, record product measurements, identify defects, and maintain quality inspection history.

## 🚀 Features

### 1. Work Order Management
- Create and view factory work orders.
- Track work order numbers, part details, and planned quantities.
- Record already-produced quantities.
- Set due dates, machine/workstation names, and work order status.
- Search and filter work orders.
- Delete work orders when required.

### 2. Quality Control
- Create quality inspections for existing work orders.
- Support First Piece, In-Process, and Final inspections.
- Record inspector details and dimensional measurements.
- Define nominal values, lower limits, and upper limits.
- Automatically determine PASS or FAIL based on measurement limits.
- Require defect notes when a measurement fails.
- Maintain quality inspection history.
- Track inspection review status.

## 🛠️ Tech Stack

**Frontend**
- React.js
- Vite
- JavaScript
- HTML5
- CSS3

**Backend**
- Python
- Django
- Django REST Framework

**API & Integration**
- REST APIs
- Fetch API
- CORS

**Database**
- SQLite (Django default database, unless configured otherwise)

## 🏗️ System Architecture

```text
React Frontend (Vite)
        |
        | REST API Requests
        v
Django REST Framework
        |
        v
Django Models & Validation
        |
        v
Database
```

## 📋 Quality Inspection Workflow

1. Select an existing work order.
2. Choose the inspection type.
3. Enter inspector and dimensional details.
4. Define the acceptable measurement range.
5. Enter the measured value.
6. The system determines the result:
   - **PASS:** The measurement is within the acceptable limits.
   - **FAIL:** The measurement is outside the acceptable limits.
7. Add defect notes when the inspection fails.
8. Save the inspection and view it in the inspection history.

## ⚙️ Installation and Setup

### Prerequisites
- Python 3.10 or later
- Node.js and npm
- Git

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd zapuza-factory-operations
```

### 2. Backend Setup

Open a terminal in the Django backend directory.

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Start the Django development server:

```bash
python manage.py runserver
```

Backend API base URL:

```text
http://127.0.0.1:8000/api/
```

### 3. Frontend Setup

Open another terminal in the React frontend directory.

```bash
npm install
npm run dev
```

Open the local URL displayed by Vite in your browser, usually:

```text
http://localhost:5173/
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/show/` | Retrieve work orders |
| POST | `/api/add/` | Create a work order |
| DELETE | `/api/<id>/delete/` | Delete a work order |
| GET | `/api/quality/` | Retrieve quality inspections |
| POST | `/api/quality/` | Create a quality inspection |
| GET | `/api/quality/<id>/` | Retrieve an inspection by ID |

## 📌 Future Enhancements

- Defect photo uploads.
- Supervisor approval and rejection workflows.
- Production and quality analytics dashboard.
- Automated testing and deployment.
- AI-assisted visual defect detection.

## 🎯 Project Objective

To develop a centralized factory operations application that improves work order tracking, simplifies dimensional quality inspections, and provides a consistent record of production quality.

---

**Project Type:** Full-Stack Web Application  
**Frontend:** React.js  
**Backend:** Django REST Framework  
**Developer:** [Your Name]

