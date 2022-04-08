# use the `mongo` image
FROM mongo:latest

RUN apt-get update && apt-get install -y python3.9 python3-pip

# copy the app directory and any files needed for your implementation from your local to the container
COPY app .

# equip it with all the packages and installs needed to run the flask app (packages are defined in app/requirements.txt. `pip install -r app/requirements.txt`)
RUN pip install -r requirements.txt

# expose the port flask app will run on
EXPOSE 5000

CMD [ "python3", "app.py"]
