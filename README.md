仅作参考

添加了YCB_urdf模型，但是只能加载obj格式的文件（）

更改了YCB_urdf中的`.mtl`文件中的一些路径

在`envs/utils/create_actor.py`下增加了一个用于创建来自YCB的模型的函数

如果发现无法正确加载YCB中的模型，可以尝试运行`script/clean_mtl。py`解决