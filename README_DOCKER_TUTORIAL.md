# Docker tutorial

These are the instructions you can use to help you follow along
the Docker tutorial organized for the SDSC Academic team on 
October 19th.

## Basic Docker CLI commands

List images

```bash
docker images
```

Pull an image

```bash
docker pull python:3.11-slim-bookworm
```

Run a container

```bash
docker run -ti --rm python:3.11-slim-bookworm
```

List all containers

```bash
docker container ls -a
```

Stop a running container

```bash
docker stop <container-name-or-id>
```

Remove a stopped or failed container

```bash
docker rm <container-name-or-id>
```

## Entrypoint headaches

1. Navigate to the `entrypoint-headaches` folder
2. Build the image by using the `docker build` command

```bash
docker build -t <Your-dockerhub-username>/docker-headaches:0.0.1 .
```

3. Push the image to a the Dockerhub registry

```bash
docker push <Your-dockerhub-username>/docker-headaches:0.0.1
```

4. Run the commands below and note the differences

```bash
docker run --entrypoint python image
docker run --entrypoint python image script.py
docker run image script.py
docker run image python script.py ENV_VAR1
docker run image “python script.py $ENV_VAR1”
docker run image ‘python script.py $ENV_VAR1’
```

5. How would you change the `ENTRYPOINT` and `CMD` in the Dockerfile to be more reasonable?

  - The entrypoint can be `ENTRYPOINT ["python", "script.py"]`
  - Leave the `CMD` empty, put defaults in the code
  - Access environment variables from the code (i.e. `os.environ.get("ENV_VAR1")`)

## More complicated Dockerfile

1. Add your SSH public keys to the `.ssh/authorized_keys` file in this repo.

2. Build the Dockerfile at the base of this repository

```bash
docker build -t <Your-dockerhub-username>/docker-demo:0.0.1 .
```

3. Run the container

```bash
docker run -p 2022:22 -v $PWD:/home/jovyan/work -w /home/jovyan/work image1
```

4. SSH into the container

```bash
ssh -p 2022 jovyan@localhost
```

5. Install the python packages

```bash
cd /home/jovyan/work
conda env create -f environment.yml
```

6. Activate the environment and run the experiments

```bash
cd /home/jovyan/work
conda activate demopkg
python experiments/train_mlp.py
```
