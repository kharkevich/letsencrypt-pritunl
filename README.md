# letsencrypt-pritunl
Letsencrypt plugin for Pritunl

Installation guide:
* Deploy latest version of [Let's Encrypt](https://github.com/letsencrypt/letsencrypt)
* Deploy latest version of [pritunl](https://github.com/pritunl/pritunl)
* In the letsencrypt folder run ./venv/bin/python path/to/letsencrypt-pritunl/setup.py develop
* Put pritunl.py in the letsencrypt folder

## Use cases:
* Get/Renew and install new certificate
 `./letsencrypt-auto run --standalone-supported-challenges http-01 -t -i letsencrypt-pritunl:pritunl -d some.domain.tld --no-redirect`
* Install-only existing certificate
 `./letsencrypt-auto install -t -i letsencrypt-pritunl:pritunl  --letsencrypt-pritunl:pritunl-conf-path /etc/pritunl.conf --cert-path /etc/letsencrypt/live/some.domain.tld/cert.pem --key-path /etc/letsencrypt/live/some.domain.tld/privkey.pem -d some.domain.tld --no-redirect`
 `./letsencrypt-auto install -t -i letsencrypt-pritunl:pritunl  --cert-path /etc/letsencrypt/live/some.domain.tld/cert.pem --key-path /etc/letsencrypt/live/some.domain.tld/privkey.pem -d some.domain.tld --no-redirect`
