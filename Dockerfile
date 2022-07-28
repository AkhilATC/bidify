FROM python:3.7
# (WORKDIR): create /app as the working directory for the application
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
# (COPY source destination): copy file(s) from the source folder to the destination folder.
COPY . /app
ENTRYPOINT ["streamlit", "run"]
CMD ["src/app.py"]