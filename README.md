It is about an image which gives the real-time streaming with 2 different frames 
  - one frame consist of simple real-time streaming , and
  - the other will stream with original and three basic colour in single frame(red,blue and green)
  
Technology used - Machine learning(with python) and Docker

Used Dockerfile to create an image

Steps how to run :
1. cd python
2. docker build path_of_dockerfile (like /root/python)
3. now you get the image Id 
       - you can this image Id with the name you want
            - use docker tag image_Id new_name(or new_name:tag)
4. finally run the image with the command
      - docker run -it --net=host  
                       --ipc=host
                       --device=/dev/video0:/dev/video0
                       -e DISPLAY=$DISPLAY
                       --env="QT_X11_N0_MITSHM=1"
                       image_Id (or image_name)
                       
        here I run this command to get the image run
         docker run -it --net=host  
                       --ipc=host
                       --device=/dev/video0:/dev/video0
                       -e DISPLAY=$DISPLAY
                       --env="QT_X11_N0_MITSHM=1"
                       video_filtering:v1.0       #this is my image name which i created by running the dockerfile
                       
