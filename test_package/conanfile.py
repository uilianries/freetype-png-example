#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools, RunEnvironment
import os
import mimetypes


class TestPackageConan(ConanFile):
    generators = 'cmake'
    settings = "os", "arch", "compiler", "build_type"

    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            ttf_path = os.path.join('..', '..', 'OpenSans-Bold.ttf')
            bin_path = "freetype_example"
            if self.settings.os == "Windows":
                self.run("{0} {1} Foobar".format(bin_path, ttf_path))
            else:
                self.run("LD_LIBRARY_PATH=%s %s %s Foobar" % (os.environ.get('LD_LIBRARY_PATH', ''), bin_path, ttf_path))
            file = mimetypes.guess_type('out.png')
            assert file[0] == 'image/png'
