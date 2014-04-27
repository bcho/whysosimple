# coding: utf-8

from whysosimple import Simple, Repo


soeasy = Repo('soeasy', providers=['github', 'another-site'])


@soeasy('push')
def handle_push_event(income_data):
    print('Got data: {0}'.format(income_data))


@soeasy.register_event('create')
def handle_create_event(income_data):
    print('Somebody just create some new files...')


app = Simple()


@app.register_provider('another-site', pattern='/another-site')
def another_site_resolver(request):
    return {
        'repo': 'a-awesome-repo',
        'provider': 'another-site',
        'event': 'just-a-placeholder-event'
    }


if __name__ == '__main__':
    app.register_repo(soeasy)

    app.run(host='0.0.0.0')
