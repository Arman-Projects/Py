class Permissions:
    def __init__(self):
        self.permissions = set()
    
    def grant_permission(self, permission):
        self.permissions.add(permission)
    
    def revoke_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)
    
    def has_permission(self, permission):
        return permission in self.permissions
    
    def __str__(self):
        return ", ".join(self.permissions) if self.permissions else "No permissions"

class User:
    def __init__(self, username, permissions=None):
        self.username = username
        self.permissions = permissions or Permissions()
    
    def __str__(self):
        return f"User: {self.username}, Permissions: {self.permissions}"

    def can_create_users(self):
        return self.permissions.has_permission('create_users')

class Admin(User):
    def __init__(self, username):
        super().__init__(username, Permissions())
        self.permissions.grant_permission('create_users')
        self.permissions.grant_permission('manage_permissions')
    
    def create_user(self, username, role='user'):
        if role == 'admin':
            return Admin(username)
        else:
            return User(username)
    
    def assign_permission(self, user, permission):
        if self.permissions.has_permission('manage_permissions'):
            user.permissions.grant_permission(permission)

admin = Admin('admin_user')
user1 = admin.create_user('user1')
admin.assign_permission(user1, 'create_users')
print(user1)
admin2 = admin.create_user('admin2', role='admin')
print(admin2)
print(user1.can_create_users())
admin.assign_permission(user1, 'create_users')
user1.permissions.revoke_permission('create_users')
print(user1)
