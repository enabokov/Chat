import trafaret as t

from misc.trafaret import are_equal

LoginTrafaret = t.Dict({
    t.Key('name'): t.String(max_length=20),
    t.Key('password'): t.String,
})

SignUpTrafaret = t.Dict({
    t.Key('name'): t.String(max_length=20),
    t.Key('password'): t.String,
    t.Key('confirm_password'): t.String,
}) >> are_equal('password', 'confirm_password',
                msg='Passwords are not equal')
