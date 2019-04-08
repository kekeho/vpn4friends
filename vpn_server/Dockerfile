FROM ubuntu:bionic
ARG HUB_NAME="DefaultHub"
ARG HUB_PASSWD="DefaultHubPassword"
ARG USER_NAME="DefaultUser"
ARG USER_PASSWD="DefaultUserPassword"
ARG COMMON_SECRET="CommonSec"

RUN apt-get update
RUN apt-get install -y build-essential wget git libncurses-dev libreadline6-dev libssl-dev zlib1g-dev iptables

RUN git clone https://github.com/SoftEtherVPN/SoftEtherVPN_Stable.git
WORKDIR /SoftEtherVPN_Stable
RUN ./configure
RUN make
RUN make install

WORKDIR /
COPY ./* /

CMD ./serverinit.sh
