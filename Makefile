renew-cert:
	certbot renew --config-dir certs/config --work-dir certs/work --logs-dir certs/logs

kube-secret:
	python secret.py $(DOMAIN) > letsencrypt-$(DOMAIN).json
	kubectl apply -f letsencrypt-$(DOMAIN).json

obtain-cert:
	certbot certonly --agree-tos -d $(DOMAIN) --preferred-challenges dns --manual --config-dir certs/config --work-dir certs/work --logs-dir certs/logs

generate-cert:
	ENV=$(ENV) DOMAIN=${DOMAIN} make kube-secret
