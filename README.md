# kube-letsencrypt

Use Let's Encrypt to generate a SSL Cert to be used in Kubernetes via
Kubernetes Secrets.

# Usage

## Obtain a cert

```
make obtain-cert DOMAIN=app.opszero.com
```

Make sure to check in the certs dir.

## Generate Kubernetes Secret

```
make generate-cert DOMAIN=app.opszero.com
make kube-secret
```

## Renew a cert

```
make renew-cert DOMAIN=app.opszero.com
```

# Project by opsZero

<a href="https://www.opszero.com"><img src="http://assets.opszero.com.s3.amazonaws.com/images/opszero_11_29_2016.png" width="300px"/></a>

This project is brought to you by [opsZero](https://www.opszero.com)
we provide DevOps for Startups. If you need help with your
infrastructure reach out.

# License

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
