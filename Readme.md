**题目：《图书管理软件设计报告》**

## 一、基本介绍

## 二、需求分析

### 2.1
该软件主要面向图书管理员和学生用户

### 2.2
管理员可进行图书的添加删除，也可以对书籍借出和库存情况进行统计，还可以添加新的管理员，学生用户可以查询图书的相关信息，然后进行借阅，但借阅时需要再次输入用户名和密码进行确认，归还时也需输入用户名和密码进行确认。

### 2.3
管理员在登陆时输入账号密码选择管理员登陆即可使用统计、添加、删除和添加管理员功能，学生选择用户登录，登陆后即可使用查询借阅归还功能。

## 三、概要设计

### 3.1软件功能：
![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image1.png)

![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image2.png)

![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image3.png)

### 3.2软件操作流程：

学生可借阅图书、归还图书以及查询图书信息，管理员可以添加图书、删除图书以及查询图书库存信息，还可以注册管理员。

![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image4.png)


### 3.3软件界面设计：

登陆界面
![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image5.png)
注册界面
![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image6.jpeg)
还书界面
![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image7.jpeg)
借书界面
![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image8.jpeg)
查询界面
![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image9.jpeg)
添加界面
![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image10.jpeg)
删除界面
![](https://cdn.jsdelivr.net/gh/o0wde0o/blog-image@main/data/python%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%8F%82%E8%80%83%E8%8C%83%E6%9C%AC_image11.jpeg)
## 四、详细设计

### 4.1登陆界面

**from** tkinter **import** \*  
**from** tkinter.messagebox **import** \*  
**from** User_MainPage **import** \*  
**from** Admir_MainPage **import** \*  
**from** Register_Page **import** \*  
<br/>**class** LoginPage(object):  
**def** \__init_\_(self,master = **None**):  
self.root = master _#定义内部变量root  
_self.root.geometry(**'%dx%d'** % (300,200))_#设置窗口大小  
_self.username = StringVar()  
self.password = StringVar()  
self.createPage()  
<br/>**def** createPage(self):  
self.page = Frame(self.root) _#创建Frame  
_self.page.pack()  
Label(self.page).grid(row = 0,stick = W)  
Label(self.page,text = **'账号'**).grid(row = 1,stick = W,pady = 10)  
Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)  
Label(self.page,text = **'密码'**).grid(row = 2,stick = W,pady = 10)  
Entry(self.page, textvariable=self.password, show=**'\*'**).grid(row=2, column=1, stick=E)  
Button(self.page,text = **'用户登录'**,command = self.loginCheck).grid(row = 3,stick =W, pady = 5)  
Button(self.page,text = **'管理员登录'**,command = self.admir_loginCheck).grid(row = 3,stick =E,column=1)  
Button(self.page,text = **'注册'**,command = self.registerCheck).grid(row = 4,stick =W,column=1,padx = 20,pady = 5)  
<br/>**def** loginCheck(self):  
name = self.username.get()  
password = self.password.get()  
f = open(**'login_true.txt'**)  
**for** line **in** f:  
str = line.strip()  
str2 = **','  
**user_name = str\[:str.index(str2)\]  
pass_word = str\[str.index(str2)+1:\]  
**if** name == user_name **and** pass_word == password:  
temp = 1  
**break  
else**:  
temp = 0  
**if** temp == 1 :  
self.page.destroy()  
User_MainPage(self.root)  
**elif** temp == 0 :  
showinfo(title = **'失败'**, message = **'账号或密码错误，重新登录！'**)  
<br/>**def** admir_loginCheck(self):  
admir_name = self.username.get()  
admir_password = self.password.get()  
f1 = open(**'login_admir.txt'**)  
**for** line1 **in** f1:  
str = line1.strip()  
str1 = **','  
**admir_name_txt = str\[:str.index(str1)\]  
admir_password_txt = str\[str.index(str1)+1:\]  
**if** admir_name == admir_name_txt **and** admir_password == admir_password_txt:  
temp = 3  
**break  
else**:  
temp = 4  
**if** temp == 3:  
self.page.destroy()  
Admir_MainPage(self.root)  
**elif** temp == 4:  
showinfo(title=**'失败'**, message=**'账号或密码错误，重新登录！'**)  
<br/>**def** registerCheck(self):  
self.page.destroy()  
Register_Page(self.root)

4.2注册界面

