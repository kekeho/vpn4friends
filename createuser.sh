echo -n "Input client name: "
read CLIENT_NAME

docker run -v $PWD/vpn_server/openvpn_data:/etc/openvpn --log-driver=none --rm -it vpn4friends_openvpn_server easyrsa build-client-full ${CLIENT_NAME} nopass
docker run -v $PWD/vpn_server/openvpn_data:/etc/openvpn --log-driver=none --rm vpn4friends_openvpn_server ovpn_getclient ${CLIENT_NAME} > ${CLIENT_NAME}.ovpn
