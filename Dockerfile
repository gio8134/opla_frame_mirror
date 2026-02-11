# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY udp_mirror.py .

# Expose the port (default 9999, but will be configurable)
EXPOSE 9999/udp

# Set default environment variables (can override at runtime)
ENV UDP_PORT=9999
ENV BUFFER_SIZE=1024

# Run the UDP mirror server
CMD ["python", "udp_mirror.py"]

#docker build -t udp-mirror .
#docker run -e UDP_PORT=5005 -e BUFFER_SIZE=2048 -p 5005:5005/udp udp-mirror

#-e UDP_PORT=5005 sets the port the server listens on.
#-e BUFFER_SIZE=2048 sets the buffer size for UDP packets.
#-p 5005:5005/udp maps the container’s UDP port to the host.