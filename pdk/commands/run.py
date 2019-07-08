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

import argparse
import os
from pathlib import Path
import subprocess

def prepare_kubernetes_settings(cmd_line):
    kube_directory = str(Path.home()) + "/.kube"
    if os.path.isdir(kube_directory):
        cmd_line.append("--docker-volumes")
        cmd_line.append(kube_directory + ":/kube")
        cmd_line.append("--env")
        cmd_line.append("KUBECONFIG=/kube/config")

def prepare_kubernetes_serviceaccount(kubernetes_namespace):
    os.makedirs("/tmp/pdk-serviceaccount", exist_ok=True)
    with open("/tmp/pdk-serviceaccount/namespace", 'w') as namespace_file:
        namespace_file.write(kubernetes_namespace)

def execute(job,
            docker_pull_policy,
            kubernetes_namespace,
            env,
            trace):
    prepare_kubernetes_serviceaccount(kubernetes_namespace)

    cmd_line = [
        "gitlab-runner", "exec", "docker", job,
        "--docker-pull-policy=" + docker_pull_policy,
        "--env", "CI_PROJECT_NAMESPACE=demo-namespace",
        "--env", "CI_PROJECT_NAME=demo-project",
        "--env", "CI_ENVIRONMENT_SLUG=demo-environment",
        "--docker-volumes", "/tmp/pdk-serviceaccount:/var/run/secrets/kubernetes.io/serviceaccount",
    ]

    prepare_kubernetes_settings(cmd_line)

    if env:
        for variable in env:
            cmd_line.append("--env")
            cmd_line.append(variable)

    if trace:
        cmd_line.append("--env")
        cmd_line.append("TRACE=true")
        print(cmd_line)

    subprocess.check_call(cmd_line)
