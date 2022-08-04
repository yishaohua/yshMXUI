
准备工作：
1. 本地adb环境正常工作
2. 把mx_install文件夹拷贝到本地，把mx_install文件夹路径添加到环境变量
3. 命令行cd到mx_install文件夹中，执行pip install -r requirements.txt
4. python2坏境的，修改mx_install.py文件；python3环境的，修改mx_install3.py文件，第13行download_path = 自己电脑中的文件路径，用于保存下载的apk
5. python2坏境的，修改mxinstall文件；python3环境的，修改mxinstall3文件，把mx_install3.py文件路径替换为实际的绝对路径


使用方法：
python2，命令行直接执行mxinstall [jenkins上job的代号] [build号]，
python3，命令行直接执行mxinstall3 [jenkins上job的代号] [build号]，
如：
- mxinstall ad 1111    （下载并安装jenkins上主版发版job中，build号为#1111的包）
- mxinstall ad         （下载并安装jenkins上主版发版job中，最新的build号中的包）
- mxinstall ad 1.10.47 （下载并安装jenkins上主版发版job中，build名称中包含1.10.47字段的包，前提是之前已经用前两种使用方式中的某一种方式下载安装过这个build的包）

   - 各job对应的代号如下：
   - ad:       主版发版的job MXVP_Major_Ad_Client
   - ad_dev:   主版开发的job MXVP_Major_Ad_Client_all_dev
   - beta:     beta发版的job MXPlayer Online Beta Client
   - beta_dev: beta开发的job MXVP_Online_Beta_Client_dev
   - js:       joyshare的job BuzzifyAndroid

![Note:](https://github.com/ZenMX/MXQA/blob/master/Automation-Android/Tools/mx_install/screenshot.png)
