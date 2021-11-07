FROM python:3.9.1
ADD . /SMOKE_CLASSIFICATION
WORKDIR /SMOKE_CLASSIFICATION
RUN pip install -r requirements.txt
CMD ["python","app.py"]