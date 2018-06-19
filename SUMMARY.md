
* [导读](README.md)

* 基础部分
    * [第一行代码](Hello.py)
    * [输入与输出](ioTest.py)
    * [常用的数据类型](dataTypeTest.py)
    * [变量](const.py)
    * [常量](variable.py)
    * [list数组](listTest.py)
    * [元组](tupleTest.py)
    * [选择语句](ifTest.py)
    * [循环语句](loopTest.py)
    * [字典容器相当于map](dictTest.py)
    * [set数据集合](setTest.py)
* 函数部分
   * [系统函数](build_in_function.py)
   * [关键字](python_keys.py)
   * [自定义函数](self_definition_function.py)
   * [3种参数](h6/h6_arguments.py)
   * [其他类型的参数](h7/h7_arguments.py)
   * [递归函数](h8/h8_recursive_test.py)
* 数据容器部分
   * [数据容器的截取](h8/h7_slice.py)
   * [数据的迭代输出也就是循环输出](h9/h9_iteration.py)
   * [判断数据是否可以迭代](h9/h9_iteratable.py)
   * [列表生成器](h9/h9_range.py)
   * [判断文件夹下的所有文件](h9/h9_os.py)



以下是其他的内容
* Spring 在数据层和业务层实现数据的分层结构  Service层
    * [服务层的通用接口](src/main/java/service/GenericService.java)	
    * [服务层的书籍表接口](src/main/java/service/BookService.java)	
    * [服务层的地址表接口](src/main/java/service/AddressService.java)	
    * [服务层的学生表接口](src/main/java/service/StudentService.java)	
    * [服务层的课程表接口](src/main/java/service/CourseService.java)	
    
    * [服务层的通用接口实现类](src/main/java/service/impl/GenericServiceImpl.java)	
    * [服务层的书籍表](src/main/java/service/impl/BookServiceImpl.java)	
    * [服务层的地址表](src/main/java/service/impl/AddressServiceImpl.java)	
    * [服务层的学生表](src/main/java/service/impl/StudentServiceImpl.java)	
    * [服务层的课程表](src/main/java/service/impl/CourseServiceImpl.java)	
* Spring 在数据层和数据库层实现数据的分层结构 Dao层
    * [后台数据实现的通用接口](src/main/java/dao/GenericDao.java)	
    * [书籍表数据实现的接口](src/main/java/dao/BookDao.java)	
    * [地址表数据实现的接口](src/main/java/dao/AddressDao.java)	
    * [用户表数据实现的接口](src/main/java/dao/UserDao.java)	
    * [学生表数据实现的接口](src/main/java/dao/StudentDao.java)	
    * [课程表数据实现的接口](src/main/java/dao/CourseDao.java)	
    
    * [所有表数据接口的实现类](src/main/java/dao/impl/GenericDaoImpl.java)	
    * [MyBatis书籍表数据接口的实现类](src/main/java/dao/impl/BookDaoImpl.java)	
    * [MyBatis地址表数据接口的实现类](src/main/java/dao/impl/AddressDaoImpl.java)	
    * [JDBC书籍表数据接口的实现类](src/main/java/dao/impl/JDBCBookDaoImpl.java)	
    * [MyBatis用户表数据接口的实现类](src/main/java/dao/impl/UserDaoImpl.java)	
    * [MyBatis学生表数据接口的实现类](src/main/java/dao/impl/StudentDaoImpl.java)	
    * [MyBatis课程表数据接口的实现类](src/main/java/dao/impl/CourseDaoImpl.java)	
* Spring MVC + MyBaits实现和web页面的交互
    * [MVC配置后台的父类](src/main/java/controller/BaseController.java)	
    * [MVC配置用户表对应的后台](src/main/java/controller/UserController.java)	
    * [MVC配置地址表对应的后台](src/main/java/controller/AddressController.java)	
    * [MVC配置图书表对应的后台](src/main/java/controller/BookController.java)	  
    * [MVC配置学生表对应的后台](src/main/java/controller/StudentController.java)	  
    * [MVC配置课程表对应的后台](src/main/java/controller/CourseController.java)	  
