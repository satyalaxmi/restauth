import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authproj.settings")
django.setup()

from django.contrib.auth.hashers import make_password

# from authapp.models.users import User
from django.contrib.auth.models import User
from faker import Faker

fakegen = Faker()


def users_generator():
    user_name = fakegen.user_name()
    first_name = fakegen.first_name()
    last_name = fakegen.last_name()
    email = fakegen.email()
    phonenumber = fakegen.phone_number()
    data, _ = User.objects.get_or_create(
        username=user_name,
        password=make_password("testpassword"),
        first_name=first_name,
        last_name=last_name,
        email=email,
        # phone_num=phonenumber,
    )
    data.save()
    return data


print("populating data........")
for i in range(20):
    users_generator()
print("successfully seeded.")
