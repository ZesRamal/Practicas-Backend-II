FROM postgres:16

COPY query_base.sql /docker-entrypoint-initdb.d/
COPY query.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

CMD ["postgres"]