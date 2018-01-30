import sqlalchemy as sa

meta = sa.MetaData()


users = sa.Table(
    'users',
    meta,
    # change me
    sa.Column('id', sa.Integer, nullable=False),
)