* spring框架webMVC网络框架文件的加载
  * [加载网络文件](src/main/webapp/WEB-INF/web.xml)  
  * [第二个加载网络文件](src/main/webapp/WEB-INF/web-servlet.xml)  
* 数据库相关     
    * [创建数据库SQL语句](sql/db.sql)	
* spring框架IoC_DI控制反转的理解和添加spring配置文件
   * [spring的配置文件](src/main/resources/applicationContext.xml)	
   * [配置文件的使用](src/main/java/ioc/c/Test.java)	 
   * [spring的第二个配置文件](src/main/resources/beans.xml)	
   * [第二个文件的测试文件](src/main/java/ioc/spring/Test.java)	 
   * [spring的第三个配置文件](src/main/resources/test.xml)	
   * [第三个文件的测试文件](src/main/java/ioc/spring/Calculator.java)	
* 页面对应关系
  * [注册的jsp页面](src/main/webapp/sign_up.jsp)	    
  * [主页](src/main/webapp/home.jsp)	    
  * [登录页面](src/main/webapp/index.jsp)	    
  * [图书编辑](src/main/webapp/edit.jsp)	    
  * [显示全部的图书](src/main/webapp/books.jsp)	    
  * [显示该图书对应的用户](src/main/webapp/book.jsp)	    
  * [显示全部的地址](src/main/webapp/addresses.jsp)	    
  * [显示所选用户和地址的对应关系](src/main/webapp/userAddress.jsp)	    
  * [显示所有的用户点击是用户对应的图书](src/main/webapp/users.jsp)	    
  * [显示所有的用户点击是用户对应的地址](src/main/webapp/users1.jsp)	    
  * [显示一个用户对应的图书](src/main/webapp/userBooks.jsp)	    
  * [显示多个用户和他所对应的图书](src/main/webapp/userAndBooks.jsp)	    
  * [创建地址和用户的对应关系](src/main/webapp/createAddress.jsp)	    
  * [显示一个地址对应的用户](src/main/webapp/addressUser.jsp)	    
  * [列出所有的学生](src/main/webapp/students.jsp)	    
  * [列出某个学生学习的多个课程](src/main/webapp/student.jsp)	    
  * [列出所有的课程](src/main/webapp/courses.jsp)	    
  * [列出某个课程学习的所有学生](src/main/webapp/course.jsp)	    
* MyBaits框架配置后台方法这个比较少用  结合HttpServlet类写的   
    * [用户表对应的后台](src/main/java/action/UserAction.java)	
    * [图书表对应的后台](src/main/java/action/BookAction.java)	
* MyBaits框架配置图书对应的数据库表   映射文件  
    * [配置测试类](src/main/java/demo/BookTest.java)	
    * [配置实体类和数据库表对应](src/main/java/model/Book.java)	
    * [配置数据库映射语句  并要加载进来](src/main/resources/mapper/book-mapper.xml)	
* 配置grade文件     
    * [配置grade文件](build.gradle)	
* mybatis框架的初始化java配置和测试   
    * [配置测试类](src/main/java/demo/MyBatisTest.java)	
    * [配置工具类 以后可以没有](src/main/java/util/MyBatisSession.java)	
    * [配置实体类和数据库表对应](src/main/java/model/User.java)	
    * [配置接口](src/main/java/mapper/UserMapper.java)	
* 初始化mybatis框架的数据库资源配置  
    * [配置数据库账号的属性](src/main/resources/jdbc.properties)	
    * [配置数据库参数 以后可以没有](src/main/resources/mybatis-config.xml)	
    * [配置用户表数据库映射语句](src/main/resources/mapper/user-mapper.xml)	
    * [配置图书表数据库映射语句](src/main/resources/mapper/book-mapper.xml)	
    * [配置地址表数据库映射语句](src/main/resources/mapper/address.xml)	
    * [配置课程表数据库映射语句](src/main/resources/mapper/course.xml)	
    * [配置学生表数据库映射语句](src/main/resources/mapper/student.xml)	
* 工具类相关        
    * [编码过滤器](src/main/java/util/EncodingFilter.java)	


