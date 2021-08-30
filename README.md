commands

##TO Create Virtual Environment

conda create --name djangoenv django
conda activate djangoenv

##FOR PROJECT SETUP

pip install -r requirements.txt
python manage.py makemigration
python manage.py migrated

##TO START DJANGO APPLICAION

python manage.py runserver

##FOR DJANGO TESTING

coverage run manage.py test
coverage html

##FOR REACT APPLICATION

cd blog_react\blog_app
npm install
npm start
