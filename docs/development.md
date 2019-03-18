# Desenvolvimento

## Access Token

```bash
curl -X POST \
  https://auth.fe.fernandoe.com/o/token/ \
  -F grant_type=password \
  -F client_id=wB6ZSQg9D0a77JXAP5SpIZVQ1PySLv0p4k4q4ra1 \
  -F username=dev@example.com \
  -F password=password
```

## Retornar o endereço de um CEP 

```bash
curl -X GET \
  http://localhost:7002/api/v1/enderecos/cep/91060280 \
  -H 'Authorization: Bearer [TOKEN]'
```
