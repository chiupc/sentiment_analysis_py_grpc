FROM python:3.8.3
RUN apt-get update
ADD . /SentimentAnalyticPy
WORKDIR /SentimentAnalyticPy
RUN pip install -r requirements.txt
CMD python sentiment_analytic_server.py