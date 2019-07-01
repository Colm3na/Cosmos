# Simple usage
# > docker build -t cosmos .
# > Iniciamos el contenedor con:
# ./start-container

FROM golang:alpine AS build-env

# Set up dependencies
ENV PACKAGES curl make git libc-dev bash gcc linux-headers eudev-dev python

# Set cosmos-sdk version
ENV COSMOS_VERSION v0.34.7

# Install minimum necessary dependencies, build Cosmos SDK, remove packages
RUN apk add --no-cache $PACKAGES 

# Set working directory for the build
WORKDIR /go/src/github.com/cosmos

# Add source files from repo
RUN git clone https://github.com/cosmos/cosmos-sdk.git && \
    cd cosmos-sdk && \
    git fetch --tags && \
    git checkout $COSMOS_VERSION

WORKDIR /go/src/github.com/cosmos/cosmos-sdk
RUN make tools && \
    make install

# Final image
FROM alpine:edge

# Install ca-certificates
RUN apk add --update ca-certificates bash git wget curl nodejs nodejs-npm yarn python make g++ tmux
WORKDIR /usr/src/app

# Copy over binaries from the build-env
COPY --from=build-env /go/bin/gaiad /usr/bin/gaiad
COPY --from=build-env /go/bin/gaiacli /usr/bin/gaiacli

# Copy default config and genesis
COPY config/config.toml /
COPY config/genesis.json /

# Copy Lunie repository
#COPY lunie lunie
RUN git clone https://github.com/luniehq/lunie.git

# Build the Lunie APP
RUN cd lunie && yarn install && npm run build

# We use a volume to ensure persistence of the ddbb
VOLUME /root/.gaiad
#RUN mkdir -p /root/.gaiad/config

#  Copy startup scripts
#  ###############################################################################
WORKDIR /root
COPY start_script.sh start_script.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x start_script.sh
RUN chmod +x /entrypoint.sh

#  Start
###############################################################################
# Run gaiad by default, omit entrypoint to ease using container with gaiacli
EXPOSE 26656 26657 9080
ENTRYPOINT "/entrypoint.sh" && "/bin/bash"

