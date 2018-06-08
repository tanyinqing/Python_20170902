* [目录](SUMMARY.md)


这个是Python的学习

ese和执行文件
PyCharm  专业版
交互模式 做测试
python xx.py 执行文件






web.xml Project Structure-Facets- web 修改路径配置web.xml文件
Project Structure --Facets--spring  加载spring的配置文件

- ioc 是一种设计方式 Inversion of Control  控制反转
- DI 是依赖注入

对应的老师的项目下载地址

JavaEE-Frameworks-20170902  这个是一个java的项目 配置服务器报错？？
- MyBaits 工作在工作持久层，与数据库关联 
- Spring 
1. Spring MVC
2. Spring AOP
3. Spring IOC

1.Struts 淘汰了

Java EE包含JSP和Servlet

1. build.gradle
2. db.sql
3. index.jsp
4. model.User.java
5. controller.BaseController.java
6. controller.UserController.java
7. WEB-INF/web.xml
8. resources/applicationContext.xml
9. WEB-INF/web-servlet.xml
10. resources/mybatis-config.xml
11. resources/jdbc.properties
12. resources/user-mapper.xml
13. util.MyBatisSession.java

- 应用的典范  
- 重新部署  alt+shift+F10 选redeploy
- 增加web.xml 应用配置文件  file-project Structure-facets  点加号

- run下看错误提示 
    - 因为我的代码是复制老师的，但是我的数据库是自己手敲写的，所以数据库字段对应不正确也会出现空白页面
- http://localhost:8080/

- 用户和书籍  1对多关系
- 用户和地址  多对多
- 双向1对1
- 多对1

1 修改user模型类 添加属性

student course 多对多
id name 
id title

判断是否有课
引入第三方库  3个库会下载下来
1. build.gradle jackson:jackson databind
2. 添加注解

提交头像
1. jsp中加入文件
2. 表单中加入属性
3. 依赖第三方库  
4. web-servlet文件修改
5.建立一个目录，存放用户的头像

Spring file upload
1. jsp <input type="file" ...>
2. jsp <form ...  enctype="multipart/form-data">    
3. build.gradle: commons fileupload
4. web-servlet.xml: multipartResolver bean
5. webapp: avatars folder