FROM python
WORKDIR /app
COPY Test1.py /app/echo.py
ENTRYPOINT ["python", "echo.py"]