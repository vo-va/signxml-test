#!/bin/sh 
set -e
cd /signxml/test/
python create_sample.py
xmlsec1 --verify --trusted-pem example-ca.pem --pubkey-cert-pem example.pem signed-sample.xml
node xml-crypto-verify.js
