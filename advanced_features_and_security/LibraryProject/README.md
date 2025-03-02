"""
README.md

# Permissions and Groups Setup

## Custom Permissions
Custom permissions are added to the `YourModel` model:
- can_view: Can view the model
- can_create: Can create the model
- can_edit: Can edit the model
- can_delete: Can delete the model

## User Groups
User groups are created and assigned permissions as follows:
- Editors: can_edit, can_create
- Viewers: can_view
- Admins: can_view, can_create, can_edit, can_delete

## Enforcing Permissions in Views
Permissions are enforced in views using the `@permission_required` decorator.
"""

# In your code, add comments explaining the setup
# advanced_features_and_security/views.py
"""
This view allows users to edit instances of YourModel.
Users must have the 'can_edit' permission to access this view.
"""
