Strive Text Updater
========================

When the game updates the <b>REDGame.uexp</b> is also updated. This results in the game not showing correctly some texts.
To solve this and update the modded <b>REDGame.uexp</b>, this program:
<ul>
<li>If used offline, it will try to read <b>REDGameUpdated.uexp</b>, must be provided by the user.</li>
<li>If used online, it will ask for a region code (*INT* for English e.g.) and will save it as <b>REDGameUpdated.uexp</b>.</li>
<li>Searches for the variable names and if the content is different, overwrites it with the modded one.</li>
<li>Changes will be saved on a new file: <b>NewREDGame.uexp</b></li>
</ul>

<h3>How to use</h3>  

Download <a href ="https://github.com/Ferdom-M/StriveTextUpdater/releases/download/1.0/StriveTextUpdater.zip">StriveTextUpdater.zip</a>  . It contains two files: **OnlineUpdater.exe** and **OfflineUpdater.exe**.
Extract them and place them in a folder. Copy your **REDGame.uexp** to be updated to that folder (MUST BE NAMED "**REDGame.uexp**")

If used online, it will ask for a region code and will save it as **REDGameUpdated.uexp**. That region code is the folder name where it was first located:
- CHN = Simplified Chinese 
- CHT = Traditional Chinese
- DEU = German
- ESN = Spanish
- FRA = French
- INT = English
- ITA = Italian
- JPN = Japanese
- KOR = Korean

If used offline, it will try to read **REDGameUpdated.uexp**, must be provided by the user (Find it with uModel on RED/Content/Localization/regionCode/)

When finished it will create a file named: "**NewREDGame.uexp**". Rename it to REDGame.uexp and create your pak using Unreal Pak

Have fun making text mods!
