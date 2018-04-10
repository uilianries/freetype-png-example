cmake_minimum_required(VERSION 2.8.11)
project(freetype_example)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(conanbuildinfo.cmake)
conan_basic_setup()

find_package(Freetype REQUIRED)

add_executable(${PROJECT_NAME} clfontpng.cc)
target_link_libraries(${PROJECT_NAME} ${FREETYPE_LIBRARY})

install(TARGETS ${PROJECT_NAME}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
