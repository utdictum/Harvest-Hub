# Harvest Hub

## Overview
Harvest Hub is an online platform developed in Python using the Django framework. Inspired by the need to offer a marketplace for organic and artisanal food products, it caters to foreign customers residing in Romania. The platform aims to provide a seamless and secure shopping experience.

## Features
- **User Authentication**: Allows users to register, log in, and manage their accounts.
- **Shopping Cart**: Enables users to add items to their cart and manage them without logging in.
- **Order Management**: Handles the complete lifecycle of an order.
- **Checkout Process**: Supports address management, order review, and payment processing.
- **Product Management**: Admins can add, remove, or update product details.

## Technology Stack
- **Backend**: Python, Django, Django Rest Framework
- **Frontend**: HTML, CSS, JavaScript, jQuery, Bootstrap
- **Database**: SQLite
- **Other**: Django MPTT, PayPal SDK

## Installation
### Clone the Repository
```bash
git clone https://github.com/your-username/harvest-hub.git
cd harvest-hub
Set Up a Virtual Environment
bash


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
bash

pip install -r requirements.txt
Initial Setup
bash


python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Access the Application
Open a web browser and go to http://localhost:8000/

Usage
User Interface: Explore product categories, add products to the cart, and proceed to checkout.
Admin Interface: Accessible at http://localhost:8000/admin/. Manage products, categories, orders, and users.
