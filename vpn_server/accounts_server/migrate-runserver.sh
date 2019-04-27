GLOBAL_IP=`curl globalip.me`
echo "Global IP: ${GLOBAL_IP}"
export GLOBAL_IP

echo "Start runserver"
python manage.py runserver 0.0.0.0:8000 &
ovpn_run &
python ipchange.py
