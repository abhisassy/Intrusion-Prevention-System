FROM python:3

ADD rf.py /
ADD anom.csv /

RUN pip install pandas numpy sklearn flask requests

CMD ["python", "./rf.py"]



