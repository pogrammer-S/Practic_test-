FROM python
WORKDIR /app
COPY Test2.py /app/test2.py
RUN pip install python-dotenv
RUN pip install telebot
ENTRYPOINT ["python", "test2.py"]