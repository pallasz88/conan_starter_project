cmake_minimum_required(VERSION 3.16)

project(conan_starter_project VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include Conan generated files
include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake OPTIONAL)

find_package(spdlog REQUIRED CONFIG)
find_package(fmt REQUIRED CONFIG)
find_package(GTest REQUIRED CONFIG)

add_executable(${PROJECT_NAME} src/main.cpp)

target_include_directories(${PROJECT_NAME} PRIVATE include)
target_link_libraries(${PROJECT_NAME} 
    PRIVATE
    spdlog::spdlog_header_only 
    fmt::fmt
)

enable_testing()
add_subdirectory(tests)