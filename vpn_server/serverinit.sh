echo "Run softether server" 
vpnserver start
sleep 5

vpncmd /SERVER localhost /ADMINHUB:DEFAULT /CMD HubCreate ${HUB_NAME} /PASSWORD:${HUB_PASSWD}
vpncmd /SERVER localhost /ADMINHUB:${HUB_NAME} /CMD UserCreate ${USER_NAME} /GROUP:none /REALNAME:none /NOTE:none
vpncmd /SERVER localhost /ADMINHUB:${HUB_NAME} /CMD UserPasswordSet ${USER_NAME} /PASSWORD:${USER_PASSWD}
vpncmd /SERVER localhost /ADMINHUB:${HUB_NAME} /CMD IPsecEnable /L2TP:yes /L2TPRAW:no /ETHERIP:no /PSK:${COMMON_SECRET}
vpncmd /SERVER localhost /ADMINHUB:${HUB_NAME} /CMD SecureNatEnable
vpncmd /SERVER localhost /ADMINHUB:${HUB_NAME} /CMD NatEnable
vpncmd /SERVER localhost /ADMINHUB:${HUB_NAME} /CMD DHCPEnable


# run container forever
while true; do sleep 100; done
