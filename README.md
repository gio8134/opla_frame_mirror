# UdpMirror

This class implements a simple **UdpMirror**. It continuously listens for UDP datagrams and sends them back to the sender until the orchestrator terminates the embedding pod.

## Features

- Listens for incoming UDP datagrams.
- Echoes datagrams back to the sender.
- Runs indefinitely until orchestrator kills the pod.

## Usage

```python
# Example usage
mirror = UdpMirror(host="0.0.0.0", port=12345)
mirror.start()  # Starts listening and echoing UDP packets

