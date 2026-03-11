Welcome to the Build and Update batchfiles folder. These batchfiles are a little special. There are three kinds:

build_: These will build in your Warband\Modules folder a standard Floris folder, depending on the version you wish to compile. Then they will copy all resources like textures, brf's, sounds and music to the appropriate subfolders. And finally they will compile the source to there.

compile_: These will only compile the source to the directory created by the build_ files.


create_release_version.bat: This batch file will create in your Warband/Modules folder the Expanded version, Gameplay version and NAtive version, and will copy the Dev Suite to there: then it will pack all four into a 7zip-file, and copy it to the Installer folder in this copy of your Dev Suite. And finally it will also create the installer. So it will effectively create the files necessary for a release (except a patch). Keep in mind tough that it might take a while to create (it could take up to an hour), and that you're probably not interested in using this batchfile unless you're indeed going to release a new version of the Floris Mod Pack. If you do, however, make sure that in the batchfile the references to 7zip and Innu Setup creator are correct.