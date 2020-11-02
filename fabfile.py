from fabric import *


@task
def hello(ctx):
  print("hello")

@task
def connect(ctx):
  #conn=Connection(host="rutujaharidas-HP-Pavilion-Laptop-15-cc1xx", connect_kwargs={"password": "root@123"})
  conn=Connection(host = "rutujaharidas-HP-Pavilion-Laptop-15-cc1xx",
  user = "rutujaharidas",
  connect_kwargs = {
    "password": "root@123",
  })
  conn.run('pwd')