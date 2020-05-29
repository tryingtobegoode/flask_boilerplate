FROM python:3.6

ADD . /
RUN pip install Cython
RUN pip install dnspython
RUN pip install Flask-JWT-Extended
RUN pip install gunicorn
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "wsgi:app"]