# Recipe Project Context

## Project Structure
- Django REST API for recipe management
- PostgreSQL database
- Docker containerized
- Custom user model with email authentication

## Key Files
- `server/core/settings.py` - Django settings
- `server/core/urls.py` - Main URL configuration
- `server/core/models.py` - Custom User model
- `server/user/` - User API endpoints
- `server/app/` - Main app with tests
- `docker-compose.yml` - Docker configuration

## Tech Stack
- Django 4.2
- Django REST Framework 3.14
- PostgreSQL
- drf-spectacular (Swagger/OpenAPI)

## Custom User Model
Uses email instead of username:
- Email field (unique)
- Name field
- is_active, is_staff, is_superuser flags

## Important Notes
- Always check existing files before suggesting changes
- Tests are in `app/tests/` and `core/tests/`
- API endpoints are prefixed with `/api/`