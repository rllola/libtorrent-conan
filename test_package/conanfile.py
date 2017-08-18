from conans import ConanFile, tools

class LibtorrentTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "Libtorrent/1.1.4@lola/stable"
    generators = "cmake"

    def configure(self):
        # build static libs
        self.options["Libtorrent"].deprecated_functions=False
        self.options["Libtorrent"].shared=False
        self.options["Boost"].shared=False
        self.options["zlib"].shared=False
        self.options["bzip2"].shared=False
        self.options["OpenSSL"].shared=False

        # with position independent code
        if self.settings.compiler != "Visual Studio":
          self.options["Libtorrent"].fPIC=True
          self.options["Boost"].fPIC=True
          self.options["bzip2"].fPIC=True


    def test(self):
      # self.conanfile_directory
      with tools.pythonpath(self):
            import libtorrent
            print("Libtorrent version: %s" % libtorrent.version)
