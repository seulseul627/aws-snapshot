# aws-snapshot
Demo project to manage AWS instance snapshots

# Configuring
shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`

# Running
`pipenv run python shotty/shotty.py <command> <--project=PROJECT>`

*command* is list, start, or stop
*project* is optional
