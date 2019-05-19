from django.contrib.admin.sites import AdminSite

class MyAdminSite(AdminSite):
    pass

myadmin = MyAdminSite(name="myadmin") 