# 调度计划窗口功能

## 通过式装载

通过式装载功能允许货运列车在比自身更短的站台上以移动的方式装卸货。

![通过式装载样例](images/through-load.gif)

通过式装载功能需要通过“Show advanced loading mode features”设置启用。
你可以在列车的调度计划窗口中将“\[近端\]”、“\[中间\]”或“\[远端\]”改为“\[通过式装载\]”。

![通过式装载命令](images/through-load-orders.png)

## 反转调度命令

如果需要反转调度命令，可以在调度窗口中选中“调度计划结束”（或者“共享调度计划结束”）之后，
在“管理列表”下拉菜单中选择“反转调度列表”。如果想要将反转后的列表加到调度计划当中，
可以在同一个下拉菜单中选择“将反转调度列表添加至计划末尾”。

（如果“管理列表”按钮没有启用，可以尝试按{kbd}`Ctrl`键临时启用。）

原始调度计划：

![Orders, showing manage list drop-down](images/reverse-orders-0.png)

反转后的调度计划：

![Orders after reversing](images/reverse-orders-1.png)

反转过后的调度计划添加至调度计划末：

![Orders after appending reversed orders](images/reverse-orders-2.png)
