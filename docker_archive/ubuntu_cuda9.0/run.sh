docker run \
           --runtime=nvidia \
		   --net=host \
		   --name segmap_docker \
		   -it \
		   -v /home/dyros-vehicle/docker:/root/data \
		   edward0im/dyrosvehicle:ubuntu_cuda9.0
