#!/bin/bash


aws ecs execute-command --cluster ecs-fargate \
    --task  7449f71733c447beb93a37b77ba5b73c
    --container nginx-container \
    --interactive \
    --command "/bin/sh"
