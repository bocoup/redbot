# redbot
#
# https://github.com/mnot/redbot

# Pull base image.
FROM ubuntu:16.04

MAINTAINER Julien Rottenberg <julien@rottenberg.info>

ENV        DEBIAN_FRONTEND noninteractive
ENV        PYTHONPATH      /redbot
ENV        LANG            en_US.UTF-8

# Install python requirements:
#
# - Python3 - required since REDbot version 0.5.0
# - locales - necessary to set the container's locale in support of the `thor`
#             package (which loads a file containing unicode characters as part
#             of its installation procedure); see
#             https://wiki.debian.org/Locale
# - ca-certificates - necessary to fetch Python dependencies from PyPy servers
RUN        apt-get update && \
             apt-get install -y python3-dev python3-setuptools \
               build-essential phantomjs ca-certificates locales

RUN        locale-gen "en_US.UTF-8" && dpkg-reconfigure locales
COPY       . /redbot
WORKDIR    /redbot
RUN        python3 setup.py install && easy_install3 redbot[dev]


# Expose ports.
EXPOSE     80

# Define default command.
ENTRYPOINT /redbot/bin/webui.py 80 /redbot/redbot/assets
