echo "Start migrate"
python manage.py migrate
echo "Start runserver"
python manage.py runserver 0.0.0.0:8000 &
ovpn_run
