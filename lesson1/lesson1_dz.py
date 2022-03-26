import requests


def git_api():
    """
    Выводим репозицитории пользователя

    :return: список репо в файл repos.json
    """
    resp = requests.get('https://api.github.com/users/Akishev23/repos')
    return resp.content


def nasa_api():
    """
    Авторизуемся на крупнейшем API
    :return: nasa.json
    """

    json = {
        'api_key': 'gXwWTWNFLLw34YuxNL0Md5INg2plYVr5TsgMhoMM'
    }

    resp = requests.get('https://api.nasa.gov/planetary/apod?', params=json)

    return resp.content


if __name__ == '__main__':
    with open('repos.json', 'wb') as f:
        f.write(git_api())
    with open('nasa.json', 'wb') as f:
        f.write(nasa_api())
