FROM python:3.8.6



ADD manager /code
RUN pip install psycopg2

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -P /
RUN chmod +x /wait-for-it.sh
ENTRYPOINT ["/wait-for-it.sh", "db:5432", "--"]


CMD ["python","-m","code"]
