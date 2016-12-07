WeChat Example
----------------

A simple Flask demo app that shows how to login with WeChat via WeChat-OAuth2.

Before you begin you must run \`from facebook import db; db.create_all()` from
the python interpreter from within the facebook directory!

- 可以使用`公众平台测试账号 <http://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login>`_ 完成测试

- 修改授权域名：

体验接口权限表 —> 网页授权获取用户基本信息

修改为： your-ip:port, eg. 192.168.1.2:5000
