import logging
from concurrent import futures

import grpc
import sentiment_analytic_pb2
import sentiment_analytic_pb2_grpc
import sentiment_analytic
from dotenv import load_dotenv
import os

import nltk
import pandas as pd


class SentimentAnalytic(sentiment_analytic_pb2_grpc.SentimentAnalyticServicer):
    def AnalyzeSentiment(self, request, context):
        filename = os.path.join(os.getenv("DATA_PATH"), request.fileName + "_processed.csv")
        sa = sentiment_analytic.sentiment_analytic()
        analyzed_filename = sa.analyze_sentiment(filename=filename, col=request.columnName)
        summary_data = sa.get_sentiment_summary(analyzed_filename)
        return sentiment_analytic_pb2.OutputFile(filename=analyzed_filename, summaryData=summary_data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sentiment_analytic_pb2_grpc.add_SentimentAnalyticServicer_to_server(SentimentAnalytic(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    nltk.download('vader_lexicon')
    logging.basicConfig()
    load_dotenv()
    serve()
