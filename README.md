Django Blog API

As a Flask developer transitioning into Django, I undertook this project as a 24-hour challenge to familiarize myself with Django's ecosystem. The goal was to implement a functional REST API featuring user authentication, profile management, blogging capabilities, and comments, all containerized using Docker and orchestrated with Docker Compose.

To ensure a consistent and isolated development environment, I containerized the application using Docker and managed multi-container orchestration with Docker Compose.

This Django-based REST API provides the following functionalities:

    User Management:

        Register: POST /api/users/register/

        Login: POST /api/users/login/

        Change Password: PUT /api/users/change-password/

        Update Profile: PUT /api/users/update-profile/

    Blog Management:

        Create Blog Post: POST /api/blogs/create/

        Update Blog: PUT /api/blogs/blogs/<blog_id>/update/

        Delete Blog: DELETE /api/blogs/<blog_id>/delete/
    
    Comment Management:

        Add Comment: POST /api/blogs/comments/create/

        Update Comment: PUT /api/blogs/comments/<comment_id>/update/

        Delete Comment: DELETE /api/blogs/comments/<comment_id>/delete/