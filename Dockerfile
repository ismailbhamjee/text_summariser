# syntax=docker/dockerfile:1

FROM python:3.8.13

WORKDIR /summeriser
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#RUN conda install -c apple tensorflow-macos 
#RUN conda install -c apple tensorflow-metal 
#RUN conda install pytorch torchvision torchaudio -c pytorch-nightly
#RUN conda install -c apple tensorflow-deps
#RUN conda install -c conda-forge tensorflow 
#RUN python -m pip install tensorflow-metal
#RUN pipenv install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.9.0-py3-none-any.whl

#RUN pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.9.0-py3-none-any.whl
#python -m pip install torch==1.7.0 -f https://download.pytorch.org/whl/torch_stable.html


COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]