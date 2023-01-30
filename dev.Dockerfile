FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY . /app
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

RUN echo "Doing installs in requirements.txt..."
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "run.py"]