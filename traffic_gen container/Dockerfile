FROM python:3

ADD packets.py /
ADD testdata.csv /

RUN pip install pandas flask requests

CMD ["python", "./packets.py"]



