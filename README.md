# Social Team Build

A Django-based social platform for team building and project collaboration.

## Project Overview

Social Team Build is a web application that allows users to create profiles, showcase their skills, and collaborate on projects. Users can create projects, define positions needed, and apply for roles in other users' projects.

## User Login Information

The following test users are available for development and demonstration purposes:

### Admin User
- **Name:** Admin User
- **Email:** traceh38@gmail.com
- **Password:** admin123
- **Role:** Administrator (superuser)

### Regular Users

#### User 1
- **Name:** test user1
- **Email:** testuser1@testuser.com
- **Password:** testpass123
- **Skills:** OOP, JavaScript, Python, Django

#### User 2
- **Name:** test user2
- **Email:** testuser2@testuser.com
- **Password:** testpass123
- **Skills:** Design, JavaScript, Virtual Reality Development

#### User 3
- **Name:** test user3
- **Email:** testuser3@testuser.com
- **Password:** testpass123
- **Skills:** OOP, Design, JavaScript, Python, Virtual Reality Development, Django

## Features

- **User Authentication:** Custom user model with email-based authentication
- **User Profiles:** Detailed profiles with bio, avatar, and skills
- **Project Management:** Create and manage collaborative projects
- **Position System:** Define specific roles needed for projects
- **Application System:** Apply for positions in projects
- **Skills Tracking:** Tag-based skill system for users

## Models

### User Model (accounts.NewUser)
- Email-based authentication
- Custom user manager
- Fields: email, first_name, last_name, date_of_birth, is_active, is_admin

### Profile Model (profiles.UserProfile)
- One-to-one relationship with User
- Fields: username, bio, avatar, skills (many-to-many)

### Project Models (projects.*)
- **UserProject:** Main project model with title, description, timeline, requirements
- **Position:** Specific roles within projects
- **Applicant:** Applications for positions

### Skills Model (profiles.Skills)
- Available skills: OOP, Design, JavaScript, Python, Virtual Reality Development, Django

## Installation & Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Load fixtures: `python manage.py loaddata accounts/fixtures/test_users.json accounts/fixtures/profiles.json`
5. Run the server: `python manage.py runserver`

## Database Fixtures

The project includes pre-populated test data:
- **test_users.json:** Contains 4 test users (1 admin, 3 regular users)
- **profiles.json:** Contains user profiles with skills and bio information
- **initial_skills.json:** Contains the initial set of available skills

## Deployment

This project is configured for Railway deployment. Make sure to:
1. Set up environment variables for production
2. Configure static files for production
3. Set up database for production environment

## Development Notes

- The project uses Django's built-in authentication system with a custom user model
- Static files are served from `/social/static/`
- Templates are organized by app
- The project includes comprehensive test fixtures for development

## API Endpoints

- `/accounts/` - User authentication (login, logout, registration)
- `/profiles/` - User profile management
- `/projects/` - Project and application management

## Testing

Run tests with: `python manage.py test`

Test fixtures are available in the `testing/fixtures/` directory.