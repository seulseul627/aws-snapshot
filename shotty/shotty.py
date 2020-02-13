import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "List EC2 instances"    # --help 옵션을 위해 추가
    for i in ec2.instances.all():
        print(i)

if __name__ == '__main__':
    list_instances()
