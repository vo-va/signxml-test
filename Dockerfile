FROM ubuntu:16.04

RUN \
	export DEBIAN_FRONTEND=noninteractive && \
	apt-get update  -y && \
	apt-get install -y \
        python \
		python \
		curl \
		xmlsec1 \
        git \
        &&\
	curl -O https://bootstrap.pypa.io/get-pip.py &&\
	python get-pip.py && \
	git clone https://github.com/vo-va/signxml.git &&\
	pip install /signxml &&\
	curl -sL https://deb.nodesource.com/setup_8.x | bash - &&\
	apt-get install -y nodejs && \
	npm install xml-crypto xmldom

ADD verify.sh /signxml/test/verify.sh
ADD create_sample.py /signxml/test/create_sample.py
ADD xml-crypto-verify.js /signxml/test/xml-crypto-verify.js



ENTRYPOINT ["/signxml/test/verify.sh"]
