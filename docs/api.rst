.. _api:

API
===

.. module:: wechat_oauth2

The API is exposed via service wrappers, which provide convenient WeChat OAuth2 flow methods as well as session management.

Each service type has specialized Session objects, which may be used directly.

WeChat Service
--------------

.. autoclass:: wechat_oauth2.WeChatService
    :inherited-members:


WeChat Session
--------------

.. autoclass:: wechat_oauth2.WeChatSession
    :inherited-members:
