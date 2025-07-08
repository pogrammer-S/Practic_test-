FROM Python
WORKDIR /echoPython
COPY Tes1.py /echoPython/echo.py
ENTRYPOINT ["python", "echo.py"]