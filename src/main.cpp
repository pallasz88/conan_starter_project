#include <spdlog/spdlog.h>
#include <fmt/core.h>

int main() {
    spdlog::info("Hello, Conan Starter Project!");
    fmt::print("Formatted output: {}\n", 42);
    return 0;
}
