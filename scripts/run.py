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

def prepare_kubernetes_settings(args, cmd_line):
  kube_directory = str(Path.home()) + "/.kube"
  if os.path.isdir(kube_directory):
    cmd_line.append("--docker-volumes")
    cmd_line.append(kube_directory + ":/kube")
    cmd_line.append("--env")
    cmd_line.append("KUBECONFIG=/kube/config")

def prepare_kubernetes_serviceaccount(args):
  os.makedirs("/tmp/pdk-serviceaccount", exist_ok=True)
  with open("/tmp/pdk-serviceaccount/namespace", 'w') as namespace_file:
    namespace_file.write(args.kubernetes_namespace)
  

parser = argparse.ArgumentParser(description='Run a gitlab ci job.')
parser.add_argument("job", help="GitLab CI job to execute.")
parser.add_argument("--docker-pull-policy", default="never", help="Pull policy for docker images.")
parser.add_argument("--kubernetes-namespace", default="default", help="The kubernetes namespace to inject.")
parser.add_argument("--trace", default=False, help="Enable tracing for PDK.")
args = parser.parse_args()

prepare_kubernetes_serviceaccount(args)

cmd_line = [
  "gitlab-runner", "exec", "docker", args.job,
  "--docker-pull-policy=" + args.docker_pull_policy,
  "--env", "CI_PROJECT_NAMESPACE=demo-namespace",
  "--env", "CI_PROJECT_NAME=demo-project",
  "--env", "CI_ENVIRONMENT_SLUG=demo-environment",
  "--docker-volumes", "/tmp/pdk-serviceaccount:/var/run/secrets/kubernetes.io/serviceaccount",
]

prepare_kubernetes_settings(args, cmd_line)

if args.trace:
  cmd_line.append("--env")
  cmd_line.append("TRACE=true")
  print(cmd_line)

subprocess.check_call(cmd_line)
