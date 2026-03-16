import multiprocessing
import os


bind = "0.0.0.0:8000"
workers = int(os.getenv("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2 + 1))
timeout = 120
accesslog = "-"
errorlog = "-"
wsgi_app = os.path.join(os.path.dirname(__file__), "..", "src", "config.wsgi:application")
