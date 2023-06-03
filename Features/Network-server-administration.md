## Network server administration


### Changing server settings from an attached network client

The rcon mechanism can be used edit server settings from an attached network client, however it is much more cumbersome to use than the settings window.

The settings_access mechanism can be use to authorise a network client such that is is permitted to change the following on the server:
* Game settings (using the settings window or the `setting` console command)
* Cheats (using the cheats window)
* Pause/unpause game (using the pause button in the main toolbar)
* Rename engine (using the build vehicle window)
* Rename towns and change per-town settings when these are not enabled for normal multiplayer clients (using the town window)

The `network.settings_password` setting needs to be set to a secure password (in the same way as the rcon password is set).

Run `setting network.settings_password PASSWORD` or just `settings_password PASSWORD` on the server,  
or set the `settings_password` field in the `[network]` section of secrets.cfg before starting the server.

On the network client run `settings_access PASSWORD` in the console.

To drop access if it is no longer required run `settings_access ""` in the console (i.e. an empty password).

**The settings access password should be considered just as important to keep secure as the rcon password**


### Company passwords

Company passwords are stored in savegames made by the network server in an encrypted form,  
and are automatically restored when loaded by the same network server (with the same configuration secrets).  
If the save is loaded anywhere else the company passwords cannot be decrypted and are not restored.

This includes autosaves and manual saves made from the server (e.g. using a server console or rcon).  
This does not include savegames made from attached network clients, or the temporary savegames sent to network clients when joining.


### Offering companies for sale

The `offer_company_sale COMPANY_ID` console command offers a company for sale to other companies/players in the same way as if it was about to go bankrupt.  
This must be run the network server (if necessary by using rcon).

(This can also be used in single-player).
