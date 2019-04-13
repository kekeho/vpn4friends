# Get your global ip
GLOBAL_IP=`curl globalip.me`

echo -n "Set VPN's port: "
read USE_PORT

# init openvpn server
docker run -v $PWD/vpn_server/openvpn_data:/etc/openvpn --log-driver=none --rm vpn4friends_openvpn_server ovpn_genconfig -u tcp://${GLOBAL_IP}:${USE_PORT}
docker run -v $PWD/vpn_server/openvpn_data:/etc/openvpn -it --log-driver=none --rm vpn4friends_openvpn_server ovpn_initpki
