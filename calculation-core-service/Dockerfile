FROM python:3.6

ADD . /app

ADD ./CalculationCoreServiceStart.sh /app

RUN apt-get update && \
 apt-get install -y netcat;

RUN pip install -r /app/requirements.txt

RUN chmod 777 /app/CalculationCoreServiceStart.sh
RUN chmod 777 /app
RUN chmod 777 /app/Runner.py