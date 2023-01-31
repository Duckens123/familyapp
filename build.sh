#Build the project

echo "Building the project"
python3 -m pip install requirements.txt

echo "Make migration...."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect statistics..."

python3.10.9 manage.py collectstatic --noinput --clear