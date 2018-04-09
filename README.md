### Conan Freetype validation

Trying to solve https://github.com/bincrafters/community/issues/216

#### Intro
This example build an application that uses freetype + libpng to create a
.PNG file. The application write anything on file, using a .TTF file.

On test package, freetype-example creates out.png with "Foobar"

#### build
    conan create . user/testing

#### Requirements
- Conan >1.0
- CMake >2.8
- Any compiler

#### License
[MIT](LICENSE)
