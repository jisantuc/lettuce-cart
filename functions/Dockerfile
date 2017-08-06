FROM python:3.6

COPY requirements.txt /opt/lettuce-cart/requirements.txt
WORKDIR /opt/lettuce-cart

RUN pip install -r requirements.txt

ENTRYPOINT ipython
