# gitlab pipeline development kit (PDK)

**WARNING: This is absolutely alpha quality software. This project is far from having appropriate automatic or manual tests. You have been warned.**

This is toolkit to run [GitLab CI](https://docs.gitlab.com/ee/ci/) Jobs locally for the purpose of developing and testing the pipeline.

## Installation

Please install the [GitLab Runner](https://docs.gitlab.com/runner/) first.

Currently there is no installation method for PDK (Would be a great thing for a first PR?). To add the to your path, you can run the following commands:

```
git clone https://github.com/nbyl/gitlab-pdk.git
cd gitlab-pdk
export PATH=`pwd`/bin/:$PATH
```

Afterwards you'll be able to run `pdk` commands. If you want to make this permanently, please add `PDK_DIRECTORY/bin` to your path variable.

## Quickstart

```
git clone https://gitlab.com/gitlab-examples/nodejs.git
cd nodejs
docker pull node:4.2.2
pdk run test_async
```

## Offline image caching

TBD.