**from** tkinter **import** \*  
**from** tkinter.messagebox **import** \*  
<br/>**class** Register_Page(object):  
**def** \__init_\_(self, master=**None**):  
self.root = master _#定义内部变量root  
_self.root.geometry(**'%dx%d'** % (500, 420)) _#设置窗口大小  
_self.username = StringVar()  
self.studentId = StringVar()  
self.userpassword = StringVar()  
self.userpasswordre = StringVar()  
self.createPage()  
<br/>**def** createPage(self):  
self.page = Frame(self.root)  
self.page.pack()  
Label(self.page).grid(row = 0,stick = W,pady = 20)  
Label(self.page, text = **'账 号：'**,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,stick = W,pady = 15)  
Entry(self.page,textvariable=self.username,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,column = 1,stick = E)  
Label(self.page, text = **'学 号： '**,font = (**"楷体"**,15,**"bold"**)).grid(row=2, stick=W, pady=15)  
Entry(self.page, textvariable=self.studentId,font = (**"楷体"**,15,**"bold"**)).grid(row=2, column=1, stick=E)  
Label(self.page, text = **'密 码： '**,font = (**"楷体"**,15,**"bold"**)).grid(row=3, stick=W, pady=15)  
Entry(self.page, textvariable=self.userpassword,font = (**"楷体"**,15,**"bold"**),show = **'\*'**).grid(row=3, column=1, stick=E)  
Label(self.page, text = **'重新输入密码： '**,font = (**"楷体"**,15,**"bold"**)).grid(row=4, stick=W, pady=15)  
Entry(self.page, textvariable=self.userpasswordre,font = (**"楷体"**,15,**"bold"**),show = **'#'**).grid(row=4, column=1, stick=E)  
Button(self.page, text=**'注册'**,font = (**"楷体"**,15,**"bold"**),command = self.register_admir).grid(row = 5,stick=W,column=1, pady=20,padx = 30)  
<br/>**def** register_admir(self):  
name = self.username.get()  
id = self.studentId.get()  
password = self.userpassword.get()  
passwordre = self.userpasswordre.get()  
id_str = id\[4:6\]  
f = open(**'login_true.txt'**)  
temp = 0  
**for** line **in** f:  
l = line.strip().split(**','**)  
**if** l\[0\] == name:  
showwarning(message=**'输入用户名已经存在'**)  
temp = 1  
**break  
else**:  
**continue  
if** temp != 1 **and** id_str == **'41' and** password ==passwordre:  
fw = open(**'login_true.txt'**,**'a'**)  
fw.write(name+**','**+password+**'\\n'**)  
fw.close()  
showinfo(message=**'注册成功！'**)  
**elif** temp != 1 **and** password != passwordre:  
showwarning(message=**'两次输入密码不一致'**)  
**elif** temp != 1 **and** id_str != **'41'**:  
showwarning(message=**'学号输入有误！'**)

4.3用户主界面

**from** tkinter **import** \*  
**from** view_user **import** \*  
<br/>**class** User_MainPage(object):  
**def** \__init_\_(self,master = **None**):  
self.root = master _#定义内部变量root  
_self.root.geometry(**'%dx%d'**%(510,475))  
self.creatPage()  
<br/>**def** creatPage(self):  
self.firstPage = FirstFrame(self.root)_#首页  
_self.queryPage = QueryFrame(self.root) _#查询界面  
_self.borrowPage = BorrowFrame(self.root) _#借阅界面  
_self.returnPage = ReturnFrame(self.root) _#归还界面  
_self.firstPage.pack()_#默认查询界面  
_menubar = Menu(self.root)  
menubar.add_command(label = **'首页'**,command = self.firstData)  
menubar.add_command(label = **'查询'**,command = self.queryData)  
menubar.add_command(label = **'借阅'**,command = self.borrowData)  
menubar.add_command(label = **'归还'**,command = self.returnData)  
self.root\[**'menu'**\] = menubar _#设置菜单栏  
<br/>_**def** firstData(self):  
self.firstPage.pack()  
self.queryPage.pack_forget()  
self.borrowPage.pack_forget()  
self.returnPage.pack_forget()  
<br/>**def** queryData(self):  
self.firstPage.pack_forget()  
self.queryPage.pack()  
self.borrowPage.pack_forget()  
self.returnPage.pack_forget()  
<br/>**def** borrowData(self):  
self.firstPage.pack_forget()  
self.queryPage.pack_forget()  
self.borrowPage.pack()  
self.returnPage.pack_forget()  
<br/>**def** returnData(self):  
self.firstPage.pack_forget()  
self.queryPage.pack_forget()  
self.borrowPage.pack_forget()  
self.returnPage.pack()

