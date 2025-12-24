#include "myInclude.hpp"

void print() {
  spdlog::info("Hello, Conan Starter Project!");
  constexpr int arbitraryNumber = 42;
  fmt::print("Formatted output: {}\n", arbitraryNumber);
}