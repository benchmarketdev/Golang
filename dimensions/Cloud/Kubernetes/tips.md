## Set a default value for the namespace

kubectl config set-context $(kubectl config current-context) --namespace ${NAMESPACE:-jhub}
