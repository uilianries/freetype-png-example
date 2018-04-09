cmake_minimum_required(VERSION 2.8.11)
project(freetype_example)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/clfontpng.cc)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
