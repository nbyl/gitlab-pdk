
#gitlab-runner exec docker automatic_test_setup_deploy_app \
# --docker-pull-policy=never 
# --docker-volumes "/tmp/kubernetes:/var/run/secrets/kubernetes.io/serviceaccount" 
# --docker-volumes "/home/nbyl/.kube:/kube" 
# --env TRACE=true 
# --env CI_PROJECT_NAME=gradle-demo 
# --env CI_ENVIRONMENT_SLUG=production 
# --env CI_PROJECT_NAMESPACE=demo 
# --env KUBECONFIG=/kube/config