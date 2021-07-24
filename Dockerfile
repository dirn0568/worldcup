FROM python:3.9.0

WORKDIR /home/

RUN echo "tes135135"

RUN git clone https://www.github.com/dirn0568/zerotwo.git

WORKDIR /home/zerotwo/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "testing1234567"

RUN pip install mysqlclient

RUN echo "testing1212414217"

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=worldcup.deploy && python manage.py migrate --settings=worldcup.deploy && gunicorn worldcup.wsgi --env DJANGO_SETTINGS_MODULE=worldcup.deploy --bind 0.0.0.0:8000"]