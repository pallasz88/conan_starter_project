find_package(GTest REQUIRED)

add_executable(test_main test_main.cpp)
target_include_directories(test_main PRIVATE ../include)

target_link_libraries(test_main 
    PRIVATE
    GTest::gtest_main
    spdlog::spdlog_header_only
    application
)
add_test(NAME test_main COMMAND test_main)