4.4管理员主界面**from** tkinter **import** \*  
**from** view_admir **import** \*  
<br/>**class** Admir_MainPage(object):  
**def** \__init_\_(self,master = **None**):  
self.root = master _#定义内部变量root  
_self.root.geometry(**'%dx%d'**%(510,475))  
self.creatPage()  
<br/>**def** creatPage(self):  
self.addPage = AddFrame(self.root)_#录入界面  
_self.deletePage = DeleteFrame(self.root) _#删除界面  
_self.countPage = CountFrame(self.root) _#统计界面  
_self.register_admirPage = Register_admirFrame(self.root) _#添加新管理员界面  
_self.addPage.pack()_#默认录入界面  
_menubar = Menu(self.root)  
menubar.add_command(label = **'录入书籍'**,command = self.addData)  
menubar.add_command(label = **'删除书籍'**,command = self.deleteData)  
menubar.add_command(label = **'统计书籍'**,command = self.countData)  
menubar.add_command(label = **'添加管理员'**,command = self.register_admirData)  
self.root\[**'menu'**\] = menubar _#设置菜单栏  
<br/>_**def** addData(self):  
self.addPage.pack()  
self.deletePage.pack_forget()  
self.countPage.pack_forget()  
self.register_admirPage.pack_forget()  
<br/>**def** deleteData(self):  
self.addPage.pack_forget()  
self.deletePage.pack()  
self.countPage.pack_forget()  
self.register_admirPage.pack_forget()  
<br/>**def** countData(self):  
self.addPage.pack_forget()  
self.deletePage.pack_forget()  
self.countPage.pack()  
self.register_admirPage.pack_forget()  
<br/>**def** register_admirData(self):  
self.addPage.pack_forget()  
self.deletePage.pack_forget()  
self.countPage.pack_forget()  
self.register_admirPage.pack()

4.5管理员操作界面

