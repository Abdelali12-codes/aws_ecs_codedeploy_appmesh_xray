# aws_ecs_codedeploy_appmesh_xray
## update the running service
```
aws ecs update-service --service ecs-service --enable-execute-command --cluster ecs-fargate
```
## list tasks in the service
```
aws ecs list-tasks --cluster default --service-name service-name
```

## describe the task to check whether the enable command work or not

```

aws ecs describe-tasks \
    --cluster ecs-fargate \
    --tasks task-id
    
```

## interact with the container 

```
aws ecs execute-command --cluster cluster-name \
    --task task-id \
    --container container-name \
    --interactive \
    --command "/bin/sh"
```
