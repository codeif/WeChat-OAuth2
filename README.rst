WeChat OAuth2 SDK.
==================

微信登录授权的Python库

开发文档
--------

`网站应用微信登录开发指南
<https://open.weixin.qq.com/cgi-bin/showdocument
?action=dir_list&t=resource/res_list&verify=1&id=open1419316505>`_

配置网页授权域名
----------------
  
登录微信公众平台： 开发 -> 接口权限 -> 网页授权获取用户基本信息 -> 网页授权域名


Example Usage
-------------

- 创建service

.. code-block:: python

  from wechat_oauth2 import WeChatService
  wechat = WeChatService(appid,
                         secret)

- 获取authorize_url
    
.. code-block:: python

  params = {'redirect_uri': redirect_uri, 'scope': 'snsapi_userinfo'}
  return redirect(wechat.get_authorize_url(**params))
