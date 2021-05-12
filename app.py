import click

@click.command()
@click.option('--interface', default='api', 
    help='Input to indicate interaction method (api, event, ui) ')
@click.option('--language', default='javascript', 
    help='Input desired target language (java, python, go, javascript) ')
@click.option('--storage', default='none', 
    help='Input desired storage layer (s3, dynamodb, postgres, redis) ')
@click.option('--tag', default='', 
    help='Array of tags related to functionality of the microservice ')
@click.argument('name')
def cli(name, interface, language, storage, tag):
    """ Galvanize CLI to create base microservices """
    click.echo('Creating ' + name + ' microservice with options:')
    click.echo('    --interface ' + interface)
    click.echo('    --language ' + interface)
    click.echo('    --storage ' + storage)
    click.echo('    --tag ' + tag)

    # 1. Validate options passed by the user are valid.
    # 2. Based on passed options query similar existing microservice and present
    #    most relevant matches to the user.
    # 3. If user decide to continue, based on the language and core config
    #    options go to github and retrieve the proper project template.
    # 4. Based on selected add ons modify the service to add queue, storage or
    #    additional options to set scaffold connections.
    # 5. Create Dockerfile, CI/CD pipeline file
    # 6. Update readme file with specific instructions to run this microservice
    # 7. Return prompt to the user indicating to take a look to readme file

