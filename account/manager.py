from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, username, password, first_name, last_name, national_code):
        if not phone_number:
            raise ValueError('کاربر باید حتما شماره همراه داشته باشد')

        if not email:
            raise ValueError('کاربر باید حتما آدرس ایمیل داشته باشد')

        if not username:
            raise ValueError('کاربر باید حتما نام کاربری داشته باشد')

        user = self.model(phone_number=phone_number, email=self.normalize_email(email), username=username,
                          first_name=first_name, last_name=last_name, national_code=national_code)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, username, password, first_name=None, last_name=None, national_code=None):
        user = self.create_user(
            phone_number=phone_number,
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            national_code=national_code
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
