# Task Management System

## Overview

A full-stack Task Management System built using React.js, Django REST Framework, and SQLite.

The application provides secure JWT authentication and CRUD functionality for managing tasks.

---

## Features

* User Registration
* User Login
* JWT Authentication
* Protected Dashboard
* Create Tasks
* Delete Tasks
* REST APIs
* Responsive Frontend UI

---

## Tech Stack

### Frontend

* React.js
* Bootstrap
* Axios

### Backend

* Django
* Django REST Framework
* JWT Authentication

### Database

* SQLite

---

## API Endpoints

### Authentication APIs

#### Register User

POST /api/register/

#### Login User

POST /api/login/

---

### Task APIs

#### Get Tasks

GET /api/tasks/

#### Create Task

POST /api/tasks/create/

#### Delete Task

DELETE /api/tasks/delete/<id>/

---

## Setup Instructions

### Backend Setup

cd backend

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

---

### Frontend Setup

cd frontend

npm install

npm start

---

## Security Features

* JWT Authentication
* Password Hashing
* Protected APIs
* Authentication Validation

---

## Scalability Notes

Future improvements can include:

* Redis caching
* Docker deployment
* Load balancing
* Microservices architecture
* API rate limiting
* Cloud deployment (AWS/GCP)

---

## Author

Pranali Salunkhe
