# QR-Code_security_verification
	基于二维码技术的防伪验证系统 
### 一.设计目的和意义
二维码具有信息容量大、纠错能力强、印刷成本低和唯一性等特点，广泛应用于电子商务移动支付以及防伪验证系统等诸多领域。防伪一般是通过商品的唯一性来查验真假，即每个防伪标识所包含的信息都是不一样的。基于二维码技术的防伪验证系统，可以将每件商品唯一标识生成二维码图片，以二维码图片作为防伪载体，得到查询结果。因此，设计、开发一个基于二维码技术的防伪验证系统，具有很好的实际意义。
该设计要求学生根据二维码技术的基本原理和算法，设计一个“基于二维码技术的防伪验证系统”，对商品信息的真伪进行验证查询。首先，生成商品的防伪二维码并存入数据库中。其次，用户通过手机扫描商品的二维码，与数据库中的防伪二维码信息进行比对。最后，将比对得到的结果返回给用户，从而得到该商品的真伪信息。
此外，学生通过该题目的设计过程，可以初步掌握应用系统的开发原理和开发方法，得到工程开发的训练，提高解决实际问题的能力。
### 二.设计任务及要求
- 整个系统由二维码生成子系统、手机二维码识别子系统和防伪验证子系统等组成；
- 系统分为服务器端和手机终端两部分，其中手机终端主要是二维码的识别、向服务器端发送验证请求和结果展示等。服务器端主要是对生成的商品二维码进行存储，将接受到的验证请求和生成的二维码进行比对以及返回结果等；
- 系统要实现准确、实时地检测、识别功能；
- 系统要有一定的安全控制策略，以保证二维码信息的安全；
- 系统开发技术可以选用C++、Java、Matlab等，数据库可以选用MySQL、SQL Server或Oracle；
- 系统要采用二维码进行测试。

### 三.需求池
	1.商品管理
		> 已完成增删改查
	2.二维码生成
		> 生成问题已经解决，目前在于扫码验证，后续可能会有较大变动
	3.权限验证
		> 管理部分OK
### 四.项目进度
#### QR-Code_security_verification

`2018-03-12`
> - 初始化项目，创建基础目录结构 阅读任务书

`2018-03-21`
> - 完成商品信息管理，CRUD 包括生成校验码

`2018-03-22`
> - 形成Client端使用api 目前缺失状态管理

`2018-03-26`
> - 基础功能完善，准备上线（服务器环境搭建完成）

`2018-03-27`
> - Server端上线了 api待进一步修改

`2018-03-28`
> - 可以进行wechat小程序开发了

`2018-03-30`
> - 完成一些基础功能的搭建，重心在下周（其实感觉下周就能搞完了）

`2018-04-02`
> - 好像真的搞完了...

> 备注 ： 因为之前论文查重我删除掉了这个仓库，现在还原回来，继续搞事~
  博客网址： https://kelovp.tech/nostring/blog/python/922/
