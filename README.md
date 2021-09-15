# 说明

用到了R15的参数执行方式，国人开发的pyecharts模块。

最初的打算是给中正评测做的，因为它的30轮循环图很不直观，不过，所长并不太认可，做都做了，就顺便发出来吧

不要让R15所处的路径太长，如果闪退的话，把R15拖到桌面运行即可.

# 部署
## need
├── Cinebench-R15-Loop-test-main.zip
├── Cinebench_R15_MAXON.zip
└── python-3.8.10-amd64.exe

## 安装环境
1.以管理员身份运行
2.勾选“Add Python 3.8 to PATH”
3.install now
4.Disable path length limit
5.修改dns添加GitHUB加速
6.`pip install pyecharts -U`

## 解压
解压到下载目录，减短长度链接。
Cinebench-R15-Loop-test-main.zip
Cinebench_R15_MAXON.zip

## 执行
将main.py文件移动到Cinebench_R15_MAXON文件夹，然后执行。