# 服务器管理功能

## 从客户端改变服务端设置

你*可以*在客户端使用远程控制台[^rcon]修改服务器设置。
不过通过*设置菜单*修改要简单得多——使用远程控制台远比使用设置菜单困难。

[^rcon]: 译注：RCON，即 Remote control，指远程控制/修改/操作服务端上的内容（~~リンクスタート~~）

可以通过 `settings_access` 命令授权客户端修改服务端设置。可修改的设置如下：

* 游戏设置（使用设置菜单或控制台命令 `setting`）
* 沙盒选项（使用沙盒选项窗口，旧称“作弊”）
* 暂停/取消暂停（使用工具栏中的暂停与取消暂停按钮）
* 重命名载具（使用购买载具窗口）
* 重命名城镇与修改城镇设置（使用城镇窗口）[^when_open_to_all]

[^when_open_to_all]: 译注：启用“允许联机玩家修改城镇设置”选项后所有玩家都可以修改城镇相关设置。

需要注意的是，在使用之前需要通过设置 `network.settings_password` 设置密码。 (in the same way as the rcon password is set).

Run `setting network.settings_password PASSWORD` or just `settings_password PASSWORD` on the server,
or set the `settings_password` field in the `[network]` section of secrets.cfg before starting the server.

On the network client run `settings_access PASSWORD` in the console.

To drop access if it is no longer required run `settings_access ""` in the console (i.e. an empty password).
**The settings access password should be considered just as important to keep secure as the rcon password**

## Company passwords

Company passwords are stored in savegames made by the network server in an encrypted form,
and are automatically restored when loaded by the same network server (with the same configuration secrets).
If the save is loaded anywhere else the company passwords cannot be decrypted and are not restored.

This includes autosaves and manual saves made from the server (e.g. using a server console or rcon).
This does not include savegames made from attached network clients, or the temporary savegames sent to network clients when joining.

## Merging companies

The `merge_companies MAIN_COMPANY_ID TO_MERGE_COMPANY_ID` console command directly merges one company into another.
The first company ID MAIN_COMPANY_ID will be left with the combined assets of both companies.
The second company ID TO_MERGE_COMPANY_ID will be removed, with all assets transfered to the first company ID.
This must be run on the network server (if necessary by using rcon), or can be used in single-player mode.

## Offering companies for sale

The `offer_company_sale COMPANY_ID` console command offers a company for sale to other companies/players in the same way as if it was about to go bankrupt.
This must be run on the network server (if necessary by using rcon), or can be used in single-player mode.
