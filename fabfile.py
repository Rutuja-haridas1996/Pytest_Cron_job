from fabric import *


@task
def hello(ctx):
  print("hello")

@task
def connect(ctx,user,hostname,password):
  #conn=Connection(host="rutujaharidas-HP-Pavilion-Laptop-15-cc1xx", connect_kwargs={"password": "root@123"})
  conn=Connection(host = hostname,
  user = user,
  connect_kwargs = {
    "password": password,
  })
  conn.run('pwd')