**from** tkinter **import** \*  
**from** tkinter.messagebox **import** \*  
<br/>**class** AddFrame(Frame):  
**def** \__init_\_(self,master = **None**):  
Frame.\__init_\_(self, master)  
self.root = master _#定义内部变量root  
_self.book_ID = StringVar()  
self.book_Name = StringVar()  
self.book_Writer = StringVar()  
self.book_Num = StringVar()  
self.book_Price = StringVar()  
self.createPage()  
<br/>**def** createPage(self):  
Label(self).grid(row = 0,stick = W,pady = 10)  
Label(self, text = **'编 号：'**,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,stick = W,pady = 15)  
Entry(self,textvariable=self.book_ID,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,column = 1,stick = E)  
Label(self, text = **'书 名: '**,font = (**"楷体"**,15,**"bold"**)).grid(row=2, stick=W, pady=15)  
Entry(self, textvariable=self.book_Name,font = (**"楷体"**,15,**"bold"**)).grid(row=2, column=1, stick=E)  
Label(self, text = **'作 者: '**,font = (**"楷体"**,15,**"bold"**)).grid(row=3, stick=W, pady=15)  
Entry(self, textvariable=self.book_Writer,font = (**"楷体"**,15,**"bold"**)).grid(row=3, column=1, stick=E)  
Label(self, text = **'数量 /本: '**,font = (**"楷体"**,15,**"bold"**)).grid(row=4, stick=W, pady=15)  
Entry(self, textvariable=self.book_Num,font = (**"楷体"**,15,**"bold"**)).grid(row=4, column=1, stick=E)  
Label(self, text = **'价格 /元: '**,font = (**"楷体"**,15,**"bold"**)).grid(row=5, stick=W, pady=15)  
Entry(self, textvariable=self.book_Price,font = (**"楷体"**,15,**"bold"**)).grid(row=5, column=1, stick=E)  
Button(self, text=**'录 入'**,font = (**"楷体"**,15,**"bold"**),command = self.add_books).grid(row = 6,stick=W,column=1, pady=20,padx = 40)  
<br/>**def** add_books(self):  
bookid = self.book_ID.get()  
bookname = self.book_Name.get()  
bookwriter = self.book_Writer.get()  
booknum = self.book_Num.get()  
bookprice = self.book_Price.get()  
f = open(**'books.txt'**)  
temp = 0  
**for** line **in** f:  
l = line.strip().split(**','**)  
**if** l\[1\] == bookname:  
temp = 1  
**break  
else**:  
**continue  
if** temp == 1:_#该书已经存在，则修改其数量  
_**with** open(**'books.txt'**,**'r'**) **as** fr:  
lines = fr.readlines()  
**with** open(**'books.txt'**,**'w'**) **as** fw:  
**for** line **in** lines:  
v = line.strip().split(**','**)  
**if** bookname == v\[1\]:  
num = int(booknum)+int(v\[3\])  
num_str = str(num)  
fw.write(v\[0\]+**','**+v\[1\]+**','**+v\[2\]+**','**+num_str+**','**+v\[4\]+**'\\n'**)  
**else**:  
fw.write(line)  
fr.close()  
fw.close()  
**else**:_#该书不存在，则添加录入信息  
_fw = open(**'books.txt'**,**'a'**)  
fw.write(bookid+**','**+bookname+**','**+bookwriter+**','**+booknum+**','**+bookprice+**'\\n'**)  
fw.close()  
showinfo(message=**'录入成功！'**)  
<br/>**class** DeleteFrame(Frame):  
**def** \__init_\_(self,master = **None**):  
Frame.\__init_\_(self, master)  
self.root = master _#定义内部变量root  
_self.book_Name = StringVar()  
self.booknum_Delete = StringVar()  
self.createPage()  
<br/>**def** createPage(self):  
Label(self).grid(row = 0,stick = W,pady = 10)  
Label(self, text = **'书 名：'**,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,stick = W,pady = 15)  
Entry(self,textvariable=self.book_Name,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,column = 1,stick = E)  
Label(self, text = **'删除数量 /本: '**,font = (**"楷体"**,15,**"bold"**)).grid(row=2, stick=W, pady=15)  
Entry(self, textvariable=self.booknum_Delete,font = (**"楷体"**,15,**"bold"**)).grid(row=2, column=1, stick=E)  
Button(self, text=**'删 除'**,font = (**"楷体"**,15,**"bold"**),command = self.delete_books).grid(row = 6,stick=W,column=1, pady=20,padx = 30)  
<br/>**def** delete_books(self):  
bookname = self.book_Name.get()  
book_num_delete = self.booknum_Delete.get()  
f = open(**'books.txt'**)  
temp = 0  
**for** line **in** f:  
l = line.strip().split(**','**)  
**if** bookname == l\[1\] **and** int(l\[3\]) > int(book_num_delete): _#要删除的书数量小于库存数量  
_temp = 1  
**break  
elif** bookname == l\[1\] **and** int(l\[3\]) <= int(book_num_delete):_#要删除的书数量大于等于库存数量  
_temp = 2  
**break  
else**:  
**continue  
if** temp == 1:  
**with** open(**'books.txt'**,**'r'**) **as** fr:  
lines = fr.readlines()  
**with** open(**'books.txt'**,**'w'**) **as** fw:  
**for** line **in** lines:  
v = line.strip().split(**','**)  
**if** bookname == v\[1\]:  
num = int(l\[3\]) - int(book_num_delete)  
str_value = str(num)  
fw.write(l\[0\]+**','**+l\[1\]+**','**+l\[2\]+**','**+str_value+**','**+l\[4\]+ **'\\n'**)  
**else**:  
fw.write(line)  
fr.close()  
fw.close()  
showinfo(message=**'删除成功！'**)  
**elif** temp == 2:  
**with** open(**'books.txt'**,**'r'**) **as** fr:  
lines = fr.readlines()  
**with** open(**'books.txt'**,**'w'**) **as** fw:  
**for** line **in** lines:  
v = line.strip().split(**','**)  
**if** bookname == v\[1\]:  
**continue  
**fw.write(line)  
fr.close()  
fw.close()  
showinfo(message=**'删除成功！'**)  
**else**:  
showwarning(title = **'Waring'**,message = **'您输入的图书书名有误，请重新输入！'**)  
<br/>**class** CountFrame(Frame):  
**def** \__init_\_(self,master = **None**):  
Frame.\__init_\_(self, master)  
self.root = master _#定义内部变量root  
_self.book_Name = StringVar()  
self.createPage()  
<br/>**def** createPage(self):  
Label(self).grid(row = 0,stick = W,pady = 40)  
Label(self, text = **'书 名：'**,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,stick = W,pady = 20)  
Entry(self,textvariable=self.book_Name,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,column = 1,stick = E)  
Button(self, text=**'统 计'**,font = (**"楷体"**,15,**"bold"**),command = self.count_books).grid(row = 6,stick=W,column=1, pady=20,padx = 30)  
<br/>**def** count_books(self):  
bookname = self.book_Name.get()  
f = open(**'books.txt'**)  
**for** line **in** f:  
l = line.strip().split(**','**)  
**if** l\[1\] == bookname:  
count_remain = int(l\[3\])  
**break  
else**:  
**continue  
**f1 = open(**'book_lend.txt'**)  
count_lend = 0  
**for** line1 **in** f1:  
l1 = line1.strip().split(**','**)  
**if** l1\[0\] == bookname:  
count_lend += 1 _#!Python 中是没有 ++ 和 -- 的  
_**else**:  
**continue  
**count_all = count_remain + count_lend  
countWin = Tk()  
countWin.title(**'统计信息'**)  
countWin.geometry(**'500x400'**)  
Label(countWin).grid(row = 0,stick = W,pady = 20)  
Label(countWin, text = **'书 名： '**+bookname,font = (**"楷体"**,15,**"bold"**)).grid(row=1, stick=W, pady=10,padx = 90)  
Label(countWin, text = **'总 数： '**+str(count_all),font = (**"楷体"**,15,**"bold"**)).grid(row = 2,stick = W,pady = 15,padx = 90)  
Label(countWin, text = **'借出数量： '**+str(count_lend)+**'本'**,font = (**"楷体"**,15,**"bold"**)).grid(row = 3,stick = W,pady = 15,padx = 90)  
Label(countWin, text = **'剩余数量： '**+str(count_remain)+**'本'**,font = (**"楷体"**,15,**"bold"**)).grid(row = 4,stick = W,pady = 15,padx = 90)  
<br/>**class** Register_admirFrame(Frame):  
**def** \__init_\_(self,master = **None**):  
Frame.\__init_\_(self, master)  
self.root = master _#定义内部变量root  
_self.admir_Name = StringVar()  
self.admir_Password = StringVar()  
self.admir_Password_repetion = StringVar()  
self.createPage()  
<br/>**def** createPage(self):  
Label(self).grid(row = 0,stick = W,pady = 20)  
Label(self, text = **'账 号：'**,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,stick = W,pady = 15)  
Entry(self,textvariable=self.admir_Name,font = (**"楷体"**,15,**"bold"**)).grid(row = 1,column = 1,stick = E)  
Label(self, text = **'密 码： '**,font = (**"楷体"**,15,**"bold"**)).grid(row=2, stick=W, pady=15)  
Entry(self, textvariable=self.admir_Password,font = (**"楷体"**,15,**"bold"**),show = **'\*'**).grid(row=2, column=1, stick=E)  
Label(self, text = **'重新输入密码： '**,font = (**"楷体"**,15,**"bold"**)).grid(row=3, stick=W, pady=15)  
Entry(self, textvariable=self.admir_Password_repetion,font = (**"楷体"**,15,**"bold"**),show = **'#'**).grid(row=3, column=1, stick=E)  
Button(self, text=**'注册'**,font = (**"楷体"**,15,**"bold"**),command = self.register_admir).grid(row = 4,stick=W,column=1, pady=20,padx = 30)  
<br/>**def** register_admir(self):  
admirname = self.admir_Name.get()  
admirpassword = self.admir_Password.get()  
admirpasstwo = self.admir_Password_repetion.get()  
f = open(**'login_admir.txt'**)  
temp = 0  
**for** line **in** f:  
l = line.strip().split(**','**)  
**if** l\[0\] == admirname:  
showwarning(message=**'输入用户名已经存在'**)  
temp = 1  
**break  
else**:  
**continue  
if** temp != 1 **and** admirpassword == admirpasstwo:  
fw = open(**'login_admir.txt'**,**'a'**)  
fw.write(admirname+**','**+admirpassword+**'\\n'**)  
fw.close()  
showinfo(message=**'注册成功！'**)  
**elif** temp != 1 **and** admirpassword != admirpasstwo:  
showwarning(message=**'两次输入密码不一致'**)

