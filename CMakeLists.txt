cmake_minimum_required(VERSION 3.16)

project(conan_starter_project VERSION 1.0.0 LANGUAGES CXX)

option(ENABLE_COVERAGE "Enable coverage flags" OFF)
if(ENABLE_COVERAGE AND CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    message(STATUS "Coverage enabled")
    add_compile_options(-O0 -g --coverage)
    add_link_options(--coverage)
endif()

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(spdlog REQUIRED CONFIG)
find_package(fmt REQUIRED CONFIG)
find_package(GTest REQUIRED CONFIG)

add_library(application src/application.cpp include/myInclude.hpp)
target_include_directories(application PRIVATE include)
target_link_libraries(application
    PUBLIC
    spdlog::spdlog_header_only 
    fmt::fmt
)

add_executable(${PROJECT_NAME} src/main.cpp)

target_include_directories(${PROJECT_NAME} PRIVATE include)
target_link_libraries(${PROJECT_NAME} 
    PRIVATE
    application
)

enable_testing()
add_subdirectory(tests)