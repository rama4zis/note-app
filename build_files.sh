# build_files.sh
pip3 install -r requirements.txt
pip3 install django --upgrade 

# make migrations
python3.9 manage.py migrate 
python3.9 manage.py collectstatic
