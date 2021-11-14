FROM python:3.7
ADD . /SMOKE_CLASSIFICATION
WORKDIR /SMOKE_CLASSIFICATION
RUN pip install -r requirements.txt

#CMD ["python","app.py"]
RUN chmod +x gunicorn_starter.sh
ENTRYPOINT ["./gunicorn_starter.sh"]