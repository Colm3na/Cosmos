# > Simple usage:
# > docker-compose build
# > Iniciamos el contenedor con:
# > docker-compose up

# Cosmos binaries image builder
FROM golang:alpine AS cosmos-build

# Set up dependencies
ENV PACKAGES ca-certificates curl make git libc-dev bash gcc linux-headers eudev-dev python

# Set cosmos-sdk version
ENV COSMOS_VERSION v0.34.7

# Install minimum necessary dependencies, build Cosmos SDK, remove packages
RUN apk add --no-cache $PACKAGES 

# Set working directory for the build
WORKDIR /usr/src/app

# Add source files from repo
RUN git clone https://github.com/cosmos/cosmos-sdk.git && \
    cd cosmos-sdk && \
    git fetch --tags && \
    git checkout $COSMOS_VERSION

WORKDIR /usr/src/app/cosmos-sdk
RUN make tools && \
    make install

# Lunie builder image
FROM alpine:edge as lunie-build

# Install deps
RUN apk add --update ca-certificates bash git wget curl nodejs nodejs-npm yarn python make g++ tmux
WORKDIR /usr/src/app

# Clone Lunie repository
RUN git clone https://github.com/luniehq/lunie.git

# Build the Lunie APP
RUN cd lunie \
    && sed -i '/"connect-src"/a \          `http://cosmos.public.dappnode`, \n \         `wss://cosmos.public.dappnode:26657`,' webpack.config.js \
    && yarn install \
    && npm install \
    && RPC="http://cosmos.public.dappnode:26657" yarn build:ui
#    && npm run build 

########## LAST STAGE #########
FROM nginx:alpine

WORKDIR /usr/src/app

COPY --from=lunie-build /usr/src/app/lunie/dist /usr/share/nginx/html

# Copy over binaries from the build
COPY --from=cosmos-build /go/bin/gaiad /usr/bin/gaiad
COPY --from=cosmos-build /go/bin/gaiacli /usr/bin/gaiacli

# Copy default config and genesis
COPY config/config.toml /usr/src/app
COPY config/genesis.json /usr/src/app

#  Copy startup scripts
##############################################################################
COPY start_script.sh /usr/bin/start_script.sh
RUN chmod +x /usr/bin/start_script.sh

#  Start
###############################################################################
# Run gaiad by default, omit entrypoint to ease using container with gaiacli
EXPOSE 26656 26657
ENTRYPOINT start_script.sh 
