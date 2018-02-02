import trafaret as t

LoginTrafaret = t.Dict({
    t.Key('name'): t.String(max_length=20),
    t.Key('password'): t.String,
})

SignUpTrafaret = t.Dict({
    t.Key('name'): t.String(max_length=20),
    t.Key('password'): t.String,
    t.Key('confirm_password'): t.String,
})
