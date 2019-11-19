# Docker Compose, just quieter

Docker Compose CLI utility wrapper which makes `docker-compose` quieter.

This Docker Compose CLI utility wrapper allows users to hide *Starting <...>* / *Stopping <...>* and similar messages from `docker-compose`'s output.

Docker Compose is overly verbose when starting containers for a service:

```bash
$ docker-compose --project-name test run --rm test_service bash
Creating network "test-bash_default" with the default driver
Creating test-bash_postgresql-server_1         ... done
Creating test-bash_solr-zookeeper_1            ... done
Creating test-bash_extract-article-from-page_1 ... done
Creating test-bash_rabbitmq-server_1           ... done
Creating test-bash_solr-shard-01_1             ... done
Creating test-bash_import-solr-data-for-testing_1 ... done

$ docker-compose --project-name test down --volumes
Stopping test-bash_import-solr-data-for-testing_1 ... done
Stopping test-bash_solr-shard-01_1                ... done
Stopping test-bash_postgresql-server_1            ... done
Stopping test-bash_solr-zookeeper_1               ... done
Stopping test-bash_extract-article-from-page_1    ... done
Stopping test-bash_rabbitmq-server_1              ... done
Removing test-bash_import-solr-data-for-testing_1 ... done
Removing test-bash_solr-shard-01_1                ... done
Removing test-bash_postgresql-server_1            ... done
Removing test-bash_solr-zookeeper_1               ... done
Removing test-bash_extract-article-from-page_1    ... done
Removing test-bash_rabbitmq-server_1              ... done
Removing network test-bash_default
```

Setting `--log-level` to `WARNING` doesn't seem to help, and multiple issues and PRs to address the issue have been unsuccessful so far:

* <https://github.com/docker/compose/pull/6217>
* <https://github.com/docker/compose/pull/6194>
* <https://github.com/docker/compose/issues/6026>

This wrapper monkey-patches [`ParallelStreamWriter`](https://github.com/docker/compose/blob/master/compose/parallel.py#L259-L320) for it to take into account `--log-level` setting and make the output quieter, and then runs Compose's CLI normally.


## Why it's cool to use

* This is **not a fork**, so the utility should work with newer versions of Compose as long as `ParallelStreamWriter` interface remains the same as it was at the time of writing this hack. So far, it's been tested with `docker-compose` version 1.25.0 and Python 3.7.
* It **doesn't have any third party dependencies** (except for Docker Compose itself of course).
* It **doesn't have to be installed**, you can just add this repository as a submodule to your project, or copy-paste the `docker-compose-just-quieter` script somewhere. With that said, you can `pip3 install docker-compose-just-quieter` too if you feel like it.


## Usage

1) Install Docker Compose using your [favourite method](https://docs.docker.com/compose/install/), e.g.:

```bash
$ pip3 install docker-compose
```

2) Place `docker-compose-just-quieter` script somewhere in your `PATH`, or add directory with `docker-compose-just-quieter` to your `PATH`.

3) Use `docker-compose-just-quieter` script instead of vendor's `docker-compose` script, e.g.:

```bash
docker-compose-just-quieter ps
```

4) Reduce verbosity level with `--log-level` argument just like you would for `docker-compose` itself, e.g.:

```bash
$ docker-compose-just-quieter --log-level WARNING run test_service bash
```
