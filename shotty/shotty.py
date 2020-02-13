import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
@click.option('--project', default=None,
    help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    "List EC2 instances"
    instances = []

    if project: # default값으로 들어오는 경우 false임
        print("tag project : " + project)
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
        tags = { t['Key']:t['Value'] for t in i.tags or [] }
        print(', '.join((
            i.instance_type,
            tags.get('Project', '<no project>')
        )))

if __name__ == '__main__':
    list_instances()
