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

1. Create a Dockerhub account at https://hub.docker.com/signup if you don't already have one.
2. Log into Dockerhub with the `docker login` command.
3. Navigate to the `entrypoint-headaches` folder
4. Build the image by using the `docker build` command

```bash
docker build -t <Your-dockerhub-username>/docker-headaches:0.0.1 .
```

5. Push the image to a the Dockerhub registry

```bash
docker push <Your-dockerhub-username>/docker-headaches:0.0.1
```

6. Run the commands below and note the differences

```bash
docker run --entrypoint python image
docker run --entrypoint python image script.py
docker run image script.py
docker run image python script.py ENV_VAR1
docker run image “python script.py $ENV_VAR1”
docker run image ‘python script.py $ENV_VAR1’
```

7. How would you change the `ENTRYPOINT` and `CMD` in the Dockerfile to be more reasonable?

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
docker run -p 2022:22 -v $PWD:/home/jovyan/work -w /home/jovyan/work <Your-dockerhub-username>/docker-demo:0.0.1
```

4. SSH into the container

```bash
ssh -p 2022 jovyan@localhost
```

5. Other ways to access the container

```bash
docker exec -ti <container-name> bash
```

Or simply start the container with `bash` as the entrypoint, but note that this will
then override the existing entrypoint and NOT start the SSH server.

```bash
docker run -v $PWD:/home/jovyan/work -w /home/jovyan/work --entrypoint bash <Your-dockerhub-username>/docker-demo:0.0.1
```

6. Install the python packages

```bash
cd /home/jovyan/work
conda env create -f environment.yml
```

7. Activate the environment and run the experiments

```bash
cd /home/jovyan/work
conda activate demopkg
python experiments/train_mlp.py
```

8. Use VS Code to access the container via SSH and run the jupyter notebook in `notebooks`.

VS Code allows you to connect via SSH simply by defining the SSH command that you used previously 
to connect in the shell earlier. After this you will have to open the right folder in the remote VS 
Code window that will open, install and activate the python environment and run the notebook.
