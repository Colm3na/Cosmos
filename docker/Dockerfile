FROM ubuntu:18.04 

ENV GO_VERSION 1.12.6
ENV GO_ARCH 'linux-amd64'
ENV GO_BIN_SHA 'dbcf71a3c1ea53b8d54ef1b48c85a39a6c9a935d01fc8291ff2b92028e59913c'
ENV GOPATH '/root/go'
ENV GOBIN '/root/go/bin'

#  Install required dev tools to compile gaiad
###############################################################################
RUN apt-get update && apt-get install -y --no-install-recommends wget git ca-certificates gcc make build-essential curl


#  Install golang
###############################################################################
RUN url="https://golang.org/dl/go${GO_VERSION}.${GO_ARCH}.tar.gz" && \
	wget -O go.tgz "$url" && \
	echo "${GO_BIN_SHA} *go.tgz" | sha256sum -c - && \
	tar -C /usr/local -xzf go.tgz &&\
	rm go.tgz

ENV PATH="/usr/local/go/bin:$PATH:$GOBIN"
RUN /usr/local/go/bin/go version 


# Compile gaiad
###############################################################################
RUN mkdir /root/sources
RUN cd /root/sources && git clone https://github.com/cosmos/cosmos-sdk
WORKDIR /root/sources/cosmos-sdk
RUN git fetch --tags
RUN git checkout v0.34.6
RUN cd /root/sources/cosmos-sdk && make install

#  Download genesis file and links file from IPFS
###############################################################################
RUN wget -O /genesis.json https://raw.githubusercontent.com/cosmos/launch/master/genesis.json 

#  Copy startup script
###############################################################################
COPY start_script.sh start_script.sh
RUN chmod +x start_script.sh

#  Start
###############################################################################
EXPOSE 26656 26657
CMD ["./start_script.sh"]

