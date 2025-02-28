#day09-项目开发流程&项目架构
## 1. 软件开发的一般流程

![软件开发的一般流程](F:\pythonStudy\Django\day09\doc\软件开发的一般流程.png)

```python
1. 需求分析及确认：
	由需求分析工程师与客户确认甚至挖掘需求。输出需求说明文档。

2. 概要设计及详细设计：
	开发对需求进行概要设计，包括系统的基本处理流程，组织结构、模块划分、接口设计、数据库结构设计等。然后在概要设计的基础上进行详细设计。详细设计中描述实现具体模块所涉及到的主要算法、数据结构、类的层次结构及调用关系，需要说明软件系统各个层次中的每一个程序(每个模块或子程序)的设计考虑，以便进行编码和测试。基本达到伪代码的层面。

3. 编码：
	根据详细设计文档进行编码。在实际的项目开发中，编码是占时间最少的。
	
4. 测试：
	一般有专业测试团队进行测试。
	
5. 发布或上线：
	提供各种文档，比如杀毒软件扫描文档，安装手册，操作指南等一系列文档资料打包与程序一起发布。当然后续还会有验收和维护等操作。
	
```



##2. 企业常见开发模式

```python
1.瀑布模型式:
	瀑布模型式是最典型的预见性的方法，严格遵循预先计划的需求分析、设计、编码、集成、测试、维护的步骤顺序进行。瀑布式的主要的问题是它的严格分级导致的自由度降低，项目早期即作出承诺导致对后期需求的变化难以调整，代价高昂。瀑布式方法在需求不明并且在项目进行过程中可能变化的情况下基本是不可行的。
	
2.迭代式开发 （目前公司用的较多的开发模式）
	每次只设计和实现这个产品的一部分；
	逐步逐步完成的方法叫迭代开发；
	每次设计和实现一个阶段叫做一个迭代.
	在迭代式开发方法中，整个开发工作被组织为一系列的短小的、
	固定长度（如3周）的小项目，被称为一系列的迭代。
	每一次迭代都包括了需求分析、设计、实现与测试。
		
3.敏捷开发 （比较热门的开发模式）
	和迭代式开发类似，敏捷开发的周期可能更短，并且更加强调队伍中的高度协作。一个小功能叫做一个story。开发人员要完成stroy文档的编写。
	
```



## 3， 爱鲜蜂项目架构搭建

​     项目效果：  http://121.196.211.220/axf/home/

#### 3.1 项目目录结构

![文件目录结构](F:\pythonStudy\Django\day09\doc\文件目录结构.bmp)

####  3.2 创建项目

```python
django-admin startproject AXF
```

####  3.3  创建App

```python
单独打开AXF项目, 选择运行环境， 并创建App
python manage.py startapp App
```

####  3.4 项目配置

```python
打开settings.py进行如下配置

1，设置允许主机为所有， ALLOWED_HOSTS = ["*"]

2，在INSTALLED_APPS中注册App 

3,  在项目根目录下创建templates目录，并在settings.py中TEMPLATES给DIRS添加路径

4,  在mysql中创建新数据库axf, 并配置数据库为mysql, 

	DATABASES = {    
		'default': {        
			'ENGINE': 'django.db.backends.mysql',       
		 	'NAME': 'axf',       
			'HOST': '127.0.0.1',        
			'PORT': '3306',        
			'USER': 'root',        
			'PASSWORD': 'root',    
		}
	}

5,  设置语言为中文：
	LANGUAGE_CODE = 'zh-hans'

6,  设置时区：
	TIME_ZONE = 'Asia/Shanghai'

7,  配置静态文件和媒体文件目录
	7.1 在根目录下创建static目录， 并在static目录中创建uploads目录
	7.2 在setting.py中配置
		STATICFILES_DIRS = [
			os.path.join(BASE_DIR, 'static'), 
		]
		MEDIA_ROOT = os.path.join(BASE_DIR, 'static/uploads')
	
```

#### 3.5 目录结构

##### static目录

```python
根据项目需求在static目录中创建以下目录:
	应用目录app
	样式目录css
	字体目录fonts
	图片目录img
	脚本文件目录js
	媒体文件目录uploads
 且在app目录下针对每个功能模块分别创建以下目录，分别存放每个功能模块的静态文件
	首页home
	闪购market
	购物车cart
	我的mine
```

##### templates目录

```python
根据项目需求在templates中创建以下目录和文件, 分别存放每个功能模块的模板
	首页home
	闪购market
	购物车cart
	我的mine

	基础模板: base.html 
	主体模板: base_main.html

```



#### 3.6 App配置

```
在App中创建并配置urls.py文件，并配置好工程urls.py的路由规则
```



#### 3.7 编写代码

```
此处省略一万行代码...
```

#### 3.8 复制虚拟环境中的包

```
在旧环境中使用：pip freeze > a.txt
在新环境中使用： pip install -r a.txt
```



## 4. 自学Swiper的使用

​	Swiper官网地址:  http://www.swiper.com.cn/

​				      http://www.swiper.com.cn/usage/index.html

