FROM continuumio/miniconda3:23.5.2-0
RUN groupadd --gid 1000 jovyan && \
    useradd --uid 1000 --gid 1000 -s /bin/bash -m jovyan && \
    apt-get update && \
    apt-get install -y openssh-server && \
    rm -rf /var/lib/apt/lists/*
USER jovyan
WORKDIR /home/jovyan
ENV CONDA_ENVS_PATH=/home/jovyan/.virtualenvs
COPY --chown=jovyan .ssh .ssh
RUN conda init bash && \
    mkdir -p .hostkeys/etc/ssh && \
    ssh-keygen -A -f .hostkeys && \
    chmod 700 .ssh && \
    conda config --set auto_activate_base false
ENTRYPOINT [ "bash", "-c" ]
CMD [ "/usr/sbin/sshd -o HostKey=/home/jovyan/.hostkeys/etc/ssh/ssh_host_rsa_key -o HostKey=/home/jovyan/.hostkeys/etc/ssh/ssh_host_dsa_key -o HostKey=/home/jovyan/.hostkeys/etc/ssh/ssh_host_ecdsa_key -o HostKey=/home/jovyan/.hostkeys/etc/ssh/ssh_host_ed25519_key -o PidFile=/home/jovyan/.sshd.pid && sleep 1 && cat /home/jovyan/.sshd.pid | xargs -I {} tail --pid={} -f /dev/null" ]
