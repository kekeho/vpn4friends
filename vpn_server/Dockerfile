# Original credit: https://github.com/jpetazzo/dockvpn

# Smallest base image
FROM python:3.7.3-alpine3.9

# OpenVPN Settings

# Testing: pamtester
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk add --update openvpn iptables bash easy-rsa openvpn-auth-pam google-authenticator pamtester && \
    ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

# Needed by scripts
ENV OPENVPN /etc/openvpn
ENV EASYRSA /usr/share/easy-rsa
ENV EASYRSA_PKI $OPENVPN/pki
ENV EASYRSA_VARS_FILE $OPENVPN/vars

# Prevents refused client connection because of an expired CRL
ENV EASYRSA_CRL_DAYS 3650

VOLUME ["/etc/openvpn"]

# Internally uses port 1194/udp, remap using `docker run -p 443:1194/tcp`
EXPOSE 1194/tcp

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*

# Add support for OTP authentication using a PAM module
ADD ./otp/openvpn /etc/pam.d/

# Accounts server settings
ENV PYTHONNUNBUFFERED 1

RUN apk add postgresql-dev gcc python3-dev musl-dev

# Init dirs
RUN mkdir /code
RUN mkdir /code/profiles
WORKDIR /code

# Install dependencies
COPY accounts_server/requirements.txt /code/
RUN pip install -r requirements.txt

# Copy source codes
COPY accounts_server /code/

CMD ./migrate-runserver.sh
