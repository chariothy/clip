# For docker project
# @version 1.0

FROM python:3.10
LABEL maintainer="chariothy@gmail.com"

EXPOSE 8833

ENV CLIP_MAIL_FROM="Henry TIAN <chariothy@gmail.com>"
ENV CLIP_MAIL_TO="Henry TIAN <chariothy@gmail.com>"

ENV CLIP_SMTP_HOST=smtp.gmail.com
ENV CLIP_SMTP_PORT=25
ENV CLIP_SMTP_USER=chariothy@gmail.com
ENV CLIP_SMTP_PWD=password

COPY ./requirements.txt .

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
  && echo 'Asia/Shanghai' > /etc/timezone \
  && pip install -U pip \
  && pip install --no-cache-dir -r ./requirements.txt
  
WORKDIR /root

CMD [ "python", "main.py" ]
