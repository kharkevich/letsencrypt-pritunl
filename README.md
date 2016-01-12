# letsencrypt-pritunl
Letsencrypt plugin for Pritunl

Installation guide:
* Deploy latest version of [Let's Encrypt](https://github.com/letsencrypt/letsencrypt)
* Deploy latest version of [pritunl](https://github.com/pritunl/pritunl)
* Install letsencrypt-pritunl plugin pip install letsencrypt-pritunl

## Use cases:
* Get/Renew and install new certificate

 ```./letsencrypt-auto run --standalone-supported-challenges http-01 -t -i letsencrypt-pritunl:pritunl -d some.domain.tld --no-redirect```

** To automate the renewal process without prompts (for example, with a monthly cron), you can add the letsencrypt parameters --renew-by-default --text

* Install-only existing certificate

 ```./letsencrypt-auto install -t -i letsencrypt-pritunl:pritunl  --letsencrypt-pritunl:pritunl-conf-path /etc/pritunl.conf --cert-path /etc/letsencrypt/live/some.domain.tld/cert.pem --key-path /etc/letsencrypt/live/some.domain.tld/privkey.pem -d some.domain.tld --no-redirect```

 ```./letsencrypt-auto install -t -i letsencrypt-pritunl:pritunl  --cert-path /etc/letsencrypt/live/some.domain.tld/cert.pem --key-path /etc/letsencrypt/live/some.domain.tld/privkey.pem -d some.domain.tld --no-redirect```
