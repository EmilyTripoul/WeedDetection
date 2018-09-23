# Raspberry-server

The raspberry server is hosted directly on the raspberry. It is a relay between the arduinos and the client. it is also able to take photos.

We kept the same interface as the Farmbot Web App api.

## Getting token

Each command is validated through a token. The first step is always to obtain this token from a couple of email address and password.

The following entrypoint is used : `http://ip:port/api/tokens`. You should send a post request with the email and the password in the body of the message :
```
{
    'email':'email@email.com',
    'password':'password'
}
```

If the credentials are valid, a HTTP 200 code will be emited with the token in the body.



