FROM python:3.11-slim-bookworm
ADD script.py /
ENV ENV_VAR1="ENV_VAR1_VALUE"
ENTRYPOINT [ "bash", "-c" ]
CMD [ "python script.py $ENV_VAR1" ]
