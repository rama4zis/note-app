# install all the required packages
pip3 install -r requirements.txt 

# make migrations
python3.9 manage.py migrate 
python3.9 manage.py collectstatic
