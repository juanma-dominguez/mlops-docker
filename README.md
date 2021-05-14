# mlops-docker
Running machine learning model predictions in docker files.

We are working with the Boston housing dataset https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html to build a docker image ready to make predictions.
#### BUILD IMAGE:

```
 docker build -t boston-price .  
```

Having a trained model and test data in the model folder, we can make a prediction passing those values as a docker bind mounts.

#### RUN DOCKER:
```
docker run -v "$(pwd)"/model:/app/model boston-price
```
