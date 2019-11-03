FROM python:3.6.8-alpine3.8

RUN apk add -U -q --no-cache libxml2-dev libxslt-dev gcc make musl-dev linux-headers tzdata postgresql-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV MOVIE_DATABASE_API_KEY=fd9579be45b1bde99d8f2ceab75d0acd
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]