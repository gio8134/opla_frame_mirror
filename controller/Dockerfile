# Use lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy controller code
COPY UdpMirrorKopfController.py .

# Install dependencies
RUN pip install --no-cache-dir kopf kubernetes pyyaml

# Run the controller
CMD ["kopf", "run", "UdpMirrorKopfController.py"]

#docker build -t gio8134/udp-mirror-controller:latest .
#docker tag udp-mirror-controller:latest gio8134/udp-mirror-controller:latest
#docker push gio8134/udp-mirror-controller:latest