4.6用户操作界面

**from** tkinter **import** \*  
**from** tkinter.messagebox **import** \*  
**import** datetime  
<br/>**class** FirstFrame(Frame):_\# 继承Frame  
_**def** \__init_\_(self,master=**None**):  
Frame.\__init_\_(self,master)  
self.root = master  
self.createPage()  
<br/>**def** createPage(self):  
self.photo = PhotoImage(file = **"welcome.gif"**)_#tkinter默认只显示gif图片  
_Label(self,image = self.photo).grid(row=0, column=1, stick=W, padx=3)  
<br/>**class** QueryFrame(Frame):  
**def** \__init_\_(self,master=**None**):  
Frame.\__init_\_(self,master)  
self.root = master  
self.book_Name = StringVar()  
self.createPage()  
<br/>**def** createPage(self):  
Label(self).grid(row=0, stick=W, pady=10)  
Label(self, text = **'书 名： '**,font = (**"宋体"**,14,**"bold"**)).grid(row=1, stick=W, pady=10)  
Entry(self, textvariable = self.book_Name,font = (**"宋体"**,14,**"bold"**)).grid(row=1, column=1, stick=E)  
Button(self,text = **'查 找'**,font = (**"宋体"**,14,**"bold"**),command = self.find_book).grid(row = 2,stick=W,column=1, pady=20,padx = 50)  
<br/>**def** find_book(self):  
bookname = self.book_Name.get()  
f2 = open(**'books.txt'**)  
**for** line2 **in** f2:  
str1 = line2.strip()  
List = str1.split(**','**)  
bookid_txt = List\[0\]  
bookname_txt = List\[1\]  
bookwriter_txt = List\[2\]  
booknum_txt = List\[3\]  
bookprice_txt = List\[4\]  
**if** bookname_txt == bookname:  
temp = 1  
**break  
else**:  
temp = 2  
**if** temp == 1:  
bookWindow = Tk()  
bookWindow.title(**'该图书信息'**)  
bookWindow.geometry(**'500x300'**)  
Label(bookWindow).grid(row=0, stick=W, pady=8)  
Label(bookWindow,text = **'编 号：'**+bookid_txt,font = (**"宋体"**,14,**"bold"**)).grid(row=1, stick=W, pady=10,padx = 100)  
Label(bookWindow,text = **'书 名：'**+bookname_txt,font = (**"宋体"**,14,**"bold"**)).grid(row=2, stick=W, pady=10,padx = 100)  
Label(bookWindow,text = **'作 者：'**+bookwriter_txt,font = (**"宋体"**,14,**"bold"**)).grid(row=3, stick=W, pady=10,padx = 100)  
Label(bookWindow,text = **'数 量：'**+booknum_txt+**' 本'**,font = (**"宋体"**,14,**"bold"**)).grid(row=4, stick=W, pady=10,padx = 100)  
Label(bookWindow,text = **'价 格：'**+bookprice_txt+**' 元'**,font = (**"宋体"**,14,**"bold"**)).grid(row=5, stick=W, pady=10,padx = 100)  
bookWindow.mainloop()  
**elif** temp == 2:  
showinfo(message=(**"您查询的书籍不存在！"**))  
<br/>**class** BorrowFrame(Frame):  
**def** \__init_\_(self,master=**None**):  
Frame.\__init_\_(self,master)  
self.root = master  
self.book_Name = StringVar()  
self.user_Name = StringVar()  
self.user_Password = StringVar()  
self.createPage()  
<br/>**def** createPage(self):  
Label(self).grid(row=0, stick=W, pady=10)  
Label(self, text = **'书 名： '**,font = (**"宋体"**,14,**"bold"**)).grid(row=1, stick=W, pady=20)  
Entry(self, textvariable = self.book_Name,font = (**"宋体"**,14,**"bold"**)).grid(row=1, column=1, stick=E)  
Label(self, text = **'用户名： '**,font = (**"宋体"**,14,**"bold"**)).grid(row=2, stick=W, pady=20)  
Entry(self, textvariable = self.user_Name,font = (**"宋体"**,14,**"bold"**)).grid(row=2, column=1, stick=E)  
Label(self, text = **'密 码： '**,font = (**"宋体"**,14,**"bold"**)).grid(row=3, stick=W, pady=20)  
Entry(self, textvariable = self.user_Password, show=**'\*'**,font = (**"宋体"**,14,**"bold"**)).grid(row=3, column=1, stick=E)  
Button(self,text = **'借 书'**,font = (**"宋体"**,14,**"bold"**),command = self.borrow_book).grid(row = 4,stick=W,column=1, pady=20,padx = 50)  
<br/>**def** borrow_book(self):  
f = open(**'books.txt'**)  
f1 = open(**'login_true.txt'**)  
bookname = self.book_Name.get()  
username = self.user_Name.get()  
userpassword =self.user_Password.get()  
**for** line **in** f1:  
str1 = line.strip()  
List = str1.split(**","**)  
username_txt = List\[0\]  
userpassword_txt = List\[1\]  
**if** username == username_txt **and** userpassword == userpassword_txt:  
temp = 1  
**break  
else**:  
temp = 2  
**if** temp == 1:  
**for** line2 **in** f:  
str1 = line2.strip()  
List1 = str1.split(**","**)  
bookname_txt = List1\[1\]  
booknum_txt = List1\[3\]  
**if** bookname == bookname_txt:  
**if** int(booknum_txt) > 0:  
temp1 = 1  
**else**:  
temp1 =2  
**break  
else**:  
temp1 = 0  
**if** temp1 == 0:  
showwarning(title = **'Error'**,message = **'该书不存在！'**)  
**elif** temp1 == 2:  
showwarning(title = **'Error'**,message = **'该书已被借完！'**)  
**else**:  
**with** open(**'books.txt'**, **'r'**) **as** fr:  
lines=fr.readlines()  
**with** open(**'books.txt'**, **'w'**) **as** fw:  
**for** line **in** lines:  
l = line.strip().split(**','**)  
**if** bookname == l\[1\]:  
num=int(l\[3\])-1  
str_value = str(num)  
fw.write(l\[0\]+**','**+l\[1\]+**','**+l\[2\]+**','**+str_value+**','**+l\[4\]+ **'\\n'**)  
**else**:  
fw.write(line)  
fr.close()  
fw.close()  
borrow_date = datetime.datetime.now().strftime(**'%Y-%m-%d'**)  
fw1 = open(**'book_lend.txt'**,**'a'**)  
fw1.write(bookname+**','**+username+**','**+borrow_date+**'\\n'**)  
showinfo(title = **'Success'**,message = **'借书成功！'**)  
**else**:  
showwarning(title = **'Error'**, message = **'账号或密码错误，重新登录！'**)  
<br/><br/>**class** ReturnFrame(Frame):  
**def** \__init_\_(self,master=**None**):  
Frame.\__init_\_(self,master)  
self.root = master  
self.book_Name_re = StringVar()  
self.user_Name_re = StringVar()  
self.user_Password_re = StringVar()  
self.createPage()  
<br/>**def** createPage(self):  
Label(self).grid(row=0, stick=W, pady=10)  
Label(self, text = **'书 名： '**,font = (**"宋体"**,14,**"bold"**)).grid(row=1, stick=W, pady=20)  
Entry(self, textvariable = self.book_Name_re,font = (**"宋体"**,14,**"bold"**)).grid(row=1, column=1, stick=E)  
Label(self, text = **'用户名： '**,font = (**"宋体"**,14,**"bold"**)).grid(row=2, stick=W, pady=20)  
Entry(self, textvariable = self.user_Name_re,font = (**"宋体"**,14,**"bold"**)).grid(row=2, column=1, stick=E)  
Label(self, text = **'密 码： '**,font = (**"宋体"**,14,**"bold"**)).grid(row=3, stick=W, pady=20)  
Entry(self, textvariable = self.user_Password_re, show=**'\*'**,font = (**"宋体"**,14,**"bold"**)).grid(row=3, column=1, stick=E)  
Button(self,text = **'还 书'**,font = (**"宋体"**,14,**"bold"**),command = self.return_book).grid(row = 4,stick=W,column=1, pady=20,padx = 50)  
<br/>**def** return_book(self):  
f = open(**'books.txt'**)  
f1 = open(**'login_true.txt'**)  
bookname = self.book_Name_re.get()  
username = self.user_Name_re.get()  
userpassword =self.user_Password_re.get()  
**for** line **in** f1:  
str1 = line.strip()  
List = str1.split(**","**)  
username_txt = List\[0\]  
userpassword_txt = List\[1\]  
**if** username == username_txt **and** userpassword == userpassword_txt:  
temp = 1  
**break  
else**:  
temp = 2  
**if** temp == 1:  
**for** line2 **in** f:  
List1 = line2.strip().split(**","**)  
bookname_txt = List1\[1\]  
**if** bookname == bookname_txt:_#若该书存在temp1置为1  
_temp1 = 1  
**break  
else**:  
temp1 = 0  
**if** temp1 == 0:  
showwarning(title = **'Waring'**,message = **'您输入的图书书名有误，请重新输入！'**)  
**elif** temp1 == 1:  
**with** open(**'books.txt'**,**'r'**) **as** fr:  
lines = fr.readlines()  
**with** open(**'books.txt'**,**'w'**) **as** fw:  
**for** line **in** lines:  
l = line.strip().split(**','**)  
**if** bookname == l\[1\]:  
num = int(l\[3\])+1  
str_value = str(num)  
fw.write(l\[0\]+**','**+l\[1\]+**','**+l\[2\]+**','**+str_value+**','**+l\[4\]+ **'\\n'**)  
**else**:  
fw.write(line)  
fr.close()  
fw.close()  
sign = 0  
**with** open (**'book_lend.txt'**,**'r'**) **as** fr1:  
lines1 = fr1.readlines()  
**with** open (**'book_lend.txt'**,**'w'**) **as** fw1:  
**for** line1 **in** lines1:  
v = line1.strip().split(**','**)  
**if** v\[0\] == bookname **and** v\[1\] == username **and** sign == 0:  
list2 = v\[2\].strip().split(**'-'**)  
date1 = datetime.date(year=int(list2\[0\]),month=int(list2\[1\]),day=int(list2\[2\]))  
back_date = datetime.datetime.now().strftime(**'%Y-%m-%d'**)  
list3 = back_date.strip().split(**'-'**)  
date2 = datetime.date(year=int(list3\[0\]),month=int(list3\[1\]),day=int(list3\[2\]))  
date = (date2-date1).days+1  
sign = 1 _#设置sign保证只删除1条数据  
_borrowWin = Tk()  
borrowWin.title(**'借书信息'**)  
borrowWin.geometry(**'500x300'**)  
Label(borrowWin).grid(row=0, stick=W, pady=8)  
Label(borrowWin,text = **'书 名：'**+bookname,font = (**"宋体"**,14,**"bold"**)).grid(row=1, stick=W, pady=10,padx = 100)  
Label(borrowWin,text = **'用 户：'**+username,font = (**"宋体"**,14,**"bold"**)).grid(row=2, stick=W, pady=10,padx = 100)  
Label(borrowWin,text = **'借出日期：'**+list2\[0\]+**'年'**+list2\[1\]+**'月'**+list2\[2\]+**'日'**,font = (**"宋体"**,14,**"bold"**)).grid(row=3, stick=W, pady=10,padx = 100)  
Label(borrowWin,text = **'借出天数：'**+str(date)+**' 天'**,font = (**"宋体"**,14,**"bold"**)).grid(row=4, stick=W, pady=10,padx = 100)  
**continue  
**fw1.write(line1)  
fr1.close()  
fw1.close()  
showinfo(title = **'Success'**,message = **'还书成功！'**)  
**else**:  
showwarning(title = **'Error'**, message = **'账号或密码错误，重新登录！'**)

## 五、软件测试

软件测试无异常，可正常执行。

## 六、用户使用说明

管理员账号：admir 密码：123

用户账号：gu 密码：1111（还有部分管理员账号、用户账号，此处仅给出两个范例，其他账号可打开text文件自行注册）

管理员账号和用户账号可以自行注册，所有添加的图书、注册的账号等都会保存在text文件中，运用了**文件处理**的数据处理的方法，使用tkinter第三方库完成编程。Login-true文件中存储用户账号及密码，login-admir中存储管理员账号及密码，books文件中存储书籍信息，book-lend中存储借出的书籍信息。

login Page为登录界面，register Page为注册界面，user-main page为用户登陆后的主界面，admir main page为管理员登陆后主界面，view user为用户操作的界面，view admir 为管理员操作的界面，打开main.py文件即可运行程序。

## 七、大作业总结与体会