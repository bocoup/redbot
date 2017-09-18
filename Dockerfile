# redbot
#
# https://github.com/mnot/redbot

# Pull base image.
FROM ubuntu:16.04

MAINTAINER Julien Rottenberg <julien@rottenberg.info>

ENV        DEBIAN_FRONTEND noninteractive
ENV        PYTHONPATH      /redbot


# Install python requirements
#RUN        apt-get update && apt-get install -y python-setuptools make phantomjs && easy_install thor selenium
RUN        apt-get update && apt-get install -y python-setuptools make phantomjs curl
RUN apt-get install -y python3
#RUN apt-get  install -y python3-pip
#RUN pip3 install --upgrade pip
#RUN pip3 --version
#RUN pip3 install thor selenium


ADD        . /redbot
#RUN pip3 install --upgrade setuptools
RUN apt-get install -y python3-setuptools
RUN apt-get install -y locales
#ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
RUN locale-gen "en_US.UTF-8" 
RUN dpkg-reconfigure locales
RUN locale
RUN cd /redbot/thor && python3 setup.py install
RUN cd /redbot && python3 setup.py install

RUN        make --directory=/redbot/test


# Expose ports.
EXPOSE     80

# Define default command.
ENTRYPOINT /redbot/bin/webui.py 80 /redbot/redbot/assets
