# Entrypoint headaches

A simple Docker example of how the `ENTRYPOINT` and the `CMD`
commands in a Dockerfile can have interesting consequences.

# Instructions

1. Build the image

```
docker build -t entrypoint-headaches:0.0.1 .
```

2. Run it

```
docker run -ti --rm entrypoint-headaches:0.0.1
```
