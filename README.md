# Auctionly — Online Auction Platform

Auctionly is a Django-based online auction website that brings buyers and auction listings together in one place. Users can explore auction departments, view product details, place bids, and track bid activity. The application also includes account registration, email verification, Google sign-in integration, and email notifications for auction outcomes.

> **Project type:** Django full-stack web application  
> **Repository:** https://github.com/devansh161/aution-site-project-

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Application Architecture](#application-architecture)
- [Database Design](#database-design)
- [Auction Workflow](#auction-workflow)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Deployment](#deployment)
- [Current Scope and Future Improvements](#current-scope-and-future-improvements)

## Overview

Auctionly is designed around an online auction experience. The website presents auction departments and product pages, while Django handles routing, server-side rendering, authentication, database operations, and email workflows.

The application uses Django's built-in authentication system and extends it with a Profile model for email verification. Auction listings and bids are represented as relational database models.

## Features

### 1. Auction browsing

- Homepage and informational pages for Auctionly.
- Department pages for Modern Indian Art, Jewellery, Furniture, and Timepieces.
- Separate pages for live, upcoming, and past auctions.
- Product detail pages displaying the product image, description, starting bid, auction end time, and bid history.

### 2. Bidding

- Each product has a starting bid and an auction end date/time.
- The product page displays a bid form while the auction is active.
- Bid records are associated with both the product and the user who placed them.
- Bid history is displayed in descending order of bid amount.
- The highest recorded bid is used to identify the winner after the auction ends.

### 3. User accounts

- User registration and login using Django authentication.
- Passwords are stored using Django's password hashing through set_password().
- Email verification using a generated UUID token.
- Google sign-in/sign-up integration through Django Allauth.
- Logout functionality and Django session-based authentication.

### 4. Email notifications

The application contains an auction-ending handler that:

- Finds auctions whose end time has passed and which have not yet been marked as notified.
- Identifies the highest bidder, if any.
- Emails the winner and the product owner with the auction result.
- Notifies the owner when an auction ends without bids.
- Marks the auction as processed to avoid sending the same notification repeatedly.

### 5. Contact form

- Collects a visitor's name, email, mobile number, and message.
- Saves submissions in the database for administrative review.

### 6. Django administration

The Django admin site is configured to manage:

- User verification profiles
- Contact submissions
- Auction products
- Bids

Product listings are currently managed through the Django admin interface; a dedicated seller-facing product creation workflow is not present in the current view implementation.

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Backend framework | Django 5.2 |
| Frontend | HTML5, CSS3, JavaScript |
| Templating | Django Template Language |
| Database | SQLite |
| Authentication | Django Authentication |
| Social authentication | Django Allauth, Google OAuth |
| Image processing | Pillow |
| Email service | Gmail SMTP |
| WSGI server | Gunicorn |
| Static file serving | WhiteNoise |
| Deployment configuration | Railway-compatible Procfile |

## Application Architecture

Auctionly follows Django's Model–View–Template (MVT) architecture.

~~~text
                 User / Browser
                       |
                       v
                Django URL Router
                       |
                       v
                  View Functions
                 /      |       \
                /       |        \
               v        v         v
            Models   Templates   Email Service
               |        |
               v        v
            SQLite   HTML / CSS / JS
               |
               v
         Auction & Bid Data
~~~

**Request flow:**

1. A user opens a page or submits a form in the browser.
2. Django's URL configuration maps the requested URL to the appropriate view.
3. The view processes the request and interacts with models when database access is required.
4. Django renders a template with the required context data.
5. The rendered HTML is returned to the browser.

## Database Design

The application defines four main application models in addition to Django's built-in User model.

### Profile

Stores additional account verification information.

| Field | Purpose |
|---|---|
| user | One-to-one relationship with Django User |
| auth_token | UUID-based email verification token |
| is_verified | Indicates whether the account is verified |
| created_at | Profile creation timestamp |

### Product

Stores auction listing information.

| Field | Purpose |
|---|---|
| title | Product name |
| description | Product description |
| image | Uploaded product image |
| starting_bid | Initial bid amount |
| end_auction | Auction end date and time |
| owner | Foreign key to the listing owner |
| winner | Optional foreign key to the winning user |
| notified | Tracks whether end-of-auction notifications were processed |
| is_auction_active | Auction status field |

### Bid

Stores individual bids.

| Field | Purpose |
|---|---|
| product | Foreign key to the auction product |
| user | Foreign key to the bidder |
| amount | Bid amount |
| timestamp | Time when the bid was created |

A product can have multiple bids, and each bid belongs to one product and one user.

### Contact

Stores contact form submissions.

| Field | Purpose |
|---|---|
| name | Visitor's name |
| mail | Visitor's email |
| mobile | Unique mobile number |
| text | Contact message |

## Auction Workflow

1. An administrator creates a product listing through Django admin, including its starting bid and end time.
2. A visitor opens the product detail page.
3. The view retrieves the product and its related bids.
4. The remaining auction time is calculated using Django's timezone utilities.
5. While the auction is active, the page displays the bid form and bid history.
6. When the auction has ended, the highest recorded bid is used to determine the winner.
7. The auction-ending handler can send result emails to the winner and owner and mark the product as processed.

## Project Structure

~~~text
aution-site-project-/
|
├── Auctionly/
│   ├── migrations/
│   ├── static/
│   │   └── Auctionly/
│   │       ├── images/
│   │       ├── *.css
│   │       └── *.js
│   ├── templates/
│   │   ├── Auctionly.html
│   │   ├── signin.html
│   │   ├── signup.html
│   │   ├── openpage.html
│   │   ├── modernart.html
│   │   ├── jewellery.html
│   │   ├── furniture.html
│   │   ├── timepieces.html
│   │   └── other page templates
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
|
├── Online_Auc/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
|
├── images/
├── media/
├── manage.py
├── requirements.txt
├── Procfile
└── runtime.txt
~~~

## Getting Started

### Prerequisites

- Python 3.10 or a compatible Python version.
- pip.
- Git.

### 1. Clone the repository

~~~bash
git clone https://github.com/devansh161/aution-site-project-.git
cd aution-site-project-
~~~

### 2. Create and activate a virtual environment

**Windows:**

~~~bash
python -m venv venv
venv\Scripts\activate
~~~

**macOS / Linux:**

~~~bash
python3 -m venv venv
source venv/bin/activate
~~~

### 3. Install dependencies

~~~bash
pip install -r requirements.txt
~~~

### 4. Configure environment variables

Set the required credentials and integration settings in your local environment. Do not commit secrets to Git.

At minimum, configure the values used by the project:

- EMAIL_HOST_PASSWORD — Gmail SMTP app password.
- SITE_DOMAIN — host name used to construct email verification links.
- GOOGLE_OAUTH_CLIENT_ID — Google OAuth client ID.
- GOOGLE_OAUTH_CLIENT_SECRET — Google OAuth client secret.

The project currently reads the Google OAuth credentials from environment variables in Online_Auc/settings.py. Configure the corresponding Google OAuth application and allowed redirect URLs before using Google sign-in.

### 5. Apply database migrations

~~~bash
python manage.py migrate
~~~

### 6. Create an administrator account

~~~bash
python manage.py createsuperuser
~~~

### 7. Start the development server

~~~bash
python manage.py runserver
~~~

Open the application at:

~~~text
http://127.0.0.1:8000/
~~~

The Django admin panel is available at:

~~~text
http://127.0.0.1:8000/admin/
~~~

## Configuration

The main configuration is in Online_Auc/settings.py.

- SQLite is configured as the default database.
- Media uploads are stored under the configured media directory.
- Django Allauth is configured with Google as a social authentication provider.
- Gmail SMTP is configured for sending verification and auction-result emails.
- WhiteNoise is included for static-file serving in deployment environments.

For local development, use credentials belonging to your own test accounts and configure the email and OAuth settings before testing those workflows.

## Deployment

The repository includes a Gunicorn Procfile, a Python runtime file, and WhiteNoise middleware for deployment support. The application has also been configured with a Railway deployment domain in its settings.

Before deploying or exposing the application publicly:

- Set DEBUG = False.
- Load Django's SECRET_KEY from an environment variable and rotate any key that has been committed to source control.
- Restrict ALLOWED_HOSTS to the actual application domains.
- Configure a production database and persistent media storage if required.
- Verify HTTPS, CSRF trusted origins, SMTP credentials, and Google OAuth redirect URLs.
- Configure a scheduled/background task to run the auction-ending handler automatically.

## Current Scope and Future Improvements

The repository provides the core auction data model, product detail and bidding pages, authentication flows, and auction-result email handling. The following improvements would make the application more robust and production-ready:

- Enforce authentication and authorization on bid submission and product-management actions.
- Validate every bid on the server: it should meet the starting price and exceed the current highest bid.
- Prevent users from bidding on their own listings if that is the intended business rule.
- Use database transactions and appropriate locking to handle simultaneous bids safely.
- Run auction-ending notifications through a scheduled task or background worker instead of relying on a manually triggered URL.
- Add automated tests for registration, verification, bidding, auction expiry, winner selection, and notifications.
- Add seller-facing product creation and management pages.
- Add payment processing and order/delivery workflows if required.
- Improve production configuration and secrets management.

---

**Note:** This README describes the current repository implementation. Some production-grade safeguards and workflows are listed as future improvements rather than being presented as completed features.
