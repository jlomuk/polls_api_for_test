while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py migrate
python manage.py loaddata fixtures.json