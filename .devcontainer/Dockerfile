FROM ubuntu:24.04

# Install basic tools
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    ninja-build \
    gdb \
    git \
    python3 \
    python3-pip \
    clangd \
    && rm -rf /var/lib/apt/lists/*

# Install Conan
RUN pip3 install conan --break-system-packages

# Set working directory
WORKDIR /workspace

# Copy project files
COPY . /workspace

# Setup Conan profile
RUN conan profile detect --force

# Clean and install dependencies
RUN rm -rf build
RUN conan install . --build=missing -of build --profile conan/profiles/debug --profile:build conan/profiles/debug

# Configure and build
RUN cmake --preset debug
RUN cmake --build --preset debug

# Default command
CMD ["/bin/bash"]