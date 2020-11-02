from fabric import *


@task
def hello(ctx):
  print("hello")

@task
def connect(ctx,user,hostname,password):
  conn=Connection(host = hostname,
  user = user,
  connect_kwargs = {
    "password": password,
  })
  conn.run('pwd')