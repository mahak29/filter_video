FROM python:3.6


RUN python3 --version
RUN pip3 --version


#Creating a work directory
WORKDIR /app

#Copy the requirements.txt
COPY /src/requirements.txt ./

#Run the requirements.txt 
RUN pip install -r requirements.txt
COPY src /app




#Run the python code
CMD ["python3","filter.py"]                   
