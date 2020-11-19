sudo docker build --no-cache -t flask-server .
sudo docker run -it -p 5000:5000 --rm --name Flask-Server flask-server
