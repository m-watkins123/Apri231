Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> import json
>>> from pprint import pprint
>>> from github import Github
>>> username = "m-watkins123"
>>> url = f"https://api.github.com/repos/m-watkins123/helloWorld/commits"
>>> url = f"https://api.github.com/repos/m-watkins123/helloWorld"
>>> for repo in user.get_repos():
	print_repo("helloWorld")
	print(url + commits)

	
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    for repo in user.get_repos():
NameError: name 'user' is not defined
>>> user = g.get_user()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    user = g.get_user()
NameError: name 'g' is not defined
>>> 
================================ RESTART: Shell ================================
>>> import requests
>>> import json
>>> from pprint import pprint
>>> from github import Github
>>> username = "m-watkins123"
>>> url = f"https://api.github.com/repos/m-watkins123/helloWorld/commits"
>>> user_data = requests.get(url).json()
>>> pprint (user_data)
[{'author': {'avatar_url': 'https://avatars.githubusercontent.com/u/25416602?v=4',
             'events_url': 'https://api.github.com/users/m-watkins123/events{/privacy}',
             'followers_url': 'https://api.github.com/users/m-watkins123/followers',
             'following_url': 'https://api.github.com/users/m-watkins123/following{/other_user}',
             'gists_url': 'https://api.github.com/users/m-watkins123/gists{/gist_id}',
             'gravatar_id': '',
             'html_url': 'https://github.com/m-watkins123',
             'id': 25416602,
             'login': 'm-watkins123',
             'node_id': 'MDQ6VXNlcjI1NDE2NjAy',
             'organizations_url': 'https://api.github.com/users/m-watkins123/orgs',
             'received_events_url': 'https://api.github.com/users/m-watkins123/received_events',
             'repos_url': 'https://api.github.com/users/m-watkins123/repos',
             'site_admin': False,
             'starred_url': 'https://api.github.com/users/m-watkins123/starred{/owner}{/repo}',
             'subscriptions_url': 'https://api.github.com/users/m-watkins123/subscriptions',
             'type': 'User',
             'url': 'https://api.github.com/users/m-watkins123'},
  'comments_url': 'https://api.github.com/repos/m-watkins123/helloWorld/commits/df8ada2749cab47b46968abdf8bbd8c002256d24/comments',
  'commit': {'author': {'date': '2021-08-31T15:01:02Z',
                        'email': 'manassahwatkins@gmail.com',
                        'name': 'Manassah Watkins'},
             'comment_count': 0,
             'committer': {'date': '2021-08-31T15:01:02Z',
                           'email': 'noreply@github.com',
                           'name': 'GitHub'},
             'message': 'Create README.md',
             'tree': {'sha': 'b7786883b26da5facf8520061e5a408f682ec512',
                      'url': 'https://api.github.com/repos/m-watkins123/helloWorld/git/trees/b7786883b26da5facf8520061e5a408f682ec512'},
             'url': 'https://api.github.com/repos/m-watkins123/helloWorld/git/commits/df8ada2749cab47b46968abdf8bbd8c002256d24',
             'verification': {'payload': 'tree '
                                         'b7786883b26da5facf8520061e5a408f682ec512\n'
                                         'parent '
                                         '7b051bac72c315fa764bd866937bf61d523d0d0a\n'
                                         'author Manassah Watkins '
                                         '<manassahwatkins@gmail.com> '
                                         '1630422062 -0400\n'
                                         'committer GitHub '
                                         '<noreply@github.com> 1630422062 '
                                         '-0400\n'
                                         '\n'
                                         'Create README.md',
                              'reason': 'valid',
                              'signature': '-----BEGIN PGP SIGNATURE-----\n'
                                           '\n'
                                           'wsBcBAABCAAQBQJhLkQuCRBK7hj4Ov3rIwAAuQcIAHIetq0EXtOWsIIriuL1VkCj\n'
                                           '0FA0r2BoaNIjywCjmjhkfkUnMC92ZiMQAzo681ksQw3X0dkC8ti+3yEAZD4/r8F6\n'
                                           'fwnVvsxhz9DW0q4KkqlWm3wD9bFuTAa/75MNmkx6tpbeQ3gUYGrhmPQZoW9XHgfS\n'
                                           '8wQ87eL1mYokxN5Jrq0XtX3pXxPocEgToWQKb70dxWsoEA/5FgQ0VVtGLzoRuI+X\n'
                                           'nw0pGUVzq8f+IUtZfPnKwHZnlTu9sd6uQnpHYXjXqh1u2T4BONnrOgnJAWAHuWln\n'
                                           'vNoF9ZQy1SN6zFiFlwYbri/AoBPv/MxnShxbMpQnc0spgb/RbpUvtPlTXbl7aXQ=\n'
                                           '=x44q\n'
                                           '-----END PGP SIGNATURE-----\n',
                              'verified': True}},
  'committer': {'avatar_url': 'https://avatars.githubusercontent.com/u/19864447?v=4',
                'events_url': 'https://api.github.com/users/web-flow/events{/privacy}',
                'followers_url': 'https://api.github.com/users/web-flow/followers',
                'following_url': 'https://api.github.com/users/web-flow/following{/other_user}',
                'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}',
                'gravatar_id': '',
                'html_url': 'https://github.com/web-flow',
                'id': 19864447,
                'login': 'web-flow',
                'node_id': 'MDQ6VXNlcjE5ODY0NDQ3',
                'organizations_url': 'https://api.github.com/users/web-flow/orgs',
                'received_events_url': 'https://api.github.com/users/web-flow/received_events',
                'repos_url': 'https://api.github.com/users/web-flow/repos',
                'site_admin': False,
                'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}',
                'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions',
                'type': 'User',
                'url': 'https://api.github.com/users/web-flow'},
  'html_url': 'https://github.com/m-watkins123/helloWorld/commit/df8ada2749cab47b46968abdf8bbd8c002256d24',
  'node_id': 'MDY6Q29tbWl0NDAxNzQzNjE0OmRmOGFkYTI3NDljYWI0N2I0Njk2OGFiZGY4YmJkOGMwMDIyNTZkMjQ=',
  'parents': [{'html_url': 'https://github.com/m-watkins123/helloWorld/commit/7b051bac72c315fa764bd866937bf61d523d0d0a',
               'sha': '7b051bac72c315fa764bd866937bf61d523d0d0a',
               'url': 'https://api.github.com/repos/m-watkins123/helloWorld/commits/7b051bac72c315fa764bd866937bf61d523d0d0a'}],
  'sha': 'df8ada2749cab47b46968abdf8bbd8c002256d24',
  'url': 'https://api.github.com/repos/m-watkins123/helloWorld/commits/df8ada2749cab47b46968abdf8bbd8c002256d24'},
 {'author': {'avatar_url': 'https://avatars.githubusercontent.com/u/25416602?v=4',
             'events_url': 'https://api.github.com/users/m-watkins123/events{/privacy}',
             'followers_url': 'https://api.github.com/users/m-watkins123/followers',
             'following_url': 'https://api.github.com/users/m-watkins123/following{/other_user}',
             'gists_url': 'https://api.github.com/users/m-watkins123/gists{/gist_id}',
             'gravatar_id': '',
             'html_url': 'https://github.com/m-watkins123',
             'id': 25416602,
             'login': 'm-watkins123',
             'node_id': 'MDQ6VXNlcjI1NDE2NjAy',
             'organizations_url': 'https://api.github.com/users/m-watkins123/orgs',
             'received_events_url': 'https://api.github.com/users/m-watkins123/received_events',
             'repos_url': 'https://api.github.com/users/m-watkins123/repos',
             'site_admin': False,
             'starred_url': 'https://api.github.com/users/m-watkins123/starred{/owner}{/repo}',
             'subscriptions_url': 'https://api.github.com/users/m-watkins123/subscriptions',
             'type': 'User',
             'url': 'https://api.github.com/users/m-watkins123'},
  'comments_url': 'https://api.github.com/repos/m-watkins123/helloWorld/commits/7b051bac72c315fa764bd866937bf61d523d0d0a/comments',
  'commit': {'author': {'date': '2021-08-31T14:59:18Z',
                        'email': 'manassahwatkins@gmail.com',
                        'name': 'Manassah Watkins'},
             'comment_count': 0,
             'committer': {'date': '2021-08-31T14:59:18Z',
                           'email': 'noreply@github.com',
                           'name': 'GitHub'},
             'message': 'Add files via upload',
             'tree': {'sha': 'a2b9808303dc281556e3eb585a542ef86289e464',
                      'url': 'https://api.github.com/repos/m-watkins123/helloWorld/git/trees/a2b9808303dc281556e3eb585a542ef86289e464'},
             'url': 'https://api.github.com/repos/m-watkins123/helloWorld/git/commits/7b051bac72c315fa764bd866937bf61d523d0d0a',
             'verification': {'payload': 'tree '
                                         'a2b9808303dc281556e3eb585a542ef86289e464\n'
                                         'author Manassah Watkins '
                                         '<manassahwatkins@gmail.com> '
                                         '1630421958 -0400\n'
                                         'committer GitHub '
                                         '<noreply@github.com> 1630421958 '
                                         '-0400\n'
                                         '\n'
                                         'Add files via upload',
                              'reason': 'valid',
                              'signature': '-----BEGIN PGP SIGNATURE-----\n'
                                           '\n'
                                           'wsBcBAABCAAQBQJhLkPGCRBK7hj4Ov3rIwAA5bUIADnd/r8uwKRyaquMT8bB7kIK\n'
                                           'yOBT88+JPK3/Re0aOHubJ/5JFWAlhiQ3C+PmfORU/S2cBp0jgidtkwpkhSHRwsh9\n'
                                           'IKE4zd+lIOD7ZbyFds4ruqKGJsTG1JT56x4MPl1S3ny8oh3G9Uk35DjBSZfLC/s9\n'
                                           'vz61nIYEwgM5n9nI7zo7enPqiIBonh0ghoTVaXeJwUwAeorSKVMupqp5iJG61eNX\n'
                                           'F/MzNKQvrpRTjdkBg/sPvdCeO7HgWAiGVTn91nvG6k8FaeqJ1nFqV2F56JAcRNns\n'
                                           'Rt6rZjcRk11heRKAfyRX6t8WPfUpYv01AbZz+3f/cXbb42IEdmDTOZb6VjzCKKA=\n'
                                           '=W4qi\n'
                                           '-----END PGP SIGNATURE-----\n',
                              'verified': True}},
  'committer': {'avatar_url': 'https://avatars.githubusercontent.com/u/19864447?v=4',
                'events_url': 'https://api.github.com/users/web-flow/events{/privacy}',
                'followers_url': 'https://api.github.com/users/web-flow/followers',
                'following_url': 'https://api.github.com/users/web-flow/following{/other_user}',
                'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}',
                'gravatar_id': '',
                'html_url': 'https://github.com/web-flow',
                'id': 19864447,
                'login': 'web-flow',
                'node_id': 'MDQ6VXNlcjE5ODY0NDQ3',
                'organizations_url': 'https://api.github.com/users/web-flow/orgs',
                'received_events_url': 'https://api.github.com/users/web-flow/received_events',
                'repos_url': 'https://api.github.com/users/web-flow/repos',
                'site_admin': False,
                'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}',
                'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions',
                'type': 'User',
                'url': 'https://api.github.com/users/web-flow'},
  'html_url': 'https://github.com/m-watkins123/helloWorld/commit/7b051bac72c315fa764bd866937bf61d523d0d0a',
  'node_id': 'MDY6Q29tbWl0NDAxNzQzNjE0OjdiMDUxYmFjNzJjMzE1ZmE3NjRiZDg2NjkzN2JmNjFkNTIzZDBkMGE=',
  'parents': [],
  'sha': '7b051bac72c315fa764bd866937bf61d523d0d0a',
  'url': 'https://api.github.com/repos/m-watkins123/helloWorld/commits/7b051bac72c315fa764bd866937bf61d523d0d0a'}]
>>> 