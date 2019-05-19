from ProHyre.admin import myadmin

# Register your models here.
from .models import School, Company, Education,\
	Experience, UserProfile, Address, \
	Skill, SchoolProject, Objective


myadmin.register(School, list_display=['name'])
myadmin.register(Company)
myadmin.register(Education)
myadmin.register(Objective)
myadmin.register(Experience)
myadmin.register(UserProfile)
myadmin.register(Address)
myadmin.register(Skill)
myadmin.register(SchoolProject)
