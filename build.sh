#!/bin/bash

set -e
set -x

mkdir -p build
pushd build/
rm -rf *
conan install ..
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build .
bin/freetype_example ../OpenSans-Bold.ttf Foobar
file out.png
