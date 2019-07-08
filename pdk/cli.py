# Copyright 2019 Nicolas Byl
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import click

import pdk.commands.run

# TODO: move this to context object
global_verbose = False

@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Enables verbose mode.')
def cli(verbose):
    """The pipeline development kit (PDK) wil help build GitLab CI pipelines.

    It contains helpers to run pipelines locally and shorten the feedback cycle,
    when building new pipelines.
    """
    global_verbose = verbose

@cli.command()
@click.argument('job')
@click.option('--docker-pull-policy', default="never", help='Pull policy for docker images.')
@click.option('--kubernetes-namespace', default="default", help='The kubernetes namespace to inject.')
@click.option('--env', help='Add environment variable to build.', multiple=True)
@click.option('--trace', default=False, help='Enable tracing for PDK.')
def run(job, docker_pull_policy, kubernetes_namespace, env, trace):
    """Run a gitlab ci job.
    """
    pdk.commands.run.execute(
        job=job,
        docker_pull_policy = docker_pull_policy,
        kubernetes_namespace = kubernetes_namespace,
        env = env,
        trace = trace
    )
