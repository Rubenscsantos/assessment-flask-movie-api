FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV MOVIE_DATABASE_API_KEY=fd9579be45b1bde99d8f2ceab75d0acd
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]