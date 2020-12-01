FROM ubuntu

RUN apt-get update -y

# time zone setting
RUN apt-get install -y tzdata

# PHP install
RUN apt-get install -y php

# Apache install
RUN apt-get install -y apache2

EXPOSE 80

# Apache start
CMD ["apachectl","-D","FOREGROUND"]