:orphan:

WeChat-OAuth2
=============

A simple Python WeChat OAuth2 library built on top
of `rauth`_.

.. _rauth: https://github.com/litl/rauth

Installation
------------
Install the module with one of the following commands::

    $ pip install WeChat-OAuth2

Or if you must::

    $ easy_install Wechat-OAuth2


Usage
-----

If you want to check out the complete :ref:`api` documentation, go ahead.

The easiest way to get started is by setting up a service wrapper. To do so
simply import the service container object:

.. code-block:: python
    
    from wechat_oauth2 import WeChatService

    wechat = WeChatService(
        appid='app id',
        secret='app secret')

Using the service wrapper API we can obtain an access token after the
authorization URL has been visited by the client. First generate the
authorization URL:

.. code-block:: python

    redirect_uri = 'https://example.com/connect/login_success.html'
    params = {'scope': 'snsapi_userinfo',
              'redirect_uri': redirect_uri}

    url = wechat.get_authorize_url(**params)

Once this URL has been visited and (presumably) the client authorizes the
application an access token can be obtained:

.. code-block:: python

    # the code should be returned upon the redirect from the authorize step,
    # be sure to use it here (hint: it's in the URL!)
    session = wechat.get_auth_session(code)

    print session.get('userinfo').json()['openid']

.. include:: contents.rst.inc
