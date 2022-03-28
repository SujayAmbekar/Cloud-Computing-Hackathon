# use the `mongo` image
# copy the app directory and any files needed for your implementation from your local to the container
# equip it with all the packages and installs needed to run the flask app (packages are defined in app/requirements.txt. `pip install -r app/requirements.txt`)
# expose the port flask app will run on

FROM mongo:latest

RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip


# working dir inside container, this means if we have a folder called app inside container use that
# or create it
# commands that follow will be exec inside app/ inside of the container
WORKDIR /blog

ADD . .

EXPOSE 5000

# install dependecies
RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
