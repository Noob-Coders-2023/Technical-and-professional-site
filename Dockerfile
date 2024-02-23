FROM python:3.11
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
CMD ["gunicorn",  "config.wsgi",':8000']
#FROM python:3.11
#WORKDIR /code
#
## نصب پکیج‌های اولیه
#RUN pip install -U pip
#RUN pip install virtualenv
#
## ایجاد و فعال‌سازی محیط مجازی
#RUN python -m venv venv
#RUN /bin/bash -c "source venv/bin/activate"
#
## نصب پکیج‌های مورد نیاز در محیط مجازی
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#
#COPY . /code/
#
#EXPOSE 8000
#CMD ["waitress-serve", "--port=8000", "config.wsgi:application"]