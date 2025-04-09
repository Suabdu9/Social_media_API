Social Media API
This is a Django-based Social Media API that provides functionalities such as user registration, login, profile customization, and media uploads for posts.

Features
1. User Authentication
Endpoints:
POST /api/register/: Register a new user and receive a token.
POST /api/login/: Log in to retrieve an authentication token.

2. Profile Customization
Users can update their profiles with fields such as:
Bio: A short description.
Endpoints:
GET /api/profile/<user_id>/: Retrieve profile details for a specific user.
PUT /api/profile/<user_id>/: Update profile details for a specific user.

3. Media Uploads for Posts
Users can create posts with optional media attachments.
Endpoints:
POST /api/posts/: Create a post with content and optional media uploads.

Setup Instructions
Step 1: Clone the Repository
Step 2: Install Dependencies
Step 3: Configure the Database
Step 4: Configure AWS S3 for Media Storage
Step 5: Start the Development Server

Authentication Process
Step 1: Register a New User
Send a POST request to /api/register/ with the following fields:
username
email
password

Example payload:

json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword123"
}
The response will include a success message and the authentication token.

Step 2: Log In
Send a POST request to /api/login/ with username and password:

json
{
  "username": "testuser",
  "password": "securepassword123"
}
The response will include a success message and the token:

json
{
  "message": "Login successful!",
  "token": "your-authentication-token"
}
Use the token for all authenticated API requests by including it in the Authorization header:

Authorization: Token your-authentication-token

How to Use the API

Profile Customization

Retrieve Profile:
Send a GET request to /api/profile/<user_id>/.

Update Profile:
Send a PUT request to /api/profile/<user_id>/ with any of the following fields:
bio
location
website
cover_photo

Example payload for updating a profile:

json
{
  "bio": "Software developer with a passion for learning.",
  "location": "Addis Ababa, Ethiopia",
  "website": "https://example.com"
}
Media Uploads for Posts
Create Post:

Send a POST request to /api/posts/ with the following fields:

content: The text content of the post (required).

media: Attach a media file in the request body (optional).

Example payload for creating a post:

json
{
  "content": "This is my first post!"
}
For media files, send the request as multipart/form-data.

Known Bugs
App Naming: The app is currently named "posts" instead of "accounts," which might cause confusion since it handles more functionalities than posts.

Other Minor Bugs:

Occasional slow media uploads due to AWS S3 configuration delays.

API Endpoints Overview
Endpoint	Method	Description
/api/register/	POST	Register a new user and retrieve a token.
/api/login/	POST	Log in and retrieve an authentication token.
/api/profile/<user_id>/	GET	Retrieve user profile details.
/api/profile/<user_id>/	PUT	Update user profile details.
/api/posts/	POST	Create a new post with optional media uploads.

Technologies Used
Django: Web framework.

Django REST Framework (DRF): API development.

AWS S3: Media file storage.

PostgreSQL: Relational database.