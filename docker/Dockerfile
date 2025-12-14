FROM ubuntu:24.04

# Install basic tools
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    ninja-build \
    git \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Conan
RUN pip3 install conan --break-system-packages

# Set working directory
WORKDIR /workspace

# Copy project files
COPY . /workspace

# Default command to run the executable
CMD ["./build/default/conan_starter_project"]