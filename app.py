import click

@click.command()
@click.option('--interface', default='api', 
    help='Input to indicate interaction method (api, event, ui) ')
@click.option('--language', default='javascript', 
    help='Input desired target language (java, python, go, javascript) ')
@click.option('--storage', default='none', 
    help='Input desired storage layer (s3, dynamodb, postgres, redis) ')
@click.argument('name')
def cli(name, interface, language, storage):
    """ Galvanize CLI to create base microservices """
    click.echo('Creating ' + name + ' microservice with options:')
    click.echo('--interface ' + interface)
    click.echo('--language ' + interface)
    click.echo('--storage ' + storage)

    # 1. Validate options passed by the user are valid
    # 2. Based on the language and core configuration options go to github and 
    #    retrieve the proper project template 
    # 3. Based on selected add on modify the service to add queue or storage 
    #    scaffold connections

