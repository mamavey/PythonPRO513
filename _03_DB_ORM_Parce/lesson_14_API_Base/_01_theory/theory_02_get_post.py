import requests


def display_repo_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        repo_data = response.json()
        # print(repo_data)
        print(f'Репозиторий: {repo_data['name']}')
        print(f'Звезд: {repo_data['stargazers_count']}')
        print(f'Описание: {repo_data['description']}')
    else:
        print(f'Ошибка: {response.status_code}')


if __name__ == '__main__':
    repo_url = 'https://api.github.com/repos/requests/requests'
    group_repo_url = 'https://api.github.com/repos/mamavey/PythonPRO513'
    display_repo_data(repo_url)
    print()
    display_repo_data(group_repo_url)
