# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate

pip install -r requirements.txt 

# make migrations
python3.9 manage.py migrate 
python3.9 manage.py collectstatic
