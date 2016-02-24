Simple demonstration logging configuration of `uwsgi` and Django application
inside Docker container.


# Details

My aim is run Docker container with Django application behind `uwsgi` and see
application logs on container's stdout.

I wasn't able to find right combination of settings mainly due to my lack
of knowledge about uWSGI. But smarter head pointing me to this:

    uWSGI is logging to its stderr. App will inherit both stdout/stderr fds
    from parent, so their logs are mixed on stderr, but stdout is app only.
    uWSGI is silent on stdout AFAIK.

With this information I set up first part of the puzzle -- Django application.
See [LOGGING][src/demo/demo/settings.py] and two simple [views with
logging][src/demo/demo/settings.py]. If you try it in your local environment
with internal `runserver` command, you will see log messages mixed into
`runserver` acesss logs.

Second part is uWSGI. Its launch is invoked inside container by this [Dockerfile 
commands][Dockerfile].

Last beast is Nginx. It just listening on HTTP and forwarding traffic to 
`uwsgi`.


# Run

If you want to try it, follow this steps please:

    # build images

    docker build -t msgre/common:research.uwsgi_logging .


    # run two containers, each in separated terminal

    docker run --name demo --rm -ti -p 8080:8080 -v $PWD/src:/src msgre/common:research.uwsgi_logging
    docker run --name nginx --rm -ti -p 8081:80 --link demo -v $PWD/nginx.conf:/etc/nginx/conf.d/default.conf:ro nginx

Now go to browser and enter URL http://localhost:8081 (on Linux) or
http://192.168.99.100:8081 (on OSX; to be sure about this IP check output of
`docker-machine ls`, you should see `default` machine and its IP adress which
is by default `192.168.99.100`).

## Two variants of uwsgi invoking

It is possible to run container in 2 different ways:

* If you want to see output from `uwsgi` and Django application mixed in one
  output, run [variant 1][Dockerfile]
* If you want to see **just** Django application logs, you could redirect
  stderr to `/dev/null`. See [variant 2][Dockerfile] with *shell* syntax of
  [CMD][https://docs.docker.com/engine/reference/builder/#cmd] instruction.


# Thanks

Kudos to Braňo Žarnovičan for http://lists.unbit.it/pipermail/uwsgi/2016-February/008383.html
