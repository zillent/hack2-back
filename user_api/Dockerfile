FROM python:3.8.2-alpine3.11

ADD ./requirements.txt /hack2_api/requirements.txt

RUN set -ex \
   && apk add --no-cache jpeg-dev zlib-dev \
   && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
   && python -m venv /env \
   && /env/bin/pip install --upgrade pip \
   && /env/bin/pip install --no-cache-dir -r /hack2_api/requirements.txt \
   && runDeps="$(scanelf --needed --nobanner --recursive /env \
       | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
       | sort -u \
       | xargs -r apk info --installed \
       | sort -u)" \
   && apk add --virtual rundeps $runDeps \
   && apk del .build-deps

ADD ./user_api /hack2_api/user_api
ADD ./v0 /hack2_api/v0

WORKDIR /hack2_api

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8823

CMD ["gunicorn", "--bind", ":8823", "--workers", "3", "user_api.wsgi:application"]
