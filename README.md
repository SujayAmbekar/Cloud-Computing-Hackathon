# CloudHack_1-

Team Members

1. Sujay S Ambekar   - PES1UG19CS516 - Section H
2. Sumukh J Bharadwaj     - PES1UG19CS518 - Section H
3. Suhail Sheikh       - PES1UG19CS513 - Section H
4. Sucheth Hegde - PES1UG19CS511  - Section H

# Commands to execute:

    docker build -t blog-app -f flask-app-image.dockerfile .

    kubectl apply -f secret.yaml

    kubectl apply -f configmap.yaml

    kubectl apply -f deployments.yaml

    kubectl apply -f services.yaml

    kubectl get svc

    kubectl get deployments

    kubectl describe service mongo-express-service

    kubectl describe service blog-app-service


    #cleanup command to execute at end
    kubectl delete all --all

# Inserting docs into MongoDB via Mongo shell:
Get into terminal of the mongodb server pod:
        
        (kubectl get pods)
        kubectl exec --stdin --tty mongodb-pod-name -- /bin/bash

In terminal type mongo to enter into mongo CLI (shell)
Code to insert:

        use admin
        db.auth("username", "password")
        use blog
        db.createCollection("posts")
        db.posts.insert({
            title: "title",
            author: "author",
            createdAt: ISODate("yyyy-mm-dd")
        })

exit from bash:

        exit

# Inserting docs using python file:
copy addRecords.py file to the flask-app pod:

        kubectl cp addRecords.py flask-app-pod-name:/

Get into terminal of the flask-app pod:

        kubectl exec --stdin --tty flask-app-pod-name -- /bin/bash
        ls
        python3 addRecords.py

exit from bash:

        exit

#Show all containers
docker container ls

#Show users
show users

db.posts.find()

{
        "_id": ObjectID(),
        title : "foot",
        name : "shhxsjh"
}

#Show ports of pods on command line
kubectl get svc

kubectl describe service mongo-express-service

kubectl describe service blog-app-service