#!/env/bin python
# coding: utf-8

from OpenSSL.crypto import load_certificate, FILETYPE_PEM
from OpenSSL.crypto import Error as OpenSSLCryptoError
import os
from lxml import etree
from signxml import XMLSigner

example_xml_files = (os.path.join(os.path.dirname(__file__), "example.xml"),
                     os.path.join(os.path.dirname(__file__), "example2.xml"))
ca_pem_file = os.path.join(os.path.dirname(
    __file__), "example-ca.pem").encode("utf-8")

with open(os.path.join(os.path.dirname(__file__), "example.pem"), "rb") as fh:
    cert = fh.read()
with open(os.path.join(os.path.dirname(__file__), "example.key"), "rb") as fh:
    key = fh.read()

tree = etree.parse(example_xml_files[0])

data = tree.getroot()

signed = XMLSigner(
    digest_algorithm='sha1',
    signature_algorithm='rsa-sha1',
    c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315',
    include_c14n_transform=False
).sign(data,
       passphrase=None,
       key=key,
       cert=cert)


signed_data = etree.tostring(signed)

with open(
    os.path.join(os.path.dirname(__file__),
                 "signed-sample.xml"), "wb") as f:
    f.write(signed_data)
