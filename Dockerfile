# Metube - Backend
# @ Andreas Frisch

FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y build-essential python python-dev python-setuptools nginx supervisor sqlite3
RUN easy_install pip
RUN pip install uwsgi
RUN apt-get install -y python-software-properties
RUN apt-get update
#RUN apt-add-repository -y ppa:nginx/stable

ADD . /usr/local/metube

RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN rm /etc/nginx/sites-available/default
RUN ln -s /usr/local/metube/nginx-metube.conf /etc/nginx/sites-enabled/
RUN ln -s /usr/local/metube/supervisor-metube.conf /etc/supervisor/conf.d/
    
RUN pip install -r /usr/local/metube/requirements.txt

WORKDIR /usr/local/metube
EXPOSE 80

CMD ["supervisord", "-n"]
